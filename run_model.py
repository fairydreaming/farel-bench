#!/usr/bin/env -S python3 -u

import re
import os
import csv
import sys
import codecs
import argparse
import subprocess
from collections import defaultdict

LLAMA_OPTIONS = ["--numa", "distribute", "-t", "32", "-s", "42", "-c", "1024", "--temp", "0.01"]
DEFAULT_SYSTEM_PROMPT="You are a master of logical thinking. You carefully analyze the premises step by step, take detailed notes and draw intermediate conclusions based on which you can find the final answer to any question."

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--binary", help="Path to the llama.cpp executable binary.", required=True)
parser.add_argument("-t", "--timeout", help = "llama.cpp execution timeout (seconds)", default=600, type=int)
parser.add_argument("-m", "--model", help="Path to the GGUF model file.", required=True)
parser.add_argument("-s", "--system-prompt", help="Use given system prompt. By default, the system prompt is not used. When this option is passed without a value, the default system prompt value is used: " + repr(DEFAULT_SYSTEM_PROMPT), const=DEFAULT_SYSTEM_PROMPT, default=None, nargs='?')
args = parser.parse_args()
llama_bin = args.binary
model_file = args.model
system_prompt = args.system_prompt
execution_timeout = args.timeout

if system_prompt:
    LLAMA_PROMPT_TEMPLATE="<s>[INST] <<SYS>>\n{SYS}\n<</SYS>>\n\n{USER}[/INST]\n"
    LLAMA3_PROMPT_TEMPLATE="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{SYS}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{USER}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    CHATML_PROMPT_TEMPLATE="<|im_start|>system\n{SYS}<|im_end|>\n<|im_start|>user\n{USER}<|im_end|>\n<|im_start|>assistant"
    COMMANDR_PROMPT_TEMPLATE="<BOS_TOKEN><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>{SYS}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|USER_TOKEN|>{USER}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>"
    VICUNA_PROMPT_TEMPLATE="{SYS}\nUSER: {USER}\nASSISTANT:"
    PHI3_PROMPT_TEMPLATE=None
    DEEPSEEK2_PROMPT_TEMPLATE="{SYS}\n\nUser: {USER}\n\nAssistant:"
    NEMOTRON4_PROMPT_TEMPLATE="<extra_id_0>System\n{SYS}\n<extra_id_1>User\n{USER}\n<extra_id_1>Assistant\n"
    DEEPSEEK2_0628_PROMPT_TEMPLATE="<｜begin▁of▁sentence｜>{SYS}\n\n<｜User｜>{USER}<｜Assistant｜>"
    TULU3_PROMPT_TEMPLATE="<|system|>\n{SYS}\n<|user|>\n{USER}\n<|assistant|>\n"
else:
    LLAMA_PROMPT_TEMPLATE="<s>[INST] {USER}[/INST]\n"
    LLAMA3_PROMPT_TEMPLATE="<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n{USER}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    CHATML_PROMPT_TEMPLATE="<|im_start|>user\n{USER}<|im_end|>\n<|im_start|>assistant\n"
    COMMANDR_PROMPT_TEMPLATE="<BOS_TOKEN><|START_OF_TURN_TOKEN|><|USER_TOKEN|>{USER}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>"
    VICUNA_PROMPT_TEMPLATE="USER: {USER}\nASSISTANT: "
    PHI3_PROMPT_TEMPLATE="<|user|>\n{USER}<|end|>\n<|assistant|>"
    DEEPSEEK2_PROMPT_TEMPLATE="User: {USER}\n\nAssistant:"
    NEMOTRON4_PROMPT_TEMPLATE="<extra_id_0>System\n\n<extra_id_1>User\n{USER}<extra_id_1>Assistant\n"
    DEEPSEEK2_0628_PROMPT_TEMPLATE="<｜begin▁of▁sentence｜><｜User｜>{USER}<｜Assistant｜>"
    TULU3_PROMPT_TEMPLATE="<|user|>\n{USER}\n<|assistant|>\n"

model_file_basename = os.path.basename(model_file)

if any(model_name in model_file_basename.lower() for model_name in ["llama-3"]):
    prompt_template = LLAMA3_PROMPT_TEMPLATE
elif any(model_name in model_file_basename.lower() for model_name in ["llama", "gemma", "mistral", "mixtral", "miqu"]):
    prompt_template = LLAMA_PROMPT_TEMPLATE
elif any(model_name in model_file_basename.lower() for model_name in ["qwen", "yi", "dbrx-instruct", "theprofessor", "smaug", "arctic", "internlm"]):
    prompt_template = CHATML_PROMPT_TEMPLATE
elif any(model_name in model_file_basename.lower() for model_name in ["command-r", "aya-23"]):
    prompt_template = COMMANDR_PROMPT_TEMPLATE
elif any(model_name in model_file_basename.lower() for model_name in ["wizardlm"]):
    prompt_template = VICUNA_PROMPT_TEMPLATE
elif any(model_name in model_file_basename.lower() for model_name in ["phi-3"]):
    prompt_template = PHI3_PROMPT_TEMPLATE
elif any(model_name in model_file_basename.lower() for model_name in ["deepseek-v2"]):
    if "0628" in model_file_basename:
        prompt_template = DEEPSEEK2_0628_PROMPT_TEMPLATE
    else:
        prompt_template = DEEPSEEK2_PROMPT_TEMPLATE
elif any(model_name in model_file_basename.lower() for model_name in ["nemotron"]):
    prompt_template = NEMOTRON4_PROMPT_TEMPLATE
elif any(model_name in model_file_basename.lower() for model_name in ["tulu-3"]):
    prompt_template = TULU3_PROMPT_TEMPLATE
else:
    raise RuntimeError("Could not detect model prompt template!")

quiz_reader = csv.reader(sys.stdin, delimiter=',', quotechar='"')

correct_answers = defaultdict(lambda: 0)
incorrect_answers = defaultdict(lambda: 0)
missing_answers = defaultdict(lambda: 0)
all_answers = defaultdict(lambda: 0)

for distance, relation_name, correct_answer, quiz in quiz_reader:
    quiz = codecs.escape_decode(bytes(quiz, "utf-8"))[0].decode("utf-8")
    prompt=prompt_template.format(SYS=system_prompt, USER=quiz)
    command = [llama_bin] + LLAMA_OPTIONS + ["-m", model_file, "-e", "--no-display-prompt", "-p", prompt]
    print(" ".join(command))

    try:
        result = subprocess.run(command, capture_output=True, text=False, timeout=execution_timeout)
        model_output = result.stdout.decode('utf-8')
    except subprocess.TimeoutExpired as e:
        print(f"Execution timeout of {execution_timeout}s expired.")
        model_output = e.stdout.decode("utf-8")

    print(model_output)

    all_answers[relation_name] += 1
    matches = re.findall(r'<ANSWER>(.*?)</ANSWER>', model_output)
    if matches:
        if correct_answer == matches[0].strip():
            correct_answers[relation_name] += 1
        else:
            incorrect_answers[relation_name] += 1
    else:
        missing_answers[relation_name] += 1

for relation_name in all_answers.keys():
    num_correct = correct_answers[relation_name]
    num_incorrect = incorrect_answers[relation_name]
    num_missing = missing_answers[relation_name]
    num_all = all_answers[relation_name]
    percent_correct = 100 * num_correct / num_all
    print(f"{relation_name}: {percent_correct:.2f} (C: {num_correct}, I: {num_incorrect}, M: {num_missing} A: {num_all})")

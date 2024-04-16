#!/usr/bin/env -S python3 -u

import re
import os
import csv
import sys
import codecs
import argparse
import subprocess
from collections import defaultdict
from openai import OpenAI

DEFAULT_SYSTEM_PROMPT="You are a master of logical thinking. You carefully analyze the premises step by step, take detailed notes and draw intermediate conclusions based on which you can find the final answer to any question."

client = OpenAI()

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model", help="OpenAI model name.", required=True)
parser.add_argument("-s", "--system-prompt", help="Use given system prompt. By default, the system prompt is not used. When this option is passed without a value, the default system prompt value is used: " + repr(DEFAULT_SYSTEM_PROMPT), const=DEFAULT_SYSTEM_PROMPT, default=None, nargs='?')
args = parser.parse_args()
model_name = args.model
system_prompt = args.system_prompt

quiz_reader = csv.reader(sys.stdin, delimiter=',', quotechar='"')

correct_answers = defaultdict(lambda: 0)
incorrect_answers = defaultdict(lambda: 0)
missing_answers = defaultdict(lambda: 0)
all_answers = defaultdict(lambda: 0)

for distance, relation_name, correct_answer, quiz in quiz_reader:
    quiz = codecs.escape_decode(bytes(quiz, "utf-8"))[0].decode("utf-8")

    system_messages=[{"role": "system", "content": system_prompt }]
    messages=[{"role": "user", "content": quiz }]
    if system_prompt is not None:
        messages = system_messages + messages
    print(messages)
    response = client.chat.completions.create(model=model_name, messages=messages, temperature=0.01, seed=42)

    model_response = response.choices[0].message.content
    print(model_response)

    all_answers[relation_name] += 1
    matches = re.findall(r'<ANSWER>(.*?)</ANSWER>', model_response)
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

# farel-bench
This project is a family relationship (FaRel) benchmark for testing LLM reasoning abilities with family relationship quizzes.

Note: this benchmark suffers from saturation that made it obsolete. If you are interested in logical reasoning performance of LLM models then check out its successor, lineage-bench: https://github.com/fairydreaming/lineage-bench

## Results

The table below presents 20 best FaRel-3 (family relationships of degree up to 3) benchmark results.
The benchmark result is the macro-averaged accuracy value over all the family relationship classes.

|   Nr | Model                                |   FaRel |   child |   parent |   grand-child |   sibling |   grand-parent |   great grand-child |   niece or nephew |   aunt or uncle |   great grand-parent |
|-----:|:-------------------------------------|--------:|--------:|---------:|--------------:|----------:|---------------:|--------------------:|------------------:|----------------:|---------------------:|
|    1 | deepseek-r1                      |   99.78 |  100.00 |   100.00 |        100.00 |     98.00 |         100.00 |              100.00 |            100.00 |          100.00 |               100.00 |
|    1 | o1-mini                          |   99.78 |  100.00 |   100.00 |        100.00 |    100.00 |          98.00 |              100.00 |            100.00 |          100.00 |               100.00 |
|    3 | o1-preview                       |   98.89 |  100.00 |   100.00 |         96.00 |    100.00 |         100.00 |              100.00 |             94.00 |          100.00 |               100.00 |
|    4 | qwq-32b-preview                  |   96.67 |  100.00 |   100.00 |        100.00 |     98.00 |         100.00 |               98.00 |             90.00 |           88.00 |                96.00 |
|    5 | deepseek-v3                      |   96.44 |  100.00 |   100.00 |        100.00 |     96.00 |         100.00 |              100.00 |             82.00 |           92.00 |                98.00 |
|    6 | claude-3.5-sonnet-1022           |   93.33 |  100.00 |   100.00 |        100.00 |     92.00 |         100.00 |               98.00 |             76.00 |           74.00 |               100.00 |
|    7 | qvq-72b-preview                  |   91.56 |  100.00 |   100.00 |         98.00 |     92.00 |          96.00 |               86.00 |             84.00 |           76.00 |                92.00 |
|    8 | mistral-large-2411-Q8_0          |   88.44 |  100.00 |   100.00 |         94.00 |     92.00 |         100.00 |               90.00 |             70.00 |           54.00 |                96.00 |
|    8 | Sky-T1-32B-Preview-Q8_0          |   88.44 |  100.00 |   100.00 |         80.00 |     96.00 |          98.00 |               90.00 |             82.00 |           50.00 |               100.00 |
|   10 | deepseek-v2-chat-0628-Q8_0       |   87.78 |  100.00 |   100.00 |         98.00 |     86.00 |          94.00 |               94.00 |             60.00 |           60.00 |                98.00 |
|   11 | gemini-pro-1.5-002               |   87.11 |  100.00 |   100.00 |         74.00 |     88.00 |         100.00 |               84.00 |             70.00 |           72.00 |                96.00 |
|   12 | mistral-large-2411               |   86.89 |  100.00 |   100.00 |         68.00 |     88.00 |          98.00 |               96.00 |             64.00 |           68.00 |               100.00 |
|   12 | mistral-large-2                  |   86.89 |  100.00 |   100.00 |         70.00 |     92.00 |         100.00 |               94.00 |             60.00 |           66.00 |               100.00 |
|   12 | claude-3.5-sonnet                |   86.89 |  100.00 |   100.00 |         98.00 |     80.00 |          98.00 |               94.00 |             60.00 |           56.00 |                96.00 |
|   15 | llama-3.3-70b-instruct           |   86.44 |  100.00 |   100.00 |         90.00 |     92.00 |         100.00 |               76.00 |             68.00 |           56.00 |                96.00 |
|   16 | gpt-4-turbo                      |   86.22 |  100.00 |   100.00 |         92.00 |     84.00 |          96.00 |               90.00 |             56.00 |           60.00 |                98.00 |
|   17 | llama-3.1-405b-instruct          |   85.78 |  100.00 |   100.00 |         88.00 |     92.00 |          98.00 |               88.00 |             54.00 |           52.00 |               100.00 |
|   18 | minimax-01                       |   85.56 |  100.00 |   100.00 |         96.00 |     82.00 |         100.00 |               72.00 |             52.00 |           68.00 |               100.00 |
|   19 | gpt-4o-2024-11-20                |   84.22 |  100.00 |   100.00 |         84.00 |     78.00 |          98.00 |               82.00 |             62.00 |           56.00 |                98.00 |
|   20 | gemini-2.0-flash-exp             |   84.00 |  100.00 |   100.00 |         84.00 |     78.00 |          94.00 |               86.00 |             66.00 |           50.00 |                98.00 |

To see results for all models benchmarked so far check the [results.md](results.md) file.

Notes:
- Models having quantization suffix in their name were run locally on llama.cpp, remaining models were run via OpenAI or OpenRouter APIs.
- Models with -sys suffix had system prompt set to 'You are a master of logical thinking. You carefully analyze the premises step by step, take detailed notes and draw intermediate conclusions based on which you can find the final answer to any question.'.
- Very low benchmark results for gemma-2b, qwen1_5-7b, and WizardLM-2-7B are caused by the inability of the models to mark the selected answer option as specified in the prompt.
- After running the benchmark for nemotron-4-340b-instruct I noticed that in several cases the model response was cut short by the activation of inference timeout set to 10 minutes. If not for that, the score could be even better.
- gemma-2-9b and gemma-2-27b model results are courtesy of Reddit user Healthy-Nebula-3603

I also tested some models in Polish language:

|   Nr | Model                                |   FaRel |   child |   parent |   grand-child |   sibling |   grand-parent |   great grand-child |   niece or nephew |   aunt or uncle |   great grand-parent |
|-----:|:-------------------------------------|--------:|--------:|---------:|--------------:|----------:|---------------:|--------------------:|------------------:|----------------:|---------------------:|
|    1 | llama-3.1-405b-instruct-sys-pl       |   92.89 |  100.00 |   100.00 |         98.00 |     94.00 |         100.00 |               94.00 |             72.00 |           80.00 |                98.00 |
|    2 | qwen-2.5-72b-instruct-pl             |   88.44 |  100.00 |   100.00 |         98.00 |     90.00 |         100.00 |               88.00 |             76.00 |           46.00 |                98.00 |
|    3 | llama-3.1-405b-instruct-pl           |   83.33 |  100.00 |   100.00 |        100.00 |     74.00 |         100.00 |               78.00 |             50.00 |           56.00 |                92.00 |
|    4 | Bielik-11B-v2.3-Instruct-Q8_0-sys-pl |   81.56 |  100.00 |    98.00 |         88.00 |     88.00 |          98.00 |               76.00 |             68.00 |           34.00 |                84.00 |
|    5 | qwen-2.5-72b-instruct-sys-pl         |   80.00 |  100.00 |   100.00 |         96.00 |     92.00 |         100.00 |               82.00 |             52.00 |           32.00 |                66.00 |
|    6 | Bielik-11B-v2.3-Instruct-Q8_0-pl     |   76.00 |  100.00 |   100.00 |         92.00 |     42.00 |         100.00 |               56.00 |             72.00 |           34.00 |                88.00 |

All tested models perform better in Polish compared to results for English language. Is it easier to "reason" in Polish language?

## Description
The purpose of this project is to test LLM reasoning abilities with family relationship quizzes.
Why use family relationships?
* Family relationships are commonly known concepts.
* They allow to create quizzes of scalable difficulty by increasing the relationship degree.
* Easy randomization of the quizzes by changing the names of family members and the order of listed relations.

### Basic assumptions

Consider the following graph of family relationships:
![family relationships](https://i.postimg.cc/2jWvPB2w/family-relations.png)

We can observe that:
* child and parent relationships have distance 1 from self,
* grandchild, grandparent, and sibling relationships have distance 2 from self,
* great grandchild, niece or nephew, aunt or uncle, and great grandparent relationships have distance 3 from self,
and so on.

We use such relationship graphs to programmatically generate family quizzes. 
Generated quizzes have the following properties:
* Connections between family members are specified by using only the parental relationship.
* Family member connections specify a graph of all family relationships of degree up to N.
* The quiz question is to differentiate between family relationships of degree N.
* LLM is instructed to select the i-th quiz answer option by enclosing the selected answer number with the `<ANSWER>i</ANSWER>` tag.

### Example quizzes

#### Family relationships of distance 1

```
Given the family relationships:
* Ralph is Anthony's parent.
* Albert is Ralph's parent.
What is Anthony's relationship to Ralph?
Select the correct answer:
1. Anthony is Ralph's child.
2. Anthony is Ralph's parent.
Enclose the selected answer number in the <ANSWER> tag, for example: <ANSWER>1</ANSWER>.
```

#### Family relationships of distance 2

```
Given the family relationships:
* Wayne is Brittany's parent.
* Billy is Madison's parent.
* Madison is Wayne's parent.
* Brittany is Amanda's parent.
* Madison is Michael's parent.
What is Amanda's relationship to Wayne?
Select the correct answer:
1. Amanda is Wayne's grandparent.
2. Amanda is Wayne's sibling.
3. Amanda is Wayne's grandchild.
Enclose the selected answer number in the <ANSWER> tag, for example: <ANSWER>1</ANSWER>.
```

#### Family relationships of distance 3

```
Given the family relationships:
* Brittany is Jeremy's parent.
* Peter is Lauren's parent.
* Peter is Madison's parent.
* Brittany is Peter's parent.
* Madison is Betty's parent.
* Richard is Andrea's parent.
* Lauren is Gabriel's parent.
* Gabriel is Richard's parent.
* Janet is Brittany's parent.
What is Andrea's relationship to Lauren?
Select the correct answer:
1. Andrea is Lauren's niece or nephew.
2. Andrea is Lauren's aunt or uncle.
3. Andrea is Lauren's great grandchild.
4. Andrea is Lauren's great grandparent.
Enclose the selected answer number in the <ANSWER> tag, for example: <ANSWER>1</ANSWER>.
```

### Performance metrics

We measure the performance of the LLM by macro-averaging the classification accuracy of all family relationships present in the dataset.
So for example if a given LLM has the following accuracy values for family relationship quizzes of degrees up to 3:
* child: 100.00
* parent: 100.00
* grandchild: 96.00
* sibling: 22.00
* grandparent: 72.00
* great grandchild: 46.00
* niece or nephew: 46.00
* aunt or uncle: 18.00
* great grandparent: 68.00

then the overall macro-averaged accuracy is (100 + 100 + 96 + 22 + 72 + 46 + 46 + 18 + 68) / 9 = ~63.11
To differentiate between benchmark results calculated for datasets with different maximum family relationship lengths, we propose to include the maximum family relationship length in the benchmark result label.
So if an accuracy of 63.11 was computed for family relationships of length up to 3, the overall result would be labeled as FaRel-3 and would have a value of 63.11.

## Usage

There are five Python scripts in the FaRel benchmark:
1. The farel_bench.py script generates family relationship quizzes in a CSV format.
2. The run_model.py script generates answers for the quizzes by using llama.cpp and selected LLM and calculates the accuracy values for all family relationships.
3. The run_openai.py script generates answers for the quizzes by using OpenAI API and calculates the accuracy values for all family relationships.
4. The run_openrouter.py script generates answers for the quizzes by using OpenRouter API and calculates the accuracy values for all family relationships.
5. The compute_metrics.py script analyzes log files in a given directory, calculates the macro-averaged accuracy value that is the FaRel benchmark result, and outputs a result table.

### Example workflow

Generating quizzes and storing model answers:
```
./farel_bench.py --shuffle -l 1 -n 50 -r 42|./run_model.py -b ~/projects/llama.cpp/main -m ~/projects/llama.cpp/models/llama-2-7b-chat.Q8_0.gguf|tee ./results/llama-2-7b-chat.Q8_0.log
./farel_bench.py --shuffle -l 3 -n 50 -r 42|./run_openai.py -m gpt-4|tee ./results/gpt-4.log
```

Calculating FaRel benchmark metrics:
```
./compute_metrics.py ./results/
```

### Quiz generator farel_bench.py

The farel_bench.py is the quiz generator script. It has the following options:
```
usage: farel_bench.py [-h] -l LENGTH [-p PROMPT] [-s] [-n NUMBER] [-r SEED]

options:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        Maximum length of family relationship paths.
  -p PROMPT, --prompt PROMPT
                        Prompt template of the quiz. The default prompt template is: 'Given the family
                        relationships:\n$QUIZ_RELATIONS\n$QUIZ_QUESTION\nSelect the correct
                        answer:\n$QUIZ_ANSWERS\nEnclose the selected answer number in the <ANSWER> tag, for
                        example: <ANSWER>1</ANSWER>.'
  -s, --shuffle         Shuffle the order of parental relations and answer options in the quiz.
  -n NUMBER, --number NUMBER
                        Number of quizzes generated for each family relationship.
  -r SEED, --seed SEED  Random seed value
```

### llama.cpp model executor run_model.py

The run_model.py script uses [llama.cpp](https://github.com/ggerganov/llama.cpp) to generate answers for family relationship quizzes generated by farel_bench.py for a selected LLM.

```
usage: run_model.py [-h] -b BINARY [-t TIMEOUT] -m MODEL [-s [SYSTEM_PROMPT]]

options:
  -h, --help            show this help message and exit
  -b BINARY, --binary BINARY
                        Path to the llama.cpp executable binary.
  -t TIMEOUT, --timeout TIMEOUT
                        llama.cpp execution timeout (seconds)
  -m MODEL, --model MODEL
                        Path to the GGUF model file.
  -s [SYSTEM_PROMPT], --system-prompt [SYSTEM_PROMPT]
                        Use given system prompt. By default, the system prompt is not used. When this option is
                        passed without a value, the default system prompt value is used: 'You are a master of
                        logical thinking. You carefully analyze the premises step by step, take detailed notes and
                        draw intermediate conclusions based on which you can find the final answer to any
                        question.'
```

### OpenAI model executor run_openai.py

The run_model.py script uses OpenAI API to generate answers for family relationship quizzes generated by farel_bench.py for a selected LLM.

```
usage: run_openai.py [-h] -m MODEL [-s [SYSTEM_PROMPT]]

options:
  -h, --help            show this help message and exit
  -m MODEL, --model MODEL
                        OpenAI model name.
  -s [SYSTEM_PROMPT], --system-prompt [SYSTEM_PROMPT]
                        Use given system prompt. By default, the system prompt is not used. When this option is
                        passed without a value, the default system prompt value is used: 'You are a master of
                        logical thinking. You carefully analyze the premises step by step, take detailed notes and
                        draw intermediate conclusions based on which you can find the final answer to any
                        question.'
```

### OpenRouter model executor run_openrouter.py

The run_model.py script uses OpenRouter API to generate answers for family relationship quizzes generated by farel_bench.py for a selected LLM.

```
usage: run_openrouter.py [-h] -m MODEL [-s [SYSTEM_PROMPT]]

options:
  -h, --help            show this help message and exit
  -m MODEL, --model MODEL
                        OpenRouter model name.
  -s [SYSTEM_PROMPT], --system-prompt [SYSTEM_PROMPT]
                        Use given system prompt. By default, the system prompt is not used. When this option is
                        passed without a value, the default system prompt value is used: 'You are a master of
                        logical thinking. You carefully analyze the premises step by step, take detailed notes and
                        draw intermediate conclusions based on which you can find the final answer to any
                        question.'
```

### Metrics calculator compute_metrics.py

The compute_metrics.py script reads .log files from a given directory, calculates the FaRel benchmark metrics, and prints a result table in a markdown format.

```
usage: compute_metrics.py [-h] dir

positional arguments:
  dir         Directory containing farel-bench log files.

options:
  -h, --help  show this help message and exit
```

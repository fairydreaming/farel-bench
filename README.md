# farel-bench
This project is a family relationship (FaRel) benchmark for testing LLM reasoning abilities with family relationship quizzes.

## Results

The table below presents the FaRel-3 (family relationships of degree up to 3) benchmark results for selected large language models.
The benchmark result is the macro-averaged accuracy value over all the family relationship classes.

|   Nr | Model                                |   FaRel |   child |   parent |   grand-child |   sibling |   grand-parent |   great grand-child |   niece or nephew |   aunt or uncle |   great grand-parent |
|-----:|:-------------------------------------|--------:|--------:|---------:|--------------:|----------:|---------------:|--------------------:|------------------:|----------------:|---------------------:|
|    1 | o1-mini                              |   99.78 |  100.00 |   100.00 |        100.00 |    100.00 |          98.00 |              100.00 |            100.00 |          100.00 |               100.00 |
|    2 | o1-preview                           |   98.89 |  100.00 |   100.00 |         96.00 |    100.00 |         100.00 |              100.00 |             94.00 |          100.00 |               100.00 |
|    3 | qwq-32b-preview-sys                  |   97.56 |  100.00 |   100.00 |        100.00 |     98.00 |         100.00 |              100.00 |             94.00 |           86.00 |               100.00 |
|    4 | qwq-32b-preview                      |   96.67 |  100.00 |   100.00 |        100.00 |     98.00 |         100.00 |               98.00 |             90.00 |           88.00 |                96.00 |
|    5 | claude-3.5-sonnet-1022-sys           |   95.78 |  100.00 |   100.00 |        100.00 |     96.00 |         100.00 |               98.00 |             92.00 |           76.00 |               100.00 |
|    6 | claude-3.5-sonnet-1022               |   93.33 |  100.00 |   100.00 |        100.00 |     92.00 |         100.00 |               98.00 |             76.00 |           74.00 |               100.00 |
|    7 | claude-3.5-sonnet-sys                |   88.67 |  100.00 |   100.00 |        100.00 |     86.00 |          96.00 |               92.00 |             64.00 |           60.00 |               100.00 |
|    8 | gpt-4o-sys                           |   88.44 |  100.00 |   100.00 |         86.00 |     92.00 |         100.00 |               88.00 |             72.00 |           62.00 |                96.00 |
|    8 | mistral-large-2411-Q8_0              |   88.44 |  100.00 |   100.00 |         94.00 |     92.00 |         100.00 |               90.00 |             70.00 |           54.00 |                96.00 |
|   10 | llama-3.1-405b-instruct-sys          |   87.78 |  100.00 |   100.00 |        100.00 |     96.00 |          96.00 |               92.00 |             50.00 |           56.00 |               100.00 |
|   10 | deepseek-v2-chat-0628-Q8_0           |   87.78 |  100.00 |   100.00 |         98.00 |     86.00 |          94.00 |               94.00 |             60.00 |           60.00 |                98.00 |
|   12 | gpt-4o-2024-11-20-sys                |   87.33 |  100.00 |   100.00 |         98.00 |     84.00 |         100.00 |               98.00 |             56.00 |           52.00 |                98.00 |
|   13 | gemini-pro-1.5-002                   |   87.11 |  100.00 |   100.00 |         74.00 |     88.00 |         100.00 |               84.00 |             70.00 |           72.00 |                96.00 |
|   14 | claude-3.5-sonnet                    |   86.89 |  100.00 |   100.00 |         98.00 |     80.00 |          98.00 |               94.00 |             60.00 |           56.00 |                96.00 |
|   14 | mistral-large-2                      |   86.89 |  100.00 |   100.00 |         70.00 |     92.00 |         100.00 |               94.00 |             60.00 |           66.00 |               100.00 |
|   14 | mistral-large-2411                   |   86.89 |  100.00 |   100.00 |         68.00 |     88.00 |          98.00 |               96.00 |             64.00 |           68.00 |               100.00 |
|   17 | llama-3.3-70b-instruct-sys           |   86.67 |  100.00 |   100.00 |         96.00 |     92.00 |         100.00 |               78.00 |             66.00 |           54.00 |                94.00 |
|   17 | gpt-4-turbo-sys                      |   86.67 |  100.00 |   100.00 |         94.00 |     80.00 |          94.00 |               94.00 |             54.00 |           68.00 |                96.00 |
|   19 | llama-3.3-70b-instruct               |   86.44 |  100.00 |   100.00 |         90.00 |     92.00 |         100.00 |               76.00 |             68.00 |           56.00 |                96.00 |
|   20 | gpt-4-turbo                          |   86.22 |  100.00 |   100.00 |         92.00 |     84.00 |          96.00 |               90.00 |             56.00 |           60.00 |                98.00 |
|   21 | llama-3.1-405b-instruct              |   85.78 |  100.00 |   100.00 |         88.00 |     92.00 |          98.00 |               88.00 |             54.00 |           52.00 |               100.00 |
|   22 | mistral-large-2-sys                  |   85.11 |  100.00 |   100.00 |         84.00 |     86.00 |         100.00 |               94.00 |             56.00 |           50.00 |                96.00 |
|   23 | gpt-4o-2024-11-20                    |   84.22 |  100.00 |   100.00 |         84.00 |     78.00 |          98.00 |               82.00 |             62.00 |           56.00 |                98.00 |
|   23 | llama-3.1-nemotron-70b-instruct-sys  |   84.22 |  100.00 |   100.00 |         78.00 |     90.00 |          98.00 |               88.00 |             60.00 |           46.00 |                98.00 |
|   25 | gemini-2.0-flash-exp                 |   84.00 |  100.00 |   100.00 |         84.00 |     78.00 |          94.00 |               86.00 |             66.00 |           50.00 |                98.00 |
|   26 | gpt-4o                               |   83.11 |  100.00 |   100.00 |         84.00 |     82.00 |          98.00 |               74.00 |             62.00 |           52.00 |                96.00 |
|   27 | claude-3-opus-sys                    |   82.67 |  100.00 |   100.00 |         88.00 |     72.00 |          96.00 |               92.00 |             48.00 |           50.00 |                98.00 |
|   28 | grok-2-sys                           |   81.78 |  100.00 |   100.00 |         80.00 |     92.00 |         100.00 |               90.00 |             34.00 |           42.00 |                98.00 |
|   29 | tulu-3-70b-Q8_0-sys                  |   81.11 |   98.00 |   100.00 |         98.00 |     84.00 |          98.00 |               74.00 |             42.00 |           38.00 |                98.00 |
|   30 | grok-2                               |   80.67 |  100.00 |   100.00 |         66.00 |     96.00 |         100.00 |               84.00 |             48.00 |           40.00 |                92.00 |
|   31 | grok-beta                            |   80.44 |  100.00 |   100.00 |         64.00 |     94.00 |         100.00 |               86.00 |             50.00 |           32.00 |                98.00 |
|   32 | llama-3.1-nemotron-70b-instruct      |   80.00 |  100.00 |   100.00 |         92.00 |     80.00 |          96.00 |               82.00 |             46.00 |           32.00 |                92.00 |
|   33 | nemotron-4-340b-instruct-Q8_0-sys    |   79.78 |  100.00 |   100.00 |         86.00 |     70.00 |          98.00 |               74.00 |             46.00 |           48.00 |                96.00 |
|   33 | Athene-V2-Chat-Q8_0                  |   79.78 |  100.00 |   100.00 |         82.00 |     78.00 |          98.00 |               86.00 |             32.00 |           44.00 |                98.00 |
|   35 | claude-3-opus                        |   78.89 |  100.00 |   100.00 |         86.00 |     72.00 |          94.00 |               90.00 |             40.00 |           32.00 |                96.00 |
|   36 | nemotron-4-340b-instruct-Q8_0        |   78.67 |  100.00 |   100.00 |         76.00 |     60.00 |          96.00 |               76.00 |             46.00 |           58.00 |                96.00 |
|   36 | tulu-3-70b-Q8_0                      |   78.67 |   96.00 |   100.00 |         90.00 |     66.00 |          86.00 |               80.00 |             58.00 |           42.00 |                90.00 |
|   36 | qwen-2.5-72b-instruct                |   78.67 |  100.00 |   100.00 |         60.00 |     78.00 |          96.00 |               84.00 |             42.00 |           54.00 |                94.00 |
|   39 | mistral-large-sys                    |   77.33 |  100.00 |   100.00 |         88.00 |     72.00 |          96.00 |               62.00 |             46.00 |           42.00 |                90.00 |
|   40 | gemini-flash-1.5-002                 |   77.11 |  100.00 |   100.00 |         86.00 |     58.00 |         100.00 |               64.00 |             48.00 |           42.00 |                96.00 |
|   41 | llama-3.1-70b-instruct               |   76.89 |  100.00 |   100.00 |         72.00 |     66.00 |          96.00 |               78.00 |             52.00 |           34.00 |                94.00 |
|   42 | nova-pro-v1-sys                      |   76.67 |  100.00 |   100.00 |         94.00 |     68.00 |          86.00 |               72.00 |             54.00 |           40.00 |                76.00 |
|   43 | nova-pro-v1                          |   76.44 |  100.00 |   100.00 |         90.00 |     68.00 |          88.00 |               70.00 |             54.00 |           36.00 |                82.00 |
|   44 | llama-3.1-70b-instruct-sys           |   75.11 |  100.00 |    98.00 |         76.00 |     70.00 |          90.00 |               76.00 |             44.00 |           30.00 |                92.00 |
|   44 | Meta-Llama-3-70B-Instruct.Q8_0-sys   |   75.11 |  100.00 |   100.00 |         78.00 |     68.00 |         100.00 |               74.00 |             34.00 |           26.00 |                96.00 |
|   46 | gpt-4-sys                            |   74.44 |  100.00 |   100.00 |         90.00 |     66.00 |          96.00 |               60.00 |             46.00 |           46.00 |                66.00 |
|   47 | gemini-pro-1.5                       |   74.00 |  100.00 |   100.00 |         94.00 |     74.00 |          96.00 |               58.00 |             28.00 |           28.00 |                88.00 |
|   48 | gemma-2-27b-Q5_K_M-sys               |   72.44 |  100.00 |    84.00 |         86.00 |     68.00 |          90.00 |               58.00 |             50.00 |           38.00 |                78.00 |
|   49 | gemini-flash-1.5                     |   71.33 |  100.00 |   100.00 |         94.00 |     56.00 |          98.00 |               62.00 |             30.00 |           18.00 |                84.00 |
|   49 | mistral-large                        |   71.33 |  100.00 |   100.00 |        100.00 |     54.00 |          92.00 |               58.00 |             48.00 |           10.00 |                80.00 |
|   51 | mistral-nemo-sys                     |   69.33 |   96.00 |   100.00 |         52.00 |     76.00 |          96.00 |               54.00 |             36.00 |           26.00 |                88.00 |
|   51 | gemma-2-27b-Q5_K_M                   |   69.33 |  100.00 |   100.00 |         80.00 |     54.00 |          92.00 |               58.00 |             20.00 |           32.00 |                88.00 |
|   53 | gemma-2-9b-Q8_0                      |   67.33 |  100.00 |   100.00 |         82.00 |     42.00 |          92.00 |               64.00 |             20.00 |           16.00 |                90.00 |
|   54 | gemma-2-9b-Q8_0-sys                  |   66.67 |  100.00 |   100.00 |         84.00 |     36.00 |          92.00 |               64.00 |             16.00 |           20.00 |                88.00 |
|   55 | gpt-4                                |   65.78 |  100.00 |   100.00 |         98.00 |     28.00 |          86.00 |               76.00 |             12.00 |           14.00 |                78.00 |
|   56 | mixtral-8x22b-instruct-v0.1-Q8_0     |   65.11 |  100.00 |   100.00 |        100.00 |     22.00 |          92.00 |               50.00 |             24.00 |           16.00 |                82.00 |
|   56 | Qwen2-72B-Instruct-Q8_0              |   65.11 |  100.00 |   100.00 |         86.00 |     44.00 |          88.00 |               68.00 |             22.00 |           16.00 |                62.00 |
|   58 | mixtral-8x22b-instruct-v0.1.Q8_0-sys |   64.89 |  100.00 |   100.00 |        100.00 |     22.00 |          94.00 |               44.00 |             30.00 |           16.00 |                78.00 |
|   58 | Mistral-Nemo-Instruct-2407-Q8_0-sys  |   64.89 |   98.00 |    94.00 |         34.00 |     58.00 |          88.00 |               52.00 |             40.00 |           30.00 |                90.00 |
|   60 | Meta-Llama-3-70B-Instruct.Q8_0       |   64.67 |  100.00 |   100.00 |         96.00 |     34.00 |          90.00 |               44.00 |             48.00 |           16.00 |                54.00 |
|   61 | claude-3-haiku-sys                   |   64.00 |  100.00 |   100.00 |         80.00 |     32.00 |          94.00 |               66.00 |             16.00 |           18.00 |                70.00 |
|   62 | WizardLM-2-8x22B.Q8_0                |   63.56 |  100.00 |    98.00 |         86.00 |     24.00 |          82.00 |               54.00 |             28.00 |           20.00 |                80.00 |
|   63 | Bielik-11B-v2.3-Instruct-Q8_0-sys    |   63.33 |   96.00 |    96.00 |         48.00 |     54.00 |          94.00 |               52.00 |             38.00 |           18.00 |                74.00 |
|   64 | c4ai-command-r-plus-v01.Q8_0         |   63.11 |  100.00 |   100.00 |         96.00 |     22.00 |          72.00 |               46.00 |             46.00 |           18.00 |                68.00 |
|   64 | c4ai-command-r-plus-v01.Q8_0-sys     |   63.11 |  100.00 |   100.00 |         96.00 |     22.00 |          74.00 |               48.00 |             40.00 |           22.00 |                66.00 |
|   66 | phi-3-medium-4k-instruct-Q8_0        |   62.44 |  100.00 |   100.00 |         86.00 |     18.00 |          96.00 |               58.00 |             20.00 |           18.00 |                66.00 |
|   67 | mixtral-8x7b-instruct-v0.1.Q8_0      |   62.00 |   98.00 |    96.00 |         78.00 |     24.00 |          96.00 |               50.00 |             34.00 |            8.00 |                74.00 |
|   68 | deepseek-v2-chat-Q8_0                |   61.78 |  100.00 |   100.00 |         98.00 |     24.00 |          90.00 |               56.00 |             22.00 |           20.00 |                46.00 |
|   68 | internlm2_5-20b-chat-Q8_0            |   61.78 |  100.00 |   100.00 |        100.00 |      0.00 |          96.00 |               32.00 |             50.00 |           30.00 |                48.00 |
|   70 | qwen1_5-110b-chat-q8_0               |   61.56 |  100.00 |   100.00 |         68.00 |     26.00 |          94.00 |               40.00 |             30.00 |           18.00 |                78.00 |
|   70 | Karasu-Mixtral-8x22B-v0.1.Q8_0       |   61.56 |  100.00 |   100.00 |         94.00 |     20.00 |          88.00 |               40.00 |             26.00 |           18.00 |                68.00 |
|   70 | deepseek-v2-chat-Q8_0-sys            |   61.56 |  100.00 |   100.00 |        100.00 |     16.00 |          90.00 |               74.00 |             20.00 |           12.00 |                42.00 |
|   73 | qwen1_5-110b-chat-q8_0-sys           |   61.33 |  100.00 |   100.00 |         62.00 |     54.00 |          96.00 |               36.00 |             22.00 |           14.00 |                68.00 |
|   74 | Mistral-Nemo-Instruct-2407-Q8_0      |   60.89 |   96.00 |   100.00 |         90.00 |     20.00 |          98.00 |               28.00 |             50.00 |           18.00 |                48.00 |
|   74 | mixtral-8x7b-instruct-v0.1.Q8_0-sys  |   60.89 |   98.00 |    86.00 |         50.00 |     50.00 |          88.00 |               68.00 |             34.00 |           10.00 |                64.00 |
|   74 | gpt-3.5-turbo-sys                    |   60.89 |  100.00 |    78.00 |         76.00 |     32.00 |          90.00 |               56.00 |             18.00 |           18.00 |                80.00 |
|   77 | mistral-nemo                         |   60.44 |  100.00 |   100.00 |         90.00 |     12.00 |          96.00 |               28.00 |             52.00 |           18.00 |                48.00 |
|   78 | c4ai-command-r-plus-08-2024-Q8_0     |   59.78 |  100.00 |    98.00 |         66.00 |     46.00 |          74.00 |                6.00 |             54.00 |           16.00 |                78.00 |
|   79 | internlm2_5-20b-chat-Q8_0-sys        |   59.11 |  100.00 |   100.00 |         88.00 |      4.00 |          96.00 |               34.00 |             36.00 |           16.00 |                58.00 |
|   79 | mistral-medium-sys                   |   59.11 |  100.00 |   100.00 |         60.00 |     42.00 |          82.00 |               32.00 |             24.00 |           28.00 |                64.00 |
|   81 | c4ai-command-r-08-2024-Q8_0          |   58.44 |  100.00 |   100.00 |         84.00 |     10.00 |         100.00 |               22.00 |             58.00 |           14.00 |                38.00 |
|   82 | mistral-small                        |   58.00 |   98.00 |    98.00 |         80.00 |     22.00 |          82.00 |               14.00 |             66.00 |            8.00 |                54.00 |
|   83 | qwen1_5-72b-chat-q8_0                |   57.56 |  100.00 |   100.00 |         90.00 |     14.00 |          76.00 |               46.00 |             28.00 |           32.00 |                32.00 |
|   84 | mistral-small-sys                    |   57.11 |   92.00 |   100.00 |         76.00 |     26.00 |          84.00 |                6.00 |             68.00 |           18.00 |                44.00 |
|   84 | Smaug-2-72B.Q8_0                     |   57.11 |  100.00 |   100.00 |         90.00 |      6.00 |          84.00 |               48.00 |             14.00 |           24.00 |                48.00 |
|   86 | OLMo-2-1124-13B-Instruct-Q8_0-sys    |   56.67 |   98.00 |   100.00 |         82.00 |     16.00 |          90.00 |               18.00 |             48.00 |           22.00 |                36.00 |
|   86 | qwen1_5-32b-chat-q8_0                |   56.67 |  100.00 |    94.00 |         82.00 |     16.00 |          94.00 |               18.00 |             46.00 |           12.00 |                48.00 |
|   88 | Bielik-11B-v2.3-Instruct-Q8_0        |   56.00 |  100.00 |   100.00 |         66.00 |     28.00 |          80.00 |                4.00 |             62.00 |           30.00 |                34.00 |
|   89 | claude-3-haiku                       |   55.78 |  100.00 |   100.00 |         92.00 |     10.00 |          84.00 |               14.00 |             58.00 |           22.00 |                22.00 |
|   89 | llama-2-70b-chat.Q8_0                |   55.78 |  100.00 |    92.00 |         72.00 |     14.00 |          80.00 |               52.00 |             28.00 |           10.00 |                54.00 |
|   89 | c4ai-command-r-v01-Q8_0              |   55.78 |  100.00 |   100.00 |         76.00 |      4.00 |          92.00 |               18.00 |             20.00 |           46.00 |                46.00 |
|   89 | mistral-medium                       |   55.78 |  100.00 |   100.00 |         54.00 |     64.00 |          66.00 |               24.00 |             40.00 |           24.00 |                30.00 |
|   93 | aya-23-35b-Q8_0                      |   55.33 |  100.00 |   100.00 |         92.00 |      6.00 |          98.00 |               12.00 |             24.00 |           64.00 |                 2.00 |
|   94 | Meta-Llama-3-8B-Instruct.Q8_0        |   55.11 |   96.00 |    94.00 |         46.00 |     38.00 |          96.00 |               36.00 |              8.00 |           28.00 |                54.00 |
|   95 | miqu-1-70b.q5_K_M                    |   54.89 |  100.00 |   100.00 |         50.00 |     66.00 |          64.00 |               16.00 |             40.00 |           30.00 |                28.00 |
|   95 | c4ai-command-r-v01-Q8_0-sys          |   54.89 |   94.00 |   100.00 |         72.00 |     16.00 |          88.00 |               10.00 |             18.00 |           58.00 |                38.00 |
|   97 | ggml-dbrx-instruct-16x12b-q8_0       |   54.44 |  100.00 |   100.00 |         58.00 |     34.00 |          70.00 |               12.00 |             46.00 |           20.00 |                50.00 |
|   98 | snowflake-arctic-instruct-Q5_K_M-sys |   53.56 |   86.00 |   100.00 |         56.00 |     14.00 |          86.00 |               38.00 |             28.00 |           20.00 |                54.00 |
|   99 | OLMo-2-1124-13B-Instruct-Q8_0        |   53.33 |   96.00 |   100.00 |         82.00 |      0.00 |          88.00 |               16.00 |             48.00 |           24.00 |                26.00 |
|   99 | Phi-3-mini-4k-instruct-Q8_0          |   53.33 |   98.00 |    96.00 |         98.00 |      4.00 |          90.00 |               20.00 |             26.00 |           36.00 |                12.00 |
|  101 | Meta-Llama-3-8B-Instruct.Q8_0-sys    |   51.56 |   80.00 |    88.00 |         50.00 |     32.00 |          90.00 |               42.00 |             14.00 |           18.00 |                50.00 |
|  102 | gpt-3.5-turbo                        |   50.22 |   96.00 |    54.00 |         78.00 |     18.00 |          80.00 |               22.00 |             52.00 |           18.00 |                34.00 |
|  103 | deepseek-v2-lite-chat-Q8_0           |   49.56 |   88.00 |   100.00 |         60.00 |     14.00 |          88.00 |                8.00 |             62.00 |            6.00 |                20.00 |
|  104 | llama-3.1-8b-instruct                |   48.67 |   82.00 |    92.00 |         44.00 |     32.00 |          96.00 |               24.00 |             10.00 |           10.00 |                48.00 |
|  105 | mistral-7b-instruct-v0.2.Q8_0        |   46.89 |   98.00 |    86.00 |         42.00 |     24.00 |          70.00 |               12.00 |             56.00 |           28.00 |                 6.00 |
|  106 | aya-23-8b-Q8_0                       |   45.78 |   72.00 |   100.00 |         32.00 |     46.00 |          56.00 |                2.00 |             52.00 |           48.00 |                 4.00 |
|  106 | llama-3.1-8b-instruct-sys            |   45.78 |   82.00 |    78.00 |         34.00 |     30.00 |          84.00 |               30.00 |              8.00 |            8.00 |                58.00 |
|  108 | deepseek-v2-lite-chat-Q8_0-sys       |   45.56 |   54.00 |   100.00 |         62.00 |      8.00 |          90.00 |                8.00 |             70.00 |            6.00 |                12.00 |
|  109 | snowflake-arctic-instruct-Q5_K_M     |   44.89 |   54.00 |    82.00 |         70.00 |      8.00 |          60.00 |               30.00 |             44.00 |           34.00 |                22.00 |
|  110 | gemma-7b-it-Q8_0                     |   43.56 |  100.00 |    54.00 |         62.00 |     32.00 |          36.00 |               28.00 |             50.00 |           18.00 |                12.00 |
|  111 | llama-2-13b-chat.Q8_0                |   43.33 |   88.00 |    82.00 |         32.00 |     22.00 |          76.00 |                6.00 |             42.00 |           30.00 |                12.00 |
|  112 | mistral-7b-instruct-v0.2.Q8_0-sys    |   33.33 |   72.00 |    90.00 |         20.00 |     16.00 |          52.00 |               12.00 |             20.00 |           10.00 |                 8.00 |
|  113 | llama-2-7b-chat.Q8_0                 |   31.56 |   36.00 |    72.00 |         34.00 |     24.00 |          28.00 |               22.00 |             22.00 |           30.00 |                16.00 |
|  114 | WizardLM-2-7B-Q8_0                   |   20.00 |   36.00 |    16.00 |          8.00 |     14.00 |          18.00 |               22.00 |             36.00 |           12.00 |                18.00 |
|  115 | gemma-2b-it-Q8_0                     |    5.56 |    0.00 |     0.00 |          0.00 |      0.00 |           0.00 |               12.00 |             24.00 |           14.00 |                 0.00 |
|  116 | qwen1_5-7b-chat-q8_0                 |    2.89 |    6.00 |     2.00 |          4.00 |      0.00 |           2.00 |                0.00 |              8.00 |            2.00 |                 2.00 |

Notes:
- Hand-curating the result lists by hand was getting tedious, so I merged the closed-weights and open-weights results lists into a single automatically generated list.
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

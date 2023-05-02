---
language:
- en
- code


tags:
- pytorch
- causal-lm
- code-generation
- The Pile


license: apache-2.0

---


# FIM-1.3B 

## Model Description

FIM-1.3B is the first of a series of large-scale infilling-enabled autoregressive language models trained by CarperAI. FIM-1.3B is the first of these models, and future models (both larger and smaller) trained on greater quantities of code data will be released, potentially with different architectural variations optimized for code.

This is a preliminary release of an experimental artifact and should be treated as such. We are releasing these results and this model in the hopes that it may be useful to the greater research community, especially those interested in LMs for code and pair programming tools.

CarperAI will be releasing larger LMs better tuned for code in the near future, building on these experiments.



## Model Dimensions


| Hyperparameter       | Value                                                                                                                                  |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| \\(n_{parameters}\\) | 1,331,810,304                                                                                                                           |
| \\(n_{layers}\\)     | 24                                                                                                                                     |
| \\(d_{model}\\)      | 2048                                                                                                                                   |
| \\(d_{ff}\\)         | 8192                                                                                                                                   |
| \\(n_{heads}\\)      | 16                                                                                                                                     |
| \\(d_{head}\\)       | 128                                                                                                                                    |
| \\(n_{ctx}\\)        | 2048                                                                                                                                   |
| \\(n_{vocab}\\)      | 50280                                                                                                                     |
| Positional Encoding  | [Rotary Position Embedding (RoPE)](https://arxiv.org/abs/2104.09864)                                                                   



The model consists of 24 transformer layers with a hidden dimension of 2048, and a feedforward intermediate dimension of 8192. The hidden dimension is split into 16 heads for self-attention, each with a dimension of 128. Rotary Position Embedding (RoPE) is used.


The model is trained with the same tokenizer as [GPT-NeoX-20b](https://arxiv.org/abs/2204.06745), for a vocabulary size of 50254 tokens.


## Training Data

The model was trained on the Pile, an 800Gb dataset composed of varied web corpora. The datasheet and paper for the Pile can be found [here](https://arxiv.org/abs/2201.07311) and [here](https://arxiv.org/abs/2101.00027) respectively.


## Training Details

This model was trained for 47,000 steps at a batch size of 6,291,456 tokens per step in the [GPT-NeoX codebase](https://github.com/EleutherAI/gpt-neox). It was trained as an autoregressive language model, using cross-entropy loss to maximize the likelihood of predicting the next token correctly. 

Following [Bavarian et al. 2022](https://arxiv.org/abs/2207.14255), we train the model to additionally perform infilling via a data transformation applied randomly to 90% of input contexts at train-time. 

Middle segments “to infill” were selected uniformly at random from contexts at the character level, and these contexts were then reformatted as 

\<SUF\> {last 1/3rd of the context} \<PRE\> {first 1/3rd of the context} \<MID\> {middle 1/3rd of the context} \<EOD\>






## How to use


This model can be easily loaded using the `AutoModelForCausalLM` class:


```python


from transformers import AutoTokenizer, AutoModelForCausalLM


tokenizer = AutoTokenizer.from_pretrained("CarperAI/FIM-NeoX-1.3B")
model = AutoModelForCausalLM.from_pretrained("CarperAI/FIM-NeoX-1.3B")


```

### Performing Infilling

Suppose we have some text that we would like to perform infilling on at a certain “cursor location”. 

This would have the form {some prelude text here} \<INFILLING LOCATION\> {some text following cursor}.

The way to perform infilling generation would be via placing the input text into this format:

\<SUF\> {some text following cursor} \<PRE\> {some prelude text here} \<MID\> ... 


language model output is generated after \<MID\> token!


As a concrete example, here is a code snippet that should allow a model to perform infilling:

There was an issue where the sentinel `<|SUF|>`, `<|PRE|>`, and `<|MID|>` tokens were not the correct ids in the uploaded tokenizer and model card! Please try clearing the Huggingface cache and redownloading the model :))

Here is a minimal example of performing open-ended generation with this model, on a simple function `score(x, y)`:
```
def score(x,y) -> int:
    """
    
```

and also infilling with the function and end of docstring already placed:

```
def score(x,y) -> int:
    """
    <|MID|> (infill here)
    """

    score = x + y
    return score
```

```
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model = AutoModelForCausalLM.from_pretrained("CarperAI/FIM-NeoX-1.3B")
tok = AutoTokenizer.from_pretrained("CarperAI/

# infilling demo
prefix = 'def score(x, y) -> int:\n"""\n'
suffix = '"""\n\n    score = x + y\n    return score'

 model_input = [50277, *tok(suffix)["input_ids"], 50278, *tok(prefix)["input_ids"], 50279]
 output = tok.decode(model.generate(torch.IntTensor(model_input).unsqueeze(0), max_length=40)[0])

print(output)
```
outputs: `'<|SUF|>"""\n\n    score = x + y\n    return score<|PRE|>def score(x, y) -> int:\n"""\n<|MID|>    score(x, y) -> int\n<|endoftext|>'`

```
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# non-infilling demo
prefix = 'def score(x, y) -> int:\n"""\n'
model_input = [*tok(prefix)["input_ids"]]
output = tok.decode(model.generate(torch.IntTensor(model_input).unsqueeze(0), max_length=100)[0])
print(output)
```
outputs: `'def score(x, y) -> int:\n"""\n    Return the score of the given point.\n    """\n    return sum(x * y for x, y in zip(x_list, y_list))\n\ndef get_point_score(x, y) -> int:\n    """\n    Return the score of the given point.\n    """\n    return sum(x * y for x, y in zip(x_list, y'`


The sentinel tokens are now accessible via `tokenizer.decode(50277) = "<|SUF|>"`, `tokenizer.decode(50278) = "<|PRE|>"`, `tokenizer.decode(50279) = "<|MID|>"`. 


## Intended Uses and Limitations

FIM-1.3B learns a representation of the English language that can be used to extract features useful for downstream NLP and Code generation tasks. However, the model has solely been trained on a standard next-token-prediction language modeling task on its training data.

## Limitations and Biases

FIM-1.3B was trained on the Pile, a dataset known to contain profanity, lewd, and otherwise abrasive language. FIM-1.3B may produce socially unacceptable or otherwise harmful text. See Sections 5 and 6 of the Pile paper for a more detailed analysis of the biases in the Pile.

As with all language models, it is hard to predict in advance how FIM-1.3B will respond to particular prompts, and offensive content may occur without warning. We recommend having a human curate or filter the outputs before releasing them, both to censor undesirable content and to improve the quality of the results. Code generated by FIM-1.3B should also be checked for security errors by a human before use in production.

## Evaluation results

We evaluate our model on a number of standard NLP datasets to verify that our infilling model performs on par with a comparable autoregressive model.

We use the [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) library developed by EleutherAI for all evaluations except for HumanEval-infilling, for which we use the code in [https://github.com/openai/human-eval-infilling](https://github.com/openai/human-eval-infilling) to evaluate performance.

All 3 models here are trained using the same configuration with differing FIM hyperparameters and/or different positional embeddings. "AR-1.3B" refers to a model trained without FIM and with rotary positional embeddings, "CarperAI/FIM-NeoX-1.3B" refers to this model (trained with a FIM rate of 0.9 in SPM mode according to [Bavarian et al. 2022](https://arxiv.org/abs/2207.14255)), and "FIM-1.3B-alibi" refers to a model trained with [AliBi](https://arxiv.org/abs/2108.12409) positional embeddings but otherwise the same as this model.

| Model           | HumanEval-infilling | arc\_easy | arc\_challenge | lambada | piqa   | sciq  | wsc    | winogrande |
|-----------------|---------------------|----------|---------------|---------|--------|-------|--------|------------|
| AR-1.3B         | 0.0029              | 0.5816   | 0.2465        | 7.03    | 0.7116 | 0.85  | 0.3654 | 0.5651     |
| CarperAI/FIM-NeoX-1.3B | 0.0155              | 0.5829   | 0.2457        | 7.08    | 0.7029 | 0.861 | 0.3654 | 0.5390     |
| FIM-1.3B-alibi  | 0.0029              | 0.5589   | 0.25          | 7.49    | 0.6926 | 0.856 | 0.3654 | 0.5406     |




Here HumanEval-infilling is reported as Pass@10 with a temperature of 0.8 (such that 100 times the score reported here = Pass@10 as a percentage), Lambada is reported as perplexity, and all other benchmarks report accuracy as a number between 0 and 1.


These results are subject to change, but appear to indicate that AliBi with FIM does not enable infilling, while rotary positional embeddings do allow for infilling to be learned.



## Licensing
This model is licensed under the terms of the Apache License 2.0.



```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at


   http://www.apache.org/licenses/LICENSE-2.0


Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```


## Acknowledgements
This project would not have been possible without compute resources provided by [Stability.ai](https://stability.ai) and [CarperAI](https://carper.ai/). 

This model was trained by Hailey Schoelkopf, and would also not have been possible without help, guidance, and feedback by many including Louis Castricato, Stella Biderman, Shivanshu Purohit, Quentin Anthony, and others.


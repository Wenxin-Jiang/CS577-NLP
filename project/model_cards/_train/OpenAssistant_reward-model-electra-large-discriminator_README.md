---
license: apache-2.0
datasets:
- openai/webgpt_comparisons
- openai/summarize_from_feedback
- Dahoas/instruct-synthetic-prompt-responses
language:
- en
metrics:
- accuracy
tags:
- reward-model
- reward_model
- RLHF
---
# Reward model trained from human feedback

Reward model (RM) trained to predict which generated answer is better judged by a human, given a question.

RM are useful in these domain:

- QA model evaluation

- serves as reward score in RLHF 


All models are train on these dataset with a same split seed across datasets (if validation split wasn't available)

- [webgpt_comparisons](https://huggingface.co/datasets/openai/webgpt_comparisons)

- [summarize_from_feedback](https://huggingface.co/datasets/openai/summarize_from_feedback)

- [synthetic-instruct-gptj-pairwise](https://huggingface.co/datasets/Dahoas/synthetic-instruct-gptj-pairwise)

# How to use

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer
reward_name = "OpenAssistant/reward-model-electra-large-discriminator"
rank_model, tokenizer = AutoModelForSequenceClassification.from_pretrained(reward_name), AutoTokenizer.from_pretrained(reward_name)
question, answer = "Explain nuclear fusion like I am five", "Nuclear fusion is the process by which two or more protons and neutrons combine to form a single nucleus. It is a very important process in the universe, as it is the source of energy for stars and galaxies. Nuclear fusion is also a key process in the production of energy for nuclear power plants."
inputs = tokenizer(question, answer, return_tensors='pt')
score = rank_model(**inputs).logits[0].cpu().detach()
print(score)
```


# Performance

Validation split accuracy

| Model  | [WebGPT](https://huggingface.co/datasets/openai/webgpt_comparisons)  | [Summary](https://huggingface.co/datasets/openai/summarize_from_feedback)  | [SytheticGPT](https://huggingface.co/datasets/Dahoas/synthetic-instruct-gptj-pairwise)  |
|---|---|---|---|
| [electra-large-discriminator](https://huggingface.co/OpenAssistant/reward-model-electra-large-discriminator)  | 59.30  | 68.66  | 99.85  |
| [deberta-v3-large](https://huggingface.co/OpenAssistant/reward-model-deberta-v3-large) | 61.13  | 72.23  | 99.94  |
| [deberta-v3-base](https://huggingface.co/OpenAssistant/reward-model-deberta-v3-base)  | 59.07  | 66.84  | 99.85  |

Its likely SytheticGPT has somekind of surface pattern on the choosen-rejected pair which makes it trivial to differentiate between better the answer.
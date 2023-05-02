---
language: ru
license: apache-2.0
tags:
- transformers
thumbnail: "https://github.com/RussianNLP/RuCoLA/blob/main/logo.png"
widget:
- text: "Он решил ту или иную сложную задачу."
---
This is a finetuned version of [RuRoBERTa-large](https://huggingface.co/sberbank-ai/ruRoberta-large) for the task of linguistic acceptability classification on the [RuCoLA](https://rucola-benchmark.com/) benchmark.

The hyperparameters used for finetuning are as follows:
* 5 training epochs (with early stopping based on validation MCC)
* Peak learning rate: 1e-5, linear warmup for 10% of total training time
* Weight decay: 1e-4
* Batch size: 32
* Random seed: 5
* Optimizer: [torch.optim.AdamW](https://pytorch.org/docs/stable/generated/torch.optim.AdamW.html)
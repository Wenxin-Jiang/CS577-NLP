---
tags:
- generated_from_trainer
model-index:
- name: gpt2-gpt2-TF-weight0.5-epoch5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-gpt2-TF-weight0.5-epoch5

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.4047
- Cls loss: 0.8943
- Lm loss: 3.9573
- Cls Accuracy: 0.8305
- Cls F1: 0.8305
- Cls Precision: 0.8305
- Cls Recall: 0.8305
- Perplexity: 52.31

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Cls loss | Lm loss | Cls Accuracy | Cls F1 | Cls Precision | Cls Recall | Perplexity |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:-------:|:------------:|:------:|:-------------:|:----------:|:----------:|
| 4.4891        | 1.0   | 3470  | 4.2525          | 0.4695   | 4.0177  | 0.8046       | 0.8023 | 0.8093        | 0.8046     | 55.57      |
| 4.2708        | 2.0   | 6940  | 4.2621          | 0.5568   | 3.9835  | 0.8398       | 0.8383 | 0.8438        | 0.8398     | 53.71      |
| 4.1614        | 3.0   | 10410 | 4.2509          | 0.5637   | 3.9689  | 0.8444       | 0.8443 | 0.8443        | 0.8444     | 52.93      |
| 4.0683        | 4.0   | 13880 | 4.3454          | 0.7723   | 3.9591  | 0.8282       | 0.8281 | 0.8281        | 0.8282     | 52.41      |
| 4.0036        | 5.0   | 17350 | 4.4047          | 0.8943   | 3.9573  | 0.8305       | 0.8305 | 0.8305        | 0.8305     | 52.31      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
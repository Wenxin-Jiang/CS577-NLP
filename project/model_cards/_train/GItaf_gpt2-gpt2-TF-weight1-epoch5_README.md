---
tags:
- generated_from_trainer
model-index:
- name: gpt2-gpt2-TF-weight1-epoch5-with-eval
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-gpt2-TF-weight1-epoch5-with-eval

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.9349
- Cls loss: 0.9747
- Lm loss: 3.9596
- Cls Accuracy: 0.8340
- Cls F1: 0.8334
- Cls Precision: 0.8346
- Cls Recall: 0.8340
- Perplexity: 52.44

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
| 4.8702        | 1.0   | 3470  | 4.7157          | 0.6951   | 4.0201  | 0.7752       | 0.7670 | 0.7978        | 0.7752     | 55.71      |
| 4.5856        | 2.0   | 6940  | 4.6669          | 0.6797   | 3.9868  | 0.8352       | 0.8333 | 0.8406        | 0.8352     | 53.88      |
| 4.4147        | 3.0   | 10410 | 4.6619          | 0.6899   | 3.9716  | 0.8375       | 0.8368 | 0.8384        | 0.8375     | 53.07      |
| 4.2479        | 4.0   | 13880 | 4.8305          | 0.8678   | 3.9622  | 0.8403       | 0.8396 | 0.8413        | 0.8403     | 52.57      |
| 4.1281        | 5.0   | 17350 | 4.9349          | 0.9747   | 3.9596  | 0.8340       | 0.8334 | 0.8346        | 0.8340     | 52.44      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
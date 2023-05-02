---
tags:
- generated_from_trainer
model-index:
- name: gpt2-gpt2-TF-weight2-epoch5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-gpt2-TF-weight2-epoch5

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 5.8190
- Cls loss: 0.9275
- Lm loss: 3.9629
- Cls Accuracy: 0.8467
- Cls F1: 0.8462
- Cls Precision: 0.8470
- Cls Recall: 0.8467
- Perplexity: 52.61

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
| 5.612         | 1.0   | 3470  | 5.5564          | 0.7637   | 4.0282  | 0.7689       | 0.7591 | 0.7959        | 0.7689     | 56.16      |
| 5.2267        | 2.0   | 6940  | 5.2872          | 0.6471   | 3.9922  | 0.8444       | 0.8434 | 0.8463        | 0.8444     | 54.17      |
| 4.9082        | 3.0   | 10410 | 5.5032          | 0.7631   | 3.9761  | 0.8415       | 0.8405 | 0.8435        | 0.8415     | 53.31      |
| 4.5998        | 4.0   | 13880 | 5.6560          | 0.8448   | 3.9654  | 0.8484       | 0.8483 | 0.8483        | 0.8484     | 52.74      |
| 4.4024        | 5.0   | 17350 | 5.8190          | 0.9275   | 3.9629  | 0.8467       | 0.8462 | 0.8470        | 0.8467     | 52.61      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1

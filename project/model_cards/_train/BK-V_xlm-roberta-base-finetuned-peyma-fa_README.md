---
license: mit
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: xlm-roberta-base-finetuned-peyma-fa
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-peyma-fa

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0937
- F1: 0.9249

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.1562        | 1.0   | 998  | 0.0691          | 0.8777 |
| 0.0638        | 2.0   | 1996 | 0.0703          | 0.8908 |
| 0.0457        | 3.0   | 2994 | 0.0645          | 0.8975 |
| 0.0281        | 4.0   | 3992 | 0.0842          | 0.8994 |
| 0.0206        | 5.0   | 4990 | 0.0651          | 0.9164 |
| 0.0139        | 6.0   | 5988 | 0.0787          | 0.9148 |
| 0.0083        | 7.0   | 6986 | 0.0838          | 0.9253 |
| 0.0052        | 8.0   | 7984 | 0.0833          | 0.9221 |
| 0.0031        | 9.0   | 8982 | 0.0947          | 0.9230 |
| 0.0028        | 10.0  | 9980 | 0.0937          | 0.9249 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.9.1
- Datasets 2.1.0
- Tokenizers 0.12.1

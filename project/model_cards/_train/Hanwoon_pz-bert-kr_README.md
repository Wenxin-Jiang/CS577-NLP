---
tags:
- generated_from_trainer
model-index:
- name: pz-bert-kr
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pz-bert-kr

This model is a fine-tuned version of [Hanwoon/pz-bert-kr](https://huggingface.co/Hanwoon/bert-kor-base-pz-language-test) on the Multiple datasets.
It achieves the following results on the evaluation set:
- Loss: 2.6540

## Model description

Korean Language Bert Model

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 2.7509        | 1.0   | 10546  | 2.7836          |
| 2.7325        | 2.0   | 21092  | 2.7776          |
| 2.6884        | 3.0   | 31638  | 2.7732          |
| 2.6839        | 4.0   | 42184  | 2.7663          |
| 2.655         | 5.0   | 52730  | 2.7548          |
| 2.6475        | 6.0   | 63276  | 2.7388          |
| 2.6172        | 7.0   | 73822  | 2.7406          |
| 2.6177        | 8.0   | 84368  | 2.7320          |
| 2.5885        | 9.0   | 94914  | 2.7121          |
| 2.5743        | 10.0  | 105460 | 2.7156          |
| 2.5652        | 11.0  | 116006 | 2.7047          |
| 2.5642        | 12.0  | 126552 | 2.6916          |
| 2.5644        | 13.0  | 137098 | 2.7033          |
| 2.5136        | 14.0  | 147644 | 2.6833          |
| 2.532         | 15.0  | 158190 | 2.6742          |
| 2.5224        | 16.0  | 168736 | 2.6702          |
| 2.5268        | 17.0  | 179282 | 2.6661          |
| 2.5077        | 18.0  | 189828 | 2.6629          |
| 2.5061        | 19.0  | 200374 | 2.6657          |
| 2.4853        | 20.0  | 210920 | 2.6540          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1
- Datasets 2.6.1
- Tokenizers 0.13.1

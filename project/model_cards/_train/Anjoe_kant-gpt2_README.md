---
license: mit
tags:
- generated_from_trainer
model-index:
- name: kant-gpt2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# kant-gpt2

This model is a fine-tuned version of [dbmdz/german-gpt2](https://huggingface.co/dbmdz/german-gpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8022

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 22

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 3.3257        | 1.0   | 1825  | 3.2231          |
| 2.9885        | 2.0   | 3650  | 3.0069          |
| 2.7955        | 3.0   | 5475  | 2.8440          |
| 2.5748        | 4.0   | 7300  | 2.7059          |
| 2.3545        | 5.0   | 9125  | 2.5806          |
| 2.1759        | 6.0   | 10950 | 2.4618          |
| 1.9697        | 7.0   | 12775 | 2.3553          |
| 1.7778        | 8.0   | 14600 | 2.2517          |
| 1.6192        | 9.0   | 16425 | 2.1599          |
| 1.4675        | 10.0  | 18250 | 2.0895          |
| 1.3195        | 11.0  | 20075 | 2.0138          |
| 1.2012        | 12.0  | 21900 | 1.9602          |
| 1.0828        | 13.0  | 23725 | 1.9097          |
| 0.9926        | 14.0  | 25550 | 1.8720          |
| 0.9076        | 15.0  | 27375 | 1.8426          |
| 0.8336        | 16.0  | 29200 | 1.8214          |
| 0.7649        | 17.0  | 31025 | 1.8058          |
| 0.7208        | 18.0  | 32850 | 1.7980          |
| 0.6798        | 19.0  | 34675 | 1.7938          |
| 0.647         | 20.0  | 36500 | 1.7969          |
| 0.6226        | 21.0  | 38325 | 1.7975          |
| 0.601         | 22.0  | 40150 | 1.8022          |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Tokenizers 0.12.1

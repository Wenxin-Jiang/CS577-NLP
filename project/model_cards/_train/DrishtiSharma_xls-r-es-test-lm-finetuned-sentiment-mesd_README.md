---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: xls-r-es-test-lm-finetuned-sentiment-mesd
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xls-r-es-test-lm-finetuned-sentiment-mesd

This model is a fine-tuned version of [glob-asr/xls-r-es-test-lm](https://huggingface.co/glob-asr/xls-r-es-test-lm) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7851
- Accuracy: 0.2385


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.25e-05
- train_batch_size: 64
- eval_batch_size: 40
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 0.86  | 3    | 1.7876          | 0.1923   |
| 1.9709        | 1.86  | 6    | 1.7869          | 0.2      |
| 1.9709        | 2.86  | 9    | 1.7859          | 0.2308   |
| 2.146         | 3.86  | 12   | 1.7851          | 0.2385   |
| 1.9622        | 4.86  | 15   | 1.7842          | 0.1923   |
| 1.9622        | 5.86  | 18   | 1.7834          | 0.1769   |
| 2.137         | 6.86  | 21   | 1.7823          | 0.1923   |
| 2.137         | 7.86  | 24   | 1.7812          | 0.1923   |
| 2.1297        | 8.86  | 27   | 1.7800          | 0.1846   |
| 1.9502        | 9.86  | 30   | 1.7787          | 0.1846   |
| 1.9502        | 10.86 | 33   | 1.7772          | 0.1846   |
| 2.1234        | 11.86 | 36   | 1.7760          | 0.1846   |
| 2.1234        | 12.86 | 39   | 1.7748          | 0.1846   |
| 2.1186        | 13.86 | 42   | 1.7736          | 0.1846   |
| 1.9401        | 14.86 | 45   | 1.7725          | 0.1846   |
| 1.9401        | 15.86 | 48   | 1.7715          | 0.1923   |
| 2.112         | 16.86 | 51   | 1.7706          | 0.1923   |
| 2.112         | 17.86 | 54   | 1.7701          | 0.1923   |
| 2.1094        | 18.86 | 57   | 1.7697          | 0.2      |
| 1.934         | 19.86 | 60   | 1.7696          | 0.2      |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

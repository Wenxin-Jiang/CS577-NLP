---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-base-finetuned-sentiment-mesd-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-finetuned-sentiment-mesd-v2

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7213
- Accuracy: 0.3923


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
| No log        | 0.86  | 3    | 1.7961          | 0.1462   |
| 1.9685        | 1.86  | 6    | 1.7932          | 0.1692   |
| 1.9685        | 2.86  | 9    | 1.7891          | 0.2      |
| 2.1386        | 3.86  | 12   | 1.7820          | 0.2923   |
| 1.9492        | 4.86  | 15   | 1.7750          | 0.2923   |
| 1.9492        | 5.86  | 18   | 1.7684          | 0.2846   |
| 2.1143        | 6.86  | 21   | 1.7624          | 0.3231   |
| 2.1143        | 7.86  | 24   | 1.7561          | 0.3308   |
| 2.0945        | 8.86  | 27   | 1.7500          | 0.3462   |
| 1.9121        | 9.86  | 30   | 1.7443          | 0.3385   |
| 1.9121        | 10.86 | 33   | 1.7386          | 0.3231   |
| 2.0682        | 11.86 | 36   | 1.7328          | 0.3231   |
| 2.0682        | 12.86 | 39   | 1.7272          | 0.3769   |
| 2.0527        | 13.86 | 42   | 1.7213          | 0.3923   |
| 1.8705        | 14.86 | 45   | 1.7154          | 0.3846   |
| 1.8705        | 15.86 | 48   | 1.7112          | 0.3846   |
| 2.0263        | 16.86 | 51   | 1.7082          | 0.3769   |
| 2.0263        | 17.86 | 54   | 1.7044          | 0.3846   |
| 2.0136        | 18.86 | 57   | 1.7021          | 0.3846   |
| 1.8429        | 19.86 | 60   | 1.7013          | 0.3846   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-finetuned-code-snippet-quality-scoring
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-code-snippet-quality-scoring

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4070
- Accuracy: 0.8568

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.5353        | 0.13  | 1000  | 0.5110          | 0.7574   |
| 0.4686        | 0.26  | 2000  | 0.4339          | 0.7859   |
| 0.4517        | 0.39  | 3000  | 0.4240          | 0.8002   |
| 0.4263        | 0.52  | 4000  | 0.3906          | 0.8169   |
| 0.4053        | 0.66  | 5000  | 0.3934          | 0.8191   |
| 0.3867        | 0.79  | 6000  | 0.3859          | 0.8253   |
| 0.3906        | 0.92  | 7000  | 0.3936          | 0.8335   |
| 0.3418        | 1.05  | 8000  | 0.3615          | 0.8380   |
| 0.3418        | 1.18  | 9000  | 0.3585          | 0.8400   |
| 0.3307        | 1.31  | 10000 | 0.3520          | 0.8432   |
| 0.3301        | 1.44  | 11000 | 0.3476          | 0.8475   |
| 0.3275        | 1.57  | 12000 | 0.3511          | 0.8497   |
| 0.3192        | 1.71  | 13000 | 0.3519          | 0.8540   |
| 0.3218        | 1.84  | 14000 | 0.3402          | 0.8495   |
| 0.3199        | 1.97  | 15000 | 0.3375          | 0.8580   |
| 0.2591        | 2.1   | 16000 | 0.3687          | 0.8568   |
| 0.2732        | 2.23  | 17000 | 0.3619          | 0.8521   |
| 0.2681        | 2.36  | 18000 | 0.3574          | 0.8563   |
| 0.2606        | 2.49  | 19000 | 0.3404          | 0.8581   |
| 0.2662        | 2.62  | 20000 | 0.3708          | 0.8566   |
| 0.2685        | 2.76  | 21000 | 0.3743          | 0.8591   |
| 0.246         | 2.89  | 22000 | 0.3786          | 0.8531   |
| 0.258         | 3.02  | 23000 | 0.3781          | 0.8578   |
| 0.2284        | 3.15  | 24000 | 0.3938          | 0.8583   |
| 0.2206        | 3.28  | 25000 | 0.4121          | 0.8583   |
| 0.2131        | 3.41  | 26000 | 0.4091          | 0.8575   |
| 0.2181        | 3.54  | 27000 | 0.4264          | 0.8535   |
| 0.2289        | 3.67  | 28000 | 0.3998          | 0.8568   |
| 0.2262        | 3.81  | 29000 | 0.3983          | 0.8580   |
| 0.2095        | 3.94  | 30000 | 0.4070          | 0.8568   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

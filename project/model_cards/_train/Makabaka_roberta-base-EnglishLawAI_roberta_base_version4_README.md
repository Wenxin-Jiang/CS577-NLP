---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-base-EnglishLawAI_roberta_base_version4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-EnglishLawAI_roberta_base_version4

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8089

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 12

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 2.3575        | 1.0   | 23702  | 2.1592          |
| 2.2419        | 2.0   | 47404  | 2.1005          |
| 2.1663        | 3.0   | 71106  | 2.0487          |
| 2.1013        | 4.0   | 94808  | 2.0135          |
| 2.0497        | 5.0   | 118510 | 1.9840          |
| 1.9968        | 6.0   | 142212 | 1.9398          |
| 1.9507        | 7.0   | 165914 | 1.9163          |
| 1.9076        | 8.0   | 189616 | 1.8893          |
| 1.8662        | 9.0   | 213318 | 1.8604          |
| 1.8264        | 10.0  | 237020 | 1.8416          |
| 1.7927        | 11.0  | 260722 | 1.8134          |
| 1.7641        | 12.0  | 284424 | 1.8089          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: t5-base-detox
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-detox

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2615

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.337         | 1.0   | 135  | 0.4810          |
| 0.5238        | 2.0   | 270  | 0.3886          |
| 0.4301        | 3.0   | 405  | 0.3378          |
| 0.3755        | 4.0   | 540  | 0.3122          |
| 0.3359        | 5.0   | 675  | 0.2910          |
| 0.3068        | 6.0   | 810  | 0.2737          |
| 0.2861        | 7.0   | 945  | 0.2710          |
| 0.2744        | 8.0   | 1080 | 0.2617          |
| 0.2649        | 9.0   | 1215 | 0.2630          |
| 0.2585        | 10.0  | 1350 | 0.2615          |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.12.0.dev20220429
- Datasets 2.1.0
- Tokenizers 0.10.3

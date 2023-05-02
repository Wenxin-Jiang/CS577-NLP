---
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: san_2409_1325
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# san_2409_1325

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0992
- F1: 0.7727

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
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 0.91  | 5    | 1.9727          | 0.1939 |
| No log        | 1.91  | 10   | 1.5642          | 0.3535 |
| No log        | 2.91  | 15   | 1.2698          | 0.6818 |
| No log        | 3.91  | 20   | 1.3642          | 0.6429 |
| No log        | 4.91  | 25   | 1.3411          | 0.6818 |
| No log        | 5.91  | 30   | 1.2627          | 0.6818 |
| No log        | 6.91  | 35   | 1.1269          | 0.7727 |
| No log        | 7.91  | 40   | 1.0719          | 0.7727 |
| No log        | 8.91  | 45   | 1.0567          | 0.7727 |
| No log        | 9.91  | 50   | 1.1256          | 0.7727 |
| No log        | 10.91 | 55   | 0.7085          | 0.7727 |
| No log        | 11.91 | 60   | 0.9290          | 0.7727 |
| No log        | 12.91 | 65   | 1.0355          | 0.7727 |
| No log        | 13.91 | 70   | 1.0866          | 0.7727 |
| No log        | 14.91 | 75   | 1.0992          | 0.7727 |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1

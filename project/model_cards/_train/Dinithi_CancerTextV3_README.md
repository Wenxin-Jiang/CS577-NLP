---
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: CancerTextV3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CancerTextV3

This model is a fine-tuned version of [dmis-lab/biobert-base-cased-v1.1](https://huggingface.co/dmis-lab/biobert-base-cased-v1.1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6660
- Accuracy: 0.8658
- Precision: 0.8448
- Recall: 0.8868
- F1: 0.8653

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.4603        | 1.0   | 600  | 0.3671          | 0.8575   | 0.8056    | 0.9314 | 0.8640 |
| 0.3208        | 2.0   | 1200 | 0.3296          | 0.8658   | 0.8613    | 0.8628 | 0.8620 |
| 0.2619        | 3.0   | 1800 | 0.4023          | 0.8667   | 0.8797    | 0.8405 | 0.8596 |
| 0.2125        | 4.0   | 2400 | 0.3948          | 0.8733   | 0.8459    | 0.9039 | 0.8740 |
| 0.1789        | 5.0   | 3000 | 0.4971          | 0.8617   | 0.8243    | 0.9091 | 0.8646 |
| 0.1568        | 6.0   | 3600 | 0.5372          | 0.8633   | 0.8384    | 0.8902 | 0.8636 |
| 0.1332        | 7.0   | 4200 | 0.6037          | 0.865    | 0.8502    | 0.8765 | 0.8632 |
| 0.1176        | 8.0   | 4800 | 0.6255          | 0.8675   | 0.8430    | 0.8937 | 0.8676 |
| 0.1043        | 9.0   | 5400 | 0.6479          | 0.865    | 0.8434    | 0.8868 | 0.8645 |
| 0.096         | 10.0  | 6000 | 0.6660          | 0.8658   | 0.8448    | 0.8868 | 0.8653 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

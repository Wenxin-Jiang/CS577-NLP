---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: hasoc19-microsoft-mdeberta-v3-base-sentiment-new
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hasoc19-microsoft-mdeberta-v3-base-sentiment-new

This model is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3933
- Accuracy: 0.8800
- Precision: 0.8799
- Recall: 0.8800
- F1: 0.8799

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.4517        | 1.0   | 537  | 0.3339          | 0.8616   | 0.8614    | 0.8616 | 0.8614 |
| 0.3101        | 2.0   | 1074 | 0.3144          | 0.8763   | 0.8762    | 0.8763 | 0.8762 |
| 0.2612        | 3.0   | 1611 | 0.3505          | 0.8632   | 0.8651    | 0.8632 | 0.8619 |
| 0.2166        | 4.0   | 2148 | 0.3385          | 0.8747   | 0.8753    | 0.8747 | 0.8749 |
| 0.1939        | 5.0   | 2685 | 0.3794          | 0.8747   | 0.8746    | 0.8747 | 0.8746 |
| 0.1604        | 6.0   | 3222 | 0.3933          | 0.8800   | 0.8799    | 0.8800 | 0.8799 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- clinc_oos
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-finetuned-clinc
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: clinc_oos
      type: clinc_oos
      config: plus
      split: train
      args: plus
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9148387096774193
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-clinc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7720
- Accuracy: 0.9148

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
- train_batch_size: 48
- eval_batch_size: 48
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 4.2942        | 1.0   | 318  | 3.2870          | 0.7539   |
| 2.6283        | 2.0   | 636  | 1.8724          | 0.8368   |
| 1.5478        | 3.0   | 954  | 1.1554          | 0.8961   |
| 1.0103        | 4.0   | 1272 | 0.8562          | 0.9113   |
| 0.7956        | 5.0   | 1590 | 0.7720          | 0.9148   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu102
- Datasets 2.4.0
- Tokenizers 0.12.1

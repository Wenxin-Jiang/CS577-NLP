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
      args: plus
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9174193548387096
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-clinc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7711
- Accuracy: 0.9174

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
| 4.2892        | 1.0   | 318  | 3.2830          | 0.7426   |
| 2.627         | 2.0   | 636  | 1.8728          | 0.8410   |
| 1.5429        | 3.0   | 954  | 1.1555          | 0.8913   |
| 1.0089        | 4.0   | 1272 | 0.8530          | 0.9126   |
| 0.7939        | 5.0   | 1590 | 0.7711          | 0.9174   |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.11.0
- Datasets 1.16.1
- Tokenizers 0.10.3

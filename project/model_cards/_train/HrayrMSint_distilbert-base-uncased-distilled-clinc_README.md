---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- clinc_oos
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-distilled-clinc
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
      value: 0.9429032258064516
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-distilled-clinc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3209
- Accuracy: 0.9429

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
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 3.0228        | 1.0   | 318  | 2.2545          | 0.7548   |
| 1.7605        | 2.0   | 636  | 1.2040          | 0.8513   |
| 0.959         | 3.0   | 954  | 0.6910          | 0.9123   |
| 0.5707        | 4.0   | 1272 | 0.4821          | 0.9294   |
| 0.3877        | 5.0   | 1590 | 0.3890          | 0.9394   |
| 0.3025        | 6.0   | 1908 | 0.3476          | 0.9410   |
| 0.258         | 7.0   | 2226 | 0.3264          | 0.9432   |
| 0.2384        | 8.0   | 2544 | 0.3209          | 0.9429   |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.0
- Datasets 2.2.2
- Tokenizers 0.10.3

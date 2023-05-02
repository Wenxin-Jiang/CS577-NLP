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
      config: plus
      split: validation
      args: plus
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9470967741935484
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-distilled-clinc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1800
- Accuracy: 0.9471

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
- num_epochs: 9

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 318  | 1.1371          | 0.7587   |
| 1.3942        | 2.0   | 636  | 0.5981          | 0.8813   |
| 1.3942        | 3.0   | 954  | 0.3519          | 0.9216   |
| 0.5437        | 4.0   | 1272 | 0.2509          | 0.9368   |
| 0.2651        | 5.0   | 1590 | 0.2124          | 0.9413   |
| 0.2651        | 6.0   | 1908 | 0.1945          | 0.9468   |
| 0.1875        | 7.0   | 2226 | 0.1853          | 0.9477   |
| 0.161         | 8.0   | 2544 | 0.1815          | 0.9474   |
| 0.161         | 9.0   | 2862 | 0.1800          | 0.9471   |


### Framework versions

- Transformers 4.26.1
- Pytorch 1.13.1+cu116
- Datasets 2.9.0
- Tokenizers 0.13.2

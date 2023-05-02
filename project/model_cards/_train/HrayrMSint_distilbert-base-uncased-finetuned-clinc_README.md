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
      value: 0.9135483870967742
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-clinc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7771
- Accuracy: 0.9135

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
| 4.2843        | 1.0   | 318  | 3.2793          | 0.7448   |
| 2.6208        | 2.0   | 636  | 1.8750          | 0.8297   |
| 1.5453        | 3.0   | 954  | 1.1565          | 0.8919   |
| 1.0141        | 4.0   | 1272 | 0.8628          | 0.9090   |
| 0.795         | 5.0   | 1590 | 0.7771          | 0.9135   |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.0
- Datasets 2.2.2
- Tokenizers 0.10.3

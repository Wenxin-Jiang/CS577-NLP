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
      value: 0.9183870967741935
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-clinc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7721
- Accuracy: 0.9184

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
| No log        | 1.0   | 318  | 3.2890          | 0.7432   |
| 3.7868        | 2.0   | 636  | 1.8756          | 0.8377   |
| 3.7868        | 3.0   | 954  | 1.1572          | 0.8961   |
| 1.6929        | 4.0   | 1272 | 0.8573          | 0.9132   |
| 0.9058        | 5.0   | 1590 | 0.7721          | 0.9184   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

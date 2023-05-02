---
tags:
- generated_from_trainer
datasets:
- klue
metrics:
- accuracy
model-index:
- name: bert-base-finetuned-nli
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: klue
      type: klue
      args: nli
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.085
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-finetuned-nli

This model is a fine-tuned version of [klue/bert-base](https://huggingface.co/klue/bert-base) on the klue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6210
- Accuracy: 0.085

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
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 196  | 0.6210          | 0.085    |
| No log        | 2.0   | 392  | 0.5421          | 0.0643   |
| 0.5048        | 3.0   | 588  | 0.5523          | 0.062    |
| 0.5048        | 4.0   | 784  | 0.5769          | 0.0533   |
| 0.5048        | 5.0   | 980  | 0.5959          | 0.052    |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0

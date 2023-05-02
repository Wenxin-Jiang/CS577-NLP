---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
datasets:
- cord-layoutlmv3
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: layoutlmv3-finetuned-cord_100
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: cord-layoutlmv3
      type: cord-layoutlmv3
      config: cord
      split: train
      args: cord
    metrics:
    - name: Precision
      type: precision
      value: 0.9415247964470762
    - name: Recall
      type: recall
      value: 0.9520958083832335
    - name: F1
      type: f1
      value: 0.9467807964272422
    - name: Accuracy
      type: accuracy
      value: 0.9575551782682513
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-finetuned-cord_100

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the cord-layoutlmv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2246
- Precision: 0.9415
- Recall: 0.9521
- F1: 0.9468
- Accuracy: 0.9576

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
- train_batch_size: 5
- eval_batch_size: 5
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 2500

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.56  | 250  | 1.0265          | 0.7630    | 0.8099 | 0.7858 | 0.8086   |
| 1.4021        | 3.12  | 500  | 0.5804          | 0.8290    | 0.8638 | 0.8460 | 0.8718   |
| 1.4021        | 4.69  | 750  | 0.3937          | 0.8882    | 0.9034 | 0.8957 | 0.9126   |
| 0.4062        | 6.25  | 1000 | 0.3171          | 0.9137    | 0.9274 | 0.9205 | 0.9351   |
| 0.4062        | 7.81  | 1250 | 0.2798          | 0.9332    | 0.9409 | 0.9370 | 0.9444   |
| 0.2212        | 9.38  | 1500 | 0.2558          | 0.9277    | 0.9416 | 0.9346 | 0.9461   |
| 0.2212        | 10.94 | 1750 | 0.2479          | 0.9335    | 0.9454 | 0.9394 | 0.9516   |
| 0.1525        | 12.5  | 2000 | 0.2356          | 0.9444    | 0.9536 | 0.9490 | 0.9588   |
| 0.1525        | 14.06 | 2250 | 0.2286          | 0.9365    | 0.9491 | 0.9428 | 0.9563   |
| 0.1134        | 15.62 | 2500 | 0.2246          | 0.9415    | 0.9521 | 0.9468 | 0.9576   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

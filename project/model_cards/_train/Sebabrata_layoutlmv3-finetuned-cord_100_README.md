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
      value: 0.9385640266469282
    - name: Recall
      type: recall
      value: 0.9491017964071856
    - name: F1
      type: f1
      value: 0.9438034983252697
    - name: Accuracy
      type: accuracy
      value: 0.9516129032258065
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-finetuned-cord_100

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the cord-layoutlmv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2144
- Precision: 0.9386
- Recall: 0.9491
- F1: 0.9438
- Accuracy: 0.9516

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
| No log        | 1.56  | 250  | 1.0830          | 0.6854    | 0.7582 | 0.7200 | 0.7725   |
| 1.4266        | 3.12  | 500  | 0.5944          | 0.8379    | 0.8630 | 0.8503 | 0.8680   |
| 1.4266        | 4.69  | 750  | 0.3868          | 0.8828    | 0.9079 | 0.8952 | 0.9155   |
| 0.4084        | 6.25  | 1000 | 0.3146          | 0.9133    | 0.9304 | 0.9218 | 0.9338   |
| 0.4084        | 7.81  | 1250 | 0.2658          | 0.9240    | 0.9371 | 0.9305 | 0.9419   |
| 0.2139        | 9.38  | 1500 | 0.2432          | 0.9299    | 0.9439 | 0.9368 | 0.9474   |
| 0.2139        | 10.94 | 1750 | 0.2333          | 0.9291    | 0.9416 | 0.9353 | 0.9482   |
| 0.1478        | 12.5  | 2000 | 0.2098          | 0.9358    | 0.9491 | 0.9424 | 0.9529   |
| 0.1478        | 14.06 | 2250 | 0.2134          | 0.9379    | 0.9491 | 0.9435 | 0.9516   |
| 0.1124        | 15.62 | 2500 | 0.2144          | 0.9386    | 0.9491 | 0.9438 | 0.9516   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1

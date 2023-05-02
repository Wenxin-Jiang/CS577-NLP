---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article250v6_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_250v6_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article250v6_wikigold_split
      type: article250v6_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6596500820120285
    - name: Recall
      type: recall
      value: 0.6778089887640449
    - name: F1
      type: f1
      value: 0.6686062621224717
    - name: Accuracy
      type: accuracy
      value: 0.9273733137978073
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_250v6_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article250v6_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2146
- Precision: 0.6597
- Recall: 0.6778
- F1: 0.6686
- Accuracy: 0.9274

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 72   | 0.2332          | 0.5912    | 0.6053 | 0.5982 | 0.9199   |
| No log        | 2.0   | 144  | 0.2202          | 0.6511    | 0.6638 | 0.6574 | 0.9240   |
| No log        | 3.0   | 216  | 0.2146          | 0.6597    | 0.6778 | 0.6686 | 0.9274   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

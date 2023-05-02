---
license: mit
tags:
- generated_from_trainer
datasets:
- wnut_17
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: microsoft-deberta-v3-large_ner_wnut_17
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wnut_17
      type: wnut_17
      args: wnut_17
    metrics:
    - name: Precision
      type: precision
      value: 0.7670623145400594
    - name: Recall
      type: recall
      value: 0.618421052631579
    - name: F1
      type: f1
      value: 0.6847682119205298
    - name: Accuracy
      type: accuracy
      value: 0.9666942096230853
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# microsoft-deberta-v3-large_ner_wnut_17

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the wnut_17 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2199
- Precision: 0.7671
- Recall: 0.6184
- F1: 0.6848
- Accuracy: 0.9667

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 213  | 0.1751          | 0.6884    | 0.5682 | 0.6225 | 0.9601   |
| No log        | 2.0   | 426  | 0.1702          | 0.7351    | 0.6208 | 0.6732 | 0.9655   |
| 0.1003        | 3.0   | 639  | 0.1954          | 0.7360    | 0.6136 | 0.6693 | 0.9656   |
| 0.1003        | 4.0   | 852  | 0.2113          | 0.7595    | 0.6232 | 0.6846 | 0.9669   |
| 0.015         | 5.0   | 1065 | 0.2199          | 0.7671    | 0.6184 | 0.6848 | 0.9667   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

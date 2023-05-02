---
license: mit
tags:
- generated_from_trainer
datasets:
- wikiann
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: microsoft-deberta-v3-large_ner_wikiann
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wikiann
      type: wikiann
      config: en
      split: train
      args: en
    metrics:
    - name: Precision
      type: precision
      value: 0.8557286258220838
    - name: Recall
      type: recall
      value: 0.8738159196946134
    - name: F1
      type: f1
      value: 0.8646776957783918
    - name: Accuracy
      type: accuracy
      value: 0.9406352438660972
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# microsoft-deberta-v3-large_ner_wikiann

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3108
- Precision: 0.8557
- Recall: 0.8738
- F1: 0.8647
- Accuracy: 0.9406

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
| 0.3005        | 1.0   | 1250 | 0.2462          | 0.8205    | 0.8400 | 0.8301 | 0.9294   |
| 0.1931        | 2.0   | 2500 | 0.2247          | 0.8448    | 0.8630 | 0.8538 | 0.9386   |
| 0.1203        | 3.0   | 3750 | 0.2341          | 0.8468    | 0.8693 | 0.8579 | 0.9403   |
| 0.0635        | 4.0   | 5000 | 0.2948          | 0.8596    | 0.8745 | 0.8670 | 0.9411   |
| 0.0451        | 5.0   | 6250 | 0.3108          | 0.8557    | 0.8738 | 0.8647 | 0.9406   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2

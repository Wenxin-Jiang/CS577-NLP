---
license: apache-2.0
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
- name: albert-large-v2_ner_wikiann
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wikiann
      type: wikiann
      args: en
    metrics:
    - name: Precision
      type: precision
      value: 0.8239671720684378
    - name: Recall
      type: recall
      value: 0.8374805598755832
    - name: F1
      type: f1
      value: 0.8306689103912495
    - name: Accuracy
      type: accuracy
      value: 0.926951922121784
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-large-v2_ner_wikiann

This model is a fine-tuned version of [albert-large-v2](https://huggingface.co/albert-large-v2) on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3416
- Precision: 0.8240
- Recall: 0.8375
- F1: 0.8307
- Accuracy: 0.9270

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.3451        | 1.0   | 2500  | 0.3555          | 0.7745    | 0.7850 | 0.7797 | 0.9067   |
| 0.2995        | 2.0   | 5000  | 0.2927          | 0.7932    | 0.8240 | 0.8083 | 0.9205   |
| 0.252         | 3.0   | 7500  | 0.2936          | 0.8094    | 0.8236 | 0.8164 | 0.9239   |
| 0.1676        | 4.0   | 10000 | 0.3302          | 0.8256    | 0.8359 | 0.8307 | 0.9268   |
| 0.1489        | 5.0   | 12500 | 0.3416          | 0.8240    | 0.8375 | 0.8307 | 0.9270   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

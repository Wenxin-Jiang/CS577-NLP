---
license: apache-2.0
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
- name: albert-large-v2_ner_wnut_17
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
      value: 0.7445742904841403
    - name: Recall
      type: recall
      value: 0.5334928229665071
    - name: F1
      type: f1
      value: 0.621602787456446
    - name: Accuracy
      type: accuracy
      value: 0.9581637843336724
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-large-v2_ner_wnut_17

This model is a fine-tuned version of [albert-large-v2](https://huggingface.co/albert-large-v2) on the wnut_17 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2429
- Precision: 0.7446
- Recall: 0.5335
- F1: 0.6216
- Accuracy: 0.9582

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
| No log        | 1.0   | 213  | 0.3051          | 0.7929    | 0.3206 | 0.4566 | 0.9410   |
| No log        | 2.0   | 426  | 0.2151          | 0.7443    | 0.4665 | 0.5735 | 0.9516   |
| 0.17          | 3.0   | 639  | 0.2310          | 0.7364    | 0.5012 | 0.5964 | 0.9559   |
| 0.17          | 4.0   | 852  | 0.2387          | 0.7564    | 0.5311 | 0.6240 | 0.9578   |
| 0.0587        | 5.0   | 1065 | 0.2429          | 0.7446    | 0.5335 | 0.6216 | 0.9582   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

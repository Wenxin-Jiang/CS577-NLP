---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: distilbert-base-uncased-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      config: conll2003
      split: train
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9266725742135579
    - name: Recall
      type: recall
      value: 0.9358988701197002
    - name: F1
      type: f1
      value: 0.9312628708187232
    - name: Accuracy
      type: accuracy
      value: 0.9835734824534926
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0625
- Precision: 0.9267
- Recall: 0.9359
- F1: 0.9313
- Accuracy: 0.9836

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
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2395        | 1.0   | 878  | 0.0709          | 0.9148    | 0.9186 | 0.9167 | 0.9809   |
| 0.0538        | 2.0   | 1756 | 0.0628          | 0.9228    | 0.9332 | 0.9280 | 0.9828   |
| 0.03          | 3.0   | 2634 | 0.0625          | 0.9267    | 0.9359 | 0.9313 | 0.9836   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
datasets:
- skript
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: wikineural-multilingual-ner-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: skript
      type: skript
      config: myscript
      split: train
      args: myscript
    metrics:
    - name: Precision
      type: precision
      value: 0.9007335298553506
    - name: Recall
      type: recall
      value: 0.9301946902654867
    - name: F1
      type: f1
      value: 0.9152270827528559
    - name: Accuracy
      type: accuracy
      value: 0.9653644982020269
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wikineural-multilingual-ner-finetuned-ner

This model is a fine-tuned version of [Babelscape/wikineural-multilingual-ner](https://huggingface.co/Babelscape/wikineural-multilingual-ner) on the skript dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1243
- Precision: 0.9007
- Recall: 0.9302
- F1: 0.9152
- Accuracy: 0.9654

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
| No log        | 1.0   | 298  | 0.1179          | 0.8975    | 0.8981 | 0.8978 | 0.9592   |
| 0.104         | 2.0   | 596  | 0.1161          | 0.9051    | 0.9201 | 0.9126 | 0.9648   |
| 0.104         | 3.0   | 894  | 0.1243          | 0.9007    | 0.9302 | 0.9152 | 0.9654   |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

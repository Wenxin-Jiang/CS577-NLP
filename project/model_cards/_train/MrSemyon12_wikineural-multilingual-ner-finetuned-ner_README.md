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
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9013505175841503
    - name: Recall
      type: recall
      value: 0.9308318584070796
    - name: F1
      type: f1
      value: 0.9158539983282251
    - name: Accuracy
      type: accuracy
      value: 0.9658385093167702
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wikineural-multilingual-ner-finetuned-ner

This model is a fine-tuned version of [Babelscape/wikineural-multilingual-ner](https://huggingface.co/Babelscape/wikineural-multilingual-ner) on the skript dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1219
- Precision: 0.9014
- Recall: 0.9308
- F1: 0.9159
- Accuracy: 0.9658

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
| No log        | 1.0   | 298  | 0.1208          | 0.9016    | 0.8988 | 0.9002 | 0.9604   |
| 0.118         | 2.0   | 596  | 0.1152          | 0.9016    | 0.9210 | 0.9112 | 0.9645   |
| 0.118         | 3.0   | 894  | 0.1219          | 0.9014    | 0.9308 | 0.9159 | 0.9658   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

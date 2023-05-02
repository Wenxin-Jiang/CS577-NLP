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
- name: bert-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9329136988570482
    - name: Recall
      type: recall
      value: 0.9478290138000673
    - name: F1
      type: f1
      value: 0.9403122130394858
    - name: Accuracy
      type: accuracy
      value: 0.9855477718255137
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0663
- Precision: 0.9329
- Recall: 0.9478
- F1: 0.9403
- Accuracy: 0.9855

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
| 0.0837        | 1.0   | 1756 | 0.0656          | 0.9151    | 0.9392 | 0.9270 | 0.9834   |
| 0.0388        | 2.0   | 3512 | 0.0619          | 0.9249    | 0.9475 | 0.9361 | 0.9855   |
| 0.0198        | 3.0   | 5268 | 0.0663          | 0.9329    | 0.9478 | 0.9403 | 0.9855   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

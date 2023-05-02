---
license: mit
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
- name: microsoft-deberta-v3-large_ner_conll2003
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
      value: 0.9667057052032793
    - name: Recall
      type: recall
      value: 0.972399865365197
    - name: F1
      type: f1
      value: 0.9695444248678582
    - name: Accuracy
      type: accuracy
      value: 0.9945095595965889
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# microsoft-deberta-v3-large_ner_conll2003

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0293
- Precision: 0.9667
- Recall: 0.9724
- F1: 0.9695
- Accuracy: 0.9945

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
| 0.0986        | 1.0   | 878  | 0.0323          | 0.9453    | 0.9596 | 0.9524 | 0.9921   |
| 0.0212        | 2.0   | 1756 | 0.0270          | 0.9571    | 0.9675 | 0.9623 | 0.9932   |
| 0.009         | 3.0   | 2634 | 0.0280          | 0.9638    | 0.9714 | 0.9676 | 0.9940   |
| 0.0035        | 4.0   | 3512 | 0.0290          | 0.9657    | 0.9712 | 0.9685 | 0.9943   |
| 0.0022        | 5.0   | 4390 | 0.0293          | 0.9667    | 0.9724 | 0.9695 | 0.9945   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

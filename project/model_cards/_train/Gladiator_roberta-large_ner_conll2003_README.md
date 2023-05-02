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
- name: roberta-large_ner_conll2003
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
      value: 0.9622389306599833
    - name: Recall
      type: recall
      value: 0.9692022887916526
    - name: F1
      type: f1
      value: 0.9657080573488722
    - name: Accuracy
      type: accuracy
      value: 0.9939449398387913
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large_ner_conll2003

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0345
- Precision: 0.9622
- Recall: 0.9692
- F1: 0.9657
- Accuracy: 0.9939

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
| 0.1227        | 1.0   | 878  | 0.0431          | 0.9511    | 0.9559 | 0.9535 | 0.9914   |
| 0.0295        | 2.0   | 1756 | 0.0334          | 0.9541    | 0.9657 | 0.9599 | 0.9930   |
| 0.0163        | 3.0   | 2634 | 0.0327          | 0.9616    | 0.9682 | 0.9649 | 0.9938   |
| 0.0073        | 4.0   | 3512 | 0.0342          | 0.9624    | 0.9692 | 0.9658 | 0.9939   |
| 0.0042        | 5.0   | 4390 | 0.0345          | 0.9622    | 0.9692 | 0.9657 | 0.9939   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

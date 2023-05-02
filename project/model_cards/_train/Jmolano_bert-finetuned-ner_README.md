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
      config: conll2003
      split: train
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9327383903487027
    - name: Recall
      type: recall
      value: 0.9498485358465163
    - name: F1
      type: f1
      value: 0.9412157091636788
    - name: Accuracy
      type: accuracy
      value: 0.9860923058809677
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0617
- Precision: 0.9327
- Recall: 0.9498
- F1: 0.9412
- Accuracy: 0.9861

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
| 0.0868        | 1.0   | 1756 | 0.0697          | 0.9204    | 0.9297 | 0.9250 | 0.9807   |
| 0.0342        | 2.0   | 3512 | 0.0647          | 0.9273    | 0.9465 | 0.9368 | 0.9853   |
| 0.0175        | 3.0   | 5268 | 0.0617          | 0.9327    | 0.9498 | 0.9412 | 0.9861   |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

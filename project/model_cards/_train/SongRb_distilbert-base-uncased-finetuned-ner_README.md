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
model_index:
- name: distilbert-base-uncased-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      args: conll2003
    metric:
      name: Accuracy
      type: accuracy
      value: 0.9850826886110537
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0746
- Precision: 0.9347
- Recall: 0.9426
- F1: 0.9386
- Accuracy: 0.9851

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0832        | 1.0   | 3511  | 0.0701          | 0.9317    | 0.9249 | 0.9283 | 0.9827   |
| 0.0384        | 2.0   | 7022  | 0.0701          | 0.9282    | 0.9410 | 0.9346 | 0.9845   |
| 0.0222        | 3.0   | 10533 | 0.0746          | 0.9347    | 0.9426 | 0.9386 | 0.9851   |


### Framework versions

- Transformers 4.10.0.dev0
- Pytorch 1.8.1
- Datasets 1.11.0
- Tokenizers 0.10.3

---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: distilbert-base-uncased-finetuned-ner-invoiceSenderName
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner-invoiceSenderName

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0254
- Precision: 0.0
- Recall: 0.0
- F1: 0.0
- Accuracy: 0.9924

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
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1  | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:---:|:--------:|
| 0.0306        | 1.0   | 1956 | 0.0273          | 0.0       | 0.0    | 0.0 | 0.9901   |
| 0.0195        | 2.0   | 3912 | 0.0240          | 0.0       | 0.0    | 0.0 | 0.9914   |
| 0.0143        | 3.0   | 5868 | 0.0251          | 0.0       | 0.0    | 0.0 | 0.9921   |
| 0.0107        | 4.0   | 7824 | 0.0254          | 0.0       | 0.0    | 0.0 | 0.9924   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1
- Datasets 2.3.2
- Tokenizers 0.10.3

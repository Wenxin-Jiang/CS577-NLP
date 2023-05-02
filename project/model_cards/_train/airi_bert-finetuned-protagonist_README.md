---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-protagonist
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-protagonist

This model is a fine-tuned version of [Davlan/bert-base-multilingual-cased-ner-hrl](https://huggingface.co/Davlan/bert-base-multilingual-cased-ner-hrl) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0745
- Precision: 0.8392
- Recall: 0.7767
- F1: 0.8068
- Accuracy: 0.9863

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 106  | 0.0695          | 0.8251    | 0.8558 | 0.8402 | 0.9870   |
| No log        | 2.0   | 212  | 0.0667          | 0.8244    | 0.7860 | 0.8048 | 0.9857   |
| No log        | 3.0   | 318  | 0.0624          | 0.86      | 0.8    | 0.8289 | 0.9870   |
| No log        | 4.0   | 424  | 0.0698          | 0.8357    | 0.8047 | 0.8199 | 0.9867   |
| 0.0074        | 5.0   | 530  | 0.0745          | 0.8392    | 0.7767 | 0.8068 | 0.9863   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1

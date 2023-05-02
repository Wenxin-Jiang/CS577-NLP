---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-ADEs_model_1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ADEs_model_1

This model is a fine-tuned version of [jsylee/scibert_scivocab_uncased-finetuned-ner](https://huggingface.co/jsylee/scibert_scivocab_uncased-finetuned-ner) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1938
- Precision: 0.6759
- Recall: 0.6710
- F1: 0.6735
- Accuracy: 0.9132

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-07
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1987        | 1.0   | 640  | 0.1989          | 0.6618    | 0.6692 | 0.6655 | 0.9116   |
| 0.1954        | 2.0   | 1280 | 0.1953          | 0.6710    | 0.6532 | 0.6620 | 0.9132   |
| 0.1934        | 3.0   | 1920 | 0.1961          | 0.6586    | 0.6823 | 0.6702 | 0.9120   |
| 0.1879        | 4.0   | 2560 | 0.1940          | 0.6727    | 0.6718 | 0.6722 | 0.9133   |
| 0.1897        | 5.0   | 3200 | 0.1938          | 0.6759    | 0.6710 | 0.6735 | 0.9132   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1

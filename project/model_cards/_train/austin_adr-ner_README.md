---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: adr-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# adr-ner

This model is a fine-tuned version of [austin/Austin-MeDeBERTa](https://huggingface.co/austin/Austin-MeDeBERTa) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0434
- Precision: 0.7305
- Recall: 0.6934
- F1: 0.7115
- Accuracy: 0.9941

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 12
- eval_batch_size: 12
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 107  | 0.0630          | 0.0       | 0.0    | 0.0    | 0.9876   |
| No log        | 2.0   | 214  | 0.0308          | 0.4282    | 0.3467 | 0.3832 | 0.9900   |
| No log        | 3.0   | 321  | 0.0254          | 0.5544    | 0.5603 | 0.5573 | 0.9920   |
| No log        | 4.0   | 428  | 0.0280          | 0.6430    | 0.5751 | 0.6071 | 0.9929   |
| 0.0465        | 5.0   | 535  | 0.0266          | 0.5348    | 0.7146 | 0.6118 | 0.9915   |
| 0.0465        | 6.0   | 642  | 0.0423          | 0.7632    | 0.5793 | 0.6587 | 0.9939   |
| 0.0465        | 7.0   | 749  | 0.0336          | 0.6957    | 0.6765 | 0.6860 | 0.9939   |
| 0.0465        | 8.0   | 856  | 0.0370          | 0.6876    | 0.6702 | 0.6788 | 0.9936   |
| 0.0465        | 9.0   | 963  | 0.0349          | 0.6555    | 0.7040 | 0.6789 | 0.9932   |
| 0.0044        | 10.0  | 1070 | 0.0403          | 0.6910    | 0.6808 | 0.6858 | 0.9938   |
| 0.0044        | 11.0  | 1177 | 0.0415          | 0.7140    | 0.6808 | 0.6970 | 0.9939   |
| 0.0044        | 12.0  | 1284 | 0.0440          | 0.7349    | 0.6681 | 0.6999 | 0.9941   |
| 0.0044        | 13.0  | 1391 | 0.0423          | 0.7097    | 0.6977 | 0.7036 | 0.9941   |
| 0.0044        | 14.0  | 1498 | 0.0435          | 0.7174    | 0.6977 | 0.7074 | 0.9941   |
| 0.0006        | 15.0  | 1605 | 0.0434          | 0.7305    | 0.6934 | 0.7115 | 0.9941   |


### Framework versions

- Transformers 4.14.1
- Pytorch 1.10.0+cu113
- Datasets 1.16.1
- Tokenizers 0.10.3

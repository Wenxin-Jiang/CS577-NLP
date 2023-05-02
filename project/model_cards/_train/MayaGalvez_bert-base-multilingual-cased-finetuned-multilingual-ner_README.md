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
- name: bert-base-multilingual-cased-finetuned-multilingual-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-multilingual-cased-finetuned-multilingual-ner

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2352
- Precision: 0.8109
- Recall: 0.8332
- F1: 0.8219
- Accuracy: 0.9264

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.7301        | 0.16  | 100  | 0.3827          | 0.6189    | 0.7009 | 0.6573 | 0.8734   |
| 0.3841        | 0.32  | 200  | 0.3195          | 0.7057    | 0.7511 | 0.7277 | 0.8922   |
| 0.3451        | 0.48  | 300  | 0.2862          | 0.7094    | 0.7750 | 0.7407 | 0.8952   |
| 0.3187        | 0.65  | 400  | 0.2735          | 0.7372    | 0.7802 | 0.7581 | 0.9019   |
| 0.3058        | 0.81  | 500  | 0.2533          | 0.7536    | 0.8015 | 0.7768 | 0.9052   |
| 0.2918        | 0.97  | 600  | 0.2458          | 0.7587    | 0.8085 | 0.7828 | 0.9126   |
| 0.2425        | 1.13  | 700  | 0.2379          | 0.7742    | 0.7976 | 0.7857 | 0.9150   |
| 0.2387        | 1.29  | 800  | 0.2300          | 0.7772    | 0.8108 | 0.7936 | 0.9165   |
| 0.2125        | 1.45  | 900  | 0.2387          | 0.7900    | 0.8130 | 0.8014 | 0.9180   |
| 0.2026        | 1.62  | 1000 | 0.2317          | 0.7877    | 0.8152 | 0.8012 | 0.9186   |
| 0.1963        | 1.78  | 1100 | 0.2326          | 0.7842    | 0.8269 | 0.8049 | 0.9220   |
| 0.2052        | 1.94  | 1200 | 0.2247          | 0.7924    | 0.8234 | 0.8076 | 0.9212   |
| 0.1868        | 2.1   | 1300 | 0.2410          | 0.7903    | 0.8282 | 0.8088 | 0.9204   |
| 0.1556        | 2.26  | 1400 | 0.2428          | 0.8064    | 0.8317 | 0.8189 | 0.9256   |
| 0.153         | 2.42  | 1500 | 0.2316          | 0.8017    | 0.8282 | 0.8147 | 0.9238   |
| 0.1484        | 2.58  | 1600 | 0.2379          | 0.8054    | 0.8338 | 0.8194 | 0.9258   |
| 0.137         | 2.75  | 1700 | 0.2331          | 0.8101    | 0.8324 | 0.8211 | 0.9270   |
| 0.1638        | 2.91  | 1800 | 0.2352          | 0.8109    | 0.8332 | 0.8219 | 0.9264   |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu102
- Datasets 2.4.0
- Tokenizers 0.12.1

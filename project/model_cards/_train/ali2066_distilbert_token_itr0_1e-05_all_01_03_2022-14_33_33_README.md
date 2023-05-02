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
- name: distilbert_token_itr0_1e-05_all_01_03_2022-14_33_33
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert_token_itr0_1e-05_all_01_03_2022-14_33_33

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3255
- Precision: 0.1412
- Recall: 0.25
- F1: 0.1805
- Accuracy: 0.8491

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 30   | 0.4549          | 0.0228    | 0.0351 | 0.0276 | 0.7734   |
| No log        | 2.0   | 60   | 0.3577          | 0.0814    | 0.1260 | 0.0989 | 0.8355   |
| No log        | 3.0   | 90   | 0.3116          | 0.1534    | 0.2648 | 0.1943 | 0.8611   |
| No log        | 4.0   | 120  | 0.2975          | 0.1792    | 0.2967 | 0.2234 | 0.8690   |
| No log        | 5.0   | 150  | 0.2935          | 0.1873    | 0.2998 | 0.2305 | 0.8715   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

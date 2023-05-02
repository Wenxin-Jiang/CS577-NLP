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
- name: finetuned_token_itr0_2e-05_all_16_02_2022-20_09_36
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_2e-05_all_16_02_2022-20_09_36

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1743
- Precision: 0.3429
- Recall: 0.3430
- F1: 0.3430
- Accuracy: 0.9446

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 38   | 0.3322          | 0.0703    | 0.1790 | 0.1010 | 0.8318   |
| No log        | 2.0   | 76   | 0.2644          | 0.1180    | 0.2343 | 0.1570 | 0.8909   |
| No log        | 3.0   | 114  | 0.2457          | 0.1624    | 0.2583 | 0.1994 | 0.8980   |
| No log        | 4.0   | 152  | 0.2487          | 0.1486    | 0.2583 | 0.1887 | 0.8931   |
| No log        | 5.0   | 190  | 0.2395          | 0.1670    | 0.2694 | 0.2062 | 0.8988   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

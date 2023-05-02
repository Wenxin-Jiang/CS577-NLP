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
- name: finetuned_token_2e-05_16_02_2022-01_30_30
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_2e-05_16_02_2022-01_30_30

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1748
- Precision: 0.3384
- Recall: 0.3492
- F1: 0.3437
- Accuracy: 0.9442

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
| No log        | 1.0   | 38   | 0.3180          | 0.0985    | 0.1648 | 0.1233 | 0.8643   |
| No log        | 2.0   | 76   | 0.2667          | 0.1962    | 0.2698 | 0.2272 | 0.8926   |
| No log        | 3.0   | 114  | 0.2374          | 0.2268    | 0.3005 | 0.2585 | 0.9062   |
| No log        | 4.0   | 152  | 0.2305          | 0.2248    | 0.3247 | 0.2657 | 0.9099   |
| No log        | 5.0   | 190  | 0.2289          | 0.2322    | 0.3166 | 0.2679 | 0.9102   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

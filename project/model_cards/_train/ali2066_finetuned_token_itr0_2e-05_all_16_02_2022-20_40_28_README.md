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
- name: finetuned_token_itr0_2e-05_all_16_02_2022-20_40_28
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_2e-05_all_16_02_2022-20_40_28

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1736
- Precision: 0.3358
- Recall: 0.3447
- F1: 0.3402
- Accuracy: 0.9452

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
| No log        | 1.0   | 38   | 0.3058          | 0.1200    | 0.2102 | 0.1528 | 0.8629   |
| No log        | 2.0   | 76   | 0.2488          | 0.1605    | 0.2774 | 0.2034 | 0.9003   |
| No log        | 3.0   | 114  | 0.2296          | 0.1947    | 0.2880 | 0.2324 | 0.9057   |
| No log        | 4.0   | 152  | 0.2208          | 0.2201    | 0.2986 | 0.2534 | 0.9113   |
| No log        | 5.0   | 190  | 0.2235          | 0.2110    | 0.3039 | 0.2491 | 0.9101   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

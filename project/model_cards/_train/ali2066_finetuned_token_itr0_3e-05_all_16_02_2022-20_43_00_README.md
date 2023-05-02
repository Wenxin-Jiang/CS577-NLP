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
- name: finetuned_token_itr0_3e-05_all_16_02_2022-20_43_00
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_3e-05_all_16_02_2022-20_43_00

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1626
- Precision: 0.3811
- Recall: 0.3865
- F1: 0.3838
- Accuracy: 0.9482

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 38   | 0.3697          | 0.0933    | 0.2235 | 0.1317 | 0.8259   |
| No log        | 2.0   | 76   | 0.3193          | 0.1266    | 0.2948 | 0.1771 | 0.8494   |
| No log        | 3.0   | 114  | 0.3025          | 0.1606    | 0.3160 | 0.2130 | 0.8540   |
| No log        | 4.0   | 152  | 0.2978          | 0.1867    | 0.3449 | 0.2422 | 0.8605   |
| No log        | 5.0   | 190  | 0.2984          | 0.1706    | 0.3507 | 0.2295 | 0.8551   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

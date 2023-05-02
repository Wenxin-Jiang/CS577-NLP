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
- name: finetuned_token_itr0_3e-05_all_16_02_2022-21_11_08
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_3e-05_all_16_02_2022-21_11_08

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2731
- Precision: 0.1928
- Recall: 0.3457
- F1: 0.2475
- Accuracy: 0.8826

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
| No log        | 1.0   | 30   | 0.3010          | 0.1330    | 0.2345 | 0.1697 | 0.8707   |
| No log        | 2.0   | 60   | 0.2446          | 0.1739    | 0.2948 | 0.2188 | 0.8949   |
| No log        | 3.0   | 90   | 0.2235          | 0.2446    | 0.3032 | 0.2708 | 0.9080   |
| No log        | 4.0   | 120  | 0.2226          | 0.2670    | 0.3350 | 0.2972 | 0.9058   |
| No log        | 5.0   | 150  | 0.2166          | 0.2779    | 0.3417 | 0.3065 | 0.9063   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

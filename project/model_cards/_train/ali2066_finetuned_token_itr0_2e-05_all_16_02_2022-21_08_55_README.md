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
- name: finetuned_token_itr0_2e-05_all_16_02_2022-21_08_55
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_2e-05_all_16_02_2022-21_08_55

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2853
- Precision: 0.1677
- Recall: 0.3106
- F1: 0.2178
- Accuracy: 0.8755

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
| No log        | 1.0   | 30   | 0.3452          | 0.0526    | 0.1055 | 0.0702 | 0.8507   |
| No log        | 2.0   | 60   | 0.2598          | 0.1575    | 0.2680 | 0.1984 | 0.8909   |
| No log        | 3.0   | 90   | 0.2398          | 0.1866    | 0.2982 | 0.2295 | 0.9007   |
| No log        | 4.0   | 120  | 0.2354          | 0.1949    | 0.3049 | 0.2378 | 0.9002   |
| No log        | 5.0   | 150  | 0.2314          | 0.2026    | 0.3166 | 0.2471 | 0.9004   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

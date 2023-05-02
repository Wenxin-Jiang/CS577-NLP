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
- name: finetuned_token_2e-05_all_16_02_2022-15_41_15
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_2e-05_all_16_02_2022-15_41_15

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1742
- Precision: 0.3447
- Recall: 0.3410
- F1: 0.3428
- Accuracy: 0.9455

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
| No log        | 1.0   | 38   | 0.3692          | 0.0868    | 0.2030 | 0.1216 | 0.8238   |
| No log        | 2.0   | 76   | 0.3198          | 0.1674    | 0.3029 | 0.2157 | 0.8567   |
| No log        | 3.0   | 114  | 0.3156          | 0.1520    | 0.3096 | 0.2039 | 0.8510   |
| No log        | 4.0   | 152  | 0.3129          | 0.1753    | 0.3266 | 0.2281 | 0.8500   |
| No log        | 5.0   | 190  | 0.3038          | 0.1716    | 0.3401 | 0.2281 | 0.8595   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

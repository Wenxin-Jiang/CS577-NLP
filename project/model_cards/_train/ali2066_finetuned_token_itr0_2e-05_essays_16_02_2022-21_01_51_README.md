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
- name: finetuned_token_itr0_2e-05_essays_16_02_2022-21_01_51
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_2e-05_essays_16_02_2022-21_01_51

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2525
- Precision: 0.3997
- Recall: 0.5117
- F1: 0.4488
- Accuracy: 0.9115

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
| No log        | 1.0   | 11   | 0.4652          | 0.1528    | 0.3588 | 0.2144 | 0.7851   |
| No log        | 2.0   | 22   | 0.3646          | 0.2913    | 0.4847 | 0.3639 | 0.8521   |
| No log        | 3.0   | 33   | 0.3453          | 0.3789    | 0.5611 | 0.4523 | 0.8708   |
| No log        | 4.0   | 44   | 0.3270          | 0.3673    | 0.5496 | 0.4404 | 0.8729   |
| No log        | 5.0   | 55   | 0.3268          | 0.4011    | 0.5725 | 0.4717 | 0.8760   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

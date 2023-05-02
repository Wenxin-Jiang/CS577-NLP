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
- name: finetuned_token_itr0_3e-05_essays_16_02_2022-21_02_59
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_3e-05_essays_16_02_2022-21_02_59

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2374
- Precision: 0.4766
- Recall: 0.5549
- F1: 0.5127
- Accuracy: 0.9173

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
| No log        | 1.0   | 11   | 0.4155          | 0.1569    | 0.3168 | 0.2099 | 0.8163   |
| No log        | 2.0   | 22   | 0.3584          | 0.3827    | 0.5725 | 0.4587 | 0.8691   |
| No log        | 3.0   | 33   | 0.3483          | 0.4353    | 0.5649 | 0.4917 | 0.8737   |
| No log        | 4.0   | 44   | 0.3187          | 0.4403    | 0.5916 | 0.5049 | 0.8770   |
| No log        | 5.0   | 55   | 0.3188          | 0.4463    | 0.6031 | 0.5130 | 0.8806   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

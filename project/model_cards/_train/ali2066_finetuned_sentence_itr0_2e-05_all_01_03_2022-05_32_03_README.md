---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: finetuned_sentence_itr0_2e-05_all_01_03_2022-05_32_03
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_sentence_itr0_2e-05_all_01_03_2022-05_32_03

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4208
- Accuracy: 0.8283
- F1: 0.8915
- Precision: 0.8487
- Recall: 0.9389

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| No log        | 1.0   | 390  | 0.4443          | 0.7768   | 0.8589 | 0.8072    | 0.9176 |
| 0.4532        | 2.0   | 780  | 0.4603          | 0.8098   | 0.8791 | 0.8302    | 0.9341 |
| 0.2608        | 3.0   | 1170 | 0.5284          | 0.8061   | 0.8713 | 0.8567    | 0.8863 |
| 0.1577        | 4.0   | 1560 | 0.6398          | 0.8085   | 0.8749 | 0.8472    | 0.9044 |
| 0.1577        | 5.0   | 1950 | 0.7089          | 0.8085   | 0.8741 | 0.8516    | 0.8979 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

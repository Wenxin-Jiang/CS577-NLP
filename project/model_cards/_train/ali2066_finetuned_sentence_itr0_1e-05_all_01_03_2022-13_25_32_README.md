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
- name: finetuned_sentence_itr0_1e-05_all_01_03_2022-13_25_32
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_sentence_itr0_1e-05_all_01_03_2022-13_25_32

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4787
- Accuracy: 0.8138
- F1: 0.8785
- Precision: 0.8489
- Recall: 0.9101

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| No log        | 1.0   | 390  | 0.4335          | 0.7732   | 0.8533 | 0.8209    | 0.8883 |
| 0.5141        | 2.0   | 780  | 0.4196          | 0.8037   | 0.8721 | 0.8446    | 0.9015 |
| 0.3368        | 3.0   | 1170 | 0.4519          | 0.8098   | 0.8779 | 0.8386    | 0.9212 |
| 0.2677        | 4.0   | 1560 | 0.4787          | 0.8122   | 0.8785 | 0.8452    | 0.9146 |
| 0.2677        | 5.0   | 1950 | 0.4912          | 0.8146   | 0.8794 | 0.8510    | 0.9097 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

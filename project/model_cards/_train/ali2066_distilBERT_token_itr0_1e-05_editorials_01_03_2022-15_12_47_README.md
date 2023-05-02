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
- name: distilBERT_token_itr0_1e-05_editorials_01_03_2022-15_12_47
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilBERT_token_itr0_1e-05_editorials_01_03_2022-15_12_47

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1194
- Precision: 0.0637
- Recall: 0.0080
- F1: 0.0141
- Accuracy: 0.9707

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 15   | 0.0877          | 0.12      | 0.0194 | 0.0333 | 0.9830   |
| No log        | 2.0   | 30   | 0.0806          | 0.12      | 0.0194 | 0.0333 | 0.9830   |
| No log        | 3.0   | 45   | 0.0758          | 0.12      | 0.0194 | 0.0333 | 0.9830   |
| No log        | 4.0   | 60   | 0.0741          | 0.12      | 0.0194 | 0.0333 | 0.9830   |
| No log        | 5.0   | 75   | 0.0741          | 0.12      | 0.0194 | 0.0333 | 0.9830   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

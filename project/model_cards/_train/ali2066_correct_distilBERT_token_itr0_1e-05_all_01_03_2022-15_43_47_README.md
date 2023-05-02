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
- name: correct_distilBERT_token_itr0_1e-05_all_01_03_2022-15_43_47
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# correct_distilBERT_token_itr0_1e-05_all_01_03_2022-15_43_47

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3343
- Precision: 0.1651
- Recall: 0.3039
- F1: 0.2140
- Accuracy: 0.8493

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
| No log        | 1.0   | 30   | 0.4801          | 0.0352    | 0.0591 | 0.0441 | 0.7521   |
| No log        | 2.0   | 60   | 0.3795          | 0.0355    | 0.0795 | 0.0491 | 0.8020   |
| No log        | 3.0   | 90   | 0.3359          | 0.0591    | 0.1294 | 0.0812 | 0.8334   |
| No log        | 4.0   | 120  | 0.3205          | 0.0785    | 0.1534 | 0.1039 | 0.8486   |
| No log        | 5.0   | 150  | 0.3144          | 0.0853    | 0.1571 | 0.1105 | 0.8516   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

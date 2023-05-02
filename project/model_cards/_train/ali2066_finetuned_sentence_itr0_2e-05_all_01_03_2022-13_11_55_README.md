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
- name: finetuned_sentence_itr0_2e-05_all_01_03_2022-13_11_55
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_sentence_itr0_2e-05_all_01_03_2022-13_11_55

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6168
- Accuracy: 0.8286
- F1: 0.8887
- Precision: 0.8628
- Recall: 0.9162

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
| No log        | 1.0   | 390  | 0.3890          | 0.8110   | 0.8749 | 0.8631    | 0.8871 |
| 0.4535        | 2.0   | 780  | 0.3921          | 0.8439   | 0.8984 | 0.8721    | 0.9264 |
| 0.266         | 3.0   | 1170 | 0.4454          | 0.8415   | 0.8947 | 0.8860    | 0.9034 |
| 0.16          | 4.0   | 1560 | 0.5610          | 0.8427   | 0.8957 | 0.8850    | 0.9067 |
| 0.16          | 5.0   | 1950 | 0.6180          | 0.8488   | 0.9010 | 0.8799    | 0.9231 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

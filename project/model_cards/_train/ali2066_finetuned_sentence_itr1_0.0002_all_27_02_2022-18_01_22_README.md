---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: finetuned_sentence_itr1_0.0002_all_27_02_2022-18_01_22
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_sentence_itr1_0.0002_all_27_02_2022-18_01_22

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7600
- Accuracy: 0.8144
- F1: 0.8788

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 195  | 0.3514          | 0.8427   | 0.8979 |
| No log        | 2.0   | 390  | 0.3853          | 0.8293   | 0.8936 |
| 0.3147        | 3.0   | 585  | 0.5494          | 0.8268   | 0.8868 |
| 0.3147        | 4.0   | 780  | 0.6235          | 0.8427   | 0.8995 |
| 0.3147        | 5.0   | 975  | 0.8302          | 0.8378   | 0.8965 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

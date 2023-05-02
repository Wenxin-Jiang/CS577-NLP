---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: finetuned_sentence_itr2_2e-05_all_26_02_2022-04_09_01
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_sentence_itr2_2e-05_all_26_02_2022-04_09_01

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4676
- Accuracy: 0.8299
- F1: 0.8892

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 195  | 0.4087          | 0.8073   | 0.8754 |
| No log        | 2.0   | 390  | 0.3952          | 0.8159   | 0.8803 |
| 0.4084        | 3.0   | 585  | 0.4183          | 0.8195   | 0.8831 |
| 0.4084        | 4.0   | 780  | 0.4596          | 0.8280   | 0.8867 |
| 0.4084        | 5.0   | 975  | 0.4919          | 0.8280   | 0.8873 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

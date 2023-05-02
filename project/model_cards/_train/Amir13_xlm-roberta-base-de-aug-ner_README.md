---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: xlm-roberta-base-de-aug-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-de-aug-ner

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3820
- Precision: 0.5214
- Recall: 0.5660
- F1: 0.5428
- Accuracy: 0.8966

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
| No log        | 1.0   | 463  | 0.6140          | 0.2884    | 0.2925 | 0.2904 | 0.8438   |
| 0.8329        | 2.0   | 926  | 0.4504          | 0.4092    | 0.4423 | 0.4251 | 0.8720   |
| 0.4385        | 3.0   | 1389 | 0.4046          | 0.4634    | 0.5042 | 0.4829 | 0.8875   |
| 0.3364        | 4.0   | 1852 | 0.3843          | 0.5       | 0.5446 | 0.5213 | 0.8954   |
| 0.2919        | 5.0   | 2315 | 0.3820          | 0.5214    | 0.5660 | 0.5428 | 0.8966   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- emotion
model-index:
- name: bert_emo_classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert_emo_classifier

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the emotion dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3768

## Target Labels

label: a classification label, with possible values including 
- sadness : 0 
- joy : 1 
- love : 2 
- anger : 3 
- fear : 4 
- surprise : 5

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.1497        | 0.25  | 500  | 0.2911          |
| 0.1221        | 0.5   | 1000 | 0.3190          |
| 0.108         | 0.75  | 1500 | 0.3343          |
| 0.1296        | 1.0   | 2000 | 0.2803          |
| 0.0611        | 1.25  | 2500 | 0.3392          |
| 0.0651        | 1.5   | 3000 | 0.3400          |
| 0.0588        | 1.75  | 3500 | 0.3733          |
| 0.0993        | 2.0   | 4000 | 0.3672          |
| 0.0385        | 2.25  | 4500 | 0.4041          |
| 0.0509        | 2.5   | 5000 | 0.3906          |
| 0.0651        | 2.75  | 5500 | 0.3809          |
| 0.0693        | 3.0   | 6000 | 0.3944          |
| 0.0471        | 3.25  | 6500 | 0.3926          |
| 0.0462        | 3.5   | 7000 | 0.3837          |
| 0.0326        | 3.75  | 7500 | 0.3752          |
| 0.0233        | 4.0   | 8000 | 0.3768          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.10.3

---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
- accuracy
- precision
- recall
model-index:
- name: bert-bert-cased-first512-Conflict
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-bert-cased-first512-Conflict

`conv_text = '\n'.join([utt.text for utt in conv.get_chronological_utterance_list()])`


This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6932
- F1: 0.6667
- Accuracy: 0.5
- Precision: 0.5
- Recall: 1.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Accuracy | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:------:|:--------:|:---------:|:------:|
| 0.7098        | 1.0   | 685  | 0.6945          | 0.0    | 0.5      | 0.0       | 0.0    |
| 0.7046        | 2.0   | 1370 | 0.6997          | 0.6667 | 0.5      | 0.5       | 1.0    |
| 0.7013        | 3.0   | 2055 | 0.6949          | 0.6667 | 0.5      | 0.5       | 1.0    |
| 0.7027        | 4.0   | 2740 | 0.6931          | 0.6667 | 0.5      | 0.5       | 1.0    |
| 0.702         | 5.0   | 3425 | 0.6932          | 0.6667 | 0.5      | 0.5       | 1.0    |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1

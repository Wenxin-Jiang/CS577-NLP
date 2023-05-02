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
- Loss: 0.2652

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
| 0.8874        | 0.25  | 500  | 0.4256          |
| 0.3255        | 0.5   | 1000 | 0.3233          |
| 0.2754        | 0.75  | 1500 | 0.2736          |
| 0.242         | 1.0   | 2000 | 0.2263          |
| 0.1661        | 1.25  | 2500 | 0.2118          |
| 0.1614        | 1.5   | 3000 | 0.1812          |
| 0.1434        | 1.75  | 3500 | 0.1924          |
| 0.1629        | 2.0   | 4000 | 0.1766          |
| 0.1066        | 2.25  | 4500 | 0.2100          |
| 0.1313        | 2.5   | 5000 | 0.1996          |
| 0.1113        | 2.75  | 5500 | 0.2185          |
| 0.115         | 3.0   | 6000 | 0.2406          |
| 0.0697        | 3.25  | 6500 | 0.2485          |
| 0.0835        | 3.5   | 7000 | 0.2391          |
| 0.0637        | 3.75  | 7500 | 0.2695          |
| 0.0707        | 4.0   | 8000 | 0.2652          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.10.3

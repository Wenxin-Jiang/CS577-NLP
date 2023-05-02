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
- Loss: 0.2748

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
| 0.9063        | 0.25  | 500  | 0.4845          |
| 0.3362        | 0.5   | 1000 | 0.3492          |
| 0.2759        | 0.75  | 1500 | 0.2819          |
| 0.2521        | 1.0   | 2000 | 0.2464          |
| 0.1705        | 1.25  | 2500 | 0.2345          |
| 0.1841        | 1.5   | 3000 | 0.2013          |
| 0.1428        | 1.75  | 3500 | 0.1926          |
| 0.1747        | 2.0   | 4000 | 0.1866          |
| 0.1082        | 2.25  | 4500 | 0.2302          |
| 0.1142        | 2.5   | 5000 | 0.2118          |
| 0.1205        | 2.75  | 5500 | 0.2318          |
| 0.1135        | 3.0   | 6000 | 0.2306          |
| 0.0803        | 3.25  | 6500 | 0.2625          |
| 0.0745        | 3.5   | 7000 | 0.2850          |
| 0.085         | 3.75  | 7500 | 0.2719          |
| 0.0701        | 4.0   | 8000 | 0.2748          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.10.3

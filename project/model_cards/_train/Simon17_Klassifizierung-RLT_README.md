---
license: mit
tags:
- generated_from_trainer
metrics:
- f1
widget:
- text: "11004RLT790AG01BS01"
- text: "11004RLT615AB01BM06"
- text: "12064RLT606KL02RM01"
- text: "11004RLT722VA01AS01"
- text: "Abl. Anl. 15 Aufzugm."
model-index:
- name: Klassifizierung-RLT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Klassifizierung-RLT

This model is a fine-tuned version of [bert-base-german-cased](https://huggingface.co/bert-base-german-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0616
- F1: 0.9852

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
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.828         | 1.0   | 292  | 0.2156          | 0.9447 |
| 0.1491        | 2.0   | 584  | 0.0832          | 0.9805 |
| 0.0695        | 3.0   | 876  | 0.0616          | 0.9852 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1

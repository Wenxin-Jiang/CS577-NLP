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
- name: xlm-roberta-base-es-aug-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-es-aug-ner

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2611
- Precision: 0.6234
- Recall: 0.6361
- F1: 0.6297
- Accuracy: 0.9279

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
| 0.6289        | 1.0   | 827  | 0.3766          | 0.4739    | 0.4639 | 0.4688 | 0.8968   |
| 0.2458        | 2.0   | 1654 | 0.2911          | 0.5828    | 0.5573 | 0.5698 | 0.9202   |
| 0.2043        | 3.0   | 2481 | 0.2739          | 0.6110    | 0.5971 | 0.6039 | 0.9256   |
| 0.1662        | 4.0   | 3308 | 0.2617          | 0.6265    | 0.6336 | 0.6300 | 0.9282   |
| 0.146         | 5.0   | 4135 | 0.2611          | 0.6234    | 0.6361 | 0.6297 | 0.9279   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

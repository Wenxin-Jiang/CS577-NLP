---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: chinese_qa_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# chinese_qa_model

This model is a fine-tuned version of [bert-base-chinese](https://huggingface.co/bert-base-chinese) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5698
- Accuracy: 0.7401

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.5784        | 1.0   | 5633  | 0.5392          | 0.7402   |
| 0.5548        | 2.0   | 11266 | 0.5698          | 0.7401   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-base-chinese-finetuned-amazon_zh_20000
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-chinese-finetuned-amazon_zh_20000

This model is a fine-tuned version of [bert-base-chinese](https://huggingface.co/bert-base-chinese) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1683
- Accuracy: 0.5224
- F1: 0.5194

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 1.2051        | 1.0   | 2500 | 1.1717          | 0.506    | 0.4847 |
| 1.0035        | 2.0   | 5000 | 1.1683          | 0.5224   | 0.5194 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.9.1
- Datasets 1.18.3
- Tokenizers 0.10.3

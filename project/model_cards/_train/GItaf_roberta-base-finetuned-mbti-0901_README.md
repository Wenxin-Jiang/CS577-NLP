---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-base-finetuned-mbti-0901
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-finetuned-mbti-0901

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.0780

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 4.3179        | 1.0   | 9920  | 4.1970          |
| 4.186         | 2.0   | 19840 | 4.1264          |
| 4.1057        | 3.0   | 29760 | 4.0955          |
| 4.0629        | 4.0   | 39680 | 4.0826          |
| 4.0333        | 5.0   | 49600 | 4.0780          |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1

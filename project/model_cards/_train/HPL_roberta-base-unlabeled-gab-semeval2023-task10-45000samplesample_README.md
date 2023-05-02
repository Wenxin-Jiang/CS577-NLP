---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-base-unlabeled-gab-semeval2023-task10-45000samplesample
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-unlabeled-gab-semeval2023-task10-45000samplesample

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1441

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.4294        | 1.0   | 1407 | 2.2323          |
| 2.3091        | 2.0   | 2814 | 2.1470          |
| 2.23          | 3.0   | 4221 | 2.1767          |
| 2.1866        | 4.0   | 5628 | 2.1625          |
| 2.171         | 5.0   | 7035 | 2.1441          |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.10.3

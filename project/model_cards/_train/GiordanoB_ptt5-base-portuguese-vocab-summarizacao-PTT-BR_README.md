---
license: mit
tags:
- generated_from_trainer
model-index:
- name: ptt5-base-portuguese-vocab-summarizacao-PTT-BR
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ptt5-base-portuguese-vocab-summarizacao-PTT-BR

This model is a fine-tuned version of [unicamp-dl/ptt5-base-portuguese-vocab](https://huggingface.co/unicamp-dl/ptt5-base-portuguese-vocab) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.6954

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 15   | 4.6282          |
| No log        | 2.0   | 30   | 3.9111          |
| No log        | 3.0   | 45   | 3.6954          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

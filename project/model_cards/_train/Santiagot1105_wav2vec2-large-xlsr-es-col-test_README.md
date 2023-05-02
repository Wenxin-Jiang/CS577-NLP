---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xlsr-es-col-test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-es-col-test

This model is a fine-tuned version of [jonatasgrosman/wav2vec2-large-xlsr-53-spanish](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-spanish) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0923
- Wer: 0.0886

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0905        | 18.18 | 400  | 0.0923          | 0.0886 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.1+cu102
- Datasets 1.13.3
- Tokenizers 0.10.3

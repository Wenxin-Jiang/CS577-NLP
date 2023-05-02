---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_10_0
model-index:
- name: wav2vec2-large-xls-r-300m-georgian-large
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-georgian-large

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice_10_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4291
- Wer: 0.6392

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
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.0867        | 4.21  | 400  | 3.1211          | 1.0    |
| 2.8871        | 8.42  | 800  | 2.2250          | 1.0    |
| 0.3667        | 12.63 | 1200 | 0.4291          | 0.6392 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 2.4.0
- Tokenizers 0.10.3

---
license: apache-2.0
tags:
- automatic-speech-recognition
- NbAiLab/NPSC
- generated_from_trainer
datasets:
- npsc
model-index:
- name: xls-npsc
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xls-npsc

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the NBAILAB/NPSC - 48K_MP3 dataset.
It achieves the following results on the evaluation set:
- Loss: 3.5006
- Wer: 1.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 10.0
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.18.1.dev0
- Tokenizers 0.10.3

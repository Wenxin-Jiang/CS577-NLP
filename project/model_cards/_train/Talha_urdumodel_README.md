---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: urdumodel
  results: []
metrics:
- wer
- cer
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# urdumodel

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4939
- Wer: 0.3698
- Cer: 0.1465

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

For training 95 hours of audio data is used. For evaluation test set of common voice 10.0 is used. 

## Training procedure
All the code is available here
https://github.com/talhaanwarch/Urdu-ASR
### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 96
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20
- mixed_precision_training: Native AMP

# Model score on test
When I train I got different WER and CER score on test set, but when I tested locally
I got WER of 0.27 without language model and 0.22 with language model.


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0
- Datasets 2.4.0
- Tokenizers 0.12.1

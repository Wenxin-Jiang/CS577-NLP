---
language:
- ur
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_7_0
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: ''
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - UR dataset.
It achieves the following results on the evaluation set:
- Loss: 3.8433
- Wer: 0.9852

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
- train_batch_size: 64
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 2000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 1.468         | 166.67 | 500  | 3.0262          | 1.0035 |
| 0.0572        | 333.33 | 1000 | 3.5352          | 0.9721 |
| 0.0209        | 500.0  | 1500 | 3.7266          | 0.9834 |
| 0.0092        | 666.67 | 2000 | 3.8433          | 0.9852 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.17.1.dev0
- Tokenizers 0.11.0

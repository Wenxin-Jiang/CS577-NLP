---
language:
- rw
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Kinyarwanda
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 rw
      type: mozilla-foundation/common_voice_11_0
      config: rw
      split: test
      args: rw
    metrics:
    - name: Wer
      type: wer
      value: 43.75236083594792
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Kinyarwanda

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the mozilla-foundation/common_voice_11_0 rw dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6424
- Wer: 43.7524

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 20
- eval_batch_size: 20
- seed: 42
- distributed_type: multi-GPU
- num_devices: 2
- total_train_batch_size: 40
- total_eval_batch_size: 40
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.7471        | 0.04  | 1000 | 0.9044          | 59.2903 |
| 0.5987        | 0.08  | 2000 | 0.7523          | 52.0232 |
| 0.5168        | 0.12  | 3000 | 0.6890          | 47.7610 |
| 0.5082        | 0.16  | 4000 | 0.6596          | 45.4013 |
| 0.4748        | 0.2   | 5000 | 0.6424          | 43.7524 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu116
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2

---
license: apache-2.0
tags:
  - whisper-event
  - generated_from_trainer
  - hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper-small-ar - Mourad Mars
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: ar
      split: test
      args: ar
    metrics:
    - name: Wer
      type: wer
      value: 44.976586
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper-small-ar - Mourad Mars

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the common_voice_11_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.322550
- Wer: 44.976586

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
    
    train_batch_size=16
    
    eval_batch_size=8
    
    optimizer: Adam
    
    learning_rate=1e-5
    
    warmup_steps=500
    
    max_steps=4000
        
    eval_steps=1000
    
    
    metric_for_best_model="wer"


### Training results


| Training Loss | Step | Validation Loss  | Wer       |
|:-------------:|:----:|:----------------:|:---------:|
| 0.2811        | 1000 | 0.393018         | 53.778349 |
| 0.2356        | 2000 | 0.348794         | 47.793591 |
| 0.1705        | 3000 | 0.332207         | 45.758883 |
| 0.1476        | 4000 | 0.322550         | 44.976586 |


### Framework versions



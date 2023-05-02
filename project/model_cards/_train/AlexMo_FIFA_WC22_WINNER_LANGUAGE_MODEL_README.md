---
language:
- nl
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: FIFA_WC22_WINNER_LANGUAGE_MODEL
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: 'null'
      split: None
      args: 'config: nl, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 14.261890699371158
---


# whisper-lt-finetune

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2588
- Wer: 14.2619

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- training_steps: 4000
- mixed_precision_training: Native AMP
### Training results
| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0783        | 1.3   | 1000 | 0.2478          | 15.5647 |
| 0.0287        | 2.6   | 2000 | 0.2441          | 14.3765 |
| 0.0087        | 3.9   | 3000 | 0.2516          | 14.3349 |
| 0.0021        | 5.19  | 4000 | 0.2588          | 14.2619 |

### Framework versions
- Transformers 4.26.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2

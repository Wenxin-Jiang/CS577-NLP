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
      value: 13.5797
---


# whisper-lt-finetune

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2550
- Wer: 13.5797

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- training_steps: 5000
- mixed_precision_training: Native AMP
### Training results
| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.1556        | 0.97  | 1000 | 0.2354          | 15.2781 |
| 0.0709        | 1.95  | 2000 | 0.2336          | 14.6419 |
| 0.0259        | 2.92  | 3000 | 0.2415          | 14.0186 |
| 0.0098        | 3.89  | 4000 | 0.2496          | 13.7355 |
| 0.0056        | 4.87  | 5000 | 0.2550          | 13.5797 |

### Framework versions
- Transformers 4.26.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2

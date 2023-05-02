---
language:
- fy
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Frisian
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 fy-NL
      type: mozilla-foundation/common_voice_11_0
      config: fy-NL
      split: test
      args: fy-NL
    metrics:
    - name: Wer
      type: wer
      value: 21.03
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small fy-NL - RuudVelo

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 11.0 dataset.
It achieves the following results on the test set:
- Loss: 0.1443
- Wer: 21.03

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
- train_batch_size: 64
- eval_batch_size: 8
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss |  Step | Validation Loss | Wer    |
|:-------------:|:-----:|:---------------:|:------:|
| 0.0053        |  1000 | 0.4201          | 21.64  |
| 0.0008        |  2000 | 0.4607          | 21.03  |
| 0.0004        |  3000 | 0.4853          | 21.11  |
| 0.0003        |  4000 | 0.5015          | 21.14  |
| 0.0002        |  5000 | 0.5084          | 21.20  |

### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
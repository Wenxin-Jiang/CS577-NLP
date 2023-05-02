---
language:
- hi
license: apache-2.0
tags:
- Openslr Multilingual
- automatic-speech-recognition
- generated_from_trainer
- hf-asr-leaderboard
- mozilla-foundation/common_voice_7_0
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_7_0
model-index:
- name: Wav2Vec2_xls_r_300m_hi_final
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7.0
      type: mozilla-foundation/common_voice_7_0
      args: hi
    metrics:
    - name: Test WER
      type: wer
      value: 34.21
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Wav2Vec2_xls_r_300m_hi_final
This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the ['Openslr Multilingual and code-switching ASR challenge'](http://www.openslr.org/103/) dataset and ['mozilla-foundation/common_voice_7_0'](https://huggingface.co/datasets/mozilla-foundation/common_voice_7_0) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3035
- Wer: 0.3137
- Cer: 0.0972
## Model description
More information needed
## Intended uses & limitations
More information needed
## Training and evaluation data
More information needed
## Training procedure
### Training hyperparameters
The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 8
- mixed_precision_training: Native AMP
### Training results
| Training Loss | Epoch | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| 0.9821        | 0.64  | 400  | 0.5059          | 0.4783 | 0.1573 |
| 0.6861        | 1.28  | 800  | 0.4201          | 0.4247 | 0.1356 |
| 0.585         | 1.92  | 1200 | 0.3797          | 0.3811 | 0.1210 |
| 0.5193        | 2.56  | 1600 | 0.3577          | 0.3652 | 0.1152 |
| 0.4583        | 3.21  | 2000 | 0.3422          | 0.3519 | 0.1111 |
| 0.4282        | 3.85  | 2400 | 0.3261          | 0.3450 | 0.1071 |
| 0.3951        | 4.49  | 2800 | 0.3201          | 0.3325 | 0.1048 |
| 0.3619        | 5.13  | 3200 | 0.3167          | 0.3296 | 0.1030 |
| 0.345         | 5.77  | 3600 | 0.3157          | 0.3210 | 0.1013 |
| 0.338         | 6.41  | 4000 | 0.3051          | 0.3143 | 0.0982 |
| 0.3155        | 7.05  | 4400 | 0.3059          | 0.3154 | 0.0986 |
| 0.3057        | 7.69  | 4800 | 0.3035          | 0.3137 | 0.0972 |
### Framework versions
- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0
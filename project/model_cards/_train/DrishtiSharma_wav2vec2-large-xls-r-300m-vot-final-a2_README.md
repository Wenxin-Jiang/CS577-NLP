---
language:
- vot
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- vot
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-vot-final-a2
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: vot
    metrics:
    - name: Test WER
      type: wer
      value: 0.8333333333333334
    - name: Test CER
      type: cer
      value: 0.48672566371681414
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: vot
    metrics:
    - name: Test WER
      type: wer
      value: NA
    - name: Test CER
      type: cer
      value: NA
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-vot-final-a2

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - VOT dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8745
- Wer: 0.8333

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py  --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-vot-final-a2  --dataset mozilla-foundation/common_voice_8_0 --config vot --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Votic language isn't available in speech-recognition-community-v2/dev_data


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0004
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 340
- num_epochs: 200
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 11.1216       | 33.33  | 100  | 4.2848          | 1.0    |
| 2.9982        | 66.67  | 200  | 2.8665          | 1.0    |
| 1.5476        | 100.0  | 300  | 2.3022          | 0.8889 |
| 0.2776        | 133.33 | 400  | 2.7480          | 0.8889 |
| 0.1136        | 166.67 | 500  | 2.5383          | 0.8889 |
| 0.0489        | 200.0  | 600  | 2.8745          | 0.8333 |




### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0


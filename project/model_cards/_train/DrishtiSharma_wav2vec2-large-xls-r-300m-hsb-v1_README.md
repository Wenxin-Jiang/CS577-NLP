---
language:
- hsb
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- hsb
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-hsb-v1
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: hsb
    metrics:
    - name: Test WER
      type: wer
      value: 0.4393
    - name: Test CER
      type: cer
      value: 0.1036
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: hsb
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

# wav2vec2-large-xls-r-300m-hsb-v1

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - HSB dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5684
- Wer: 0.4402

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-hsb-v1 --dataset mozilla-foundation/common_voice_8_0 --config hsb --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Upper Sorbian language isn't available in speech-recognition-community-v2/dev_data


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.00045
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 8.972         | 3.23  | 100  | 3.7498          | 1.0    |
| 3.3401        | 6.45  | 200  | 3.2320          | 1.0    |
| 3.2046        | 9.68  | 300  | 3.1741          | 0.9806 |
| 2.4031        | 12.9  | 400  | 1.0579          | 0.8996 |
| 1.0427        | 16.13 | 500  | 0.7989          | 0.7557 |
| 0.741         | 19.35 | 600  | 0.6405          | 0.6299 |
| 0.5699        | 22.58 | 700  | 0.6129          | 0.5928 |
| 0.4607        | 25.81 | 800  | 0.6548          | 0.5695 |
| 0.3827        | 29.03 | 900  | 0.6268          | 0.5190 |
| 0.3282        | 32.26 | 1000 | 0.5919          | 0.5016 |
| 0.2764        | 35.48 | 1100 | 0.5953          | 0.4805 |
| 0.2335        | 38.71 | 1200 | 0.5717          | 0.4728 |
| 0.2106        | 41.94 | 1300 | 0.5674          | 0.4569 |
| 0.1859        | 45.16 | 1400 | 0.5685          | 0.4502 |
| 0.1592        | 48.39 | 1500 | 0.5684          | 0.4402 |


### Framework versions

- Transformers 4.16.1
- Pytorch 1.10.0+cu111
- Datasets 1.18.2
- Tokenizers 0.11.0

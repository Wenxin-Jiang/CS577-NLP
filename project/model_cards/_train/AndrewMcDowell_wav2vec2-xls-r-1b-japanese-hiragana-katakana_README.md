---
language:
- ja
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- robust-speech-event
- ja
- hf-asr-leaderboard
datasets:
- common_voice
model-index:
- name: ''
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: ja
    metrics:
    - name: Test WER
      type: wer
      value: 95.33
    - name: Test CER
      type: cer
      value: 22.27
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: de
    metrics:
    - name: Test WER
      type: wer
      value: 100.0
    - name: Test CER
      type: cer
      value: 30.33
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: ja
    metrics:
    - name: Test CER
      type: cer
      value: 29.63
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: ja
    metrics:
    - name: Test CER
      type: cer
      value: 32.69
---



<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - JA dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5500
- Wer: 1.0132
- Cer: 0.1609

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1500
- num_epochs: 50.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| 1.7019        | 12.65 | 1000 | 1.0510          | 0.9832 | 0.2589 |
| 1.6385        | 25.31 | 2000 | 0.6670          | 0.9915 | 0.1851 |
| 1.4344        | 37.97 | 3000 | 0.6183          | 1.0213 | 0.1797 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0


#### Evaluation Commands
1. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python ./eval.py --model_id AndrewMcDowell/wav2vec2-xls-r-1b-japanese-hiragana-katakana --dataset mozilla-foundation/common_voice_8_0 --config ja --split test --log_outputs
```

2. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python ./eval.py --model_id AndrewMcDowell/wav2vec2-xls-r-1b-japanese-hiragana-katakana --dataset speech-recognition-community-v2/dev_data --config de --split validation --chunk_length_s 5.0 --stride_length_s 1.0
```
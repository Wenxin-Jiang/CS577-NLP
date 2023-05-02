---
language:
- sl
license: apache-2.0
tags:
- automatic-speech-recognition
- generated_from_trainer
- hf-asr-leaderboard
- model_for_talk
- mozilla-foundation/common_voice_8_0
- robust-speech-event
- sl
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-sl-with-LM-v1
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: sl
    metrics:
    - name: Test WER
      type: wer
      value: 0.20626555409164105
    - name: Test CER
      type: cer
      value: 0.051648321634392154
    - name: Test WER (+LM)
      type: wer
      value: 0.13482652613087395
    - name: Test CER (+LM)
      type: cer
      value: 0.038838663862562475
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: sl
    metrics:
    - name: Dev WER
      type: wer
      value: 0.5406156320830592
    - name: Dev CER
      type: cer
      value: 0.22249723590310583
    - name: Dev WER (+LM)
      type: wer
      value: 0.49783147459727384
    - name: Dev CER (+LM)
      type: cer
      value: 0.1591062599627158
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: sl
    metrics:
    - name: Test WER
      type: wer
      value: 46.17
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - SL dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2756
- Wer: 0.2279

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-sl-with-LM-v1 --dataset mozilla-foundation/common_voice_8_0 --config sl --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-sl-with-LM-v1 --dataset speech-recognition-community-v2/dev_data --config sl --split validation --chunk_length_s 10 --stride_length_s 1

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 100.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.3881        | 6.1   | 500  | 2.9710          | 1.0    |
| 2.6401        | 12.2  | 1000 | 1.7677          | 0.9734 |
| 1.5152        | 18.29 | 1500 | 0.5564          | 0.6011 |
| 1.2191        | 24.39 | 2000 | 0.4319          | 0.4390 |
| 1.0237        | 30.49 | 2500 | 0.3141          | 0.3175 |
| 0.8892        | 36.59 | 3000 | 0.2748          | 0.2689 |
| 0.8296        | 42.68 | 3500 | 0.2680          | 0.2534 |
| 0.7602        | 48.78 | 4000 | 0.2820          | 0.2506 |
| 0.7186        | 54.88 | 4500 | 0.2672          | 0.2398 |
| 0.6887        | 60.98 | 5000 | 0.2729          | 0.2402 |
| 0.6507        | 67.07 | 5500 | 0.2767          | 0.2361 |
| 0.6226        | 73.17 | 6000 | 0.2817          | 0.2332 |
| 0.6024        | 79.27 | 6500 | 0.2679          | 0.2279 |
| 0.5787        | 85.37 | 7000 | 0.2837          | 0.2316 |
| 0.5744        | 91.46 | 7500 | 0.2838          | 0.2284 |
| 0.5556        | 97.56 | 8000 | 0.2763          | 0.2281 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0

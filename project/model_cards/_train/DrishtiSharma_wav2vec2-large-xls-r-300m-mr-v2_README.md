---
language:
- mr
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- mr
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-mr-v2
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: mr
    metrics:
    - name: Test WER
      type: wer
      value: 0.49378259125551544
    - name: Test CER
      type: cer
      value: 0.12470799640610962
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: mr
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

# wav2vec2-large-xls-r-300m-mr-v2

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - MR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8729
- Wer: 0.4942

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-mr-v2 --dataset mozilla-foundation/common_voice_8_0 --config mr --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-mr-v2 --dataset speech-recognition-community-v2/dev_data --config mr --split validation --chunk_length_s 10 --stride_length_s 1

Note: Marathi language not found in speech-recognition-community-v2/dev_data!

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.000333
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 200
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 8.4934        | 9.09   | 200  | 3.7326          | 1.0    |
| 3.4234        | 18.18  | 400  | 3.3383          | 0.9996 |
| 3.2628        | 27.27  | 600  | 2.7482          | 0.9992 |
| 1.7743        | 36.36  | 800  | 0.6755          | 0.6787 |
| 1.0346        | 45.45  | 1000 | 0.6067          | 0.6193 |
| 0.8137        | 54.55  | 1200 | 0.6228          | 0.5612 |
| 0.6637        | 63.64  | 1400 | 0.5976          | 0.5495 |
| 0.5563        | 72.73  | 1600 | 0.7009          | 0.5383 |
| 0.4844        | 81.82  | 1800 | 0.6662          | 0.5287 |
| 0.4057        | 90.91  | 2000 | 0.6911          | 0.5303 |
| 0.3582        | 100.0  | 2200 | 0.7207          | 0.5327 |
| 0.3163        | 109.09 | 2400 | 0.7107          | 0.5118 |
| 0.2761        | 118.18 | 2600 | 0.7538          | 0.5118 |
| 0.2415        | 127.27 | 2800 | 0.7850          | 0.5178 |
| 0.2127        | 136.36 | 3000 | 0.8016          | 0.5034 |
| 0.1873        | 145.45 | 3200 | 0.8302          | 0.5187 |
| 0.1723        | 154.55 | 3400 | 0.9085          | 0.5223 |
| 0.1498        | 163.64 | 3600 | 0.8396          | 0.5126 |
| 0.1425        | 172.73 | 3800 | 0.8776          | 0.5094 |
| 0.1258        | 181.82 | 4000 | 0.8651          | 0.5014 |
| 0.117         | 190.91 | 4200 | 0.8772          | 0.4970 |
| 0.1093        | 200.0  | 4400 | 0.8729          | 0.4942 |


### Framework versions

- Transformers 4.16.1
- Pytorch 1.10.0+cu111
- Datasets 1.18.2
- Tokenizers 0.11.0


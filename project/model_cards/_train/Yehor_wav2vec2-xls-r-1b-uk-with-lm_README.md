---
language:
- uk
license: apache-2.0
tags:
- automatic-speech-recognition
- generated_from_trainer
- hf-asr-leaderboard
- mozilla-foundation/common_voice_7_0
- robust-speech-event
- uk
datasets:
- mozilla-foundation/common_voice_7_0
model-index:
- name: wav2vec2-xls-r-1b-uk-with-lm
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7
      type: mozilla-foundation/common_voice_7_0
      args: uk
    metrics:
    - name: Test WER
      type: wer
      value: 14.62
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: uk
    metrics:
    - name: Test WER
      type: wer
      value: 48.72
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: uk
    metrics:
    - name: Test WER
      type: wer
      value: 40.66
---

# Ukrainian STT model (with Language Model)

🇺🇦 Join Ukrainian Speech Recognition Community - https://t.me/speech_recognition_uk

⭐ See other Ukrainian models - https://github.com/egorsmkv/speech-recognition-uk

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - UK dataset.

It achieves the following results on the evaluation set without the language model:

- Loss: 0.1875
- Wer: 0.2033
- Cer: 0.0384


## Model description

On 100 test example the model shows the following results:

Without LM:

- WER: 0.1862
- CER: 0.0277

With LM:

- WER: 0.1218
- CER: 0.0190


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 20
- total_train_batch_size: 160
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 100.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| 1.2815        | 7.93  | 500  | 0.3536          | 0.4753 | 0.1009 |
| 1.0869        | 15.86 | 1000 | 0.2317          | 0.3111 | 0.0614 |
| 0.9984        | 23.8  | 1500 | 0.2022          | 0.2676 | 0.0521 |
| 0.975         | 31.74 | 2000 | 0.1948          | 0.2469 | 0.0487 |
| 0.9306        | 39.67 | 2500 | 0.1916          | 0.2377 | 0.0464 |
| 0.8868        | 47.61 | 3000 | 0.1903          | 0.2257 | 0.0439 |
| 0.8424        | 55.55 | 3500 | 0.1786          | 0.2206 | 0.0423 |
| 0.8126        | 63.49 | 4000 | 0.1849          | 0.2160 | 0.0416 |
| 0.7901        | 71.42 | 4500 | 0.1869          | 0.2138 | 0.0413 |
| 0.7671        | 79.36 | 5000 | 0.1855          | 0.2075 | 0.0394 |
| 0.7467        | 87.3  | 5500 | 0.1884          | 0.2049 | 0.0389 |
| 0.731         | 95.24 | 6000 | 0.1877          | 0.2060 | 0.0387 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.18.1.dev0
- Tokenizers 0.11.0

#### Evaluation Commands

1. To evaluate on `mozilla-foundation/common_voice_7_0` with split `test`

```bash
python eval.py --model_id Yehor/wav2vec2-xls-r-1b-uk-with-lm --dataset mozilla-foundation/common_voice_7_0 --config uk --split test
```

### Eval results on Common Voice 7 "test" (WER):

| Without LM | With LM (run `./eval.py`) |
|---|---|
| 21.52 | 14.62 |

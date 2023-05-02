---
language: ru
datasets:
- mozilla-foundation/common_voice_8_0
metrics:
- wer
- cer
tags:
- audio
- automatic-speech-recognition
- generated_from_trainer
- hf-asr-leaderboard
- mozilla-foundation/common_voice_8_0
- robust-speech-event
- speech
model-index:
- name: XLS-R 1B Wav2Vec2 Russian by Rasmus Toivanen
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: ru
    metrics:
    - name: Test WER
      type: wer
      value: 10.83
    - name: Test CER
      type: cer
      value: 2.41
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: ru
    metrics:
    - name: Test WER
      type: wer
      value: 37.71
    - name: Test CER
      type: cer
      value: 12.98
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: ru
    metrics:
    - name: Test WER
      type: wer
      value: 31.89
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xlsr-1b-ru

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1352
- Wer: 0.0971

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.5462        | 0.35  | 500   | 0.4027          | 0.3575 |
| 0.498         | 0.69  | 1000  | 0.2588          | 0.2513 |
| 0.4279        | 1.04  | 1500  | 0.2265          | 0.2204 |
| 0.4099        | 1.38  | 2000  | 0.2189          | 0.1979 |
| 0.4688        | 1.73  | 2500  | 0.2100          | 0.1920 |
| 0.2241        | 2.07  | 3000  | 0.1980          | 0.1767 |
| 0.2056        | 2.42  | 3500  | 0.2020          | 0.1683 |
| 0.3423        | 2.76  | 4000  | 0.1862          | 0.1606 |
| 0.2478        | 3.11  | 4500  | 0.1787          | 0.1563 |
| 0.3079        | 3.45  | 5000  | 0.1759          | 0.1555 |
| 0.2477        | 3.8   | 5500  | 0.1713          | 0.1423 |
| 0.1718        | 4.14  | 6000  | 0.1695          | 0.1391 |
| 0.1675        | 4.49  | 6500  | 0.1677          | 0.1372 |
| 0.1631        | 4.83  | 7000  | 0.1652          | 0.1333 |
| 0.1429        | 5.18  | 7500  | 0.1605          | 0.1308 |
| 0.1505        | 5.52  | 8000  | 0.1612          | 0.1245 |
| 0.1385        | 5.87  | 8500  | 0.1487          | 0.1225 |
| 0.1285        | 6.22  | 9000  | 0.1526          | 0.1201 |
| 0.1153        | 6.56  | 9500  | 0.1464          | 0.1172 |
| 0.1159        | 6.91  | 10000 | 0.1505          | 0.1143 |
| 0.1061        | 7.25  | 10500 | 0.1444          | 0.1106 |
| 0.1016        | 7.6   | 11000 | 0.1427          | 0.1075 |
| 0.1125        | 7.94  | 11500 | 0.1386          | 0.1045 |
| 0.0937        | 8.29  | 12000 | 0.1403          | 0.1022 |
| 0.1059        | 8.63  | 12500 | 0.1406          | 0.1022 |
| 0.0857        | 8.98  | 13000 | 0.1372          | 0.0992 |
| 0.0901        | 9.32  | 13500 | 0.1380          | 0.0977 |
| 0.0913        | 9.67  | 14000 | 0.1352          | 0.0971 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0

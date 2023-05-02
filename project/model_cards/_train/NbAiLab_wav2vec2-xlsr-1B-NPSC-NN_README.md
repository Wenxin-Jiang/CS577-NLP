---
license: apache-2.0
tags:
- generated_from_trainer
- automatic-speech-recognition
- NbAiLab/NPSC
- robust-speech-event
- false
- nn-NO
- hf-asr-leaderboard
datasets:
- NbAiLab/NPSC
language:
- nn-NO
model-index:
- name: wav2vec2-xlsr-1B-NPSC-NN
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: NPSC
      type: NbAiLab/NPSC
      args: 16K_mp3_nynorsk
    metrics:
    - name: Test (Nynorsk) WER
      type: wer
      value: 0.13347099680871036
    - name: Test (Nynorsk) CER
      type: cer
      value: 0.04537322093454329
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xlsr-1B-NPSC-NN

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the NBAILAB/NPSC - 16K_MP3 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4562
- Wer: 0.1531

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 50.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 1.6894        | 1.08  | 500   | 1.2423          | 0.8619 |
| 0.7543        | 2.15  | 1000  | 0.5956          | 0.3817 |
| 0.5481        | 3.23  | 1500  | 0.5043          | 0.3246 |
| 0.4661        | 4.3   | 2000  | 0.4813          | 0.2793 |
| 0.3901        | 5.38  | 2500  | 0.4371          | 0.2592 |
| 0.3512        | 6.45  | 3000  | 0.4216          | 0.2458 |
| 0.3016        | 7.53  | 3500  | 0.3814          | 0.2257 |
| 0.278         | 8.6   | 4000  | 0.4151          | 0.2145 |
| 0.2435        | 9.68  | 4500  | 0.4816          | 0.2130 |
| 0.2122        | 10.75 | 5000  | 0.4489          | 0.2137 |
| 0.1949        | 11.83 | 5500  | 0.3978          | 0.2063 |
| 0.1929        | 12.9  | 6000  | 0.3823          | 0.2026 |
| 0.1757        | 13.98 | 6500  | 0.3409          | 0.1965 |
| 0.1771        | 15.05 | 7000  | 0.3844          | 0.1936 |
| 0.1452        | 16.13 | 7500  | 0.3749          | 0.1900 |
| 0.1341        | 17.2  | 8000  | 0.4407          | 0.2026 |
| 0.13          | 18.28 | 8500  | 0.4253          | 0.1883 |
| 0.1183        | 19.35 | 9000  | 0.4311          | 0.1880 |
| 0.118         | 20.43 | 9500  | 0.4431          | 0.1882 |
| 0.1123        | 21.51 | 10000 | 0.4753          | 0.1820 |
| 0.1037        | 22.58 | 10500 | 0.4087          | 0.1834 |
| 0.1066        | 23.66 | 11000 | 0.4151          | 0.1845 |
| 0.0977        | 24.73 | 11500 | 0.4367          | 0.1783 |
| 0.0968        | 25.81 | 12000 | 0.4237          | 0.1756 |
| 0.0835        | 26.88 | 12500 | 0.4729          | 0.1781 |
| 0.0919        | 27.96 | 13000 | 0.4153          | 0.1701 |
| 0.0677        | 29.03 | 13500 | 0.4317          | 0.1693 |
| 0.0726        | 30.11 | 14000 | 0.4380          | 0.1736 |
| 0.066         | 31.18 | 14500 | 0.4384          | 0.1681 |
| 0.0713        | 32.26 | 15000 | 0.4215          | 0.1629 |
| 0.0605        | 33.33 | 15500 | 0.4574          | 0.1714 |
| 0.0632        | 34.41 | 16000 | 0.4343          | 0.1642 |
| 0.0567        | 35.48 | 16500 | 0.4231          | 0.1601 |
| 0.0556        | 36.56 | 17000 | 0.4404          | 0.1667 |
| 0.0426        | 37.63 | 17500 | 0.4459          | 0.1625 |
| 0.0445        | 38.71 | 18000 | 0.4484          | 0.1629 |
| 0.0463        | 39.78 | 18500 | 0.4508          | 0.1596 |
| 0.0448        | 40.86 | 19000 | 0.4395          | 0.1605 |
| 0.0434        | 41.94 | 19500 | 0.4490          | 0.1607 |
| 0.0347        | 43.01 | 20000 | 0.4772          | 0.1582 |
| 0.0332        | 44.09 | 20500 | 0.4729          | 0.1582 |
| 0.037         | 45.16 | 21000 | 0.4559          | 0.1573 |
| 0.0328        | 46.24 | 21500 | 0.4664          | 0.1560 |
| 0.0366        | 47.31 | 22000 | 0.4543          | 0.1543 |
| 0.0377        | 48.39 | 22500 | 0.4507          | 0.1560 |
| 0.0331        | 49.46 | 23000 | 0.4567          | 0.1533 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0

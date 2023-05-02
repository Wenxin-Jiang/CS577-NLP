---
language:
- bn
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Bengali
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 bn
      type: mozilla-foundation/common_voice_11_0
      config: bn
      split: test
      args: bn
    metrics:
    - name: Wer
      type: wer
      value: 14.462277064693396
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Bengali

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the mozilla-foundation/common_voice_11_0 bn dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3377
- Wer: 14.4623

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
- train_batch_size: 4
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 5000
- training_steps: 60000

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Wer     |
|:-------------:|:------:|:-----:|:---------------:|:-------:|
| 0.2431        | 1.92   | 1000  | 0.2604          | 33.5683 |
| 0.1403        | 3.83   | 2000  | 0.1703          | 23.7591 |
| 0.0799        | 5.75   | 3000  | 0.1429          | 19.5394 |
| 0.0411        | 7.66   | 4000  | 0.1568          | 19.0023 |
| 0.0244        | 9.58   | 5000  | 0.1684          | 18.3154 |
| 0.0139        | 11.49  | 6000  | 0.1856          | 17.7401 |
| 0.0085        | 13.41  | 7000  | 0.2062          | 17.5263 |
| 0.0063        | 15.33  | 8000  | 0.2146          | 17.2952 |
| 0.0041        | 17.24  | 9000  | 0.2202          | 16.9966 |
| 0.0033        | 19.16  | 10000 | 0.2163          | 16.4749 |
| 0.0027        | 21.07  | 11000 | 0.2267          | 16.5334 |
| 0.0031        | 22.99  | 12000 | 0.2313          | 16.4263 |
| 0.0033        | 24.9   | 13000 | 0.2289          | 16.3544 |
| 0.0025        | 26.82  | 14000 | 0.2384          | 16.0087 |
| 0.0023        | 28.74  | 15000 | 0.2343          | 16.1089 |
| 0.0027        | 30.65  | 16000 | 0.2389          | 16.1495 |
| 0.0022        | 32.57  | 17000 | 0.2461          | 15.9631 |
| 0.0016        | 34.48  | 18000 | 0.2364          | 15.9040 |
| 0.0015        | 36.4   | 19000 | 0.2415          | 15.7161 |
| 0.0009        | 38.31  | 20000 | 0.2411          | 15.3724 |
| 0.0013        | 40.23  | 21000 | 0.2425          | 15.5817 |
| 0.0013        | 42.15  | 22000 | 0.2469          | 15.5112 |
| 0.001         | 44.06  | 23000 | 0.2549          | 15.5474 |
| 0.0015        | 45.98  | 24000 | 0.2481          | 15.3624 |
| 0.0013        | 47.89  | 25000 | 0.2517          | 15.5316 |
| 0.0007        | 49.81  | 26000 | 0.2559          | 15.2305 |
| 0.0006        | 51.72  | 27000 | 0.2567          | 15.4066 |
| 0.0008        | 53.64  | 28000 | 0.2538          | 15.2464 |
| 0.0009        | 55.56  | 29000 | 0.2468          | 15.1284 |
| 0.0005        | 57.47  | 30000 | 0.2660          | 15.0138 |
| 0.0003        | 59.39  | 31000 | 0.2594          | 14.9384 |
| 0.0004        | 61.3   | 32000 | 0.2580          | 14.8814 |
| 0.0006        | 63.22  | 33000 | 0.2642          | 14.9374 |
| 0.0005        | 65.13  | 34000 | 0.2650          | 15.1155 |
| 0.0003        | 67.05  | 35000 | 0.2660          | 14.9939 |
| 0.0004        | 68.97  | 36000 | 0.2625          | 15.1031 |
| 0.0002        | 70.88  | 37000 | 0.2782          | 14.8139 |
| 0.0003        | 72.8   | 38000 | 0.2647          | 15.0768 |
| 0.0004        | 74.71  | 39000 | 0.2665          | 14.8680 |
| 0.0004        | 76.63  | 40000 | 0.2711          | 14.7966 |
| 0.0001        | 78.54  | 41000 | 0.2742          | 14.8075 |
| 0.0002        | 80.46  | 42000 | 0.2703          | 14.9364 |
| 0.0001        | 82.38  | 43000 | 0.2733          | 14.7604 |
| 0.0003        | 84.29  | 44000 | 0.2741          | 14.8209 |
| 0.0           | 86.21  | 45000 | 0.2792          | 14.6046 |
| 0.0           | 88.12  | 46000 | 0.2764          | 14.7356 |
| 0.0           | 90.04  | 47000 | 0.2830          | 14.6874 |
| 0.0           | 91.95  | 48000 | 0.2887          | 14.5630 |
| 0.0           | 93.87  | 49000 | 0.2951          | 14.5803 |
| 0.0           | 95.79  | 50000 | 0.3008          | 14.5476 |
| 0.0           | 97.7   | 51000 | 0.3060          | 14.5188 |
| 0.0           | 99.62  | 52000 | 0.3110          | 14.5248 |
| 0.0           | 101.53 | 53000 | 0.3158          | 14.4985 |
| 0.0           | 103.45 | 54000 | 0.3207          | 14.4980 |
| 0.0           | 105.36 | 55000 | 0.3255          | 14.5124 |
| 0.0           | 107.28 | 56000 | 0.3298          | 14.4945 |
| 0.0           | 109.2  | 57000 | 0.3342          | 14.4752 |
| 0.0           | 111.11 | 58000 | 0.3377          | 14.4623 |
| 0.0           | 113.03 | 59000 | 0.3401          | 14.4856 |
| 0.0           | 114.94 | 60000 | 0.3412          | 14.4896 |


### Framework versions

- Transformers 4.27.0.dev0
- Pytorch 2.0.0.dev20230117+cu117
- Datasets 2.8.1.dev0
- Tokenizers 0.13.2

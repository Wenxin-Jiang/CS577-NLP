---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-xls-r-300m-ar-9
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-ar-9

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 86.4276
- Wer: 0.1947

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 64
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 120
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Wer    |
|:-------------:|:------:|:-----:|:---------------:|:------:|
| 6312.2087     | 4.71   | 400   | 616.6482        | 1.0    |
| 1928.3641     | 9.41   | 800   | 135.8992        | 0.6373 |
| 502.0017      | 14.12  | 1200  | 84.4729         | 0.3781 |
| 299.4288      | 18.82  | 1600  | 76.2488         | 0.3132 |
| 224.0057      | 23.53  | 2000  | 77.6899         | 0.2868 |
| 183.0379      | 28.24  | 2400  | 77.7943         | 0.2725 |
| 160.6119      | 32.94  | 2800  | 79.4487         | 0.2643 |
| 142.7342      | 37.65  | 3200  | 81.3426         | 0.2523 |
| 127.1061      | 42.35  | 3600  | 83.4995         | 0.2489 |
| 114.0666      | 47.06  | 4000  | 82.9293         | 0.2416 |
| 108.4024      | 51.76  | 4400  | 78.6118         | 0.2330 |
| 99.6215       | 56.47  | 4800  | 87.1001         | 0.2328 |
| 95.5135       | 61.18  | 5200  | 84.0371         | 0.2260 |
| 88.2917       | 65.88  | 5600  | 85.9637         | 0.2278 |
| 82.5884       | 70.59  | 6000  | 81.7456         | 0.2237 |
| 77.6827       | 75.29  | 6400  | 88.2686         | 0.2184 |
| 73.313        | 80.0   | 6800  | 85.1965         | 0.2183 |
| 69.61         | 84.71  | 7200  | 86.1655         | 0.2100 |
| 65.6991       | 89.41  | 7600  | 84.0606         | 0.2106 |
| 62.6059       | 94.12  | 8000  | 83.8724         | 0.2036 |
| 57.8635       | 98.82  | 8400  | 85.2078         | 0.2012 |
| 55.2126       | 103.53 | 8800  | 86.6009         | 0.2021 |
| 53.1746       | 108.24 | 9200  | 88.4284         | 0.1975 |
| 52.3969       | 112.94 | 9600  | 85.2846         | 0.1972 |
| 49.8386       | 117.65 | 10000 | 86.4276         | 0.1947 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0
- Datasets 1.18.4
- Tokenizers 0.11.6

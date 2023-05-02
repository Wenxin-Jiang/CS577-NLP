---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec-base-All
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec-base-All

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0545
- Wer: 0.8861
- Cer: 0.5014

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 120
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Wer    | Cer    |
|:-------------:|:------:|:-----:|:---------------:|:------:|:------:|
| No log        | 3.33   | 500   | 4.0654          | 1.0    | 0.9823 |
| No log        | 6.67   | 1000  | 3.4532          | 1.0    | 0.9823 |
| No log        | 10.0   | 1500  | 3.0707          | 0.9992 | 0.9781 |
| No log        | 13.33  | 2000  | 2.7335          | 1.0017 | 0.9027 |
| No log        | 16.67  | 2500  | 2.5896          | 1.0690 | 0.7302 |
| No log        | 20.0   | 3000  | 2.3315          | 1.0690 | 0.6677 |
| No log        | 23.33  | 3500  | 2.2217          | 1.0150 | 0.5966 |
| No log        | 26.67  | 4000  | 2.3802          | 1.0549 | 0.5948 |
| No log        | 30.0   | 4500  | 2.2208          | 0.9975 | 0.5681 |
| 2.4224        | 33.33  | 5000  | 2.2687          | 0.9800 | 0.5537 |
| 2.4224        | 36.67  | 5500  | 2.3169          | 0.9476 | 0.5493 |
| 2.4224        | 40.0   | 6000  | 2.5196          | 0.9900 | 0.5509 |
| 2.4224        | 43.33  | 6500  | 2.4816          | 0.9501 | 0.5272 |
| 2.4224        | 46.67  | 7000  | 2.4894          | 0.9485 | 0.5276 |
| 2.4224        | 50.0   | 7500  | 2.4555          | 0.9418 | 0.5305 |
| 2.4224        | 53.33  | 8000  | 2.7326          | 0.9559 | 0.5255 |
| 2.4224        | 56.67  | 8500  | 2.5514          | 0.9227 | 0.5209 |
| 2.4224        | 60.0   | 9000  | 2.9135          | 0.9717 | 0.5455 |
| 2.4224        | 63.33  | 9500  | 3.0465          | 0.8346 | 0.5002 |
| 0.8569        | 66.67  | 10000 | 2.8177          | 0.9302 | 0.5216 |
| 0.8569        | 70.0   | 10500 | 2.9908          | 0.9310 | 0.5128 |
| 0.8569        | 73.33  | 11000 | 3.1752          | 0.9235 | 0.5284 |
| 0.8569        | 76.67  | 11500 | 2.7412          | 0.8886 | 0.5    |
| 0.8569        | 80.0   | 12000 | 2.7362          | 0.9127 | 0.5040 |
| 0.8569        | 83.33  | 12500 | 2.9636          | 0.9152 | 0.5093 |
| 0.8569        | 86.67  | 13000 | 3.0139          | 0.9011 | 0.5097 |
| 0.8569        | 90.0   | 13500 | 2.8325          | 0.8853 | 0.5032 |
| 0.8569        | 93.33  | 14000 | 3.0383          | 0.8845 | 0.5056 |
| 0.8569        | 96.67  | 14500 | 2.7931          | 0.8795 | 0.4965 |
| 0.3881        | 100.0  | 15000 | 2.8972          | 0.8928 | 0.5012 |
| 0.3881        | 103.33 | 15500 | 2.7780          | 0.8736 | 0.4947 |
| 0.3881        | 106.67 | 16000 | 3.1081          | 0.9036 | 0.5109 |
| 0.3881        | 110.0  | 16500 | 3.0078          | 0.8928 | 0.5032 |
| 0.3881        | 113.33 | 17000 | 3.0245          | 0.8886 | 0.5009 |
| 0.3881        | 116.67 | 17500 | 3.0739          | 0.8928 | 0.5065 |
| 0.3881        | 120.0  | 18000 | 3.0545          | 0.8861 | 0.5014 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.0+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1

---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-timit-demo-google-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-timit-demo-google-colab

This model is a fine-tuned version of [facebook/wav2vec2-large](https://huggingface.co/facebook/wav2vec2-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4603
- Wer: 0.3096

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
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 3.3271        | 1.0   | 500   | 1.0169          | 0.8540 |
| 0.8682        | 2.01  | 1000  | 0.5415          | 0.5366 |
| 0.6008        | 3.01  | 1500  | 0.5105          | 0.4881 |
| 0.4592        | 4.02  | 2000  | 0.5244          | 0.4596 |
| 0.3753        | 5.02  | 2500  | 0.4762          | 0.4280 |
| 0.3271        | 6.02  | 3000  | 0.4418          | 0.4035 |
| 0.2787        | 7.03  | 3500  | 0.5069          | 0.4033 |
| 0.2594        | 8.03  | 4000  | 0.5346          | 0.3871 |
| 0.2253        | 9.04  | 4500  | 0.5057          | 0.3847 |
| 0.2133        | 10.04 | 5000  | 0.5521          | 0.3772 |
| 0.1889        | 11.04 | 5500  | 0.4800          | 0.3697 |
| 0.1694        | 12.05 | 6000  | 0.5778          | 0.3749 |
| 0.1571        | 13.05 | 6500  | 0.5368          | 0.3669 |
| 0.1483        | 14.06 | 7000  | 0.5144          | 0.3577 |
| 0.141         | 15.06 | 7500  | 0.5838          | 0.3589 |
| 0.1238        | 16.06 | 8000  | 0.5242          | 0.3657 |
| 0.1138        | 17.07 | 8500  | 0.5712          | 0.3579 |
| 0.1059        | 18.07 | 9000  | 0.5715          | 0.3495 |
| 0.0994        | 19.08 | 9500  | 0.4920          | 0.3376 |
| 0.0899        | 20.08 | 10000 | 0.4696          | 0.3336 |
| 0.0795        | 21.08 | 10500 | 0.5512          | 0.3278 |
| 0.0759        | 22.09 | 11000 | 0.5155          | 0.3218 |
| 0.0722        | 23.09 | 11500 | 0.4937          | 0.3175 |
| 0.0625        | 24.1  | 12000 | 0.5750          | 0.3245 |
| 0.0579        | 25.1  | 12500 | 0.5473          | 0.3200 |
| 0.0549        | 26.1  | 13000 | 0.5079          | 0.3145 |
| 0.0463        | 27.11 | 13500 | 0.4895          | 0.3164 |
| 0.0457        | 28.11 | 14000 | 0.4757          | 0.3117 |
| 0.0481        | 29.12 | 14500 | 0.4603          | 0.3096 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.0+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1

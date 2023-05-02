---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: my_ASR_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_ASR_model

This model is a fine-tuned version of [facebook/wav2vec2-base-960h](https://huggingface.co/facebook/wav2vec2-base-960h) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2180
- Wer: 0.2546

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 2000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.6732        | 20.0  | 100  | 1.5134          | 0.4502 |
| 1.1618        | 40.0  | 200  | 1.4121          | 0.3838 |
| 0.8533        | 60.0  | 300  | 1.2672          | 0.3616 |
| 0.6095        | 80.0  | 400  | 1.8035          | 0.3506 |
| 0.4159        | 100.0 | 500  | 2.1305          | 0.3358 |
| 0.25          | 120.0 | 600  | 2.3071          | 0.3173 |
| 0.2032        | 140.0 | 700  | 2.3467          | 0.3100 |
| 0.187         | 160.0 | 800  | 2.1261          | 0.3063 |
| 0.1415        | 180.0 | 900  | 2.4187          | 0.3026 |
| 0.1268        | 200.0 | 1000 | 2.2731          | 0.2841 |
| 0.1158        | 220.0 | 1100 | 2.2680          | 0.2952 |
| 0.1112        | 240.0 | 1200 | 2.3492          | 0.2952 |
| 0.0965        | 260.0 | 1300 | 2.2798          | 0.2804 |
| 0.0857        | 280.0 | 1400 | 2.3569          | 0.2768 |
| 0.0839        | 300.0 | 1500 | 2.2247          | 0.2509 |
| 0.0732        | 320.0 | 1600 | 2.2106          | 0.2399 |
| 0.0798        | 340.0 | 1700 | 2.2425          | 0.2583 |
| 0.0862        | 360.0 | 1800 | 2.2891          | 0.2583 |
| 0.0654        | 380.0 | 1900 | 2.2015          | 0.2546 |
| 0.0731        | 400.0 | 2000 | 2.2180          | 0.2546 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

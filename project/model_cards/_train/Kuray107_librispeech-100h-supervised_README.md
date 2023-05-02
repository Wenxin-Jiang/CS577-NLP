---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: librispeech-100h-supervised
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# librispeech-100h-supervised

This model is a fine-tuned version of [facebook/wav2vec2-large-lv60](https://huggingface.co/facebook/wav2vec2-large-lv60) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0955
- Wer: 0.0345

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
- train_batch_size: 24
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 4.8277        | 0.42  | 500   | 2.9071          | 1.0    |
| 2.0261        | 0.84  | 1000  | 0.3060          | 0.2496 |
| 0.2181        | 1.26  | 1500  | 0.1172          | 0.0873 |
| 0.1255        | 1.68  | 2000  | 0.0894          | 0.0637 |
| 0.0971        | 2.1   | 2500  | 0.0821          | 0.0560 |
| 0.078         | 2.52  | 3000  | 0.0751          | 0.0500 |
| 0.0706        | 2.94  | 3500  | 0.0721          | 0.0456 |
| 0.0609        | 3.36  | 4000  | 0.0755          | 0.0464 |
| 0.0572        | 3.78  | 4500  | 0.0705          | 0.0431 |
| 0.0528        | 4.2   | 5000  | 0.0715          | 0.0423 |
| 0.0481        | 4.62  | 5500  | 0.0691          | 0.0403 |
| 0.0471        | 5.04  | 6000  | 0.0743          | 0.0401 |
| 0.0412        | 5.46  | 6500  | 0.0757          | 0.0399 |
| 0.0416        | 5.88  | 7000  | 0.0688          | 0.0378 |
| 0.0391        | 6.3   | 7500  | 0.0704          | 0.0383 |
| 0.0367        | 6.72  | 8000  | 0.0742          | 0.0387 |
| 0.0349        | 7.14  | 8500  | 0.0732          | 0.0388 |
| 0.033         | 7.56  | 9000  | 0.0719          | 0.0374 |
| 0.0327        | 7.98  | 9500  | 0.0750          | 0.0369 |
| 0.0292        | 8.4   | 10000 | 0.0734          | 0.0368 |
| 0.0303        | 8.82  | 10500 | 0.0733          | 0.0365 |
| 0.0283        | 9.24  | 11000 | 0.0766          | 0.0357 |
| 0.0269        | 9.66  | 11500 | 0.0761          | 0.0350 |
| 0.0268        | 10.08 | 12000 | 0.0802          | 0.0359 |
| 0.0245        | 10.42 | 12500 | 0.0758          | 0.0354 |
| 0.023         | 10.84 | 13000 | 0.0775          | 0.0349 |
| 0.0186        | 11.26 | 13500 | 0.0817          | 0.0355 |
| 0.0176        | 11.68 | 14000 | 0.0853          | 0.0354 |
| 0.0163        | 12.1  | 14500 | 0.0880          | 0.0347 |
| 0.0156        | 12.52 | 15000 | 0.0864          | 0.0357 |
| 0.0141        | 12.94 | 15500 | 0.0897          | 0.0355 |
| 0.0134        | 13.36 | 16000 | 0.0915          | 0.0349 |
| 0.013         | 13.78 | 16500 | 0.0928          | 0.0350 |
| 0.0097        | 13.42 | 17000 | 0.0955          | 0.0345 |


### Framework versions

- Transformers 4.14.1
- Pytorch 1.10.2
- Datasets 1.18.2
- Tokenizers 0.10.3

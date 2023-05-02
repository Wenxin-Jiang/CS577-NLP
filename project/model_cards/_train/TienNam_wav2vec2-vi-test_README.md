---
license: cc-by-nc-4.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-vi-test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-vi-test

This model is a fine-tuned version of [nguyenvulebinh/wav2vec2-base-vietnamese-250h](https://huggingface.co/nguyenvulebinh/wav2vec2-base-vietnamese-250h) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6154
- Wer: 0.3308

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 100
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.3404        | 3.81  | 50   | 0.3622          | 0.3094 |
| 0.2064        | 7.67  | 100  | 0.4312          | 0.3204 |
| 0.167         | 11.52 | 150  | 0.5050          | 0.3301 |
| 0.1268        | 15.37 | 200  | 0.4780          | 0.3508 |
| 0.1153        | 19.22 | 250  | 0.5835          | 0.3488 |
| 0.106         | 23.07 | 300  | 0.5370          | 0.3439 |
| 0.0886        | 26.89 | 350  | 0.5356          | 0.3377 |
| 0.0845        | 30.74 | 400  | 0.4925          | 0.3384 |
| 0.087         | 34.59 | 450  | 0.5850          | 0.3453 |
| 0.0712        | 38.44 | 500  | 0.5597          | 0.3432 |
| 0.0606        | 42.3  | 550  | 0.6218          | 0.3439 |
| 0.0597        | 46.15 | 600  | 0.5906          | 0.3439 |
| 0.0623        | 49.96 | 650  | 0.6310          | 0.3474 |
| 0.0478        | 53.81 | 700  | 0.6732          | 0.3619 |
| 0.0542        | 57.67 | 750  | 0.6400          | 0.3494 |
| 0.0535        | 61.52 | 800  | 0.6043          | 0.3467 |
| 0.045         | 65.37 | 850  | 0.5756          | 0.3412 |
| 0.0438        | 69.22 | 900  | 0.6089          | 0.3349 |
| 0.0341        | 73.07 | 950  | 0.6418          | 0.3398 |
| 0.0362        | 76.89 | 1000 | 0.5962          | 0.3419 |
| 0.0342        | 80.74 | 1050 | 0.6284          | 0.3356 |
| 0.0346        | 84.59 | 1100 | 0.6056          | 0.3322 |
| 0.0255        | 88.44 | 1150 | 0.6072          | 0.3308 |
| 0.0285        | 92.3  | 1200 | 0.6034          | 0.3322 |
| 0.027         | 96.15 | 1250 | 0.6145          | 0.3308 |
| 0.031         | 99.96 | 1300 | 0.6154          | 0.3308 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3

---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: librispeech-100h-supervised-aug
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# librispeech-100h-supervised-aug

This model is a fine-tuned version of [Kuray107/librispeech-5h-supervised](https://huggingface.co/Kuray107/librispeech-5h-supervised) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0776
- Wer: 0.0327

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.3099        | 1.12  | 1000  | 0.0748          | 0.0521 |
| 0.1873        | 2.24  | 2000  | 0.0674          | 0.0440 |
| 0.146         | 3.36  | 3000  | 0.0671          | 0.0406 |
| 0.1233        | 4.48  | 4000  | 0.0619          | 0.0381 |
| 0.1098        | 5.61  | 5000  | 0.0618          | 0.0381 |
| 0.0985        | 6.73  | 6000  | 0.0590          | 0.0355 |
| 0.0907        | 7.85  | 7000  | 0.0659          | 0.0352 |
| 0.0837        | 8.97  | 8000  | 0.0679          | 0.0359 |
| 0.0762        | 10.09 | 9000  | 0.0701          | 0.0349 |
| 0.0707        | 11.21 | 10000 | 0.0715          | 0.0348 |
| 0.0666        | 12.33 | 11000 | 0.0719          | 0.0346 |
| 0.0631        | 13.45 | 12000 | 0.0746          | 0.0347 |
| 0.0593        | 14.57 | 13000 | 0.0757          | 0.0340 |
| 0.0554        | 15.7  | 14000 | 0.0746          | 0.0337 |
| 0.053         | 16.82 | 15000 | 0.0757          | 0.0331 |
| 0.0525        | 17.94 | 16000 | 0.0752          | 0.0327 |
| 0.0514        | 19.06 | 17000 | 0.0776          | 0.0327 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.2
- Datasets 1.18.2
- Tokenizers 0.10.3

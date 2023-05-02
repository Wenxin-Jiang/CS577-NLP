---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-finetuned-cnn
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-cnn

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2647

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.2811        | 1.0   | 157  | 2.3283          |
| 2.3086        | 2.0   | 314  | 2.3172          |
| 2.3472        | 3.0   | 471  | 2.3033          |
| 2.3608        | 4.0   | 628  | 2.2989          |
| 2.3494        | 5.0   | 785  | 2.2975          |
| 2.3217        | 6.0   | 942  | 2.2701          |
| 2.3087        | 7.0   | 1099 | 2.2545          |
| 2.291         | 8.0   | 1256 | 2.2376          |
| 2.2983        | 9.0   | 1413 | 2.2653          |
| 2.2892        | 10.0  | 1570 | 2.2647          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

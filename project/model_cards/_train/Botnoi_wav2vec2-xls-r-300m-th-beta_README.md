---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: wav2vec2-xls-r-300m-th-beta
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-th-beta

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9096
- Wer: 0.7261
- Cer: 0.2160
- Clean Cer: 0.1909

## Model description

This model is available until Jan 12, 2023

## Intended uses & limitations

More information needed

## Training and evaluation data

We use our custom dataset splited into 70k training dataset, and 7k evaluation dataset
This is our detailed dataset

1. Common Voice 11
- filter 5k fifties age males out
- remain 25k training dataset

2. Botnoi voice
- 45k training dataset

Both dataset was through our custom cleansing text data.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 1000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    | Cer    | Clean Cer |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:---------:|
| 6.9481        | 0.34  | 500  | 3.5952          | 1.0    | 0.9815 | 0.9779    |
| 2.0387        | 0.68  | 1000 | 0.9096          | 0.7261 | 0.2160 | 0.1909    |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-vi-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-vi-colab

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2659
- Wer: 0.7160

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 5.3934        | 3.45  | 400  | 3.4806          | 1.0    |
| 2.3392        | 6.9   | 800  | 2.1210          | 0.9011 |
| 1.1786        | 10.34 | 1200 | 2.4091          | 0.7807 |
| 0.779         | 13.79 | 1600 | 2.7128          | 0.7621 |
| 0.5645        | 17.24 | 2000 | 3.0103          | 0.7428 |
| 0.4329        | 20.69 | 2400 | 3.0804          | 0.7219 |
| 0.3455        | 24.14 | 2800 | 3.1075          | 0.7190 |
| 0.2803        | 27.59 | 3200 | 3.2659          | 0.7160 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-turkish-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-turkish-colab

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3864
- Wer: 0.3077

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.8894        | 3.67  | 400  | 0.7272          | 0.7232 |
| 0.4265        | 7.34  | 800  | 0.4567          | 0.5033 |
| 0.1963        | 11.01 | 1200 | 0.4435          | 0.4511 |
| 0.1288        | 14.68 | 1600 | 0.3897          | 0.3773 |
| 0.0976        | 18.35 | 2000 | 0.4021          | 0.3502 |
| 0.079         | 22.02 | 2400 | 0.4140          | 0.3473 |
| 0.0646        | 25.69 | 2800 | 0.3993          | 0.3255 |
| 0.0502        | 29.36 | 3200 | 0.3864          | 0.3077 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3

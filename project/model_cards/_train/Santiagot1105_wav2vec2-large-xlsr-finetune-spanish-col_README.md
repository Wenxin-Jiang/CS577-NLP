---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xlsr-finetune-spanish-col
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-finetune-spanish-col

This model is a fine-tuned version of [jonatasgrosman/wav2vec2-large-xlsr-53-spanish](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-spanish) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.7105
- Wer: 0.9824

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
| 7.2829        | 3.25  | 400  | 2.9632          | 1.0    |
| 2.9664        | 6.5   | 800  | 2.8494          | 1.0542 |
| 2.8353        | 9.76  | 1200 | 2.8352          | 1.0101 |
| 2.7863        | 13.01 | 1600 | 2.7421          | 0.9837 |
| 2.762         | 16.26 | 2000 | 2.7254          | 0.9861 |
| 2.7483        | 19.51 | 2400 | 2.7228          | 0.9874 |
| 2.7482        | 22.76 | 2800 | 2.7228          | 0.9999 |
| 2.7373        | 26.02 | 3200 | 2.7163          | 0.9824 |
| 2.7328        | 29.27 | 3600 | 2.7105          | 0.9824 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.1+cu102
- Datasets 1.13.3
- Tokenizers 0.10.3

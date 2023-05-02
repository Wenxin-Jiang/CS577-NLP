---
tags:
- generated_from_trainer
datasets:
- cnn_dailymail
model-index:
- name: pegasus-cnn_dailymail_2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pegasus-cnn_dailymail_2

This model is a fine-tuned version of [google/pegasus-cnn_dailymail](https://huggingface.co/google/pegasus-cnn_dailymail) on the cnn_dailymail dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4308

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.5344        | 0.6   | 500  | 1.4497          |
| 1.5068        | 1.2   | 1000 | 1.4386          |
| 1.4983        | 1.8   | 1500 | 1.4315          |
| 1.389         | 2.39  | 2000 | 1.4308          |
| 1.4246        | 2.99  | 2500 | 1.4277          |
| 1.3656        | 3.59  | 3000 | 1.4308          |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.1
- Tokenizers 0.12.1

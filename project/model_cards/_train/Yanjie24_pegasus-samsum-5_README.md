---
tags:
- generated_from_trainer
datasets:
- samsum
model-index:
- name: pegasus-samsum-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pegasus-samsum-5

This model is a fine-tuned version of [google/pegasus-cnn_dailymail](https://huggingface.co/google/pegasus-cnn_dailymail) on the samsum dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3386

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
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.6957        | 0.54  | 500  | 1.4857          |
| 1.4033        | 1.09  | 1000 | 1.4117          |
| 1.497         | 1.63  | 1500 | 1.3742          |
| 1.4132        | 2.17  | 2000 | 1.3582          |
| 1.3858        | 2.72  | 2500 | 1.3482          |
| 1.2908        | 3.26  | 3000 | 1.3477          |
| 1.2357        | 3.8   | 3500 | 1.3386          |
| 1.2499        | 4.35  | 4000 | 1.3419          |
| 1.2349        | 4.89  | 4500 | 1.3386          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2

---
tags:
- generated_from_trainer
model-index:
- name: codeparrot-ds
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# codeparrot-ds

This model is a fine-tuned version of [](https://huggingface.co/) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2520

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 256
- eval_batch_size: 256
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 2048
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 1000
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.0285        | 0.61  | 5000 | 1.2520          |


### Framework versions

- Transformers 4.12.0
- Pytorch 1.12.1
- Datasets 1.12.1
- Tokenizers 0.10.3

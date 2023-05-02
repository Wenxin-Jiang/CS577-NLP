---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: codeparrot-ds-500sample-gpt-neo-2ep
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# codeparrot-ds-500sample-gpt-neo-2ep

This model is a fine-tuned version of [EleutherAI/gpt-neo-125M](https://huggingface.co/EleutherAI/gpt-neo-125M) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5483

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 1000
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 4.5248        | 0.19  | 1000  | 2.9757          |
| 2.5422        | 0.37  | 2000  | 2.4397          |
| 2.1642        | 0.56  | 3000  | 2.1880          |
| 1.9135        | 0.74  | 4000  | 1.9884          |
| 1.7236        | 0.93  | 5000  | 1.8470          |
| 1.5459        | 1.11  | 6000  | 1.7501          |
| 1.4363        | 1.3   | 7000  | 1.6761          |
| 1.3639        | 1.49  | 8000  | 1.6105          |
| 1.3046        | 1.67  | 9000  | 1.5667          |
| 1.273         | 1.86  | 10000 | 1.5483          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

---
license: mit
tags:
- generated_from_trainer
model-index:
- name: codeparrot-ds-sample-2ep-batchsize32
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# codeparrot-ds-sample-2ep-batchsize32

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5721

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
- distributed_type: tpu
- gradient_accumulation_steps: 8
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 1000
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 4.3529        | 0.19  | 1000  | 2.8073          |
| 2.4602        | 0.37  | 2000  | 2.2907          |
| 2.1127        | 0.56  | 3000  | 2.0745          |
| 1.9187        | 0.74  | 4000  | 1.9287          |
| 1.782         | 0.93  | 5000  | 1.8234          |
| 1.639         | 1.11  | 6000  | 1.7456          |
| 1.5519        | 1.3   | 7000  | 1.6738          |
| 1.489         | 1.49  | 8000  | 1.6235          |
| 1.4372        | 1.67  | 9000  | 1.5874          |
| 1.4122        | 1.86  | 10000 | 1.5721          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu102
- Datasets 2.1.0
- Tokenizers 0.12.1

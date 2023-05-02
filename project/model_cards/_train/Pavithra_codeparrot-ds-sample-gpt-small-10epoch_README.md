---
license: mit
tags:
- generated_from_trainer
model-index:
- name: codeparrot-ds-sample-gpt-small-10epoch
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# codeparrot-ds-sample-gpt-small-10epoch

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0943

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
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 4.29          | 0.94  | 1000  | 2.8452          |
| 2.3155        | 1.88  | 2000  | 2.3659          |
| 1.8817        | 2.82  | 3000  | 2.2085          |
| 1.6245        | 3.77  | 4000  | 2.1260          |
| 1.4314        | 4.71  | 5000  | 2.0705          |
| 1.2698        | 5.65  | 6000  | 2.0603          |
| 1.1281        | 6.59  | 7000  | 2.0599          |
| 1.0108        | 7.53  | 8000  | 2.0769          |
| 0.9167        | 8.47  | 9000  | 2.0870          |
| 0.8551        | 9.42  | 10000 | 2.0943          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

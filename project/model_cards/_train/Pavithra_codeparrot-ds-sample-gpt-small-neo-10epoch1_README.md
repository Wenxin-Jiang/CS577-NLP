---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: codeparrot-ds-sample-gpt-small-neo-10epoch1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# codeparrot-ds-sample-gpt-small-neo-10epoch1

This model is a fine-tuned version of [EleutherAI/gpt-neo-125M](https://huggingface.co/EleutherAI/gpt-neo-125M) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5696

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
| 3.5639        | 0.94  | 1000  | 2.9253          |
| 2.3253        | 1.88  | 2000  | 2.4563          |
| 1.8494        | 2.82  | 3000  | 2.2655          |
| 1.5133        | 3.77  | 4000  | 2.1635          |
| 1.249         | 4.71  | 5000  | 2.1414          |
| 1.0194        | 5.65  | 6000  | 2.1818          |
| 0.7999        | 6.59  | 7000  | 2.2738          |
| 0.5971        | 7.53  | 8000  | 2.3910          |
| 0.4238        | 8.47  | 9000  | 2.5062          |
| 0.3107        | 9.42  | 10000 | 2.5696          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

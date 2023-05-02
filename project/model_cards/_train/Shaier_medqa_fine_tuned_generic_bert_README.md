---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: medqa_fine_tuned_generic_bert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medqa_fine_tuned_generic_bert

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4239
- Accuracy: 0.2869

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 318  | 1.3851          | 0.2594   |
| 1.3896        | 2.0   | 636  | 1.3805          | 0.2807   |
| 1.3896        | 3.0   | 954  | 1.3852          | 0.2948   |
| 1.3629        | 4.0   | 1272 | 1.3996          | 0.2980   |
| 1.3068        | 5.0   | 1590 | 1.4239          | 0.2869   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.3.2
- Tokenizers 0.11.0

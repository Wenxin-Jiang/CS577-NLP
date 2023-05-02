---
tags:
- generated_from_trainer
datasets:
- custom_squad_v2
model-index:
- name: kobigbird-pure45-34458617
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# kobigbird-pure45-34458617

This model is a fine-tuned version of [monologg/kobigbird-bert-base](https://huggingface.co/monologg/kobigbird-bert-base) on the custom_squad_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 4.3725

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 45
- gradient_accumulation_steps: 8
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 0.84  | 4    | 5.0505          |
| No log        | 1.84  | 8    | 4.4642          |
| No log        | 2.84  | 12   | 4.3725          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

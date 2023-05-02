---
tags:
- generated_from_trainer
datasets:
- custom_squad_v2
model-index:
- name: koelectra-68397641
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# koelectra-68397641

This model is a fine-tuned version of [klue/roberta-large](https://huggingface.co/klue/roberta-large) on the custom_squad_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3509

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 64
- eval_batch_size: 64
- seed: 30
- gradient_accumulation_steps: 8
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 0.99  | 21   | 1.8294          |
| No log        | 1.99  | 42   | 1.3509          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

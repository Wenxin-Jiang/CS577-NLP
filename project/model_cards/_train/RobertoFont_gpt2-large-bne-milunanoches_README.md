---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: gpt2-large-bne-milunanoches
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-large-bne-milunanoches

This model is a fine-tuned version of [PlanTL-GOB-ES/gpt2-large-bne](https://huggingface.co/PlanTL-GOB-ES/gpt2-large-bne) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9118

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 1
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 32
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 0.97  | 25   | 3.2210          |
| No log        | 1.97  | 50   | 2.9247          |
| No log        | 2.97  | 75   | 2.8850          |
| No log        | 3.97  | 100  | 2.9118          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

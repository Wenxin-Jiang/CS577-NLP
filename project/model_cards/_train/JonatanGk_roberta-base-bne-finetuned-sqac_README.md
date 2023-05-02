---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- sqac
model-index:
- name: roberta-base-bne-finetuned-sqac
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-bne-finetuned-sqac

This model is a fine-tuned version of [PlanTL-GOB-ES/roberta-base-bne](https://huggingface.co/PlanTL-GOB-ES/roberta-base-bne) on the sqac dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2066

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.9924        | 1.0   | 1196 | 0.8670          |
| 0.474         | 2.0   | 2392 | 0.8923          |
| 0.1637        | 3.0   | 3588 | 1.2066          |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.14.0
- Tokenizers 0.10.3

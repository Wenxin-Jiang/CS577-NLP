---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- squad_v2_sv
model-index:
- name: flan-t5-base-squad-swe2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# flan-t5-base-squad-swe2

This model is a fine-tuned version of [google/flan-t5-base](https://huggingface.co/google/flan-t5-base) on the squad_v2_sv dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4248

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.0881        | 1.0   | 890  | 1.6422          |
| 1.7772        | 2.0   | 1780 | 1.5586          |
| 1.6763        | 3.0   | 2670 | 1.5153          |
| 1.6215        | 4.0   | 3560 | 1.4852          |
| 1.5912        | 5.0   | 4450 | 1.4629          |
| 1.5651        | 6.0   | 5340 | 1.4481          |
| 1.5407        | 7.0   | 6230 | 1.4374          |
| 1.5278        | 8.0   | 7120 | 1.4308          |
| 1.5137        | 9.0   | 8010 | 1.4269          |
| 1.5116        | 10.0  | 8900 | 1.4248          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

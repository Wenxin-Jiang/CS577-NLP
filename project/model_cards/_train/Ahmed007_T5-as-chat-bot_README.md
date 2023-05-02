---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: T5-as-chat-bot
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# T5-as-chat-bot

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2717

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
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 187  | 2.4258          |
| No log        | 2.0   | 374  | 2.3627          |
| 2.5802        | 3.0   | 561  | 2.3284          |
| 2.5802        | 4.0   | 748  | 2.3109          |
| 2.5802        | 5.0   | 935  | 2.2958          |
| 2.3212        | 6.0   | 1122 | 2.2850          |
| 2.3212        | 7.0   | 1309 | 2.2779          |
| 2.3212        | 8.0   | 1496 | 2.2726          |
| 2.1892        | 9.0   | 1683 | 2.2703          |
| 2.1892        | 10.0  | 1870 | 2.2689          |
| 2.111         | 11.0  | 2057 | 2.2683          |
| 2.111         | 12.0  | 2244 | 2.2672          |
| 2.111         | 13.0  | 2431 | 2.2655          |
| 2.0484        | 14.0  | 2618 | 2.2685          |
| 2.0484        | 15.0  | 2805 | 2.2703          |
| 2.0484        | 16.0  | 2992 | 2.2698          |
| 2.0019        | 17.0  | 3179 | 2.2699          |
| 2.0019        | 18.0  | 3366 | 2.2715          |
| 1.9803        | 19.0  | 3553 | 2.2719          |
| 1.9803        | 20.0  | 3740 | 2.2717          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

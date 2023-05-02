---
license: mit
tags:
- generated_from_trainer
model-index:
- name: poem-gen-spanish-t5-small-d2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# poem-gen-spanish-t5-small-d2

This model is a fine-tuned version of [flax-community/spanish-t5-small](https://huggingface.co/flax-community/spanish-t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9027

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 3.223         | 0.73  | 30000  | 3.1479          |
| 3.0109        | 1.46  | 60000  | 3.0544          |
| 2.8649        | 2.19  | 90000  | 2.9730          |
| 2.7603        | 2.93  | 120000 | 2.9301          |
| 2.6343        | 3.66  | 150000 | 2.9188          |
| 2.5094        | 4.39  | 180000 | 2.9064          |
| 2.391         | 5.12  | 210000 | 2.9073          |
| 2.3592        | 5.85  | 240000 | 2.9022          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

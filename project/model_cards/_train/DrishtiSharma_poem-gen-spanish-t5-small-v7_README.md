---
license: mit
tags:
- generated_from_trainer
model-index:
- name: poem-gen-spanish-t5-small-v7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# poem-gen-spanish-t5-small-v7

This model is a fine-tuned version of [hackathon-pln-es/poem-gen-spanish-t5-small](https://huggingface.co/hackathon-pln-es/poem-gen-spanish-t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9201

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.000333
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 3.1716        | 0.73  | 30000  | 3.1114          |
| 2.9666        | 1.46  | 60000  | 3.0271          |
| 2.8292        | 2.19  | 90000  | 2.9531          |
| 2.7264        | 2.93  | 120000 | 2.9126          |
| 2.6057        | 3.66  | 150000 | 2.9175          |
| 2.4876        | 4.39  | 180000 | 2.9077          |
| 2.3791        | 5.12  | 210000 | 2.9240          |
| 2.3515        | 5.85  | 240000 | 2.9169          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

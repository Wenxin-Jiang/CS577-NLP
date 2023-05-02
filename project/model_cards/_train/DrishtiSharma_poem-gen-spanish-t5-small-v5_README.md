---
license: mit
tags:
- generated_from_trainer
model-index:
- name: poem-gen-spanish-t5-small-v5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# poem-gen-spanish-t5-small-v5

This model is a fine-tuned version of [hackathon-pln-es/poem-gen-spanish-t5-small](https://huggingface.co/hackathon-pln-es/poem-gen-spanish-t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8881

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.000125
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 2.9366        | 0.73  | 30000  | 2.9656          |
| 2.7518        | 1.46  | 60000  | 2.9120          |
| 2.6018        | 2.19  | 90000  | 2.8870          |
| 2.5262        | 2.93  | 120000 | 2.8646          |
| 2.3886        | 3.66  | 150000 | 2.8816          |
| 2.2758        | 4.39  | 180000 | 2.8900          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: ViT-chess-V4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ViT-chess-V4

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.2867
- Accuracy: 0.1942

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
- train_batch_size: 10
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Accuracy |
|:-------------:|:-----:|:------:|:---------------:|:--------:|
| 5.4877        | 1.0   | 45000  | 5.4554          | 0.1044   |
| 4.9794        | 2.0   | 90000  | 5.0001          | 0.1371   |
| 4.5956        | 3.0   | 135000 | 4.6720          | 0.1596   |
| 4.3402        | 4.0   | 180000 | 4.4082          | 0.1834   |
| 4.097         | 5.0   | 225000 | 4.2867          | 0.1942   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

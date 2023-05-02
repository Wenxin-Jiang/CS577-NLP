---
tags:
- generated_from_trainer
model-index:
- name: scibert_scivocab_cased-new-finetuned-breastcancer
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# scibert_scivocab_cased-new-finetuned-breastcancer

This model is a fine-tuned version of [allenai/scibert_scivocab_cased](https://huggingface.co/allenai/scibert_scivocab_cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2439

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 40   | 3.1340          |
| No log        | 2.0   | 80   | 1.6044          |
| No log        | 3.0   | 120  | 1.2439          |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

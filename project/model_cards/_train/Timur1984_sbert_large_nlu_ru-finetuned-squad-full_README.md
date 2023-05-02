---
tags:
- generated_from_trainer
model-index:
- name: sbert_large_nlu_ru-finetuned-squad-full
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sbert_large_nlu_ru-finetuned-squad-full

This model is a fine-tuned version of [ruselkomp/sbert_large_nlu_ru-finetuned-squad-full](https://huggingface.co/ruselkomp/sbert_large_nlu_ru-finetuned-squad-full) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6119

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
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 17   | 0.5747          |
| No log        | 2.0   | 34   | 0.6119          |


### Framework versions

- Transformers 4.19.0.dev0
- Pytorch 1.10.0+cu111
- Datasets 2.0.1.dev0
- Tokenizers 0.11.6

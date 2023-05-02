---
license: cc-by-nc-4.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: videomae-base-finetuned-kinetics-finetuned-ucf101-subset-finetuned-ucf101-subset
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# videomae-base-finetuned-kinetics-finetuned-ucf101-subset-finetuned-ucf101-subset

This model is a fine-tuned version of [sayakpaul/videomae-base-finetuned-kinetics-finetuned-ucf101-subset](https://huggingface.co/sayakpaul/videomae-base-finetuned-kinetics-finetuned-ucf101-subset) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4351
- Accuracy: 0.2727

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- training_steps: 36

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.6409        | 1.0   | 36   | 1.4351          | 0.2727   |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1+cu116
- Datasets 2.8.0
- Tokenizers 0.12.1

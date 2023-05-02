---
tags:
- generated_from_trainer
datasets:
- ydshieh/coco_dataset_script
model-index:
- name: clip-roberta-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clip-roberta-finetuned

This model is a fine-tuned version of [./clip-roberta](https://huggingface.co/./clip-roberta) on the ydshieh/coco_dataset_script 2017 dataset.

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- distributed_type: tpu
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1+cu102
- Datasets 2.7.1
- Tokenizers 0.13.2

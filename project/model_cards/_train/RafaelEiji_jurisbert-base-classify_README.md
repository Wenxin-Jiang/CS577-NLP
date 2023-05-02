---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: output
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [juridics/jurisbert-base-portuguese-uncased](https://huggingface.co/juridics/jurisbert-base-portuguese-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4838
- Accuracy: 0.7176

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
- train_batch_size: 24
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20.0

### Training results



### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.12.0+cu116
- Datasets 2.6.1
- Tokenizers 0.13.1

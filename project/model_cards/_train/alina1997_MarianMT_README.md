---
language:
- en
- de
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: model_output_en_de
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model_output_en_de

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-en-de](https://huggingface.co/Helsinki-NLP/opus-mt-en-de) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1298
- Bleu: 33.9121
- Gen Len: 76.8132

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0+cu111
- Datasets 1.15.1
- Tokenizers 0.10.3

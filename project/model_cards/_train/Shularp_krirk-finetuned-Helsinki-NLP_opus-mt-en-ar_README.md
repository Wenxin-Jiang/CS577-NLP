---
license: apache-2.0
tags:
- translation
- generated_from_trainer
metrics:
- bleu
model-index:
- name: krirk-finetuned-Helsinki-NLP_opus-mt-en-ar
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# krirk-finetuned-Helsinki-NLP_opus-mt-en-ar

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-en-ar](https://huggingface.co/Helsinki-NLP/opus-mt-en-ar) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4468
- Bleu: 26.9281

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
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 1.6252        | 1.0   | 32   | 1.4686          | 26.1394 |
| 1.4867        | 2.0   | 64   | 1.4496          | 26.8139 |
| 1.4121        | 3.0   | 96   | 1.4468          | 26.9281 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2

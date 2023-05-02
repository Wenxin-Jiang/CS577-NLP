---
license: apache-2.0
tags:
- translation
- generated_from_trainer
datasets:
- tatoeba_mt
metrics:
- bleu
model-index:
- name: fine-tuned_ar-en
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: tatoeba_mt
      type: tatoeba_mt
      config: ara-eng
      split: validation
      args: ara-eng
    metrics:
    - name: Bleu
      type: bleu
      value: 51.81577100911173
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fine-tuned_ar-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-ar-en](https://huggingface.co/Helsinki-NLP/opus-mt-ar-en) on the tatoeba_mt dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8464
- Bleu: 51.8158

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



### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

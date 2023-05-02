---
license: mit
tags:
- translation
- generated_from_trainer
datasets:
- kde4
metrics:
- bleu
model-index:
- name: m2m100_418M-fr
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: kde4
      type: kde4
      args: en-fr
    metrics:
    - name: Bleu
      type: bleu
      value: 51.1339693938271
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# m2m100_418M-fr

This model is a fine-tuned version of [facebook/m2m100_418M](https://huggingface.co/facebook/m2m100_418M) on the kde4 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7021
- Bleu: 51.1340

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
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu    |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 0.749         | 1.0   | 23645 | 0.7021          | 51.1344 |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.15.2.dev0
- Tokenizers 0.10.3

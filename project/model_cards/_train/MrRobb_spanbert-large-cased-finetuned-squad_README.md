---
tags:
- generated_from_trainer
datasets:
- squad_v2
model-index:
- name: spanbert-large-cased-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# spanbert-large-cased-finetuned-squad

This model is a fine-tuned version of [SpanBERT/spanbert-large-cased](https://huggingface.co/SpanBERT/spanbert-large-cased) on the squad_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6976

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 1.6057        | 1.0   | 132932 | 1.5069          |
| 1.1252        | 2.0   | 265864 | 1.4578          |
| 0.7214        | 3.0   | 398796 | 1.6976          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1
- Datasets 2.8.0
- Tokenizers 0.13.2

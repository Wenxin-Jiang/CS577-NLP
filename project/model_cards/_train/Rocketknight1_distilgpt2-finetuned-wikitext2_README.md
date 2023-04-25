---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Rocketknight1/distilgpt2-finetuned-wikitext2
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Rocketknight1/distilgpt2-finetuned-wikitext2

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 3.8577
- Validation Loss: 3.6752
- Epoch: 0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 3.8577     | 3.6752          | 0     |


### Framework versions

- Transformers 4.16.0.dev0
- TensorFlow 2.8.0-rc0
- Datasets 1.17.0
- Tokenizers 0.11.0
---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Rocketknight1/opus-mt-en-ROMANCE-finetuned-en-to-ro
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Rocketknight1/opus-mt-en-ROMANCE-finetuned-en-to-ro

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-en-ROMANCE](https://huggingface.co/Helsinki-NLP/opus-mt-en-ROMANCE) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.7140
- Validation Loss: 1.2757
- Train Bleu: 26.7914
- Train Gen Len: 41.4932
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

| Train Loss | Validation Loss | Train Bleu | Train Gen Len | Epoch |
|:----------:|:---------------:|:----------:|:-------------:|:-----:|
| 0.7140     | 1.2757          | 26.7914    | 41.4932       | 0     |


### Framework versions

- Transformers 4.21.0.dev0
- TensorFlow 2.9.1
- Datasets 2.4.0
- Tokenizers 0.11.0

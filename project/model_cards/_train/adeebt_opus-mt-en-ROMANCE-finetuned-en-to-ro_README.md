---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: adeebt/opus-mt-en-ROMANCE-finetuned-en-to-ro
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# adeebt/opus-mt-en-ROMANCE-finetuned-en-to-ro

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-en-ROMANCE](https://huggingface.co/Helsinki-NLP/opus-mt-en-ROMANCE) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.6202
- Validation Loss: 1.2497
- Train Bleu: 25.1980
- Train Gen Len: 42.5208
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
| 0.6202     | 1.2497          | 25.1980    | 42.5208       | 0     |


### Framework versions

- Transformers 4.19.2
- TensorFlow 2.8.0
- Datasets 2.2.1
- Tokenizers 0.12.1

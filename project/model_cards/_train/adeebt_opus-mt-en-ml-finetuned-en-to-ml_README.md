---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: adeebt/opus-mt-en-ml-finetuned-en-to-ml
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# adeebt/opus-mt-en-ml-finetuned-en-to-ml

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-en-ml](https://huggingface.co/Helsinki-NLP/opus-mt-en-ml) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 2.5102
- Validation Loss: 2.2650
- Train Bleu: 6.9525
- Train Gen Len: 22.3542
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 0.0002, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Bleu | Train Gen Len | Epoch |
|:----------:|:---------------:|:----------:|:-------------:|:-----:|
| 2.5102     | 2.2650          | 6.9525     | 22.3542       | 0     |


### Framework versions

- Transformers 4.20.1
- TensorFlow 2.8.2
- Datasets 2.3.2
- Tokenizers 0.12.1

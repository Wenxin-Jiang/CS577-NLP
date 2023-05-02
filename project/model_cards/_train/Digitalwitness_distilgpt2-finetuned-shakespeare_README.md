---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Digitalwitness/distilgpt2-finetuned-shakespeare
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Digitalwitness/distilgpt2-finetuned-shakespeare

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 2.0603
- Validation Loss: 2.2069
- Epoch: 19

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
| 3.4056     | 3.1490          | 0     |
| 3.1359     | 2.9958          | 1     |
| 2.9970     | 2.9052          | 2     |
| 2.9003     | 2.8363          | 3     |
| 2.8192     | 2.7759          | 4     |
| 2.7524     | 2.7306          | 5     |
| 2.6881     | 2.6775          | 6     |
| 2.6294     | 2.6329          | 7     |
| 2.5716     | 2.5949          | 8     |
| 2.5213     | 2.5512          | 9     |
| 2.4652     | 2.5107          | 10    |
| 2.4156     | 2.4803          | 11    |
| 2.3677     | 2.4329          | 12    |
| 2.3163     | 2.3989          | 13    |
| 2.2735     | 2.3695          | 14    |
| 2.2311     | 2.3317          | 15    |
| 2.1842     | 2.2924          | 16    |
| 2.1386     | 2.2688          | 17    |
| 2.1015     | 2.2297          | 18    |
| 2.0603     | 2.2069          | 19    |


### Framework versions

- Transformers 4.23.1
- TensorFlow 2.9.2
- Datasets 2.6.0
- Tokenizers 0.13.1

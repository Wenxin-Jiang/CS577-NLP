---
tags:
- generated_from_keras_callback
model-index:
- name: AdwayK/biobert_ncbi_disease_ner_tuned_on_TAC2017
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# AdwayK/biobert_ncbi_disease_ner_tuned_on_TAC2017

This model is a fine-tuned version of [ugaray96/biobert_ncbi_disease_ner](https://huggingface.co/ugaray96/biobert_ncbi_disease_ner) on the TAC 2017 dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0343
- Validation Loss: 0.0679
- Epoch: 4

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 975, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 0.5377     | 0.1269          | 0     |
| 0.0997     | 0.0776          | 1     |
| 0.0621     | 0.0700          | 2     |
| 0.0434     | 0.0757          | 3     |
| 0.0343     | 0.0679          | 4     |


### Framework versions

- Transformers 4.18.0
- TensorFlow 2.8.0
- Datasets 2.1.0
- Tokenizers 0.12.1

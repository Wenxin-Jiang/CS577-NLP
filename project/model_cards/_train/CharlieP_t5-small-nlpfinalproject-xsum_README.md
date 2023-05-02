---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: CharlieP/t5-small-nlpfinalproject-xsum
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# CharlieP/t5-small-nlpfinalproject-xsum

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 3.2391
- Validation Loss: 3.0511
- Train Rouge1: 21.2434
- Train Rouge2: 4.0808
- Train Rougel: 16.6836
- Train Rougelsum: 16.6460
- Train Gen Len: 18.42
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Rouge1 | Train Rouge2 | Train Rougel | Train Rougelsum | Train Gen Len | Epoch |
|:----------:|:---------------:|:------------:|:------------:|:------------:|:---------------:|:-------------:|:-----:|
| 3.8204     | 3.2757          | 18.2829      | 2.7616       | 14.7101      | 14.7047         | 18.59         | 0     |
| 3.4646     | 3.1560          | 20.4371      | 3.6903       | 16.0587      | 16.0790         | 18.35         | 1     |
| 3.3630     | 3.1028          | 20.7907      | 3.9282       | 15.9696      | 15.8916         | 18.42         | 2     |
| 3.2904     | 3.0713          | 21.6980      | 4.3218       | 16.7261      | 16.6776         | 18.42         | 3     |
| 3.2391     | 3.0511          | 21.2434      | 4.0808       | 16.6836      | 16.6460         | 18.42         | 4     |


### Framework versions

- Transformers 4.23.1
- TensorFlow 2.9.2
- Datasets 2.6.1
- Tokenizers 0.13.1

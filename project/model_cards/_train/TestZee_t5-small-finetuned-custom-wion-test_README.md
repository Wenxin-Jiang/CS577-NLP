---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: TestZee/t5-small-finetuned-custom-wion-test
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# TestZee/t5-small-finetuned-custom-wion-test

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.9773
- Validation Loss: 0.8028
- Epoch: 9

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
| 2.2933     | 0.9052          | 0     |
| 2.3077     | 0.8923          | 1     |
| 2.1972     | 0.8797          | 2     |
| 2.1740     | 0.8677          | 3     |
| 2.1535     | 0.8564          | 4     |
| 2.1772     | 0.8452          | 5     |
| 2.1227     | 0.8342          | 6     |
| 2.0875     | 0.8234          | 7     |
| 2.0279     | 0.8129          | 8     |
| 1.9773     | 0.8028          | 9     |


### Framework versions

- Transformers 4.20.1
- TensorFlow 2.8.2
- Tokenizers 0.12.1

---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: opus-mt-en-ar-finetunedSTEM-v5-en-to-ar
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# opus-mt-en-ar-finetunedSTEM-v5-en-to-ar

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-en-ar](https://huggingface.co/Helsinki-NLP/opus-mt-en-ar) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0921
- Validation Loss: 8.1798
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

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 0.1178     | 7.5286          | 0     |
| 0.1103     | 7.7336          | 1     |
| 0.1028     | 7.6719          | 2     |
| 0.0976     | 8.1806          | 3     |
| 0.0921     | 8.1798          | 4     |


### Framework versions

- Transformers 4.17.0.dev0
- TensorFlow 2.7.0
- Datasets 1.18.4.dev0
- Tokenizers 0.10.3

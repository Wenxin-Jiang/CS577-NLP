---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: AnnaR/literature_summarizer
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# AnnaR/literature_summarizer

This model is a fine-tuned version of [sshleifer/distilbart-xsum-1-1](https://huggingface.co/sshleifer/distilbart-xsum-1-1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 3.2180
- Validation Loss: 4.7198
- Epoch: 10

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5.6e-05, 'decay_steps': 5300, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.1}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 5.6694     | 5.0234          | 0     |
| 4.9191     | 4.8161          | 1     |
| 4.5770     | 4.7170          | 2     |
| 4.3268     | 4.6571          | 3     |
| 4.1073     | 4.6296          | 4     |
| 3.9225     | 4.6279          | 5     |
| 3.7564     | 4.6288          | 6     |
| 3.5989     | 4.6731          | 7     |
| 3.4611     | 4.6767          | 8     |
| 3.3356     | 4.6934          | 9     |
| 3.2180     | 4.7198          | 10    |


### Framework versions

- Transformers 4.17.0
- TensorFlow 2.8.0
- Datasets 2.0.0
- Tokenizers 0.11.6

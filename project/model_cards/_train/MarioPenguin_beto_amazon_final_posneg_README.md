---
tags:
- generated_from_keras_callback
model-index:
- name: beto_amazon_final_posneg
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# beto_amazon_final_posneg

This model is a fine-tuned version of [dccuchile/bert-base-spanish-wwm-uncased](https://huggingface.co/dccuchile/bert-base-spanish-wwm-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1429
- Train Accuracy: 0.9510
- Validation Loss: 0.2942
- Validation Accuracy: 0.8913
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
- optimizer: {'name': 'Adam', 'learning_rate': 5e-07, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Accuracy | Validation Loss | Validation Accuracy | Epoch |
|:----------:|:--------------:|:---------------:|:-------------------:|:-----:|
| 0.6474     | 0.6545         | 0.5618          | 0.7893              | 0     |
| 0.4576     | 0.8360         | 0.3672          | 0.8560              | 1     |
| 0.3088     | 0.8925         | 0.3096          | 0.8752              | 2     |
| 0.2529     | 0.9028         | 0.2888          | 0.8855              | 3     |
| 0.2177     | 0.9168         | 0.2876          | 0.8865              | 4     |
| 0.1973     | 0.9280         | 0.2921          | 0.8865              | 5     |
| 0.1792     | 0.9373         | 0.2844          | 0.8903              | 6     |
| 0.1686     | 0.9423         | 0.2859          | 0.8898              | 7     |
| 0.1525     | 0.9480         | 0.2884          | 0.8917              | 8     |
| 0.1429     | 0.9510         | 0.2942          | 0.8913              | 9     |


### Framework versions

- Transformers 4.17.0
- TensorFlow 2.8.0
- Datasets 1.18.3
- Tokenizers 0.11.6

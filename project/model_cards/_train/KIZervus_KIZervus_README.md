---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: tmp3y468_8j
  results: []
widget:
- text: "Ich liebe dich!"
  example_title: "Non-vulgar"
- text: "Leck mich am arsch"
  example_title: "Vulgar"
---

# KIZervus

This model is a fine-tuned version of [distilbert-base-german-cased](https://huggingface.co/distilbert-base-german-cased).
It is trained to classify german text into the classes "vulgar" speech and "non-vulgar" speech. 
The data set is a collection of other labeled sources in german. For an overview, see the github repository here: https://github.com/NKDataConv/KIZervus
Both data and training procedure are documented in the GitHub repo. Your are welcome to contribute.

It achieves the following results on the evaluation set:
- Train Loss: 0.4640
- Train Accuracy: 0.7744
- Validation Loss: 0.4852
- Validation Accuracy: 0.7937
- Epoch: 1

## Training procedure
For details, see the repo and documentation here: https://github.com/NKDataConv/KIZervus

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 5e-05, 'decay_steps': 822, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train Accuracy | Validation Loss | Validation Accuracy | Epoch |
|:----------:|:--------------:|:---------------:|:-------------------:|:-----:|
| 0.4830     | 0.7617         | 0.5061          | 0.7406              | 0     |
| 0.4640     | 0.7744         | 0.4852          | 0.7937              | 1     |


### Framework versions

- Transformers 4.21.2
- TensorFlow 2.8.2
- Datasets 2.2.2
- Tokenizers 0.12.1

### Supporter

![BMBF Logo](./BMBF_Logo.png)

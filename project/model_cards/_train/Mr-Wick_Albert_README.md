---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Mr-Wick/Albert
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Mr-Wick/Albert

This model is a fine-tuned version of [Mr-Wick/Albert](https://huggingface.co/Mr-Wick/Albert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.4248
- Train End Logits Accuracy: 0.3423
- Train Loss Accuracy: 0.0664
- Train Start Logits Accuracy: 0.3437
- Validation Loss: 0.9468
- Validation End Logits Accuracy: 0.4724
- Validation Loss Accuracy: 0.0591
- Validation Start Logits Accuracy: 0.4772
- Epoch: 1

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 16494, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Train End Logits Accuracy | Train Loss Accuracy | Train Start Logits Accuracy | Validation Loss | Validation End Logits Accuracy | Validation Loss Accuracy | Validation Start Logits Accuracy | Epoch |
|:----------:|:-------------------------:|:-------------------:|:---------------------------:|:---------------:|:------------------------------:|:------------------------:|:--------------------------------:|:-----:|
| 0.6581     | 0.3488                    | 0.0671              | 0.3529                      | 0.9366          | 0.4415                         | 0.0657                   | 0.4486                           | 0     |
| 0.4248     | 0.3423                    | 0.0664              | 0.3437                      | 0.9468          | 0.4724                         | 0.0591                   | 0.4772                           | 1     |


### Framework versions

- Transformers 4.17.0
- TensorFlow 2.8.0
- Datasets 2.0.0
- Tokenizers 0.11.6

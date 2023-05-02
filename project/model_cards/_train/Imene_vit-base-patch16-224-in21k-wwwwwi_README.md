---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: Imene/vit-base-patch16-224-in21k-wwwwwi
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Imene/vit-base-patch16-224-in21k-wwwwwi

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 3.2187
- Train Accuracy: 0.5652
- Train Top-3-accuracy: 0.7611
- Validation Loss: 3.8221
- Validation Accuracy: 0.2540
- Validation Top-3-accuracy: 0.4409
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
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 3e-05, 'decay_steps': 4920, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16

### Training results

| Train Loss | Train Accuracy | Train Top-3-accuracy | Validation Loss | Validation Accuracy | Validation Top-3-accuracy | Epoch |
|:----------:|:--------------:|:--------------------:|:---------------:|:-------------------:|:-------------------------:|:-----:|
| 5.3476     | 0.0283         | 0.0716               | 5.1306          | 0.0483              | 0.1240                    | 0     |
| 4.9357     | 0.0914         | 0.2057               | 4.7998          | 0.1158              | 0.2385                    | 1     |
| 4.6155     | 0.1641         | 0.3230               | 4.5616          | 0.1430              | 0.2891                    | 2     |
| 4.3325     | 0.2269         | 0.4188               | 4.3480          | 0.1722              | 0.3391                    | 3     |
| 4.0702     | 0.2915         | 0.4984               | 4.1662          | 0.2042              | 0.3886                    | 4     |
| 3.8262     | 0.3638         | 0.5758               | 4.0416          | 0.2296              | 0.4067                    | 5     |
| 3.6117     | 0.4258         | 0.6415               | 3.9451          | 0.2329              | 0.4234                    | 6     |
| 3.4324     | 0.4855         | 0.6956               | 3.8690          | 0.2499              | 0.4397                    | 7     |
| 3.2991     | 0.5320         | 0.7376               | 3.8351          | 0.2553              | 0.4359                    | 8     |
| 3.2187     | 0.5652         | 0.7611               | 3.8221          | 0.2540              | 0.4409                    | 9     |


### Framework versions

- Transformers 4.21.2
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1

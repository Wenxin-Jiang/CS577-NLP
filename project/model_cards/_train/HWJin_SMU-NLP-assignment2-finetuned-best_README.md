---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: HWJin/SMU-NLP-assignment2-finetuned-best
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# HWJin/SMU-NLP-assignment2-finetuned-best

This model is a fine-tuned version of [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.9936
- Validation Loss: 0.9867
- Epoch: 13

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'WarmUp', 'config': {'initial_learning_rate': 2e-05, 'decay_schedule_fn': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 990, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}, '__passive_serialization__': True}, 'warmup_steps': 10, 'power': 1.0, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: mixed_float16

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 1.6490     | 1.2199          | 0     |
| 1.2679     | 1.1622          | 1     |
| 1.1796     | 1.0931          | 2     |
| 1.1200     | 1.0274          | 3     |
| 1.0841     | 1.0739          | 4     |
| 1.0567     | 1.0317          | 5     |
| 1.0164     | 0.9895          | 6     |
| 0.9819     | 1.0365          | 7     |
| 0.9960     | 0.9857          | 8     |
| 1.0143     | 0.9954          | 9     |
| 1.0156     | 1.0173          | 10    |
| 0.9915     | 1.0391          | 11    |
| 1.0246     | 1.0288          | 12    |
| 0.9936     | 0.9867          | 13    |


### Framework versions

- Transformers 4.19.2
- TensorFlow 2.8.2
- Datasets 2.2.2
- Tokenizers 0.12.1

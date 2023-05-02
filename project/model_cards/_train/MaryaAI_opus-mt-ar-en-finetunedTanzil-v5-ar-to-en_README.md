---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: opus-mt-ar-en-finetunedTanzil-v5-ar-to-en
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# opus-mt-ar-en-finetunedTanzil-v5-ar-to-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-ar-en](https://huggingface.co/Helsinki-NLP/opus-mt-ar-en) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.8101
- Validation Loss: 0.9477
- Train Bleu: 9.3241
- Train Gen Len: 88.73
- Train Rouge1: 56.4906
- Train Rouge2: 34.2668
- Train Rougel: 53.2279
- Train Rougelsum: 53.7836
- Epoch: 2

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

| Train Loss | Validation Loss | Train Bleu | Train Gen Len | Train Rouge1 | Train Rouge2 | Train Rougel | Train Rougelsum | Epoch |
|:----------:|:---------------:|:----------:|:-------------:|:------------:|:------------:|:------------:|:---------------:|:-----:|
| 0.8735     | 0.9809          | 11.0863    | 78.68         | 56.4557      | 33.3673      | 53.4828      | 54.1197         | 0     |
| 0.8408     | 0.9647          | 9.8543     | 88.955        | 57.3797      | 34.3539      | 53.8783      | 54.3714         | 1     |
| 0.8101     | 0.9477          | 9.3241     | 88.73         | 56.4906      | 34.2668      | 53.2279      | 53.7836         | 2     |


### Framework versions

- Transformers 4.17.0.dev0
- TensorFlow 2.7.0
- Datasets 1.18.4.dev0
- Tokenizers 0.10.3

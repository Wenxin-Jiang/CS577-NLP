---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: MaryaAI/opus-mt-ar-en-finetunedQAdata-v1-ar-to-en
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# MaryaAI/opus-mt-ar-en-finetunedQAdata-v1-ar-to-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-ar-en](https://huggingface.co/Helsinki-NLP/opus-mt-ar-en) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0053
- Validation Loss: 8.2764
- Epoch: 14

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
| 0.0090     | 12.3530         | 0     |
| 0.0134     | 11.3018         | 1     |
| 0.0110     | 10.5958         | 2     |
| 0.0083     | 9.7381          | 3     |
| 0.0068     | 8.9434          | 4     |
| 0.0080     | 12.7723         | 5     |
| 0.0071     | 11.5191         | 6     |
| 0.0077     | 10.6246         | 7     |
| 0.0101     | 10.3368         | 8     |
| 0.0092     | 8.7824          | 9     |
| 0.0070     | 7.7344          | 10    |
| 0.0070     | 8.2180          | 11    |
| 0.0079     | 7.8572          | 12    |
| 0.0070     | 9.3053          | 13    |
| 0.0053     | 8.2764          | 14    |


### Framework versions

- Transformers 4.19.2
- TensorFlow 2.8.0
- Datasets 2.2.1
- Tokenizers 0.12.1

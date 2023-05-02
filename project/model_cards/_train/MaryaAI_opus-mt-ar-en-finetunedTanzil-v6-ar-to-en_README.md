---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: opus-mt-ar-en-finetunedTanzil-v6-ar-to-en
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# opus-mt-ar-en-finetunedTanzil-v6-ar-to-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-ar-en](https://huggingface.co/Helsinki-NLP/opus-mt-ar-en) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.6863
- Validation Loss: 0.8789
- Train Rouge1: 56.4999
- Train Rouge2: 33.3152
- Train Rougel: 52.7922
- Train Rougelsum: 53.4004
- Train Gen Len: 65.66
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

| Train Loss | Validation Loss | Train Rouge1 | Train Rouge2 | Train Rougel | Train Rougelsum | Train Gen Len | Epoch |
|:----------:|:---------------:|:------------:|:------------:|:------------:|:---------------:|:-------------:|:-----:|
| 1.2958     | 1.2191          | 55.4125      | 33.4250      | 52.1444      | 52.4427         | 109.29        | 0     |
| 1.1928     | 1.1607          | 57.1190      | 35.0261      | 53.9195      | 54.3028         | 103.37        | 1     |
| 1.1152     | 1.1133          | 56.7848      | 34.9767      | 53.6885      | 54.0708         | 81.705        | 2     |
| 1.0531     | 1.0795          | 56.5101      | 35.1214      | 53.2131      | 53.4955         | 104.285       | 3     |
| 0.9999     | 1.0493          | 57.7130      | 35.7997      | 54.7519      | 55.0195         | 98.01         | 4     |
| 0.9544     | 1.0233          | 57.4034      | 35.3118      | 54.2593      | 54.6092         | 56.94         | 5     |
| 0.9135     | 1.0009          | 56.7008      | 35.3027      | 53.6876      | 53.8885         | 94.855        | 6     |
| 0.8770     | 0.9793          | 56.6660      | 34.4890      | 53.1461      | 53.5412         | 93.33         | 7     |
| 0.8434     | 0.9624          | 55.3198      | 33.4441      | 52.3099      | 52.7027         | 94.63         | 8     |
| 0.8135     | 0.9468          | 55.2723      | 33.4791      | 51.9936      | 52.2751         | 69.765        | 9     |
| 0.7842     | 0.9335          | 55.9241      | 33.1444      | 52.5591      | 52.8279         | 63.895        | 10    |
| 0.7572     | 0.9170          | 57.7109      | 34.8199      | 54.0893      | 54.6004         | 75.57         | 11    |
| 0.7322     | 0.9009          | 55.7067      | 33.2829      | 52.2642      | 52.5643         | 96.515        | 12    |
| 0.7084     | 0.8912          | 55.2352      | 32.1104      | 51.6885      | 52.1647         | 91.595        | 13    |
| 0.6863     | 0.8789          | 56.4999      | 33.3152      | 52.7922      | 53.4004         | 65.66         | 14    |


### Framework versions

- Transformers 4.17.0.dev0
- TensorFlow 2.7.0
- Datasets 1.18.4.dev0
- Tokenizers 0.10.3

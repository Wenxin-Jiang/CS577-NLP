---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: MiguelCosta/distilbert-1-finetuned-cisco
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# MiguelCosta/distilbert-1-finetuned-cisco

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 2.2723
- Validation Loss: 2.4284
- Epoch: 39

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'class_name': 'WarmUp', 'config': {'initial_learning_rate': 2e-05, 'decay_schedule_fn': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': -964, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}, '__passive_serialization__': True}, 'warmup_steps': 1000, 'power': 1.0, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 4.4357     | 4.3213          | 0     |
| 4.1763     | 3.9111          | 1     |
| 3.8803     | 3.6751          | 2     |
| 3.7135     | 3.5458          | 3     |
| 3.5861     | 3.4489          | 4     |
| 3.5176     | 3.4323          | 5     |
| 3.4022     | 3.3658          | 6     |
| 3.3259     | 3.2113          | 7     |
| 3.2499     | 3.0623          | 8     |
| 3.2129     | 3.0298          | 9     |
| 3.1177     | 2.9181          | 10    |
| 3.0144     | 2.9550          | 11    |
| 2.9502     | 2.8758          | 12    |
| 2.9074     | 2.8674          | 13    |
| 2.8922     | 2.7877          | 14    |
| 2.8333     | 2.8283          | 15    |
| 2.7982     | 2.7717          | 16    |
| 2.7453     | 2.7578          | 17    |
| 2.6611     | 2.5425          | 18    |
| 2.6330     | 2.6145          | 19    |
| 2.5642     | 2.5415          | 20    |
| 2.5352     | 2.5437          | 21    |
| 2.4939     | 2.4214          | 22    |
| 2.4287     | 2.4882          | 23    |
| 2.4142     | 2.5091          | 24    |
| 2.3676     | 2.3997          | 25    |
| 2.3121     | 2.4515          | 26    |
| 2.3085     | 2.2349          | 27    |
| 2.2839     | 2.3205          | 28    |
| 2.3248     | 2.3273          | 29    |
| 2.2763     | 2.2583          | 30    |
| 2.2710     | 2.3896          | 31    |
| 2.2950     | 2.3224          | 32    |
| 2.3026     | 2.3910          | 33    |
| 2.3116     | 2.3255          | 34    |
| 2.2640     | 2.3186          | 35    |
| 2.2958     | 2.3332          | 36    |
| 2.3256     | 2.3646          | 37    |
| 2.2831     | 2.3751          | 38    |
| 2.2723     | 2.4284          | 39    |


### Framework versions

- Transformers 4.22.1
- TensorFlow 2.8.2
- Datasets 2.4.0
- Tokenizers 0.12.1

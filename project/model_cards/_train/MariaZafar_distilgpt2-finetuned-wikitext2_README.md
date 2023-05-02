---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: MariaZafar/distilgpt2-finetuned-wikitext2
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# MariaZafar/distilgpt2-finetuned-wikitext2

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0603
- Validation Loss: 5.5023
- Epoch: 49

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 0.001, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 3.4903     | 2.4602          | 0     |
| 2.5910     | 2.5912          | 1     |
| 2.1133     | 2.8207          | 2     |
| 1.5857     | 3.1597          | 3     |
| 1.0852     | 3.3317          | 4     |
| 0.6812     | 3.6312          | 5     |
| 0.4490     | 3.8533          | 6     |
| 0.3188     | 4.0209          | 7     |
| 0.2401     | 4.1932          | 8     |
| 0.1987     | 4.3469          | 9     |
| 0.1705     | 4.4238          | 10    |
| 0.1515     | 4.5274          | 11    |
| 0.1329     | 4.5066          | 12    |
| 0.1302     | 4.6625          | 13    |
| 0.1202     | 4.6441          | 14    |
| 0.1133     | 4.7448          | 15    |
| 0.1076     | 4.8144          | 16    |
| 0.1025     | 4.9662          | 17    |
| 0.0976     | 4.7328          | 18    |
| 0.0928     | 4.8394          | 19    |
| 0.0862     | 4.8873          | 20    |
| 0.0824     | 4.9153          | 21    |
| 0.0869     | 5.2097          | 22    |
| 0.0847     | 5.1124          | 23    |
| 0.0824     | 5.0528          | 24    |
| 0.0826     | 5.0547          | 25    |
| 0.0840     | 5.1079          | 26    |
| 0.0846     | 4.9867          | 27    |
| 0.0802     | 4.9700          | 28    |
| 0.0806     | 5.2266          | 29    |
| 0.0827     | 5.0909          | 30    |
| 0.0784     | 5.2329          | 31    |
| 0.0744     | 5.0834          | 32    |
| 0.0712     | 5.3750          | 33    |
| 0.0715     | 5.2754          | 34    |
| 0.0695     | 5.4315          | 35    |
| 0.0703     | 5.4119          | 36    |
| 0.0732     | 5.5824          | 37    |
| 0.0679     | 5.4020          | 38    |
| 0.0627     | 5.7249          | 39    |
| 0.0659     | 5.1686          | 40    |
| 0.0656     | 5.2962          | 41    |
| 0.0642     | 5.3573          | 42    |
| 0.0661     | 5.4822          | 43    |
| 0.0643     | 5.6516          | 44    |
| 0.0612     | 5.6201          | 45    |
| 0.0666     | 5.4791          | 46    |
| 0.0677     | 5.6865          | 47    |
| 0.0628     | 5.4184          | 48    |
| 0.0603     | 5.5023          | 49    |


### Framework versions

- Transformers 4.19.2
- TensorFlow 2.8.0
- Datasets 2.2.1
- Tokenizers 0.12.1

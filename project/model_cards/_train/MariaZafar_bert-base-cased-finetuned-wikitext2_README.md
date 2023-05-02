---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: MariaZafar/bert-base-cased-finetuned-wikitext2
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# MariaZafar/bert-base-cased-finetuned-wikitext2

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 3.9493
- Validation Loss: 4.7051
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
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 8.2068     | 7.6525          | 0     |
| 6.6638     | 6.6271          | 1     |
| 5.8170     | 6.1477          | 2     |
| 5.3501     | 5.3407          | 3     |
| 5.0362     | 5.4742          | 4     |
| 4.8317     | 5.1391          | 5     |
| 4.7290     | 5.4559          | 6     |
| 4.6790     | 5.0211          | 7     |
| 4.5944     | 5.2506          | 8     |
| 4.5684     | 4.8315          | 9     |
| 4.4865     | 5.1707          | 10    |
| 4.4708     | 4.8314          | 11    |
| 4.3995     | 5.3617          | 12    |
| 4.3861     | 5.2180          | 13    |
| 4.3372     | 4.7870          | 14    |
| 4.3451     | 5.3501          | 15    |
| 4.3038     | 4.8667          | 16    |
| 4.2838     | 5.2157          | 17    |
| 4.2933     | 5.2800          | 18    |
| 4.2698     | 5.2693          | 19    |
| 4.2178     | 5.1873          | 20    |
| 4.2222     | 5.0830          | 21    |
| 4.2031     | 4.5132          | 22    |
| 4.1933     | 5.3241          | 23    |
| 4.2139     | 4.7762          | 24    |
| 4.1444     | 4.7879          | 25    |
| 4.1353     | 5.0958          | 26    |
| 4.1227     | 5.2084          | 27    |
| 4.1253     | 4.8306          | 28    |
| 4.1134     | 5.2234          | 29    |
| 4.1084     | 4.9941          | 30    |
| 4.1097     | 4.9499          | 31    |
| 4.1208     | 4.9498          | 32    |
| 4.0924     | 5.0711          | 33    |
| 4.0825     | 4.9263          | 34    |
| 4.0774     | 4.8652          | 35    |
| 4.0702     | 4.8445          | 36    |
| 4.0816     | 4.2916          | 37    |
| 4.0420     | 4.7277          | 38    |
| 4.0456     | 4.9395          | 39    |
| 4.0873     | 4.9632          | 40    |
| 4.0295     | 4.6388          | 41    |
| 4.0228     | 4.8170          | 42    |
| 4.0393     | 4.4831          | 43    |
| 4.0249     | 4.8268          | 44    |
| 3.9565     | 4.7934          | 45    |
| 3.9567     | 4.5622          | 46    |
| 4.0054     | 4.8992          | 47    |
| 3.9582     | 4.8162          | 48    |
| 3.9493     | 4.7051          | 49    |


### Framework versions

- Transformers 4.19.2
- TensorFlow 2.8.0
- Datasets 2.2.1
- Tokenizers 0.12.1

---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: TestZee/t5-small-finetuned-kaggle-data-t5-v3.0
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# TestZee/t5-small-finetuned-kaggle-data-t5-v3.0

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.6248
- Validation Loss: 1.6558
- Train Rouge1: 26.3006
- Train Rouge2: 15.0931
- Train Rougel: 22.7561
- Train Rougelsum: 24.3816
- Train Gen Len: 19.0
- Epoch: 29

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 1e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.001}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Rouge1 | Train Rouge2 | Train Rougel | Train Rougelsum | Train Gen Len | Epoch |
|:----------:|:---------------:|:------------:|:------------:|:------------:|:---------------:|:-------------:|:-----:|
| 2.1318     | 1.8436          | 24.0637      | 12.9655      | 20.6308      | 22.1857         | 19.0          | 0     |
| 2.0035     | 1.7955          | 24.9502      | 13.7602      | 21.4422      | 23.0424         | 19.0          | 1     |
| 1.9561     | 1.7670          | 25.6590      | 14.5211      | 22.0967      | 23.5134         | 19.0          | 2     |
| 1.9227     | 1.7496          | 25.8863      | 14.7209      | 22.3661      | 23.8629         | 19.0          | 3     |
| 1.8951     | 1.7334          | 26.0026      | 14.7861      | 22.4126      | 23.8936         | 19.0          | 4     |
| 1.8716     | 1.7234          | 26.3796      | 14.9421      | 22.7097      | 24.2118         | 19.0          | 5     |
| 1.8558     | 1.7138          | 26.2830      | 14.9347      | 22.8008      | 24.1908         | 19.0          | 6     |
| 1.8362     | 1.7072          | 26.0811      | 14.6698      | 22.5673      | 23.9941         | 19.0          | 7     |
| 1.8222     | 1.7020          | 26.0600      | 14.8445      | 22.6614      | 23.9462         | 19.0          | 8     |
| 1.8086     | 1.6929          | 26.3903      | 15.0590      | 22.9725      | 24.3007         | 19.0          | 9     |
| 1.7958     | 1.6870          | 26.2563      | 14.8773      | 22.7601      | 24.1487         | 19.0          | 10    |
| 1.7802     | 1.6847          | 26.2638      | 15.0330      | 22.8279      | 24.2225         | 19.0          | 11    |
| 1.7709     | 1.6823          | 26.0351      | 14.9826      | 22.6653      | 24.0415         | 19.0          | 12    |
| 1.7610     | 1.6796          | 26.1864      | 15.0833      | 22.7959      | 24.1713         | 19.0          | 13    |
| 1.7486     | 1.6754          | 26.2693      | 15.2384      | 22.8580      | 24.2483         | 19.0          | 14    |
| 1.7354     | 1.6744          | 26.1257      | 14.9953      | 22.7029      | 24.0956         | 19.0          | 15    |
| 1.7262     | 1.6740          | 26.1954      | 15.0393      | 22.8311      | 24.1282         | 19.0          | 16    |
| 1.7206     | 1.6703          | 26.1409      | 14.9949      | 22.7586      | 24.1355         | 19.0          | 17    |
| 1.7083     | 1.6663          | 26.1880      | 15.1119      | 22.7500      | 24.1816         | 19.0          | 18    |
| 1.7002     | 1.6662          | 25.9666      | 14.9556      | 22.5439      | 23.9713         | 19.0          | 19    |
| 1.6926     | 1.6654          | 26.1649      | 15.1911      | 22.8287      | 24.2002         | 19.0          | 20    |
| 1.6839     | 1.6589          | 26.2105      | 15.0021      | 22.7778      | 24.2852         | 19.0          | 21    |
| 1.6768     | 1.6596          | 26.1263      | 14.8676      | 22.6634      | 24.1171         | 19.0          | 22    |
| 1.6670     | 1.6612          | 25.9718      | 14.8101      | 22.5048      | 23.9592         | 19.0          | 23    |
| 1.6604     | 1.6590          | 26.2419      | 15.0633      | 22.7685      | 24.3165         | 19.0          | 24    |
| 1.6498     | 1.6564          | 26.2757      | 15.0082      | 22.8157      | 24.3126         | 19.0          | 25    |
| 1.6455     | 1.6570          | 26.2307      | 14.9338      | 22.6259      | 24.2636         | 19.0          | 26    |
| 1.6368     | 1.6573          | 26.4114      | 15.3485      | 22.9117      | 24.4928         | 19.0          | 27    |
| 1.6325     | 1.6547          | 26.5272      | 15.4393      | 23.0764      | 24.6935         | 19.0          | 28    |
| 1.6248     | 1.6558          | 26.3006      | 15.0931      | 22.7561      | 24.3816         | 19.0          | 29    |


### Framework versions

- Transformers 4.20.1
- TensorFlow 2.8.2
- Datasets 2.3.2
- Tokenizers 0.12.1

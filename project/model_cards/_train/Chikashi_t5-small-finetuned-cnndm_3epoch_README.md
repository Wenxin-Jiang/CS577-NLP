---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cnn_dailymail
metrics:
- rouge
model-index:
- name: t5-small-finetuned-cnndm_3epoch
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: cnn_dailymail
      type: cnn_dailymail
      args: 3.0.0
    metrics:
    - name: Rouge1
      type: rouge
      value: 24.5435
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-cnndm_3epoch

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the cnn_dailymail dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6622
- Rouge1: 24.5435
- Rouge2: 11.7919
- Rougel: 20.2929
- Rougelsum: 23.1661
- Gen Len: 18.9996

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:------:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 1.9113        | 0.14  | 5000   | 1.7162          | 24.4374 | 11.6932 | 20.1741 | 23.0427   | 18.9997 |
| 1.8772        | 0.28  | 10000  | 1.7008          | 24.3715 | 11.6699 | 20.1387 | 22.9772   | 18.9997 |
| 1.8609        | 0.42  | 15000  | 1.6911          | 24.4174 | 11.6986 | 20.1756 | 23.0205   | 18.9997 |
| 1.8564        | 0.56  | 20000  | 1.6871          | 24.4374 | 11.6801 | 20.1663 | 23.0366   | 18.9995 |
| 1.8495        | 0.7   | 25000  | 1.6796          | 24.4019 | 11.6901 | 20.177  | 23.034    | 18.999  |
| 1.8448        | 0.84  | 30000  | 1.6787          | 24.4813 | 11.7227 | 20.1985 | 23.0847   | 18.999  |
| 1.8427        | 0.98  | 35000  | 1.6762          | 24.4905 | 11.7591 | 20.2548 | 23.1006   | 18.9993 |
| 1.8341        | 1.11  | 40000  | 1.6747          | 24.4743 | 11.7124 | 20.1782 | 23.0726   | 18.9996 |
| 1.822         | 1.25  | 45000  | 1.6753          | 24.4797 | 11.7292 | 20.2319 | 23.0816   | 18.9993 |
| 1.8262        | 1.39  | 50000  | 1.6713          | 24.4865 | 11.7079 | 20.2214 | 23.0919   | 18.9986 |
| 1.8281        | 1.53  | 55000  | 1.6702          | 24.5095 | 11.7364 | 20.2534 | 23.1264   | 18.9991 |
| 1.8228        | 1.67  | 60000  | 1.6678          | 24.5153 | 11.7595 | 20.2544 | 23.1138   | 18.9993 |
| 1.824         | 1.81  | 65000  | 1.6662          | 24.5324 | 11.7804 | 20.2671 | 23.1498   | 18.9997 |
| 1.8265        | 1.95  | 70000  | 1.6648          | 24.5795 | 11.7917 | 20.2935 | 23.1855   | 18.9992 |
| 1.8179        | 2.09  | 75000  | 1.6658          | 24.5426 | 11.804  | 20.2861 | 23.1586   | 18.9996 |
| 1.8147        | 2.23  | 80000  | 1.6646          | 24.5429 | 11.7914 | 20.2889 | 23.1542   | 18.9993 |
| 1.8026        | 2.37  | 85000  | 1.6632          | 24.5451 | 11.8045 | 20.2781 | 23.1555   | 18.9996 |
| 1.8141        | 2.51  | 90000  | 1.6643          | 24.5078 | 11.7781 | 20.2631 | 23.121    | 18.9996 |
| 1.8124        | 2.65  | 95000  | 1.6628          | 24.5728 | 11.7958 | 20.2875 | 23.178    | 18.9996 |
| 1.8098        | 2.79  | 100000 | 1.6635          | 24.5534 | 11.7998 | 20.2979 | 23.169    | 18.9996 |
| 1.8153        | 2.93  | 105000 | 1.6622          | 24.5435 | 11.7919 | 20.2929 | 23.1661   | 18.9996 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

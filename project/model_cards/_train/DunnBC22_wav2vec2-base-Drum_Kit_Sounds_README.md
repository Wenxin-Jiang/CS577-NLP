---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- audiofolder
metrics:
- accuracy
model-index:
- name: wav2vec2-base-Drum_Kit_Sounds
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-Drum_Kit_Sounds

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the audiofolder dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0887
- Accuracy: 0.7812
- Weighted f1: 0.7692
- Micro f1: 0.7812
- Macro f1: 0.7845
- Weighted recall: 0.7812
- Micro recall: 0.7812
- Macro recall: 0.8187
- Weighted precision: 0.8717
- Micro precision: 0.7812
- Macro precision: 0.8534

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 12

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Weighted f1 | Micro f1 | Macro f1 | Weighted recall | Micro recall | Macro recall | Weighted precision | Micro precision | Macro precision |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:-----------:|:--------:|:--------:|:---------------:|:------------:|:------------:|:------------------:|:---------------:|:---------------:|
| 1.3743        | 1.0   | 4    | 1.3632          | 0.5625   | 0.5801      | 0.5625   | 0.5678   | 0.5625          | 0.5625       | 0.5670       | 0.6786             | 0.5625          | 0.6429          |
| 1.3074        | 2.0   | 8    | 1.3149          | 0.3438   | 0.2567      | 0.3438   | 0.2696   | 0.3438          | 0.3438       | 0.375        | 0.3067             | 0.3438          | 0.3148          |
| 1.2393        | 3.0   | 12   | 1.3121          | 0.2188   | 0.0785      | 0.2188   | 0.0897   | 0.2188          | 0.2188       | 0.25         | 0.0479             | 0.2188          | 0.0547          |
| 1.2317        | 4.0   | 16   | 1.3112          | 0.2812   | 0.1800      | 0.2812   | 0.2057   | 0.2812          | 0.2812       | 0.3214       | 0.2698             | 0.2812          | 0.3083          |
| 1.2107        | 5.0   | 20   | 1.2604          | 0.4375   | 0.3030      | 0.4375   | 0.3462   | 0.4375          | 0.4375       | 0.5          | 0.2552             | 0.4375          | 0.2917          |
| 1.1663        | 6.0   | 24   | 1.2112          | 0.4688   | 0.3896      | 0.4688   | 0.4310   | 0.4688          | 0.4688       | 0.5268       | 0.5041             | 0.4688          | 0.5404          |
| 1.1247        | 7.0   | 28   | 1.1746          | 0.5938   | 0.5143      | 0.5938   | 0.5603   | 0.5938          | 0.5938       | 0.6562       | 0.5220             | 0.5938          | 0.5609          |
| 1.0856        | 8.0   | 32   | 1.1434          | 0.5938   | 0.5143      | 0.5938   | 0.5603   | 0.5938          | 0.5938       | 0.6562       | 0.5220             | 0.5938          | 0.5609          |
| 1.0601        | 9.0   | 36   | 1.1417          | 0.6562   | 0.6029      | 0.6562   | 0.6389   | 0.6562          | 0.6562       | 0.7125       | 0.8440             | 0.6562          | 0.8217          |
| 1.0375        | 10.0  | 40   | 1.1227          | 0.6875   | 0.6582      | 0.6875   | 0.6831   | 0.6875          | 0.6875       | 0.7330       | 0.8457             | 0.6875          | 0.8237          |
| 1.0168        | 11.0  | 44   | 1.1065          | 0.7812   | 0.7692      | 0.7812   | 0.7845   | 0.7812          | 0.7812       | 0.8187       | 0.8717             | 0.7812          | 0.8534          |
| 1.0093        | 12.0  | 48   | 1.0887          | 0.7812   | 0.7692      | 0.7812   | 0.7845   | 0.7812          | 0.7812       | 0.8187       | 0.8717             | 0.7812          | 0.8534          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1
- Datasets 2.8.0
- Tokenizers 0.12.1

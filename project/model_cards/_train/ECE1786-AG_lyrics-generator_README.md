---
license: mit
tags:
- generated_from_trainer
model-index:
- name: lyrics-generator-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# lyrics-generator-v2

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1114

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.4325        | 0.36  | 200  | 2.3267          |
| 2.4121        | 0.71  | 400  | 2.2693          |
| 2.3582        | 1.07  | 600  | 2.2401          |
| 2.2903        | 1.42  | 800  | 2.2182          |
| 2.2738        | 1.78  | 1000 | 2.2046          |
| 2.2322        | 2.14  | 1200 | 2.1922          |
| 2.1933        | 2.49  | 1400 | 2.1832          |
| 2.1944        | 2.85  | 1600 | 2.1736          |
| 2.1632        | 3.2   | 1800 | 2.1648          |
| 2.1366        | 3.56  | 2000 | 2.1554          |
| 2.1492        | 3.91  | 2200 | 2.1491          |
| 2.1108        | 4.27  | 2400 | 2.1472          |
| 2.0882        | 4.63  | 2600 | 2.1422          |
| 2.0971        | 4.98  | 2800 | 2.1343          |
| 2.0829        | 5.34  | 3000 | 2.1318          |
| 2.042         | 5.69  | 3200 | 2.1280          |
| 2.0375        | 6.05  | 3400 | 2.1261          |
| 2.0146        | 6.41  | 3600 | 2.1245          |
| 2.0551        | 6.76  | 3800 | 2.1217          |
| 1.992         | 7.12  | 4000 | 2.1182          |
| 1.9994        | 7.47  | 4200 | 2.1170          |
| 2.0189        | 7.83  | 4400 | 2.1156          |
| 1.9795        | 8.19  | 4600 | 2.1133          |
| 2.0101        | 8.54  | 4800 | 2.1143          |
| 1.9864        | 8.9   | 5000 | 2.1111          |
| 1.9602        | 9.25  | 5200 | 2.1120          |
| 1.9899        | 9.61  | 5400 | 2.1117          |
| 1.9928        | 9.96  | 5600 | 2.1114          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2

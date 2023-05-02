---
tags:
- generated_from_trainer
model-index:
- name: clip-archdaily-5k
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clip-archdaily-5k

This model is a fine-tuned version of [](https://huggingface.co/) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5681

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
- train_batch_size: 56
- eval_batch_size: 56
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.533         | 0.34  | 200  | 2.4607          |
| 2.1012        | 0.68  | 400  | 1.9922          |
| 1.6059        | 1.02  | 600  | 1.7986          |
| 1.4557        | 1.36  | 800  | 1.6130          |
| 1.4268        | 1.7   | 1000 | 1.4073          |
| 0.8588        | 2.04  | 1200 | 1.2657          |
| 0.8191        | 2.38  | 1400 | 1.1214          |
| 0.81          | 2.72  | 1600 | 1.0418          |
| 0.5546        | 3.06  | 1800 | 0.9735          |
| 0.4905        | 3.4   | 2000 | 0.9006          |
| 0.5209        | 3.74  | 2200 | 0.8762          |
| 0.3127        | 4.08  | 2400 | 0.8457          |
| 0.3145        | 4.42  | 2600 | 0.7886          |
| 0.3265        | 4.76  | 2800 | 0.7853          |
| 0.2215        | 5.1   | 3000 | 0.7309          |
| 0.2351        | 5.44  | 3200 | 0.7082          |
| 0.2332        | 5.78  | 3400 | 0.6770          |
| 0.1793        | 6.12  | 3600 | 0.6856          |
| 0.1617        | 6.46  | 3800 | 0.6470          |
| 0.1468        | 6.8   | 4000 | 0.6700          |
| 0.1293        | 7.14  | 4200 | 0.6460          |
| 0.1257        | 7.48  | 4400 | 0.6415          |
| 0.0975        | 7.82  | 4600 | 0.6454          |
| 0.0835        | 8.16  | 4800 | 0.6111          |
| 0.0856        | 8.5   | 5000 | 0.6124          |
| 0.0887        | 8.84  | 5200 | 0.5956          |
| 0.069         | 9.18  | 5400 | 0.5877          |
| 0.0625        | 9.52  | 5600 | 0.5798          |
| 0.0599        | 9.86  | 5800 | 0.5681          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

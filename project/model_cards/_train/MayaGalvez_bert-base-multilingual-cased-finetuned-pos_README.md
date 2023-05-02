---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-base-multilingual-cased-finetuned-pos
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-multilingual-cased-finetuned-pos

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1736
- Precision: 0.9499
- Recall: 0.9504
- F1: 0.9501
- Accuracy: 0.9551

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.7663        | 0.27  | 200  | 0.2047          | 0.9318    | 0.9312 | 0.9315 | 0.9388   |
| 0.5539        | 0.53  | 400  | 0.1815          | 0.9381    | 0.9404 | 0.9392 | 0.9460   |
| 0.5222        | 0.8   | 600  | 0.1787          | 0.9400    | 0.9424 | 0.9412 | 0.9468   |
| 0.5084        | 1.07  | 800  | 0.1591          | 0.9470    | 0.9463 | 0.9467 | 0.9519   |
| 0.4703        | 1.33  | 1000 | 0.1622          | 0.9456    | 0.9458 | 0.9457 | 0.9510   |
| 0.5005        | 1.6   | 1200 | 0.1666          | 0.9470    | 0.9464 | 0.9467 | 0.9519   |
| 0.4677        | 1.87  | 1400 | 0.1583          | 0.9483    | 0.9483 | 0.9483 | 0.9532   |
| 0.4704        | 2.13  | 1600 | 0.1635          | 0.9472    | 0.9475 | 0.9473 | 0.9528   |
| 0.4639        | 2.4   | 1800 | 0.1569          | 0.9475    | 0.9488 | 0.9482 | 0.9536   |
| 0.4627        | 2.67  | 2000 | 0.1605          | 0.9474    | 0.9478 | 0.9476 | 0.9527   |
| 0.4608        | 2.93  | 2200 | 0.1535          | 0.9485    | 0.9495 | 0.9490 | 0.9538   |
| 0.4306        | 3.2   | 2400 | 0.1646          | 0.9489    | 0.9487 | 0.9488 | 0.9536   |
| 0.4583        | 3.47  | 2600 | 0.1642          | 0.9488    | 0.9495 | 0.9491 | 0.9539   |
| 0.453         | 3.73  | 2800 | 0.1646          | 0.9498    | 0.9505 | 0.9501 | 0.9554   |
| 0.4347        | 4.0   | 3000 | 0.1629          | 0.9494    | 0.9504 | 0.9499 | 0.9552   |
| 0.4425        | 4.27  | 3200 | 0.1738          | 0.9495    | 0.9502 | 0.9498 | 0.9550   |
| 0.4335        | 4.53  | 3400 | 0.1733          | 0.9499    | 0.9506 | 0.9503 | 0.9550   |
| 0.4306        | 4.8   | 3600 | 0.1736          | 0.9499    | 0.9504 | 0.9501 | 0.9551   |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu102
- Datasets 2.4.0
- Tokenizers 0.12.1

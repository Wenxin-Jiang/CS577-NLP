---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-squad

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 5.0244

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 60

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 30   | 3.5643          |
| No log        | 2.0   | 60   | 2.4546          |
| No log        | 3.0   | 90   | 2.3018          |
| No log        | 4.0   | 120  | 2.4636          |
| No log        | 5.0   | 150  | 2.4736          |
| No log        | 6.0   | 180  | 2.5580          |
| No log        | 7.0   | 210  | 2.6686          |
| No log        | 8.0   | 240  | 2.7249          |
| No log        | 9.0   | 270  | 3.2596          |
| No log        | 10.0  | 300  | 3.5904          |
| No log        | 11.0  | 330  | 3.6709          |
| No log        | 12.0  | 360  | 3.6431          |
| No log        | 13.0  | 390  | 3.6343          |
| No log        | 14.0  | 420  | 3.8316          |
| No log        | 15.0  | 450  | 3.6363          |
| No log        | 16.0  | 480  | 3.8468          |
| 0.8931        | 17.0  | 510  | 3.7114          |
| 0.8931        | 18.0  | 540  | 3.8719          |
| 0.8931        | 19.0  | 570  | 4.0872          |
| 0.8931        | 20.0  | 600  | 4.2989          |
| 0.8931        | 21.0  | 630  | 4.5494          |
| 0.8931        | 22.0  | 660  | 4.2565          |
| 0.8931        | 23.0  | 690  | 4.3009          |
| 0.8931        | 24.0  | 720  | 4.1816          |
| 0.8931        | 25.0  | 750  | 4.2583          |
| 0.8931        | 26.0  | 780  | 4.2276          |
| 0.8931        | 27.0  | 810  | 4.3481          |
| 0.8931        | 28.0  | 840  | 4.4369          |
| 0.8931        | 29.0  | 870  | 4.4891          |
| 0.8931        | 30.0  | 900  | 4.5521          |
| 0.8931        | 31.0  | 930  | 4.5201          |
| 0.8931        | 32.0  | 960  | 4.6323          |
| 0.8931        | 33.0  | 990  | 4.4766          |
| 0.0297        | 34.0  | 1020 | 4.7612          |
| 0.0297        | 35.0  | 1050 | 4.9057          |
| 0.0297        | 36.0  | 1080 | 4.7580          |
| 0.0297        | 37.0  | 1110 | 4.6351          |
| 0.0297        | 38.0  | 1140 | 4.6495          |
| 0.0297        | 39.0  | 1170 | 4.5980          |
| 0.0297        | 40.0  | 1200 | 4.6370          |
| 0.0297        | 41.0  | 1230 | 4.6523          |
| 0.0297        | 42.0  | 1260 | 4.5802          |
| 0.0297        | 43.0  | 1290 | 4.6304          |
| 0.0297        | 44.0  | 1320 | 4.7111          |
| 0.0297        | 45.0  | 1350 | 4.7219          |
| 0.0297        | 46.0  | 1380 | 4.7323          |
| 0.0297        | 47.0  | 1410 | 4.9115          |
| 0.0297        | 48.0  | 1440 | 4.7873          |
| 0.0297        | 49.0  | 1470 | 4.9340          |
| 0.0023        | 50.0  | 1500 | 5.0638          |
| 0.0023        | 51.0  | 1530 | 5.0750          |
| 0.0023        | 52.0  | 1560 | 4.9338          |
| 0.0023        | 53.0  | 1590 | 4.9197          |
| 0.0023        | 54.0  | 1620 | 4.9282          |
| 0.0023        | 55.0  | 1650 | 5.0038          |
| 0.0023        | 56.0  | 1680 | 4.9848          |
| 0.0023        | 57.0  | 1710 | 4.9932          |
| 0.0023        | 58.0  | 1740 | 5.0134          |
| 0.0023        | 59.0  | 1770 | 5.0303          |
| 0.0023        | 60.0  | 1800 | 5.0244          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Tokenizers 0.12.1

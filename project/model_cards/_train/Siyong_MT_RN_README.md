---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: run1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# run1

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6666
- Wer: 0.6375
- Cer: 0.3170

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|
| 1.0564        | 2.36  | 2000  | 2.3456          | 0.9628 | 0.5549 |
| 0.5071        | 4.73  | 4000  | 2.0652          | 0.9071 | 0.5115 |
| 0.3952        | 7.09  | 6000  | 2.3649          | 0.9108 | 0.4628 |
| 0.3367        | 9.46  | 8000  | 1.7615          | 0.8253 | 0.4348 |
| 0.2765        | 11.82 | 10000 | 1.6151          | 0.7937 | 0.4087 |
| 0.2493        | 14.18 | 12000 | 1.4976          | 0.7881 | 0.3905 |
| 0.2318        | 16.55 | 14000 | 1.6731          | 0.8160 | 0.3925 |
| 0.2074        | 18.91 | 16000 | 1.5822          | 0.7658 | 0.3913 |
| 0.1825        | 21.28 | 18000 | 1.5442          | 0.7361 | 0.3704 |
| 0.1824        | 23.64 | 20000 | 1.5988          | 0.7621 | 0.3711 |
| 0.1699        | 26.0  | 22000 | 1.4261          | 0.7119 | 0.3490 |
| 0.158         | 28.37 | 24000 | 1.7482          | 0.7658 | 0.3648 |
| 0.1385        | 30.73 | 26000 | 1.4103          | 0.6784 | 0.3348 |
| 0.1199        | 33.1  | 28000 | 1.5214          | 0.6636 | 0.3273 |
| 0.116         | 35.46 | 30000 | 1.4288          | 0.7212 | 0.3486 |
| 0.1071        | 37.83 | 32000 | 1.5344          | 0.7138 | 0.3411 |
| 0.1007        | 40.19 | 34000 | 1.4501          | 0.6691 | 0.3237 |
| 0.0943        | 42.55 | 36000 | 1.5367          | 0.6859 | 0.3265 |
| 0.0844        | 44.92 | 38000 | 1.5321          | 0.6599 | 0.3273 |
| 0.0762        | 47.28 | 40000 | 1.6721          | 0.6264 | 0.3142 |
| 0.0778        | 49.65 | 42000 | 1.6666          | 0.6375 | 0.3170 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.12.0+cu113
- Datasets 2.0.0
- Tokenizers 0.12.1

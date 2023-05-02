---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-base-timit-demo-google-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-timit-demo-google-colab

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5430
- Wer: 0.3434

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
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 3.5342        | 1.0   | 500   | 1.7432          | 1.0005 |
| 0.852         | 2.01  | 1000  | 0.6003          | 0.5692 |
| 0.4306        | 3.01  | 1500  | 0.4681          | 0.4750 |
| 0.2972        | 4.02  | 2000  | 0.4397          | 0.4192 |
| 0.2262        | 5.02  | 2500  | 0.4120          | 0.3985 |
| 0.1902        | 6.02  | 3000  | 0.4680          | 0.3988 |
| 0.1664        | 7.03  | 3500  | 0.4740          | 0.4022 |
| 0.1398        | 8.03  | 4000  | 0.4200          | 0.3788 |
| 0.1237        | 9.04  | 4500  | 0.4645          | 0.3827 |
| 0.1087        | 10.04 | 5000  | 0.4520          | 0.3805 |
| 0.0961        | 11.04 | 5500  | 0.4862          | 0.3712 |
| 0.0844        | 12.05 | 6000  | 0.4768          | 0.3695 |
| 0.0808        | 13.05 | 6500  | 0.5238          | 0.3720 |
| 0.0708        | 14.06 | 7000  | 0.5249          | 0.3736 |
| 0.0649        | 15.06 | 7500  | 0.5245          | 0.3745 |
| 0.0639        | 16.06 | 8000  | 0.5152          | 0.3648 |
| 0.0553        | 17.07 | 8500  | 0.5048          | 0.3682 |
| 0.0556        | 18.07 | 9000  | 0.5316          | 0.3634 |
| 0.0469        | 19.08 | 9500  | 0.5179          | 0.3668 |
| 0.0432        | 20.08 | 10000 | 0.5441          | 0.3679 |
| 0.0402        | 21.08 | 10500 | 0.5362          | 0.3498 |
| 0.0344        | 22.09 | 11000 | 0.5497          | 0.3537 |
| 0.0321        | 23.09 | 11500 | 0.5426          | 0.3499 |
| 0.0311        | 24.1  | 12000 | 0.5637          | 0.3508 |
| 0.0279        | 25.1  | 12500 | 0.5346          | 0.3491 |
| 0.025         | 26.1  | 13000 | 0.5310          | 0.3426 |
| 0.0237        | 27.11 | 13500 | 0.5419          | 0.3444 |
| 0.0221        | 28.11 | 14000 | 0.5457          | 0.3437 |
| 0.0214        | 29.12 | 14500 | 0.5430          | 0.3434 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1

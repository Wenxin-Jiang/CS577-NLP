---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- matthews_correlation
model-index:
- name: distilbert-base-uncased-finetuned-cola
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-cola

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6550
- Matthews Correlation: 0.2820

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| 1.7255        | 1.0   | 712  | 1.6687          | 0.1995               |
| 1.3584        | 2.0   | 1424 | 1.6550          | 0.2820               |
| 1.024         | 3.0   | 2136 | 1.7990          | 0.2564               |
| 0.8801        | 4.0   | 2848 | 2.1304          | 0.2657               |
| 0.7138        | 5.0   | 3560 | 2.1946          | 0.2584               |
| 0.5799        | 6.0   | 4272 | 2.4351          | 0.2660               |
| 0.5385        | 7.0   | 4984 | 2.6819          | 0.2539               |
| 0.4088        | 8.0   | 5696 | 2.8667          | 0.2436               |
| 0.3722        | 9.0   | 6408 | 2.9077          | 0.2612               |
| 0.3173        | 10.0  | 7120 | 2.9795          | 0.2542               |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

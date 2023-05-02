---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: wav2vec2-xls-r-300m-th-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-th-v2

This model is a fine-tuned version of [Botnoi/wav2vec2-xls-r-300m-th-v1](https://huggingface.co/Botnoi/wav2vec2-xls-r-300m-th-v1) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3630
- Wer: 0.3962
- Cer: 0.0942
- Clean Cer: 0.0767

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.533e-08
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 9000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    | Cer    | Clean Cer |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:---------:|
| 0.3323        | 0.68  | 1000 | 0.3635          | 0.3961 | 0.0942 | 0.0767    |
| 0.3386        | 1.36  | 2000 | 0.3632          | 0.3962 | 0.0943 | 0.0768    |
| 0.3453        | 2.03  | 3000 | 0.3632          | 0.3964 | 0.0943 | 0.0768    |
| 0.3392        | 2.71  | 4000 | 0.3632          | 0.3961 | 0.0943 | 0.0767    |
| 0.3399        | 3.39  | 5000 | 0.3634          | 0.3961 | 0.0942 | 0.0768    |
| 0.347         | 4.07  | 6000 | 0.3632          | 0.3961 | 0.0942 | 0.0767    |
| 0.3414        | 4.74  | 7000 | 0.3631          | 0.3962 | 0.0942 | 0.0767    |
| 0.3378        | 5.42  | 8000 | 0.3631          | 0.3961 | 0.0942 | 0.0767    |
| 0.3421        | 6.1   | 9000 | 0.3630          | 0.3962 | 0.0942 | 0.0767    |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

---
license: apache-2.0
tags:
- automatic-speech-recognition
- google/xtreme_s
- generated_from_trainer
datasets:
- xtreme_s
metrics:
- accuracy
model-index:
- name: xtreme_s_xlsr_minds14_fr
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xtreme_s_xlsr_minds14_fr

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the GOOGLE/XTREME_S - MINDS14.FR-FR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3922
- Accuracy: 0.9135

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 2
- total_train_batch_size: 64
- total_eval_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 50.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.9751        | 10.0  | 50   | 2.0203          | 0.3462   |
| 0.4275        | 20.0  | 100  | 0.7434          | 0.7981   |
| 0.2484        | 30.0  | 150  | 0.7686          | 0.8462   |
| 0.0263        | 40.0  | 200  | 0.3922          | 0.9135   |
| 0.0118        | 50.0  | 250  | 0.4859          | 0.9038   |


### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.10.2+cu113
- Datasets 1.18.4.dev0
- Tokenizers 0.11.6

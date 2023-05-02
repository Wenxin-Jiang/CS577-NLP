---
license: apache-2.0
tags:
- audio-classification
- generated_from_trainer
datasets:
- superb
metrics:
- accuracy
model-index:
- name: wav2vec2-base-ks-padpt1600
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-ks-padpt1600

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the superb dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6019
- Accuracy: 0.6111

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.003
- train_batch_size: 256
- eval_batch_size: 256
- seed: 0
- gradient_accumulation_steps: 4
- total_train_batch_size: 1024
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.3499        | 1.0   | 50   | 1.6019          | 0.6111   |
| 0.9698        | 2.0   | 100  | 1.4349          | 0.5613   |
| 0.866         | 3.0   | 150  | 1.4232          | 0.5547   |
| 0.8162        | 4.0   | 200  | 1.5573          | 0.4675   |
| 0.7632        | 5.0   | 250  | 1.4991          | 0.4950   |
| 0.7461        | 6.0   | 300  | 1.4251          | 0.5321   |
| 0.7374        | 7.0   | 350  | 1.6291          | 0.4247   |
| 0.7237        | 8.0   | 400  | 1.5307          | 0.4797   |
| 0.7273        | 9.0   | 450  | 1.5635          | 0.4520   |
| 0.7007        | 10.0  | 500  | 1.5841          | 0.4497   |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.11.0+cu115
- Datasets 2.4.0
- Tokenizers 0.12.1

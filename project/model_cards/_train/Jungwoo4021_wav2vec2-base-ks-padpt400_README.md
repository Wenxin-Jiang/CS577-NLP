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
- name: wav2vec2-base-ks-padpt400
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-ks-padpt400

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the superb dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2218
- Accuracy: 0.6343

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
| 1.2948        | 1.0   | 50   | 1.6527          | 0.6108   |
| 0.8861        | 2.0   | 100  | 1.2653          | 0.6130   |
| 0.7809        | 3.0   | 150  | 1.2615          | 0.5924   |
| 0.7364        | 4.0   | 200  | 1.2218          | 0.6343   |
| 0.6944        | 5.0   | 250  | 1.2137          | 0.6324   |
| 0.6817        | 6.0   | 300  | 1.2822          | 0.5930   |
| 0.6601        | 7.0   | 350  | 1.3292          | 0.5599   |
| 0.6464        | 8.0   | 400  | 1.2744          | 0.5869   |
| 0.653         | 9.0   | 450  | 1.3916          | 0.5272   |
| 0.633         | 10.0  | 500  | 1.3344          | 0.5606   |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.11.0+cu115
- Datasets 2.4.0
- Tokenizers 0.12.1

---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xlsr-finetune-es-col
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-finetune-es-col

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.6514
- Wer: 0.9874

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 4.9709        | 3.25  | 400  | 2.9673          | 1.0    |
| 2.9488        | 6.5   | 800  | 2.9075          | 0.9973 |
| 2.907         | 9.76  | 1200 | 2.8772          | 0.9688 |
| 2.886         | 13.01 | 1600 | 2.8245          | 0.9484 |
| 2.8043        | 16.26 | 2000 | 2.7134          | 0.9874 |
| 2.7288        | 19.51 | 2400 | 2.6750          | 0.9874 |
| 2.7072        | 22.76 | 2800 | 2.6651          | 0.9874 |
| 2.6892        | 26.02 | 3200 | 2.6573          | 0.9874 |
| 2.683         | 29.27 | 3600 | 2.6514          | 0.9874 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.1+cu102
- Datasets 1.13.3
- Tokenizers 0.10.3
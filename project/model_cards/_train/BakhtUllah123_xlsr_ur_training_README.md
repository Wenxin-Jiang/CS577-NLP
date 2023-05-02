---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_8_0
model-index:
- name: xlsr_ur_training
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlsr_ur_training

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the common_voice_8_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8325
- Wer: 0.4863

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

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 6.9537        | 3.25  | 1000 | 3.0940          | 0.9989 |
| 2.1696        | 6.49  | 2000 | 0.9705          | 0.6830 |
| 0.8637        | 9.74  | 3000 | 0.8098          | 0.5919 |
| 0.6297        | 12.99 | 4000 | 0.8002          | 0.5469 |
| 0.5034        | 16.23 | 5000 | 0.8019          | 0.5214 |
| 0.4267        | 19.48 | 6000 | 0.8223          | 0.5085 |
| 0.3847        | 22.73 | 7000 | 0.8081          | 0.4948 |
| 0.342         | 25.97 | 8000 | 0.8300          | 0.4930 |
| 0.3201        | 29.22 | 9000 | 0.8325          | 0.4863 |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

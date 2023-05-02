---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- asvspoof2019
metrics:
- accuracy
model-index:
- name: wav2vec2-base-960h-finetuned-deepfake
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-960h-finetuned-deepfake

This model is a fine-tuned version of [facebook/wav2vec2-base-960h](https://huggingface.co/facebook/wav2vec2-base-960h) on the asvspoof2019 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0009
- Accuracy: 0.9998

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.0027        | 1.0   | 793  | 0.0070          | 0.9990   |
| 0.0006        | 2.0   | 1586 | 0.0032          | 0.9995   |
| 0.0271        | 3.0   | 2379 | 0.0022          | 0.9995   |
| 0.0002        | 4.0   | 3172 | 0.0009          | 0.9998   |
| 0.0002        | 5.0   | 3965 | 0.0020          | 0.9998   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

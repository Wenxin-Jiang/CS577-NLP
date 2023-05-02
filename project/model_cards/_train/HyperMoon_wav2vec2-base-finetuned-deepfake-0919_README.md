---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- asvspoof2019
metrics:
- accuracy
model-index:
- name: wav2vec2-base-finetuned-deepfake-0919
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-finetuned-deepfake-0919

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the asvspoof2019 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3335
- Accuracy: 0.8974

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.3025        | 1.0   | 1586 | 0.3335          | 0.8974   |
| 0.4214        | 2.0   | 3172 | 0.3331          | 0.8974   |
| 0.4378        | 3.0   | 4758 | 0.3307          | 0.8974   |
| 0.3993        | 4.0   | 6344 | 0.3331          | 0.8974   |
| 0.2839        | 5.0   | 7930 | 0.3315          | 0.8974   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

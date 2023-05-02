---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- superb
metrics:
- accuracy
model-index:
- name: wav2vec2-base-finetuned-ks
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-finetuned-ks

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the superb dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0993
- Accuracy: 0.9812

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7367        | 1.0   | 399  | 0.6341          | 0.8819   |
| 0.3087        | 2.0   | 798  | 0.1900          | 0.9771   |
| 0.1979        | 3.0   | 1197 | 0.1232          | 0.9800   |
| 0.171         | 4.0   | 1596 | 0.1057          | 0.9794   |
| 0.1253        | 5.0   | 1995 | 0.0993          | 0.9812   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0
- Datasets 2.4.0
- Tokenizers 0.12.1

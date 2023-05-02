---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: longformer_openbook
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# longformer_openbook

This model is a fine-tuned version of [allenai/longformer-base-4096](https://huggingface.co/allenai/longformer-base-4096) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7773
- Accuracy: 0.71

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 25
- total_train_batch_size: 100
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 0.99  | 49   | 0.8618          | 0.662    |
| No log        | 1.99  | 98   | 0.7773          | 0.71     |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1
- Datasets 2.5.1
- Tokenizers 0.11.0

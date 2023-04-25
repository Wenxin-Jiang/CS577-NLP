---
license: mit
tags:
- generated_from_trainer
datasets:
- clinc_oos
metrics:
- accuracy
model-index:
- name: roberta-large-finetuned-clinc
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: clinc_oos
      type: clinc_oos
      args: plus
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9703225806451613
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-finetuned-clinc

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on the clinc_oos dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2109
- Accuracy: 0.9703

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 5.0643        | 1.0   | 120  | 5.0440          | 0.0065   |
| 4.2726        | 2.0   | 240  | 2.7488          | 0.7255   |
| 1.9687        | 3.0   | 360  | 0.8694          | 0.9174   |
| 0.5773        | 4.0   | 480  | 0.3267          | 0.9539   |
| 0.1842        | 5.0   | 600  | 0.2109          | 0.9703   |


### Framework versions

- Transformers 4.19.0.dev0
- Pytorch 1.10.2+cu113
- Datasets 1.18.4
- Tokenizers 0.11.6

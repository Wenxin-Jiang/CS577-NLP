---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: Lilt_xlmRoberta-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Lilt_xlmRoberta-finetuned

This model is a fine-tuned version of [RobertoFont/lilt-xlm-roberta-base](https://huggingface.co/RobertoFont/lilt-xlm-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8585
- Accuracy: 0.756

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 32
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 78   | 1.6469          | 0.524    |
| No log        | 2.0   | 156  | 1.2372          | 0.644    |
| No log        | 3.0   | 234  | 1.0487          | 0.686    |
| No log        | 4.0   | 312  | 0.9515          | 0.723    |
| No log        | 5.0   | 390  | 0.9319          | 0.735    |
| No log        | 6.0   | 468  | 0.8965          | 0.742    |
| No log        | 7.0   | 546  | 0.8809          | 0.754    |
| No log        | 8.0   | 624  | 0.8597          | 0.756    |
| No log        | 9.0   | 702  | 0.8673          | 0.758    |
| No log        | 10.0  | 780  | 0.8585          | 0.756    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

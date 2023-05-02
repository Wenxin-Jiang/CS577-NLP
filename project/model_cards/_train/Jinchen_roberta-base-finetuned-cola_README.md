---
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
model-index:
- name: roberta-base-finetuned-cola
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-finetuned-cola

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4211
- Matthews Correlation: 0.6279

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: IPU
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- total_eval_batch_size: 20
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- training precision: Mixed Precision

### Training results

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| 0.4218        | 1.0   | 133  | 0.4236          | 0.5243               |
| 0.2077        | 2.0   | 266  | 0.3970          | 0.5930               |
| 0.184         | 3.0   | 399  | 0.4211          | 0.6279               |
| 0.1807        | 4.0   | 532  | 0.4854          | 0.6197               |
| 0.1405        | 5.0   | 665  | 0.5693          | 0.5968               |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.0+cpu
- Datasets 2.3.2
- Tokenizers 0.12.1

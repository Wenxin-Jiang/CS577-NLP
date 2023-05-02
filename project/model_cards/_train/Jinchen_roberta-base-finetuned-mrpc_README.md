---
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
- f1
model-index:
- name: roberta-base-finetuned-mrpc
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-finetuned-mrpc

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2891
- Accuracy: 0.8925
- F1: 0.9228

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.5998        | 1.0   | 57   | 0.5425          | 0.74     | 0.8349 |
| 0.5058        | 2.0   | 114  | 0.3020          | 0.875    | 0.9084 |
| 0.3316        | 3.0   | 171  | 0.2891          | 0.8925   | 0.9228 |
| 0.1617        | 4.0   | 228  | 0.2937          | 0.8825   | 0.9138 |
| 0.3161        | 5.0   | 285  | 0.3193          | 0.8875   | 0.9171 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.0+cpu
- Datasets 2.3.2
- Tokenizers 0.12.1

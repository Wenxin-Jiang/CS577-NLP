---
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: mpnet-base-finetuned-AdamW-mnli
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      config: mnli
      split: validation_matched
      args: mnli
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8290371879775853
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mpnet-base-finetuned-AdamW-mnli

This model is a fine-tuned version of [microsoft/mpnet-base](https://huggingface.co/microsoft/mpnet-base) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5741
- Accuracy: 0.8290

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6.7e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 196351
- num_epochs: 0.2

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.6323        | 0.2   | 19636 | 0.5741          | 0.8290   |


### Framework versions

- Transformers 4.26.1
- Pytorch 1.13.1+cu117
- Datasets 2.10.0
- Tokenizers 0.13.2

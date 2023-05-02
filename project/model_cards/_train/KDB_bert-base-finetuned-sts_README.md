---
tags:
- generated_from_trainer
datasets:
- klue
metrics:
- pearsonr
model-index:
- name: bert-base-finetuned-sts
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: klue
      type: klue
      args: sts
    metrics:
    - name: Pearsonr
      type: pearsonr
      value: 0.8970473420720607
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-finetuned-sts

This model is a fine-tuned version of [klue/bert-base](https://huggingface.co/klue/bert-base) on the klue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4770
- Pearsonr: 0.8970

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Pearsonr |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 92   | 0.6330          | 0.8717   |
| No log        | 2.0   | 184  | 0.6206          | 0.8818   |
| No log        | 3.0   | 276  | 0.5010          | 0.8947   |
| No log        | 4.0   | 368  | 0.4717          | 0.8956   |
| No log        | 5.0   | 460  | 0.4770          | 0.8970   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

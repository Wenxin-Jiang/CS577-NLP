---
tags:
- generated_from_trainer
datasets:
- klue
metrics:
- accuracy
model_index:
- name: bert-base-finetuned-nli
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: klue
      type: klue
      args: nli
    metric:
      name: Accuracy
      type: accuracy
      value: 0.756
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-finetuned-nli

This model is a fine-tuned version of [klue/bert-base](https://huggingface.co/klue/bert-base) on the klue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1357
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
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 196  | 0.7357          | 0.156    |
| No log        | 2.0   | 392  | 0.5952          | 0.0993   |
| 0.543         | 3.0   | 588  | 0.5630          | 0.099    |
| 0.543         | 4.0   | 784  | 0.5670          | 0.079    |
| 0.543         | 5.0   | 980  | 0.5795          | 0.078    |


### Framework versions

- Transformers 4.9.2
- Pytorch 1.9.0+cu102
- Datasets 1.11.0
- Tokenizers 0.10.3

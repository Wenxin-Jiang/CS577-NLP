---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: rubert-base-cased-sentence-finetuned-headlines_X
  results:
  - task:
      name: Text Classification
      type: text-classification
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.952
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# rubert-base-cased-sentence-finetuned-headlines_X

This model is a fine-tuned version of [DeepPavlov/rubert-base-cased-sentence](https://huggingface.co/DeepPavlov/rubert-base-cased-sentence) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2535
- Accuracy: 0.952

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 157  | 0.2759          | 0.912    |
| No log        | 2.0   | 314  | 0.2538          | 0.936    |
| No log        | 3.0   | 471  | 0.2556          | 0.945    |
| 0.1908        | 4.0   | 628  | 0.2601          | 0.95     |
| 0.1908        | 5.0   | 785  | 0.2535          | 0.952    |


### Framework versions

- Transformers 4.10.2
- Pytorch 1.9.0+cu102
- Datasets 1.12.1
- Tokenizers 0.10.3

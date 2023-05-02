---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: bert-base-uncased-finetuned_for_sentiment_analysis1-sst2
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      args: sst2
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8853211009174312
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned_for_sentiment_analysis1-sst2

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4723
- Accuracy: 0.8853

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 63   | 0.3697          | 0.8544   |
| No log        | 2.0   | 126  | 0.2904          | 0.8956   |
| No log        | 3.0   | 189  | 0.4000          | 0.8830   |
| No log        | 4.0   | 252  | 0.4410          | 0.8911   |
| No log        | 5.0   | 315  | 0.4723          | 0.8853   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1

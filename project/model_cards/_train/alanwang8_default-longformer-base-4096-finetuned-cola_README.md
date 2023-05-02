---
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
model-index:
- name: longformer-base-4096-finetuned-cola
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      args: cola
    metrics:
    - name: Matthews Correlation
      type: matthews_correlation
      value: 0.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# longformer-base-4096-finetuned-cola

This model is a fine-tuned version of [allenai/longformer-base-4096](https://huggingface.co/allenai/longformer-base-4096) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7005
- Matthews Correlation: 0.0

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

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| No log        | 1.0   | 268  | 0.7005          | 0.0                  |
| 0.6995        | 2.0   | 536  | 0.6960          | -0.0043              |
| 0.6995        | 3.0   | 804  | 0.6976          | -0.0057              |
| 0.6962        | 4.0   | 1072 | 0.6983          | -0.0123              |
| 0.6962        | 5.0   | 1340 | 0.6977          | -0.0529              |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu102
- Datasets 2.3.2
- Tokenizers 0.12.1

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
model-index:
- name: English_Grammar_Checker
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      config: cola
      split: train
      args: cola
    metrics:
    - name: Matthews Correlation
      type: matthews_correlation
      value: 0.5324115893962171
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# English_Grammar_Checker

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1117
- Matthews Correlation: 0.5324

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| 0.527         | 1.0   | 1069 | 0.6183          | 0.3947               |
| 0.387         | 2.0   | 2138 | 0.5165          | 0.5156               |
| 0.2772        | 3.0   | 3207 | 0.6716          | 0.5211               |
| 0.176         | 4.0   | 4276 | 0.9270          | 0.5123               |
| 0.0975        | 5.0   | 5345 | 1.1117          | 0.5324               |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

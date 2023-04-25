---
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
model-index:
- name: deberta-base-mnli-finetuned-cola
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
      value: 0.6281691768918801
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-base-mnli-finetuned-cola

This model is a fine-tuned version of [microsoft/deberta-base-mnli](https://huggingface.co/microsoft/deberta-base-mnli) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8205
- Matthews Correlation: 0.6282

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

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| 0.4713        | 1.0   | 535  | 0.5110          | 0.5797               |
| 0.2678        | 2.0   | 1070 | 0.6648          | 0.5154               |
| 0.1811        | 3.0   | 1605 | 0.6681          | 0.6121               |
| 0.113         | 4.0   | 2140 | 0.8205          | 0.6282               |
| 0.0831        | 5.0   | 2675 | 1.0413          | 0.6057               |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.14.0
- Tokenizers 0.10.3

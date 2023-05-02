---
language:
- en
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
model-index:
- name: roberta-base-cola
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE COLA
      type: glue
      args: cola
    metrics:
    - name: Matthews Correlation
      type: matthews_correlation
      value: 0.5960380981891474
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-cola

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the GLUE COLA dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3829
- Matthews Correlation: 0.5960

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| 0.5446        | 0.93  | 500  | 0.4946          | 0.5260               |
| 0.3638        | 1.87  | 1000 | 0.3829          | 0.5960               |
| 0.2658        | 2.8   | 1500 | 0.6063          | 0.6018               |
| 0.2097        | 3.74  | 2000 | 0.7701          | 0.5931               |
| 0.1806        | 4.67  | 2500 | 0.8445          | 0.6181               |
| 0.1405        | 5.61  | 3000 | 0.8823          | 0.5978               |
| 0.1091        | 6.54  | 3500 | 1.0399          | 0.5806               |
| 0.0758        | 7.48  | 4000 | 1.0440          | 0.6220               |
| 0.0625        | 8.41  | 4500 | 1.1968          | 0.5981               |
| 0.0456        | 9.35  | 5000 | 1.2408          | 0.6008               |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.7.1
- Datasets 1.18.3
- Tokenizers 0.11.6

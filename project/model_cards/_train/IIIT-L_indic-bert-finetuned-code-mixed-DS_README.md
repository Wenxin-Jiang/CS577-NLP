---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: indic-bert-finetuned-code-mixed-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# indic-bert-finetuned-code-mixed-DS

This model is a fine-tuned version of [ai4bharat/indic-bert](https://huggingface.co/ai4bharat/indic-bert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8647
- Accuracy: 0.5795
- Precision: 0.5485
- Recall: 0.5287
- F1: 0.4391

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 16
- eval_batch_size: 16
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0937        | 2.0   | 497  | 1.0813          | 0.3602   | 0.3587    | 0.4257 | 0.2834 |
| 1.0189        | 3.99  | 994  | 0.9482          | 0.5493   | 0.3887    | 0.5246 | 0.4080 |
| 0.9208        | 5.99  | 1491 | 0.9002          | 0.5714   | 0.3813    | 0.5292 | 0.4170 |
| 0.8803        | 7.98  | 1988 | 0.8758          | 0.5654   | 0.3889    | 0.5300 | 0.4159 |
| 0.8482        | 9.98  | 2485 | 0.8657          | 0.5795   | 0.3867    | 0.5365 | 0.4228 |
| 0.8293        | 11.98 | 2982 | 0.8734          | 0.5835   | 0.3796    | 0.5298 | 0.4214 |
| 0.8131        | 13.97 | 3479 | 0.8567          | 0.5835   | 0.5018    | 0.5414 | 0.4350 |
| 0.8           | 15.97 | 3976 | 0.8547          | 0.5835   | 0.5610    | 0.5460 | 0.4361 |
| 0.7933        | 17.96 | 4473 | 0.8650          | 0.5775   | 0.5317    | 0.5252 | 0.4373 |
| 0.7835        | 19.96 | 4970 | 0.8647          | 0.5795   | 0.5485    | 0.5287 | 0.4391 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1

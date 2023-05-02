---
license: cc-by-4.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: hing-roberta-finetuned-ours-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hing-roberta-finetuned-ours-DS

This model is a fine-tuned version of [l3cube-pune/hing-roberta](https://huggingface.co/l3cube-pune/hing-roberta) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7267
- Accuracy: 0.68
- Precision: 0.6320
- Recall: 0.6234
- F1: 0.6133

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.0638650088808569e-05
- train_batch_size: 16
- eval_batch_size: 32
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0144        | 0.99  | 99   | 0.8326          | 0.585    | 0.4260    | 0.5589 | 0.4470 |
| 0.7626        | 1.98  | 198  | 0.7314          | 0.625    | 0.5366    | 0.5541 | 0.4828 |
| 0.6243        | 2.97  | 297  | 0.7064          | 0.65     | 0.5702    | 0.5888 | 0.5562 |
| 0.5539        | 3.96  | 396  | 0.7261          | 0.695    | 0.6598    | 0.6362 | 0.6326 |
| 0.4881        | 4.95  | 495  | 0.7267          | 0.68     | 0.6320    | 0.6234 | 0.6133 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1

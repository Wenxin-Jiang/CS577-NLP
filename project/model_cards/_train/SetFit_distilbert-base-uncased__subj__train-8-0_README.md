---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__subj__train-8-0
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__subj__train-8-0

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4440
- Accuracy: 0.789

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7163        | 1.0   | 3    | 0.6868          | 0.5      |
| 0.6683        | 2.0   | 6    | 0.6804          | 0.75     |
| 0.6375        | 3.0   | 9    | 0.6702          | 0.75     |
| 0.5997        | 4.0   | 12   | 0.6686          | 0.75     |
| 0.5345        | 5.0   | 15   | 0.6720          | 0.75     |
| 0.4673        | 6.0   | 18   | 0.6646          | 0.75     |
| 0.4214        | 7.0   | 21   | 0.6494          | 0.75     |
| 0.3439        | 8.0   | 24   | 0.6313          | 0.75     |
| 0.3157        | 9.0   | 27   | 0.6052          | 0.75     |
| 0.2329        | 10.0  | 30   | 0.5908          | 0.75     |
| 0.1989        | 11.0  | 33   | 0.5768          | 0.75     |
| 0.1581        | 12.0  | 36   | 0.5727          | 0.75     |
| 0.1257        | 13.0  | 39   | 0.5678          | 0.75     |
| 0.1005        | 14.0  | 42   | 0.5518          | 0.75     |
| 0.0836        | 15.0  | 45   | 0.5411          | 0.75     |
| 0.0611        | 16.0  | 48   | 0.5320          | 0.75     |
| 0.0503        | 17.0  | 51   | 0.5299          | 0.75     |
| 0.0407        | 18.0  | 54   | 0.5368          | 0.75     |
| 0.0332        | 19.0  | 57   | 0.5455          | 0.75     |
| 0.0293        | 20.0  | 60   | 0.5525          | 0.75     |
| 0.0254        | 21.0  | 63   | 0.5560          | 0.75     |
| 0.0231        | 22.0  | 66   | 0.5569          | 0.75     |
| 0.0201        | 23.0  | 69   | 0.5572          | 0.75     |
| 0.0179        | 24.0  | 72   | 0.5575          | 0.75     |
| 0.0184        | 25.0  | 75   | 0.5547          | 0.75     |
| 0.0148        | 26.0  | 78   | 0.5493          | 0.75     |
| 0.0149        | 27.0  | 81   | 0.5473          | 0.75     |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3

---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: convnext-base-224_finetuned_on_unlabelled_IA_with_snorkel_labels
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# convnext-base-224_finetuned_on_unlabelled_IA_with_snorkel_labels

This model is a fine-tuned version of [facebook/convnext-base-224](https://huggingface.co/facebook/convnext-base-224) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3443
- Precision: 0.9864
- Recall: 0.9822
- F1: 0.9843
- Accuracy: 0.9884

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP
- label_smoothing_factor: 0.2

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.3611        | 1.0   | 2021  | 0.3467          | 0.9843    | 0.9729 | 0.9784 | 0.9842   |
| 0.3524        | 2.0   | 4042  | 0.3453          | 0.9853    | 0.9790 | 0.9821 | 0.9868   |
| 0.3466        | 3.0   | 6063  | 0.3438          | 0.9854    | 0.9847 | 0.9851 | 0.9889   |
| 0.3433        | 4.0   | 8084  | 0.3434          | 0.9850    | 0.9808 | 0.9829 | 0.9873   |
| 0.3404        | 5.0   | 10105 | 0.3459          | 0.9853    | 0.9790 | 0.9821 | 0.9868   |
| 0.3384        | 6.0   | 12126 | 0.3453          | 0.9853    | 0.9790 | 0.9821 | 0.9868   |
| 0.3382        | 7.0   | 14147 | 0.3437          | 0.9864    | 0.9822 | 0.9843 | 0.9884   |
| 0.3358        | 8.0   | 16168 | 0.3441          | 0.9857    | 0.9829 | 0.9843 | 0.9884   |
| 0.3349        | 9.0   | 18189 | 0.3448          | 0.9857    | 0.9829 | 0.9843 | 0.9884   |
| 0.3325        | 10.0  | 20210 | 0.3443          | 0.9864    | 0.9822 | 0.9843 | 0.9884   |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1

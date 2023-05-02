---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: ASCEND_Dataset_Model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ASCEND_Dataset_Model

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.9199
- Wer: 0.9540
- Cer: 0.9868

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 8
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|
| 16.9063       | 1.0   | 687   | 4.7768          | 1.0    | 1.0    |
| 5.0252        | 2.0   | 1374  | 4.7004          | 1.0    | 1.0    |
| 4.9378        | 3.0   | 2061  | 4.6715          | 1.0    | 1.0    |
| 5.1468        | 4.0   | 2748  | 4.6605          | 1.0    | 1.0    |
| 4.9353        | 5.0   | 3435  | 4.6470          | 1.0    | 1.0    |
| 4.913         | 6.0   | 4122  | 4.6177          | 1.0    | 1.0    |
| 4.8034        | 7.0   | 4809  | 4.7699          | 1.0    | 1.0    |
| 4.6905        | 8.0   | 5496  | 4.3596          | 1.0    | 1.0    |
| 4.5251        | 9.0   | 6183  | 4.2670          | 1.0    | 1.0    |
| 4.4527        | 10.0  | 6870  | 4.2087          | 1.0    | 1.0    |
| 4.3731        | 11.0  | 7557  | 4.1950          | 0.9982 | 0.9997 |
| 4.3461        | 12.0  | 8244  | 4.2287          | 0.9928 | 0.9988 |
| 4.3224        | 13.0  | 8931  | 4.1565          | 0.9802 | 0.9971 |
| 4.2504        | 14.0  | 9618  | 4.1254          | 0.9619 | 0.9937 |
| 4.2196        | 15.0  | 10305 | 4.0377          | 0.9562 | 0.9913 |
| 4.1911        | 16.0  | 10992 | 4.0576          | 0.9601 | 0.9887 |
| 4.1079        | 17.0  | 11679 | 4.0630          | 0.9544 | 0.9857 |
| 4.1117        | 18.0  | 12366 | 4.0009          | 0.9558 | 0.9880 |
| 4.0324        | 19.0  | 13053 | 3.9245          | 0.9540 | 0.9877 |
| 3.9871        | 20.0  | 13740 | 3.9199          | 0.9540 | 0.9868 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

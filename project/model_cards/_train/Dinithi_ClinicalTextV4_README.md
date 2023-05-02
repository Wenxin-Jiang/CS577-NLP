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
- name: ClinicalTextV4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ClinicalTextV4

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5609
- Accuracy: 0.8658
- Precision: 0.8371
- Recall: 0.8939
- F1: 0.8646

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.4824        | 1.0   | 600  | 0.3630          | 0.8458   | 0.825     | 0.8609 | 0.8426 |
| 0.3314        | 2.0   | 1200 | 0.3583          | 0.8558   | 0.8252    | 0.8870 | 0.8550 |
| 0.2673        | 3.0   | 1800 | 0.3437          | 0.8583   | 0.8189    | 0.9043 | 0.8595 |
| 0.2255        | 4.0   | 2400 | 0.3678          | 0.8675   | 0.8302    | 0.9096 | 0.8680 |
| 0.1883        | 5.0   | 3000 | 0.4002          | 0.8642   | 0.8259    | 0.9078 | 0.8650 |
| 0.1562        | 6.0   | 3600 | 0.4695          | 0.8633   | 0.8352    | 0.8904 | 0.8620 |
| 0.1372        | 7.0   | 4200 | 0.4940          | 0.8658   | 0.8371    | 0.8939 | 0.8646 |
| 0.1269        | 8.0   | 4800 | 0.5376          | 0.865    | 0.8402    | 0.8870 | 0.8629 |
| 0.1097        | 9.0   | 5400 | 0.5539          | 0.8633   | 0.8397    | 0.8835 | 0.8610 |
| 0.0997        | 10.0  | 6000 | 0.5609          | 0.8658   | 0.8371    | 0.8939 | 0.8646 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

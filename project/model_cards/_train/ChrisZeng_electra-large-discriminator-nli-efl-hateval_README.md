---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: electra-large-discriminator-nli-efl-hateval
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# electra-large-discriminator-nli-efl-hateval

This model is a fine-tuned version of [ynie/electra-large-discriminator-snli_mnli_fever_anli_R1_R2_R3-nli](https://huggingface.co/ynie/electra-large-discriminator-snli_mnli_fever_anli_R1_R2_R3-nli) on the None dataset.
It achieves the following results on the evaluation set:
- Accuracy: 0.798
- F1: 0.7968
- Loss: 0.4166

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Accuracy | F1     | Validation Loss |
|:-------------:|:-----:|:----:|:--------:|:------:|:---------------:|
| 0.4175        | 1.0   | 210  | 0.7317   | 0.7305 | 0.4020          |
| 0.3061        | 2.0   | 420  | 0.768    | 0.7675 | 0.3520          |
| 0.2588        | 3.0   | 630  | 0.79     | 0.7888 | 0.3253          |
| 0.234         | 4.0   | 840  | 0.788    | 0.7877 | 0.3373          |
| 0.2116        | 5.0   | 1050 | 0.804    | 0.8033 | 0.3247          |
| 0.1974        | 6.0   | 1260 | 0.793    | 0.7928 | 0.3400          |
| 0.1807        | 7.0   | 1470 | 0.7973   | 0.7969 | 0.3511          |
| 0.1715        | 8.0   | 1680 | 0.7993   | 0.7989 | 0.3496          |
| 0.1577        | 9.0   | 1890 | 0.8043   | 0.8032 | 0.3507          |
| 0.1469        | 10.0  | 2100 | 0.798    | 0.7970 | 0.3604          |
| 0.1394        | 11.0  | 2310 | 0.7967   | 0.7957 | 0.3734          |
| 0.1322        | 12.0  | 2520 | 0.7913   | 0.7906 | 0.3929          |
| 0.1231        | 13.0  | 2730 | 0.795    | 0.7941 | 0.3954          |
| 0.1189        | 14.0  | 2940 | 0.7977   | 0.7963 | 0.3994          |
| 0.1143        | 15.0  | 3150 | 0.7993   | 0.7980 | 0.3995          |
| 0.1083        | 16.0  | 3360 | 0.7927   | 0.7918 | 0.4125          |
| 0.1079        | 17.0  | 3570 | 0.7993   | 0.7979 | 0.4036          |
| 0.1055        | 18.0  | 3780 | 0.7967   | 0.7956 | 0.4121          |
| 0.1006        | 19.0  | 3990 | 0.7973   | 0.7961 | 0.4152          |
| 0.101         | 20.0  | 4200 | 0.798    | 0.7968 | 0.4166          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.0.0
- Tokenizers 0.11.6

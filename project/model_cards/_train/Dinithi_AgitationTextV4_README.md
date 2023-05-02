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
- name: AgitationTextV4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# AgitationTextV4

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5320
- Accuracy: 0.76
- Precision: 0.8507
- Recall: 0.8028
- F1: 0.8261

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
| 0.6223        | 1.0   | 50   | 0.6247          | 0.66     | 0.7403    | 0.8028 | 0.7703 |
| 0.5431        | 2.0   | 100  | 0.5636          | 0.66     | 0.9302    | 0.5634 | 0.7018 |
| 0.4361        | 3.0   | 150  | 0.5346          | 0.7      | 0.8475    | 0.7042 | 0.7692 |
| 0.3617        | 4.0   | 200  | 0.5255          | 0.72     | 0.8413    | 0.7465 | 0.7910 |
| 0.2878        | 5.0   | 250  | 0.5009          | 0.74     | 0.8358    | 0.7887 | 0.8116 |
| 0.2282        | 6.0   | 300  | 0.5116          | 0.76     | 0.8615    | 0.7887 | 0.8235 |
| 0.1747        | 7.0   | 350  | 0.5235          | 0.75     | 0.8966    | 0.7324 | 0.8062 |
| 0.1454        | 8.0   | 400  | 0.5663          | 0.79     | 0.8472    | 0.8592 | 0.8531 |
| 0.125         | 9.0   | 450  | 0.5371          | 0.77     | 0.8529    | 0.8169 | 0.8345 |
| 0.1188        | 10.0  | 500  | 0.5320          | 0.76     | 0.8507    | 0.8028 | 0.8261 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

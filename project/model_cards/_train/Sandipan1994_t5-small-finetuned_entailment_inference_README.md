---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: t5-small-finetuned_entailment_inference
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned_entailment_inference

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0249

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 1.2885        | 1.0   | 522   | 1.2005          |
| 1.2209        | 2.0   | 1044  | 1.1594          |
| 1.1871        | 3.0   | 1566  | 1.1263          |
| 1.1455        | 4.0   | 2088  | 1.1098          |
| 1.1124        | 5.0   | 2610  | 1.0949          |
| 1.0758        | 6.0   | 3132  | 1.0825          |
| 1.0485        | 7.0   | 3654  | 1.0707          |
| 1.0205        | 8.0   | 4176  | 1.0606          |
| 0.9913        | 9.0   | 4698  | 1.0523          |
| 1.0099        | 10.0  | 5220  | 1.0463          |
| 0.97          | 11.0  | 5742  | 1.0395          |
| 0.9699        | 12.0  | 6264  | 1.0370          |
| 0.9531        | 13.0  | 6786  | 1.0337          |
| 0.9449        | 14.0  | 7308  | 1.0312          |
| 0.9354        | 15.0  | 7830  | 1.0274          |
| 0.9342        | 16.0  | 8352  | 1.0266          |
| 0.9188        | 17.0  | 8874  | 1.0262          |
| 0.9219        | 18.0  | 9396  | 1.0251          |
| 0.9044        | 19.0  | 9918  | 1.0252          |
| 0.9223        | 20.0  | 10440 | 1.0249          |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2

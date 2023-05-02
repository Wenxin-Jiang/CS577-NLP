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
- name: convnext-tiny-224_finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# convnext-tiny-224_finetuned

This model is a fine-tuned version of [facebook/convnext-tiny-224](https://huggingface.co/facebook/convnext-tiny-224) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0895
- Precision: 0.9807
- Recall: 0.9608
- F1: 0.9702
- Accuracy: 0.9776

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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 46   | 0.3080          | 0.9096    | 0.6852 | 0.7206 | 0.8365   |
| No log        | 2.0   | 92   | 0.1644          | 0.9660    | 0.9176 | 0.9386 | 0.9551   |
| No log        | 3.0   | 138  | 0.0974          | 0.9742    | 0.9586 | 0.9661 | 0.9744   |
| No log        | 4.0   | 184  | 0.0795          | 0.9829    | 0.9670 | 0.9746 | 0.9808   |
| No log        | 5.0   | 230  | 0.0838          | 0.9807    | 0.9608 | 0.9702 | 0.9776   |
| No log        | 6.0   | 276  | 0.0838          | 0.9807    | 0.9608 | 0.9702 | 0.9776   |
| No log        | 7.0   | 322  | 0.0803          | 0.9829    | 0.9670 | 0.9746 | 0.9808   |
| No log        | 8.0   | 368  | 0.0869          | 0.9807    | 0.9608 | 0.9702 | 0.9776   |
| No log        | 9.0   | 414  | 0.0897          | 0.9807    | 0.9608 | 0.9702 | 0.9776   |
| No log        | 10.0  | 460  | 0.0895          | 0.9807    | 0.9608 | 0.9702 | 0.9776   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1

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
- name: levit-192_finetuned_on_unlabelled_IA_with_snorkel_labels
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# levit-192_finetuned_on_unlabelled_IA_with_snorkel_labels

This model is a fine-tuned version of [facebook/levit-192](https://huggingface.co/facebook/levit-192) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: nan
- Precision: 0.9836
- Recall: 0.9822
- F1: 0.9829
- Accuracy: 0.9873

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
- train_batch_size: 128
- eval_batch_size: 256
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 253  | nan             | 0.9743    | 0.9791 | 0.9766 | 0.9826   |
| 0.0557        | 2.0   | 506  | nan             | 0.9829    | 0.9801 | 0.9815 | 0.9863   |
| 0.0557        | 3.0   | 759  | nan             | 0.9836    | 0.9822 | 0.9829 | 0.9873   |
| 0.0543        | 4.0   | 1012 | nan             | 0.9839    | 0.9775 | 0.9807 | 0.9858   |
| 0.0543        | 5.0   | 1265 | nan             | 0.9616    | 0.9727 | 0.9670 | 0.9752   |
| 0.0457        | 6.0   | 1518 | nan             | 0.9563    | 0.9699 | 0.9629 | 0.9720   |
| 0.0457        | 7.0   | 1771 | nan             | 0.9822    | 0.9808 | 0.9815 | 0.9863   |
| 0.0418        | 8.0   | 2024 | nan             | 0.9735    | 0.9769 | 0.9752 | 0.9815   |
| 0.0418        | 9.0   | 2277 | nan             | 0.9832    | 0.9811 | 0.9822 | 0.9868   |
| 0.0396        | 10.0  | 2530 | nan             | 0.9843    | 0.9815 | 0.9829 | 0.9873   |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.2
- Tokenizers 0.12.1

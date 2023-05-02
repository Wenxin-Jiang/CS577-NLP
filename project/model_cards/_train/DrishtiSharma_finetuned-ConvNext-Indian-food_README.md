---
license: apache-2.0
tags:
- image-classification
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: finetuned-ConvNext-Indian-food
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: indian_food_images
      type: imagefolder
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9107332624867163
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned-ConvNext-Indian-food

This model is a fine-tuned version of [facebook/convnext-tiny-224](https://huggingface.co/facebook/convnext-tiny-224) on the indian_food_images dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2977
- Accuracy: 0.9107

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.3145        | 0.3   | 100  | 1.0460          | 0.8151   |
| 0.6694        | 0.6   | 200  | 0.5439          | 0.8757   |
| 0.5057        | 0.9   | 300  | 0.4398          | 0.8831   |
| 0.4381        | 1.2   | 400  | 0.4286          | 0.8820   |
| 0.4376        | 1.5   | 500  | 0.3400          | 0.9044   |
| 0.2499        | 1.8   | 600  | 0.3312          | 0.9065   |
| 0.2802        | 2.1   | 700  | 0.3338          | 0.9033   |
| 0.3014        | 2.4   | 800  | 0.3572          | 0.8948   |
| 0.2508        | 2.7   | 900  | 0.3432          | 0.9022   |
| 0.2012        | 3.0   | 1000 | 0.3060          | 0.9086   |
| 0.2634        | 3.3   | 1100 | 0.3451          | 0.9086   |
| 0.2483        | 3.6   | 1200 | 0.3550          | 0.9044   |
| 0.2273        | 3.9   | 1300 | 0.2977          | 0.9107   |
| 0.1214        | 4.2   | 1400 | 0.3265          | 0.9160   |
| 0.2048        | 4.5   | 1500 | 0.3126          | 0.9214   |
| 0.0997        | 4.8   | 1600 | 0.3164          | 0.9160   |
| 0.1145        | 5.11  | 1700 | 0.3055          | 0.9139   |
| 0.1578        | 5.41  | 1800 | 0.3195          | 0.9171   |
| 0.0615        | 5.71  | 1900 | 0.3401          | 0.9107   |
| 0.1537        | 6.01  | 2000 | 0.3428          | 0.9097   |
| 0.1278        | 6.31  | 2100 | 0.3058          | 0.9192   |
| 0.1274        | 6.61  | 2200 | 0.3189          | 0.9192   |
| 0.0877        | 6.91  | 2300 | 0.3370          | 0.9182   |
| 0.1058        | 7.21  | 2400 | 0.3225          | 0.9192   |
| 0.1742        | 7.51  | 2500 | 0.3341          | 0.9214   |
| 0.0949        | 7.81  | 2600 | 0.3126          | 0.9256   |
| 0.1732        | 8.11  | 2700 | 0.3078          | 0.9235   |
| 0.0894        | 8.41  | 2800 | 0.3098          | 0.9267   |
| 0.1257        | 8.71  | 2900 | 0.3030          | 0.9320   |
| 0.1747        | 9.01  | 3000 | 0.3106          | 0.9256   |
| 0.2119        | 9.31  | 3100 | 0.3037          | 0.9299   |
| 0.1074        | 9.61  | 3200 | 0.3049          | 0.9277   |
| 0.1275        | 9.91  | 3300 | 0.3046          | 0.9309   |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1

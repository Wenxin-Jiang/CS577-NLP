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
- name: finetuned-SwinT-Indian-Food-Classification-v3
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: Indian-Food-Images
      type: imagefolder
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9436769394261424
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned-SwinT-Indian-Food-Classification-v3

This model is a fine-tuned version of [microsoft/swin-base-patch4-window7-224-in22k](https://huggingface.co/microsoft/swin-base-patch4-window7-224-in22k) on the Indian-Food-Images dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2910
- Accuracy: 0.9437

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
| 0.9511        | 0.3   | 100  | 0.6092          | 0.8172   |
| 0.6214        | 0.6   | 200  | 0.4406          | 0.8672   |
| 0.7355        | 0.9   | 300  | 0.3665          | 0.8927   |
| 0.6078        | 1.2   | 400  | 0.3285          | 0.9065   |
| 0.439         | 1.5   | 500  | 0.3855          | 0.8916   |
| 0.3644        | 1.8   | 600  | 0.4082          | 0.8969   |
| 0.4748        | 2.1   | 700  | 0.3496          | 0.9022   |
| 0.3966        | 2.4   | 800  | 0.3626          | 0.8905   |
| 0.5799        | 2.7   | 900  | 0.4833          | 0.8767   |
| 0.2995        | 3.0   | 1000 | 0.3387          | 0.9044   |
| 0.3152        | 3.3   | 1100 | 0.3739          | 0.9097   |
| 0.3284        | 3.6   | 1200 | 0.4217          | 0.8916   |
| 0.3631        | 3.9   | 1300 | 0.4118          | 0.9044   |
| 0.219         | 4.2   | 1400 | 0.3721          | 0.9139   |
| 0.2874        | 4.5   | 1500 | 0.3030          | 0.9288   |
| 0.2819        | 4.8   | 1600 | 0.4056          | 0.9150   |
| 0.1755        | 5.11  | 1700 | 0.4039          | 0.9097   |
| 0.2462        | 5.41  | 1800 | 0.3550          | 0.9118   |
| 0.1737        | 5.71  | 1900 | 0.3444          | 0.9150   |
| 0.174         | 6.01  | 2000 | 0.3667          | 0.9160   |
| 0.1536        | 6.31  | 2100 | 0.3301          | 0.9288   |
| 0.0911        | 6.61  | 2200 | 0.3390          | 0.9299   |
| 0.0907        | 6.91  | 2300 | 0.2923          | 0.9288   |
| 0.0921        | 7.21  | 2400 | 0.3502          | 0.9256   |
| 0.1662        | 7.51  | 2500 | 0.3197          | 0.9341   |
| 0.0607        | 7.81  | 2600 | 0.3092          | 0.9362   |
| 0.111         | 8.11  | 2700 | 0.3146          | 0.9394   |
| 0.0588        | 8.41  | 2800 | 0.3069          | 0.9341   |
| 0.131         | 8.71  | 2900 | 0.2971          | 0.9405   |
| 0.1903        | 9.01  | 3000 | 0.3078          | 0.9384   |
| 0.2116        | 9.31  | 3100 | 0.3112          | 0.9341   |
| 0.1415        | 9.61  | 3200 | 0.2956          | 0.9405   |
| 0.1106        | 9.91  | 3300 | 0.2910          | 0.9437   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

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
- name: finetuned-ViT-Indian-Food-Classification-v3
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: Human_Action_Recognition
      type: imagefolder
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9383634431455898
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned-ViT-Indian-Food-Classification-v3

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the Human_Action_Recognition dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2878
- Accuracy: 0.9384

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
| 1.1913        | 0.3   | 100  | 0.9307          | 0.8395   |
| 0.6846        | 0.6   | 200  | 0.5650          | 0.8852   |
| 0.5783        | 0.9   | 300  | 0.5147          | 0.8895   |
| 0.5635        | 1.2   | 400  | 0.5310          | 0.8650   |
| 0.4487        | 1.5   | 500  | 0.4155          | 0.8980   |
| 0.2803        | 1.8   | 600  | 0.3848          | 0.9012   |
| 0.4496        | 2.1   | 700  | 0.4308          | 0.8852   |
| 0.4071        | 2.4   | 800  | 0.4004          | 0.8905   |
| 0.3747        | 2.7   | 900  | 0.3795          | 0.8927   |
| 0.2665        | 3.0   | 1000 | 0.3618          | 0.8927   |
| 0.3696        | 3.3   | 1100 | 0.3588          | 0.8990   |
| 0.2808        | 3.6   | 1200 | 0.3794          | 0.8884   |
| 0.158         | 3.9   | 1300 | 0.3416          | 0.9054   |
| 0.2062        | 4.2   | 1400 | 0.3686          | 0.8916   |
| 0.2039        | 4.5   | 1500 | 0.3219          | 0.9118   |
| 0.2392        | 4.8   | 1600 | 0.3392          | 0.9086   |
| 0.1276        | 5.11  | 1700 | 0.3249          | 0.9192   |
| 0.1812        | 5.41  | 1800 | 0.2970          | 0.9245   |
| 0.1352        | 5.71  | 1900 | 0.3366          | 0.9118   |
| 0.1333        | 6.01  | 2000 | 0.3111          | 0.9203   |
| 0.189         | 6.31  | 2100 | 0.3604          | 0.9139   |
| 0.1048        | 6.61  | 2200 | 0.3496          | 0.9171   |
| 0.0913        | 6.91  | 2300 | 0.3046          | 0.9224   |
| 0.1678        | 7.21  | 2400 | 0.3154          | 0.9288   |
| 0.0705        | 7.51  | 2500 | 0.3229          | 0.9235   |
| 0.1057        | 7.81  | 2600 | 0.2895          | 0.9330   |
| 0.1219        | 8.11  | 2700 | 0.2984          | 0.9299   |
| 0.0521        | 8.41  | 2800 | 0.3083          | 0.9288   |
| 0.1181        | 8.71  | 2900 | 0.3020          | 0.9288   |
| 0.1339        | 9.01  | 3000 | 0.2885          | 0.9373   |
| 0.2393        | 9.31  | 3100 | 0.2895          | 0.9277   |
| 0.1044        | 9.61  | 3200 | 0.2912          | 0.9362   |
| 0.096         | 9.91  | 3300 | 0.2878          | 0.9384   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

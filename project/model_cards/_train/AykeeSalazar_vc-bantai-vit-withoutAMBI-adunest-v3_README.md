---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: vc-bantai-vit-withoutAMBI-adunest-v3
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: imagefolder
      type: imagefolder
      args: Violation-Classification---Raw-10
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8218352310783658
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vc-bantai-vit-withoutAMBI-adunest-v3

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8889
- Accuracy: 0.8218

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 200
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 0.38  | 100  | 0.8208          | 0.7147   |
| No log        | 0.76  | 200  | 0.8861          | 0.7595   |
| No log        | 1.14  | 300  | 0.4306          | 0.7910   |
| No log        | 1.52  | 400  | 0.5222          | 0.8245   |
| 0.3448        | 1.9   | 500  | 0.8621          | 0.7602   |
| 0.3448        | 2.28  | 600  | 0.2902          | 0.8801   |
| 0.3448        | 2.66  | 700  | 0.3687          | 0.8426   |
| 0.3448        | 3.04  | 800  | 0.3585          | 0.8694   |
| 0.3448        | 3.42  | 900  | 0.6546          | 0.7897   |
| 0.2183        | 3.8   | 1000 | 0.3881          | 0.8272   |
| 0.2183        | 4.18  | 1100 | 0.9650          | 0.7709   |
| 0.2183        | 4.56  | 1200 | 0.6444          | 0.7917   |
| 0.2183        | 4.94  | 1300 | 0.4685          | 0.8707   |
| 0.2183        | 5.32  | 1400 | 0.4972          | 0.8506   |
| 0.157         | 5.7   | 1500 | 0.4010          | 0.8513   |
| 0.157         | 6.08  | 1600 | 0.4629          | 0.8419   |
| 0.157         | 6.46  | 1700 | 0.4258          | 0.8714   |
| 0.157         | 6.84  | 1800 | 0.4383          | 0.8573   |
| 0.157         | 7.22  | 1900 | 0.5324          | 0.8493   |
| 0.113         | 7.6   | 2000 | 0.3212          | 0.8942   |
| 0.113         | 7.98  | 2100 | 0.8621          | 0.8326   |
| 0.113         | 8.37  | 2200 | 0.6050          | 0.8131   |
| 0.113         | 8.75  | 2300 | 0.7173          | 0.7991   |
| 0.113         | 9.13  | 2400 | 0.5313          | 0.8125   |
| 0.0921        | 9.51  | 2500 | 0.6584          | 0.8158   |
| 0.0921        | 9.89  | 2600 | 0.8727          | 0.7930   |
| 0.0921        | 10.27 | 2700 | 0.4222          | 0.8922   |
| 0.0921        | 10.65 | 2800 | 0.5811          | 0.8265   |
| 0.0921        | 11.03 | 2900 | 0.6175          | 0.8372   |
| 0.0701        | 11.41 | 3000 | 0.3914          | 0.8835   |
| 0.0701        | 11.79 | 3100 | 0.3364          | 0.8654   |
| 0.0701        | 12.17 | 3200 | 0.6223          | 0.8359   |
| 0.0701        | 12.55 | 3300 | 0.7830          | 0.8125   |
| 0.0701        | 12.93 | 3400 | 0.4356          | 0.8942   |
| 0.0552        | 13.31 | 3500 | 0.7553          | 0.8232   |
| 0.0552        | 13.69 | 3600 | 0.9107          | 0.8292   |
| 0.0552        | 14.07 | 3700 | 0.6108          | 0.8580   |
| 0.0552        | 14.45 | 3800 | 0.5732          | 0.8567   |
| 0.0552        | 14.83 | 3900 | 0.5087          | 0.8614   |
| 0.0482        | 15.21 | 4000 | 0.8889          | 0.8218   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

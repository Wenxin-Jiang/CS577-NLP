---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: delivery_truck_classification
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: imagefolder
      type: imagefolder
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9733333333333334
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# delivery_truck_classification

This model is a fine-tuned version of [microsoft/swin-tiny-patch4-window7-224](https://huggingface.co/microsoft/swin-tiny-patch4-window7-224) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1787
- Accuracy: 0.9733

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 60

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 0.91  | 5    | 0.1787          | 0.9733   |
| No log        | 1.91  | 10   | 0.1787          | 0.9733   |
| No log        | 2.91  | 15   | 0.1787          | 0.9733   |
| 0.3799        | 3.91  | 20   | 0.1787          | 0.9733   |
| 0.3799        | 4.91  | 25   | 0.1787          | 0.9733   |
| 0.3799        | 5.91  | 30   | 0.1787          | 0.9733   |
| 0.3799        | 6.91  | 35   | 0.1787          | 0.9733   |
| 0.3648        | 7.91  | 40   | 0.1787          | 0.9733   |
| 0.3648        | 8.91  | 45   | 0.1787          | 0.9733   |
| 0.3648        | 9.91  | 50   | 0.1787          | 0.9733   |
| 0.3648        | 10.91 | 55   | 0.1787          | 0.9733   |
| 0.3954        | 11.91 | 60   | 0.1787          | 0.9733   |
| 0.3954        | 12.91 | 65   | 0.1787          | 0.9733   |
| 0.3954        | 13.91 | 70   | 0.1787          | 0.9733   |
| 0.3954        | 14.91 | 75   | 0.1787          | 0.9733   |
| 0.3926        | 15.91 | 80   | 0.1787          | 0.9733   |
| 0.3926        | 16.91 | 85   | 0.1787          | 0.9733   |
| 0.3926        | 17.91 | 90   | 0.1787          | 0.9733   |
| 0.3926        | 18.91 | 95   | 0.1787          | 0.9733   |
| 0.3801        | 19.91 | 100  | 0.1787          | 0.9733   |
| 0.3801        | 20.91 | 105  | 0.1787          | 0.9733   |
| 0.3801        | 21.91 | 110  | 0.1787          | 0.9733   |
| 0.3801        | 22.91 | 115  | 0.1787          | 0.9733   |
| 0.3815        | 23.91 | 120  | 0.1787          | 0.9733   |
| 0.3815        | 24.91 | 125  | 0.1787          | 0.9733   |
| 0.3815        | 25.91 | 130  | 0.1787          | 0.9733   |
| 0.3815        | 26.91 | 135  | 0.1787          | 0.9733   |
| 0.3955        | 27.91 | 140  | 0.1787          | 0.9733   |
| 0.3955        | 28.91 | 145  | 0.1787          | 0.9733   |
| 0.3955        | 29.91 | 150  | 0.1787          | 0.9733   |
| 0.3955        | 30.91 | 155  | 0.1787          | 0.9733   |
| 0.3854        | 31.91 | 160  | 0.1787          | 0.9733   |
| 0.3854        | 32.91 | 165  | 0.1787          | 0.9733   |
| 0.3854        | 33.91 | 170  | 0.1787          | 0.9733   |
| 0.3854        | 34.91 | 175  | 0.1787          | 0.9733   |
| 0.3949        | 35.91 | 180  | 0.1787          | 0.9733   |
| 0.3949        | 36.91 | 185  | 0.1787          | 0.9733   |
| 0.3949        | 37.91 | 190  | 0.1787          | 0.9733   |
| 0.3949        | 38.91 | 195  | 0.1787          | 0.9733   |
| 0.423         | 39.91 | 200  | 0.1787          | 0.9733   |
| 0.423         | 40.91 | 205  | 0.1787          | 0.9733   |
| 0.423         | 41.91 | 210  | 0.1787          | 0.9733   |
| 0.423         | 42.91 | 215  | 0.1787          | 0.9733   |
| 0.3761        | 43.91 | 220  | 0.1787          | 0.9733   |
| 0.3761        | 44.91 | 225  | 0.1787          | 0.9733   |
| 0.3761        | 45.91 | 230  | 0.1787          | 0.9733   |
| 0.3761        | 46.91 | 235  | 0.1787          | 0.9733   |
| 0.3673        | 47.91 | 240  | 0.1787          | 0.9733   |
| 0.3673        | 48.91 | 245  | 0.1787          | 0.9733   |
| 0.3673        | 49.91 | 250  | 0.1787          | 0.9733   |
| 0.3673        | 50.91 | 255  | 0.1787          | 0.9733   |
| 0.3639        | 51.91 | 260  | 0.1787          | 0.9733   |
| 0.3639        | 52.91 | 265  | 0.1787          | 0.9733   |
| 0.3639        | 53.91 | 270  | 0.1787          | 0.9733   |
| 0.3639        | 54.91 | 275  | 0.1787          | 0.9733   |
| 0.4031        | 55.91 | 280  | 0.1787          | 0.9733   |
| 0.4031        | 56.91 | 285  | 0.1787          | 0.9733   |
| 0.4031        | 57.91 | 290  | 0.1787          | 0.9733   |
| 0.4031        | 58.91 | 295  | 0.1787          | 0.9733   |
| 0.3787        | 59.91 | 300  | 0.1787          | 0.9733   |


### Framework versions

- Transformers 4.26.0
- Pytorch 1.13.1+cu116
- Datasets 2.9.0
- Tokenizers 0.13.2

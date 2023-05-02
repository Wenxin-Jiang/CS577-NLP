---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: swin-tiny-patch4-window7-224-finetuned-woody
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
      value: 0.7927272727272727
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# swin-tiny-patch4-window7-224-finetuned-woody

This model is a fine-tuned version of [microsoft/swin-tiny-patch4-window7-224](https://huggingface.co/microsoft/swin-tiny-patch4-window7-224) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4349
- Accuracy: 0.7927

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
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.632         | 1.0   | 58   | 0.5883          | 0.6836   |
| 0.6067        | 2.0   | 116  | 0.6017          | 0.6848   |
| 0.5865        | 3.0   | 174  | 0.5695          | 0.7042   |
| 0.553         | 4.0   | 232  | 0.5185          | 0.7515   |
| 0.5468        | 5.0   | 290  | 0.5108          | 0.7430   |
| 0.5473        | 6.0   | 348  | 0.4882          | 0.7648   |
| 0.5381        | 7.0   | 406  | 0.4800          | 0.7588   |
| 0.5468        | 8.0   | 464  | 0.5056          | 0.7358   |
| 0.5191        | 9.0   | 522  | 0.4784          | 0.7673   |
| 0.5318        | 10.0  | 580  | 0.4762          | 0.7636   |
| 0.5079        | 11.0  | 638  | 0.4859          | 0.7673   |
| 0.5216        | 12.0  | 696  | 0.4691          | 0.7697   |
| 0.515         | 13.0  | 754  | 0.4857          | 0.7624   |
| 0.5186        | 14.0  | 812  | 0.4685          | 0.7733   |
| 0.4748        | 15.0  | 870  | 0.4536          | 0.7818   |
| 0.4853        | 16.0  | 928  | 0.4617          | 0.7770   |
| 0.4868        | 17.0  | 986  | 0.4622          | 0.7782   |
| 0.4572        | 18.0  | 1044 | 0.4583          | 0.7770   |
| 0.4679        | 19.0  | 1102 | 0.4590          | 0.7733   |
| 0.4508        | 20.0  | 1160 | 0.4576          | 0.7903   |
| 0.4663        | 21.0  | 1218 | 0.4542          | 0.7891   |
| 0.4533        | 22.0  | 1276 | 0.4428          | 0.7903   |
| 0.4892        | 23.0  | 1334 | 0.4372          | 0.7867   |
| 0.4704        | 24.0  | 1392 | 0.4414          | 0.7903   |
| 0.4304        | 25.0  | 1450 | 0.4430          | 0.7988   |
| 0.4411        | 26.0  | 1508 | 0.4348          | 0.7818   |
| 0.4604        | 27.0  | 1566 | 0.4387          | 0.7927   |
| 0.441         | 28.0  | 1624 | 0.4378          | 0.7964   |
| 0.442         | 29.0  | 1682 | 0.4351          | 0.7915   |
| 0.4585        | 30.0  | 1740 | 0.4349          | 0.7927   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.0
- Tokenizers 0.13.1

---
license: apache-2.0
tags:
- image-classification
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: finetuned-ViT-human-action-recognition-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned-ViT-human-action-recognition-v1

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the Human_Action_Recognition dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1427
- Accuracy: 0.0791

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
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.4986        | 0.13  | 100  | 3.1427          | 0.0791   |
| 1.1929        | 0.25  | 200  | 3.4083          | 0.0726   |
| 1.2673        | 0.38  | 300  | 3.4615          | 0.0769   |
| 0.9805        | 0.51  | 400  | 3.9192          | 0.0824   |
| 1.158         | 0.63  | 500  | 4.2648          | 0.0698   |
| 1.2544        | 0.76  | 600  | 4.5536          | 0.0574   |
| 1.0073        | 0.89  | 700  | 4.0310          | 0.0819   |
| 0.9315        | 1.02  | 800  | 4.5154          | 0.0702   |
| 0.9063        | 1.14  | 900  | 4.7162          | 0.0633   |
| 0.6756        | 1.27  | 1000 | 4.6482          | 0.0626   |
| 1.0239        | 1.4   | 1100 | 4.6437          | 0.0635   |
| 0.7634        | 1.52  | 1200 | 4.5625          | 0.0752   |
| 0.8365        | 1.65  | 1300 | 4.9912          | 0.0561   |
| 0.8979        | 1.78  | 1400 | 5.1739          | 0.0356   |
| 0.9448        | 1.9   | 1500 | 4.8946          | 0.0541   |
| 0.697         | 2.03  | 1600 | 4.9516          | 0.0741   |
| 0.7861        | 2.16  | 1700 | 5.0090          | 0.0776   |
| 0.6404        | 2.28  | 1800 | 5.3905          | 0.0643   |
| 0.7939        | 2.41  | 1900 | 4.9159          | 0.1015   |
| 0.6331        | 2.54  | 2000 | 5.3083          | 0.0589   |
| 0.6082        | 2.66  | 2100 | 4.8538          | 0.0857   |
| 0.6229        | 2.79  | 2200 | 5.3086          | 0.0689   |
| 0.6964        | 2.92  | 2300 | 5.3745          | 0.0713   |
| 0.5246        | 3.05  | 2400 | 5.0369          | 0.0796   |
| 0.6097        | 3.17  | 2500 | 5.2935          | 0.0743   |
| 0.5778        | 3.3   | 2600 | 5.5431          | 0.0709   |
| 0.4196        | 3.43  | 2700 | 5.5508          | 0.0759   |
| 0.5495        | 3.55  | 2800 | 5.5728          | 0.0813   |
| 0.5932        | 3.68  | 2900 | 5.7992          | 0.0663   |
| 0.4382        | 3.81  | 3000 | 5.8010          | 0.0643   |
| 0.4827        | 3.93  | 3100 | 5.7529          | 0.0680   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

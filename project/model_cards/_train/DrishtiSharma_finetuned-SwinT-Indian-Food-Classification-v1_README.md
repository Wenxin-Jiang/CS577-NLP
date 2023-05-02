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
- name: finetuned-SwinT-Indian-Food-Classification-v1
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
      value: 0.9373007438894793
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned-SwinT-Indian-Food-Classification-v1

This model is a fine-tuned version of [microsoft/swin-base-patch4-window7-224-in22k](https://huggingface.co/microsoft/swin-base-patch4-window7-224-in22k) on the Indian-Food-Images dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2868
- Accuracy: 0.9373

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
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.2433        | 0.3   | 100  | 0.7067          | 0.8193   |
| 0.6458        | 0.6   | 200  | 0.4692          | 0.8789   |
| 0.635         | 0.9   | 300  | 0.4864          | 0.8682   |
| 0.6219        | 1.2   | 400  | 0.4240          | 0.8831   |
| 0.4889        | 1.5   | 500  | 0.3840          | 0.8948   |
| 0.2963        | 1.8   | 600  | 0.4279          | 0.8959   |
| 0.4405        | 2.1   | 700  | 0.3508          | 0.9118   |
| 0.3803        | 2.4   | 800  | 0.3659          | 0.9086   |
| 0.3499        | 2.7   | 900  | 0.3347          | 0.9214   |
| 0.3131        | 3.0   | 1000 | 0.2910          | 0.9277   |
| 0.3036        | 3.3   | 1100 | 0.3938          | 0.9107   |
| 0.2697        | 3.6   | 1200 | 0.3566          | 0.9171   |
| 0.1551        | 3.9   | 1300 | 0.3369          | 0.9341   |
| 0.0752        | 4.2   | 1400 | 0.2868          | 0.9373   |
| 0.132         | 4.5   | 1500 | 0.3023          | 0.9373   |
| 0.1133        | 4.8   | 1600 | 0.2978          | 0.9416   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

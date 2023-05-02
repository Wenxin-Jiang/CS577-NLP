---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: vc-bantai-vit-withoutAMBI-adunest-v1
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: imagefolder
      type: imagefolder
      args: Violation-Classification---Raw-6
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9181222707423581
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vc-bantai-vit-withoutAMBI-adunest-v1

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3318
- Accuracy: 0.9181

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
| No log        | 0.23  | 100  | 0.3365          | 0.8581   |
| No log        | 0.45  | 200  | 0.3552          | 0.8472   |
| No log        | 0.68  | 300  | 0.3165          | 0.8581   |
| No log        | 0.91  | 400  | 0.2882          | 0.8690   |
| 0.3813        | 1.13  | 500  | 0.2825          | 0.8745   |
| 0.3813        | 1.36  | 600  | 0.2686          | 0.9007   |
| 0.3813        | 1.59  | 700  | 0.2381          | 0.9017   |
| 0.3813        | 1.81  | 800  | 0.3643          | 0.8734   |
| 0.3813        | 2.04  | 900  | 0.2873          | 0.8930   |
| 0.2736        | 2.27  | 1000 | 0.2236          | 0.9039   |
| 0.2736        | 2.49  | 1100 | 0.2652          | 0.8723   |
| 0.2736        | 2.72  | 1200 | 0.2793          | 0.8952   |
| 0.2736        | 2.95  | 1300 | 0.2158          | 0.8974   |
| 0.2736        | 3.17  | 1400 | 0.2410          | 0.8886   |
| 0.2093        | 3.4   | 1500 | 0.2262          | 0.9017   |
| 0.2093        | 3.63  | 1600 | 0.2110          | 0.9214   |
| 0.2093        | 3.85  | 1700 | 0.2048          | 0.9138   |
| 0.2093        | 4.08  | 1800 | 0.2044          | 0.9127   |
| 0.2093        | 4.31  | 1900 | 0.2591          | 0.9007   |
| 0.1764        | 4.54  | 2000 | 0.2466          | 0.8952   |
| 0.1764        | 4.76  | 2100 | 0.2554          | 0.9017   |
| 0.1764        | 4.99  | 2200 | 0.2145          | 0.9203   |
| 0.1764        | 5.22  | 2300 | 0.3187          | 0.9039   |
| 0.1764        | 5.44  | 2400 | 0.3336          | 0.9050   |
| 0.1454        | 5.67  | 2500 | 0.2542          | 0.9127   |
| 0.1454        | 5.9   | 2600 | 0.2796          | 0.8952   |
| 0.1454        | 6.12  | 2700 | 0.2410          | 0.9181   |
| 0.1454        | 6.35  | 2800 | 0.2503          | 0.9148   |
| 0.1454        | 6.58  | 2900 | 0.2966          | 0.8996   |
| 0.1216        | 6.8   | 3000 | 0.1978          | 0.9312   |
| 0.1216        | 7.03  | 3100 | 0.2297          | 0.9214   |
| 0.1216        | 7.26  | 3200 | 0.2768          | 0.9203   |
| 0.1216        | 7.48  | 3300 | 0.3356          | 0.9083   |
| 0.1216        | 7.71  | 3400 | 0.3415          | 0.9138   |
| 0.1038        | 7.94  | 3500 | 0.2398          | 0.9061   |
| 0.1038        | 8.16  | 3600 | 0.3347          | 0.8963   |
| 0.1038        | 8.39  | 3700 | 0.2199          | 0.9203   |
| 0.1038        | 8.62  | 3800 | 0.2943          | 0.9061   |
| 0.1038        | 8.84  | 3900 | 0.2561          | 0.9181   |
| 0.0925        | 9.07  | 4000 | 0.4170          | 0.8777   |
| 0.0925        | 9.3   | 4100 | 0.3638          | 0.8974   |
| 0.0925        | 9.52  | 4200 | 0.3233          | 0.9094   |
| 0.0925        | 9.75  | 4300 | 0.3496          | 0.9203   |
| 0.0925        | 9.98  | 4400 | 0.3621          | 0.8996   |
| 0.0788        | 10.2  | 4500 | 0.3260          | 0.9116   |
| 0.0788        | 10.43 | 4600 | 0.3979          | 0.9061   |
| 0.0788        | 10.66 | 4700 | 0.3301          | 0.8974   |
| 0.0788        | 10.88 | 4800 | 0.2197          | 0.9105   |
| 0.0788        | 11.11 | 4900 | 0.3306          | 0.9148   |
| 0.0708        | 11.34 | 5000 | 0.3318          | 0.9181   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

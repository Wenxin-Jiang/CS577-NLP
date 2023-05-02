---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: vc-bantai-vit-withoutAMBI-adunest-v2
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
      value: 0.7705338809034907
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vc-bantai-vit-withoutAMBI-adunest-v2

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8271
- Accuracy: 0.7705

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
| No log        | 0.4   | 100  | 0.3811          | 0.8511   |
| No log        | 0.81  | 200  | 0.3707          | 0.8609   |
| No log        | 1.21  | 300  | 0.5708          | 0.7325   |
| No log        | 1.61  | 400  | 0.3121          | 0.8778   |
| 0.3308        | 2.02  | 500  | 0.3358          | 0.8445   |
| 0.3308        | 2.42  | 600  | 0.2820          | 0.8768   |
| 0.3308        | 2.82  | 700  | 0.4825          | 0.7695   |
| 0.3308        | 3.23  | 800  | 0.3133          | 0.8640   |
| 0.3308        | 3.63  | 900  | 0.4509          | 0.8219   |
| 0.2028        | 4.03  | 1000 | 0.5426          | 0.7551   |
| 0.2028        | 4.44  | 1100 | 0.4886          | 0.8552   |
| 0.2028        | 4.84  | 1200 | 0.5649          | 0.7695   |
| 0.2028        | 5.24  | 1300 | 0.5925          | 0.7900   |
| 0.2028        | 5.65  | 1400 | 0.4203          | 0.8439   |
| 0.1471        | 6.05  | 1500 | 0.4275          | 0.8486   |
| 0.1471        | 6.45  | 1600 | 0.3683          | 0.8727   |
| 0.1471        | 6.85  | 1700 | 0.5709          | 0.8121   |
| 0.1471        | 7.26  | 1800 | 0.6209          | 0.7680   |
| 0.1471        | 7.66  | 1900 | 0.4971          | 0.8147   |
| 0.101         | 8.06  | 2000 | 0.8792          | 0.7567   |
| 0.101         | 8.47  | 2100 | 0.3288          | 0.8670   |
| 0.101         | 8.87  | 2200 | 0.3643          | 0.8342   |
| 0.101         | 9.27  | 2300 | 0.4883          | 0.8711   |
| 0.101         | 9.68  | 2400 | 0.2892          | 0.8943   |
| 0.0667        | 10.08 | 2500 | 0.5437          | 0.8398   |
| 0.0667        | 10.48 | 2600 | 0.5841          | 0.8450   |
| 0.0667        | 10.89 | 2700 | 0.8016          | 0.8219   |
| 0.0667        | 11.29 | 2800 | 0.6389          | 0.7772   |
| 0.0667        | 11.69 | 2900 | 0.3714          | 0.8753   |
| 0.0674        | 12.1  | 3000 | 0.9811          | 0.7130   |
| 0.0674        | 12.5  | 3100 | 0.6359          | 0.8101   |
| 0.0674        | 12.9  | 3200 | 0.5691          | 0.8285   |
| 0.0674        | 13.31 | 3300 | 0.6123          | 0.8316   |
| 0.0674        | 13.71 | 3400 | 0.3655          | 0.8978   |
| 0.0525        | 14.11 | 3500 | 0.4988          | 0.8583   |
| 0.0525        | 14.52 | 3600 | 0.6153          | 0.8450   |
| 0.0525        | 14.92 | 3700 | 0.4189          | 0.8881   |
| 0.0525        | 15.32 | 3800 | 0.9713          | 0.7967   |
| 0.0525        | 15.73 | 3900 | 1.1224          | 0.7967   |
| 0.0438        | 16.13 | 4000 | 0.5725          | 0.8578   |
| 0.0438        | 16.53 | 4100 | 0.4725          | 0.8532   |
| 0.0438        | 16.94 | 4200 | 0.4696          | 0.8640   |
| 0.0438        | 17.34 | 4300 | 0.4028          | 0.8789   |
| 0.0438        | 17.74 | 4400 | 0.9452          | 0.7746   |
| 0.0462        | 18.15 | 4500 | 0.4455          | 0.8783   |
| 0.0462        | 18.55 | 4600 | 0.6328          | 0.8311   |
| 0.0462        | 18.95 | 4700 | 0.6707          | 0.8296   |
| 0.0462        | 19.35 | 4800 | 0.7771          | 0.8429   |
| 0.0462        | 19.76 | 4900 | 1.2832          | 0.7408   |
| 0.0381        | 20.16 | 5000 | 0.5415          | 0.8737   |
| 0.0381        | 20.56 | 5100 | 0.8932          | 0.7977   |
| 0.0381        | 20.97 | 5200 | 0.5182          | 0.8691   |
| 0.0381        | 21.37 | 5300 | 0.5967          | 0.8794   |
| 0.0381        | 21.77 | 5400 | 0.8271          | 0.7705   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: vc-bantai-vit-withoutAMBI-adunest
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
      value: 0.9388646288209607
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vc-bantai-vit-withoutAMBI-adunest

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1950
- Accuracy: 0.9389

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.4821        | 0.11  | 100  | 0.7644          | 0.6714   |
| 0.7032        | 0.23  | 200  | 0.5568          | 0.75     |
| 0.5262        | 0.34  | 300  | 0.4440          | 0.7806   |
| 0.4719        | 0.45  | 400  | 0.3893          | 0.8144   |
| 0.5021        | 0.57  | 500  | 0.5129          | 0.8090   |
| 0.3123        | 0.68  | 600  | 0.4536          | 0.7980   |
| 0.3606        | 0.79  | 700  | 0.3679          | 0.8483   |
| 0.4081        | 0.91  | 800  | 0.3335          | 0.8559   |
| 0.3624        | 1.02  | 900  | 0.3149          | 0.8592   |
| 0.1903        | 1.14  | 1000 | 0.3296          | 0.8766   |
| 0.334         | 1.25  | 1100 | 0.2832          | 0.8897   |
| 0.2731        | 1.36  | 1200 | 0.2546          | 0.8930   |
| 0.311         | 1.48  | 1300 | 0.2585          | 0.8908   |
| 0.3209        | 1.59  | 1400 | 0.2701          | 0.8854   |
| 0.4005        | 1.7   | 1500 | 0.2643          | 0.8897   |
| 0.3128        | 1.82  | 1600 | 0.2864          | 0.8843   |
| 0.3376        | 1.93  | 1700 | 0.2882          | 0.8657   |
| 0.2698        | 2.04  | 1800 | 0.2876          | 0.9028   |
| 0.2347        | 2.16  | 1900 | 0.2405          | 0.8974   |
| 0.2436        | 2.27  | 2000 | 0.2804          | 0.8886   |
| 0.1764        | 2.38  | 2100 | 0.2852          | 0.8952   |
| 0.1197        | 2.5   | 2200 | 0.2312          | 0.9127   |
| 0.1082        | 2.61  | 2300 | 0.2133          | 0.9116   |
| 0.1245        | 2.72  | 2400 | 0.2677          | 0.8985   |
| 0.1335        | 2.84  | 2500 | 0.2098          | 0.9181   |
| 0.2194        | 2.95  | 2600 | 0.1911          | 0.9127   |
| 0.089         | 3.06  | 2700 | 0.2062          | 0.9181   |
| 0.0465        | 3.18  | 2800 | 0.2414          | 0.9247   |
| 0.0985        | 3.29  | 2900 | 0.1869          | 0.9389   |
| 0.1113        | 3.41  | 3000 | 0.1819          | 0.9323   |
| 0.1392        | 3.52  | 3100 | 0.2101          | 0.9312   |
| 0.0621        | 3.63  | 3200 | 0.2201          | 0.9367   |
| 0.1168        | 3.75  | 3300 | 0.1935          | 0.9389   |
| 0.059         | 3.86  | 3400 | 0.1946          | 0.9367   |
| 0.0513        | 3.97  | 3500 | 0.1950          | 0.9389   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

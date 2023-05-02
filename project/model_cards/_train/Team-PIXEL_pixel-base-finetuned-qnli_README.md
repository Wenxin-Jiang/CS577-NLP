---
language:
- en
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: pixel-base-finetuned-qnli
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE QNLI
      type: glue
      args: qnli
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8859600951857953
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pixel-base-finetuned-qnli

This model is a fine-tuned version of [Team-PIXEL/pixel-base](https://huggingface.co/Team-PIXEL/pixel-base) on the GLUE QNLI dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9503
- Accuracy: 0.8860

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 64
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- training_steps: 15000
- mixed_precision_training: Apex, opt level O1

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.5451        | 0.31  | 500   | 0.5379          | 0.7282   |
| 0.4451        | 0.61  | 1000  | 0.3846          | 0.8318   |
| 0.4567        | 0.92  | 1500  | 0.3543          | 0.8525   |
| 0.3558        | 1.22  | 2000  | 0.3294          | 0.8638   |
| 0.3324        | 1.53  | 2500  | 0.3221          | 0.8666   |
| 0.3434        | 1.83  | 3000  | 0.2976          | 0.8774   |
| 0.2573        | 2.14  | 3500  | 0.3193          | 0.8750   |
| 0.2411        | 2.44  | 4000  | 0.3044          | 0.8794   |
| 0.253         | 2.75  | 4500  | 0.2932          | 0.8834   |
| 0.1653        | 3.05  | 5000  | 0.3364          | 0.8841   |
| 0.1662        | 3.36  | 5500  | 0.3348          | 0.8797   |
| 0.1816        | 3.67  | 6000  | 0.3440          | 0.8869   |
| 0.1699        | 3.97  | 6500  | 0.3453          | 0.8845   |
| 0.1027        | 4.28  | 7000  | 0.4277          | 0.8810   |
| 0.0987        | 4.58  | 7500  | 0.4590          | 0.8832   |
| 0.0974        | 4.89  | 8000  | 0.4311          | 0.8783   |
| 0.0669        | 5.19  | 8500  | 0.5214          | 0.8819   |
| 0.0583        | 5.5   | 9000  | 0.5776          | 0.8850   |
| 0.065         | 5.8   | 9500  | 0.5646          | 0.8821   |
| 0.0381        | 6.11  | 10000 | 0.6252          | 0.8796   |
| 0.0314        | 6.41  | 10500 | 0.7222          | 0.8801   |
| 0.0453        | 6.72  | 11000 | 0.6951          | 0.8823   |
| 0.0264        | 7.03  | 11500 | 0.7620          | 0.8828   |
| 0.0215        | 7.33  | 12000 | 0.8160          | 0.8834   |
| 0.0176        | 7.64  | 12500 | 0.8583          | 0.8828   |
| 0.0245        | 7.94  | 13000 | 0.8484          | 0.8867   |
| 0.0124        | 8.25  | 13500 | 0.8927          | 0.8836   |
| 0.0112        | 8.55  | 14000 | 0.9368          | 0.8827   |
| 0.0154        | 8.86  | 14500 | 0.9405          | 0.8860   |
| 0.0046        | 9.16  | 15000 | 0.9503          | 0.8860   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.0.0
- Tokenizers 0.11.6

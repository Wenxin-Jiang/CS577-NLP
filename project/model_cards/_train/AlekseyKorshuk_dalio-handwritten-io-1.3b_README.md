---
license: other
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/dalio-handwritten-io
metrics:
- accuracy
model-index:
- name: dalio-handwritten-io-1.3b
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
    dataset:
      name: AlekseyKorshuk/dalio-handwritten-io
      type: AlekseyKorshuk/dalio-handwritten-io
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.06143479984145858
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dalio-handwritten-io-1.3b

This model is a fine-tuned version of [facebook/opt-1.3b](https://huggingface.co/facebook/opt-1.3b) on the AlekseyKorshuk/dalio-handwritten-io dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3789
- Accuracy: 0.0614

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 16
- total_eval_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.9219        | 0.1   | 1    | 2.6484          | 0.0529   |
| 2.6938        | 0.2   | 2    | 2.6484          | 0.0529   |
| 2.6365        | 0.3   | 3    | 2.5508          | 0.0560   |
| 2.5088        | 0.4   | 4    | 2.5332          | 0.0562   |
| 2.7307        | 0.5   | 5    | 2.5176          | 0.0565   |
| 2.969         | 0.6   | 6    | 2.4941          | 0.0571   |
| 2.7283        | 0.7   | 7    | 2.4883          | 0.0567   |
| 2.6157        | 0.8   | 8    | 2.4766          | 0.0578   |
| 2.6406        | 0.9   | 9    | 2.4590          | 0.0583   |
| 2.5701        | 1.0   | 10   | 2.4375          | 0.0587   |
| 2.2017        | 1.1   | 11   | 2.4238          | 0.0587   |
| 2.0039        | 1.2   | 12   | 2.4219          | 0.0586   |
| 1.8981        | 1.3   | 13   | 2.4160          | 0.0589   |
| 1.7683        | 1.4   | 14   | 2.4160          | 0.0595   |
| 1.6746        | 1.5   | 15   | 2.4121          | 0.0600   |
| 1.8051        | 1.6   | 16   | 2.4102          | 0.0600   |
| 2.0457        | 1.7   | 17   | 2.4043          | 0.0602   |
| 1.8257        | 1.8   | 18   | 2.4004          | 0.0606   |
| 1.744         | 1.9   | 19   | 2.3887          | 0.0607   |
| 1.8232        | 2.0   | 20   | 2.3887          | 0.0607   |
| 1.4741        | 2.1   | 21   | 2.3828          | 0.0610   |
| 1.651         | 2.2   | 22   | 2.3770          | 0.0608   |
| 1.3732        | 2.3   | 23   | 2.3730          | 0.0610   |
| 1.3151        | 2.4   | 24   | 2.3730          | 0.0610   |
| 1.5302        | 2.5   | 25   | 2.3730          | 0.0610   |
| 1.2539        | 2.6   | 26   | 2.375           | 0.0612   |
| 1.6211        | 2.7   | 27   | 2.3770          | 0.0612   |
| 1.6047        | 2.8   | 28   | 2.3770          | 0.0613   |
| 1.1953        | 2.9   | 29   | 2.3789          | 0.0614   |
| 1.1621        | 3.0   | 30   | 2.3789          | 0.0614   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

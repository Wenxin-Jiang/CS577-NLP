---
license: other
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/dalio-all-io
metrics:
- accuracy
model-index:
- name: dalio-all-io-1.3b
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
    dataset:
      name: AlekseyKorshuk/dalio-all-io
      type: AlekseyKorshuk/dalio-all-io
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.05582538140677676
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dalio-all-io-1.3b

This model is a fine-tuned version of [facebook/opt-1.3b](https://huggingface.co/facebook/opt-1.3b) on the AlekseyKorshuk/dalio-all-io dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3652
- Accuracy: 0.0558

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
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.6543        | 0.03  | 1    | 2.6113          | 0.0513   |
| 2.6077        | 0.07  | 2    | 2.6113          | 0.0513   |
| 2.5964        | 0.1   | 3    | 2.5605          | 0.0519   |
| 2.7302        | 0.14  | 4    | 2.5234          | 0.0527   |
| 2.7           | 0.17  | 5    | 2.5078          | 0.0528   |
| 2.5674        | 0.21  | 6    | 2.4941          | 0.0532   |
| 2.6406        | 0.24  | 7    | 2.4883          | 0.0534   |
| 2.5315        | 0.28  | 8    | 2.4805          | 0.0536   |
| 2.7202        | 0.31  | 9    | 2.4727          | 0.0537   |
| 2.5144        | 0.34  | 10   | 2.4648          | 0.0536   |
| 2.4983        | 0.38  | 11   | 2.4512          | 0.0537   |
| 2.7029        | 0.41  | 12   | 2.4414          | 0.0539   |
| 2.5198        | 0.45  | 13   | 2.4336          | 0.0540   |
| 2.5706        | 0.48  | 14   | 2.4258          | 0.0545   |
| 2.5688        | 0.52  | 15   | 2.4180          | 0.0548   |
| 2.3793        | 0.55  | 16   | 2.4102          | 0.0552   |
| 2.4785        | 0.59  | 17   | 2.4043          | 0.0554   |
| 2.4688        | 0.62  | 18   | 2.3984          | 0.0553   |
| 2.5674        | 0.66  | 19   | 2.3984          | 0.0553   |
| 2.5054        | 0.69  | 20   | 2.3945          | 0.0554   |
| 2.452         | 0.72  | 21   | 2.3887          | 0.0555   |
| 2.5999        | 0.76  | 22   | 2.3828          | 0.0556   |
| 2.3665        | 0.79  | 23   | 2.3789          | 0.0556   |
| 2.6223        | 0.83  | 24   | 2.375           | 0.0557   |
| 2.3562        | 0.86  | 25   | 2.3711          | 0.0557   |
| 2.429         | 0.9   | 26   | 2.3691          | 0.0557   |
| 2.563         | 0.93  | 27   | 2.3672          | 0.0558   |
| 2.4573        | 0.97  | 28   | 2.3652          | 0.0558   |
| 2.4883        | 1.0   | 29   | 2.3652          | 0.0558   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

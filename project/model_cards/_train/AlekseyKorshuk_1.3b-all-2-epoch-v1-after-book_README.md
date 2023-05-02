---
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/dalio-all-io
metrics:
- accuracy
model-index:
- name: 1.3b-all-2-epoch-v1-after-book
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
      value: 0.06395348837209303
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 1.3b-all-2-epoch-v1-after-book

This model is a fine-tuned version of [/models/1.3b-dalio-principles-book](https://huggingface.co//models/1.3b-dalio-principles-book) on the AlekseyKorshuk/dalio-all-io dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9482
- Accuracy: 0.0640

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 32
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 2.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.17          | 0.07  | 1    | 2.0547          | 0.0621   |
| 2.1814        | 0.13  | 2    | 2.0547          | 0.0621   |
| 2.0963        | 0.2   | 3    | 2.0234          | 0.0625   |
| 2.1383        | 0.27  | 4    | 2.0195          | 0.0625   |
| 2.1625        | 0.33  | 5    | 2.0195          | 0.0625   |
| 2.1808        | 0.4   | 6    | 2.0156          | 0.0624   |
| 2.1587        | 0.47  | 7    | 2.0176          | 0.0626   |
| 2.0847        | 0.53  | 8    | 2.0137          | 0.0627   |
| 2.0336        | 0.6   | 9    | 2.0137          | 0.0627   |
| 2.1777        | 0.67  | 10   | 2.0059          | 0.0629   |
| 2.2034        | 0.73  | 11   | 2.0             | 0.0630   |
| 2.1665        | 0.8   | 12   | 1.9941          | 0.0628   |
| 2.0352        | 0.87  | 13   | 1.9883          | 0.0629   |
| 2.1263        | 0.93  | 14   | 1.9834          | 0.0628   |
| 2.1282        | 1.0   | 15   | 1.9785          | 0.0632   |
| 1.7159        | 1.07  | 16   | 1.9766          | 0.0633   |
| 1.8346        | 1.13  | 17   | 1.9775          | 0.0635   |
| 1.7183        | 1.2   | 18   | 1.9824          | 0.0634   |
| 1.6086        | 1.27  | 19   | 1.9883          | 0.0635   |
| 1.6497        | 1.33  | 20   | 1.9893          | 0.0634   |
| 1.6267        | 1.4   | 21   | 1.9854          | 0.0637   |
| 1.5962        | 1.47  | 22   | 1.9766          | 0.0637   |
| 1.5168        | 1.53  | 23   | 1.9697          | 0.0637   |
| 1.6213        | 1.6   | 24   | 1.9619          | 0.0637   |
| 1.4789        | 1.67  | 25   | 1.9580          | 0.0638   |
| 1.6796        | 1.73  | 26   | 1.9551          | 0.0638   |
| 1.5964        | 1.8   | 27   | 1.9531          | 0.0638   |
| 1.787         | 1.87  | 28   | 1.9512          | 0.0639   |
| 1.6536        | 1.93  | 29   | 1.9492          | 0.0640   |
| 1.7178        | 2.0   | 30   | 1.9482          | 0.0640   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

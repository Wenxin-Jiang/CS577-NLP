---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: albert-base-ours-run-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-base-ours-run-2

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2462
- Accuracy: 0.695
- Precision: 0.6550
- Recall: 0.6529
- F1: 0.6539

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.999         | 1.0   | 200  | 0.9155          | 0.615    | 0.5590    | 0.5590 | 0.5524 |
| 0.7736        | 2.0   | 400  | 0.8488          | 0.6      | 0.5639    | 0.5689 | 0.5256 |
| 0.5836        | 3.0   | 600  | 0.8760          | 0.67     | 0.6259    | 0.6158 | 0.6191 |
| 0.4153        | 4.0   | 800  | 1.0050          | 0.675    | 0.6356    | 0.6212 | 0.5974 |
| 0.3188        | 5.0   | 1000 | 1.2033          | 0.655    | 0.6254    | 0.5977 | 0.5991 |
| 0.2335        | 6.0   | 1200 | 1.3407          | 0.625    | 0.5955    | 0.6039 | 0.5937 |
| 0.1752        | 7.0   | 1400 | 1.4246          | 0.72     | 0.6846    | 0.6815 | 0.6820 |
| 0.1056        | 8.0   | 1600 | 1.9654          | 0.69     | 0.6589    | 0.6251 | 0.6311 |
| 0.0696        | 9.0   | 1800 | 1.9376          | 0.715    | 0.6908    | 0.6632 | 0.6627 |
| 0.0352        | 10.0  | 2000 | 1.9970          | 0.72     | 0.6880    | 0.6784 | 0.6817 |
| 0.0227        | 11.0  | 2200 | 2.1449          | 0.705    | 0.6901    | 0.6641 | 0.6679 |
| 0.0199        | 12.0  | 2400 | 2.2213          | 0.72     | 0.6891    | 0.6685 | 0.6749 |
| 0.0077        | 13.0  | 2600 | 2.1500          | 0.69     | 0.6729    | 0.6704 | 0.6647 |
| 0.0067        | 14.0  | 2800 | 2.1780          | 0.69     | 0.6632    | 0.6651 | 0.6621 |
| 0.0034        | 15.0  | 3000 | 2.1759          | 0.71     | 0.6800    | 0.6786 | 0.6788 |
| 0.0013        | 16.0  | 3200 | 2.2139          | 0.71     | 0.6760    | 0.6721 | 0.6735 |
| 0.0005        | 17.0  | 3400 | 2.2282          | 0.7      | 0.6606    | 0.6593 | 0.6599 |
| 0.0003        | 18.0  | 3600 | 2.2257          | 0.7      | 0.6606    | 0.6593 | 0.6599 |
| 0.0003        | 19.0  | 3800 | 2.2492          | 0.695    | 0.6550    | 0.6529 | 0.6539 |
| 0.0002        | 20.0  | 4000 | 2.2462          | 0.695    | 0.6550    | 0.6529 | 0.6539 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Tokenizers 0.13.2

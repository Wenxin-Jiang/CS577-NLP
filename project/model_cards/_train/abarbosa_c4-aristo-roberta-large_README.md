---
metrics:
- accuracy

model-index:
- name: c4-aristo-roberta-large
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# c4-aristo-roberta-large

This model was trained from scratch on an unkown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0332
- Accuracy: 0.7370

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.98) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.8204        | 1.0   | 140  | 0.7246          | 0.7171   |
| 0.5512        | 2.0   | 280  | 0.7441          | 0.7312   |
| 0.3437        | 3.0   | 420  | 0.8940          | 0.7363   |
| 0.291         | 4.0   | 560  | 1.0332          | 0.7370   |


### Framework versions

- Transformers 4.6.1
- Pytorch 1.10.0.dev20210620+cu113
- Datasets 1.6.2
- Tokenizers 0.10.2

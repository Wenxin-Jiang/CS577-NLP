---
license: other
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/amazon-reviews-input-output
metrics:
- accuracy
model-index:
- name: amazon-reviews-input-output-6.7b-best
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
    dataset:
      name: AlekseyKorshuk/amazon-reviews-input-output
      type: AlekseyKorshuk/amazon-reviews-input-output
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.040325203252032524
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# amazon-reviews-input-output-6.7b-best

This model is a fine-tuned version of [facebook/opt-6.7b](https://huggingface.co/facebook/opt-6.7b) on the AlekseyKorshuk/amazon-reviews-input-output dataset.
It achieves the following results on the evaluation set:
- Loss: 2.6953
- Accuracy: 0.0403
- Samples: 100
- Perplexity: 14.8101
- Table: <wandb.data_types.Table object at 0x7fc684448b50>

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 64
- total_eval_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.9912        | 0.06  | 1    | 2.7441          | 0.0404   |
| 2.9329        | 0.12  | 2    | 2.7441          | 0.0404   |
| 2.9138        | 0.19  | 3    | 2.8262          | 0.0389   |
| 2.9395        | 0.25  | 4    | 2.8262          | 0.0389   |
| 2.9109        | 0.31  | 5    | 2.7949          | 0.0399   |
| 2.8391        | 0.38  | 6    | 2.7461          | 0.0403   |
| 2.9368        | 0.44  | 7    | 2.7207          | 0.0398   |
| 2.7583        | 0.5   | 8    | 2.7070          | 0.0403   |
| 2.9756        | 0.56  | 9    | 2.6836          | 0.0408   |
| 2.8442        | 0.62  | 10   | 2.6738          | 0.0403   |
| 2.7312        | 0.69  | 11   | 2.6680          | 0.0405   |
| 2.7439        | 0.75  | 12   | 2.6699          | 0.0404   |
| 2.9075        | 0.81  | 13   | 2.6797          | 0.0403   |
| 2.8518        | 0.88  | 14   | 2.6797          | 0.0403   |
| 2.8579        | 0.94  | 15   | 2.6777          | 0.0404   |
| 2.8916        | 1.0   | 16   | 2.6953          | 0.0403   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

---
license: other
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/amazon-reviews-input-output
metrics:
- accuracy
model-index:
- name: amazon-reviews-input-output-6.7b
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
      value: 0.03882113821138211
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# amazon-reviews-input-output-6.7b

This model is a fine-tuned version of [facebook/opt-6.7b](https://huggingface.co/facebook/opt-6.7b) on the AlekseyKorshuk/amazon-reviews-input-output dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8574
- Accuracy: 0.0388
- Samples: 100
- Perplexity: 17.4166
- Table: <wandb.data_types.Table object at 0x7fd30eb4e940>

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
- num_epochs: 2.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.9912        | 0.06  | 1    | 2.7441          | 0.0404   |
| 2.9329        | 0.12  | 2    | 2.7441          | 0.0404   |
| 2.9138        | 0.19  | 3    | 2.8262          | 0.0389   |
| 2.9395        | 0.25  | 4    | 2.8262          | 0.0389   |
| 2.9109        | 0.31  | 5    | 2.7949          | 0.0399   |
| 2.8394        | 0.38  | 6    | 2.7461          | 0.0403   |
| 2.9365        | 0.44  | 7    | 2.7207          | 0.0399   |
| 2.7588        | 0.5   | 8    | 2.7070          | 0.0403   |
| 2.9751        | 0.56  | 9    | 2.6816          | 0.0407   |
| 2.844         | 0.62  | 10   | 2.6738          | 0.0404   |
| 2.731         | 0.69  | 11   | 2.6680          | 0.0406   |
| 2.7434        | 0.75  | 12   | 2.6699          | 0.0404   |
| 2.9043        | 0.81  | 13   | 2.6855          | 0.0400   |
| 2.8564        | 0.88  | 14   | 2.6855          | 0.0400   |
| 2.8716        | 0.94  | 15   | 2.6855          | 0.0400   |
| 2.896         | 1.0   | 16   | 2.6953          | 0.0398   |
| 1.9858        | 1.06  | 17   | 2.7070          | 0.0400   |
| 2.0563        | 1.12  | 18   | 2.7285          | 0.0400   |
| 2.04          | 1.19  | 19   | 2.7676          | 0.0398   |
| 1.9885        | 1.25  | 20   | 2.7910          | 0.0396   |
| 2.09          | 1.31  | 21   | 2.7969          | 0.0393   |
| 2.059         | 1.38  | 22   | 2.8105          | 0.0395   |
| 2.0498        | 1.44  | 23   | 2.7930          | 0.0398   |
| 1.9568        | 1.5   | 24   | 2.7910          | 0.0401   |
| 2.1418        | 1.56  | 25   | 2.7930          | 0.0398   |
| 1.975         | 1.62  | 26   | 2.7930          | 0.0397   |
| 1.996         | 1.69  | 27   | 2.7949          | 0.0393   |
| 1.9617        | 1.75  | 28   | 2.8047          | 0.0392   |
| 2.2062        | 1.81  | 29   | 2.8145          | 0.0388   |
| 1.9929        | 1.88  | 30   | 2.8145          | 0.0386   |
| 1.9235        | 1.94  | 31   | 2.8281          | 0.0390   |
| 1.9127        | 2.0   | 32   | 2.8574          | 0.0388   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

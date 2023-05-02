---
license: other
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: dalio-1.3b-test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dalio-1.3b-test

This model is a fine-tuned version of [facebook/opt-1.3b](https://huggingface.co/facebook/opt-1.3b) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.6035
- Accuracy: 0.0672

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
| 2.6133        | 0.08  | 1    | 2.625           | 0.0652   |
| 2.6199        | 0.15  | 2    | 2.625           | 0.0652   |
| 2.7202        | 0.23  | 3    | 2.6113          | 0.0658   |
| 2.6177        | 0.31  | 4    | 2.6113          | 0.0658   |
| 2.5422        | 0.38  | 5    | 2.5703          | 0.0661   |
| 2.5627        | 0.46  | 6    | 2.5566          | 0.0662   |
| 2.5784        | 0.54  | 7    | 2.5469          | 0.0664   |
| 2.5264        | 0.62  | 8    | 2.5371          | 0.0663   |
| 2.3396        | 0.69  | 9    | 2.5332          | 0.0670   |
| 2.4297        | 0.77  | 10   | 2.5273          | 0.0673   |
| 2.3914        | 0.85  | 11   | 2.5234          | 0.0672   |
| 2.429         | 0.92  | 12   | 2.5195          | 0.0671   |
| 2.3055        | 1.0   | 13   | 2.5117          | 0.0672   |
| 1.7162        | 1.08  | 14   | 2.5215          | 0.0672   |
| 1.7264        | 1.15  | 15   | 2.5469          | 0.0677   |
| 1.7559        | 1.23  | 16   | 2.5879          | 0.0671   |
| 1.7899        | 1.31  | 17   | 2.6113          | 0.0667   |
| 1.6465        | 1.38  | 18   | 2.6191          | 0.0666   |
| 1.5955        | 1.46  | 19   | 2.6074          | 0.0671   |
| 1.5389        | 1.54  | 20   | 2.5957          | 0.0672   |
| 1.5356        | 1.62  | 21   | 2.5859          | 0.0670   |
| 1.386         | 1.69  | 22   | 2.5820          | 0.0672   |
| 1.7698        | 1.77  | 23   | 2.5742          | 0.0670   |
| 1.3923        | 1.85  | 24   | 2.5801          | 0.0669   |
| 1.4723        | 1.92  | 25   | 2.5898          | 0.0672   |
| 1.5653        | 2.0   | 26   | 2.6035          | 0.0672   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

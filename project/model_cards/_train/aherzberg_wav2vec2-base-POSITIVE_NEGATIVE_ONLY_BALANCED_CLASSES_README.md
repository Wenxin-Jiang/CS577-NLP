---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-base-POSITIVE_NEGATIVE_ONLY_BALANCED_CLASSES
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-POSITIVE_NEGATIVE_ONLY_BALANCED_CLASSES

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3710
- Accuracy: 0.8822

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
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7822        | 0.96  | 18   | 0.6874          | 0.7424   |
| 0.5685        | 1.96  | 36   | 0.5974          | 0.7845   |
| 0.45          | 2.96  | 54   | 0.4988          | 0.8182   |
| 0.399         | 3.96  | 72   | 0.4583          | 0.8384   |
| 0.3457        | 4.96  | 90   | 0.4415          | 0.8451   |
| 0.352         | 5.96  | 108  | 0.3710          | 0.8822   |
| 0.2878        | 6.96  | 126  | 0.3881          | 0.8620   |
| 0.2669        | 7.96  | 144  | 0.4309          | 0.8502   |
| 0.2406        | 8.96  | 162  | 0.4271          | 0.8502   |
| 0.2491        | 9.96  | 180  | 0.4271          | 0.8502   |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.11.0
- Datasets 1.14.0
- Tokenizers 0.10.3

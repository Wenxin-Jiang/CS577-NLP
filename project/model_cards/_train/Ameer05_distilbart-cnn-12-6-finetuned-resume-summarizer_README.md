---
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: distilbart-cnn-12-6-finetuned-resume-summarizer
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbart-cnn-12-6-finetuned-resume-summarizer

This model is a fine-tuned version of [Ameer05/model-tokenizer-repo](https://huggingface.co/Ameer05/model-tokenizer-repo) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1123
- Rouge1: 52.5826
- Rouge2: 34.3861
- Rougel: 41.8525
- Rougelsum: 51.0015

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
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| No log        | 0.91  | 5    | 3.2243          | 42.8593 | 24.8652 | 34.1789 | 41.406    |
| No log        | 1.91  | 10   | 2.6948          | 48.8571 | 28.6711 | 39.2648 | 46.188    |
| No log        | 2.91  | 15   | 2.4665          | 50.6085 | 30.4034 | 39.7406 | 48.5449   |
| No log        | 3.91  | 20   | 2.3329          | 52.2357 | 32.3398 | 41.574  | 49.4316   |
| 3.6611        | 4.91  | 25   | 2.2362          | 52.0134 | 33.1612 | 41.3103 | 50.255    |
| 3.6611        | 5.91  | 30   | 2.1833          | 51.5434 | 32.7045 | 40.5683 | 49.4238   |
| 3.6611        | 6.91  | 35   | 2.1462          | 53.5144 | 35.4518 | 42.8615 | 51.4053   |
| 3.6611        | 7.91  | 40   | 2.1518          | 52.0985 | 33.6754 | 41.5936 | 50.5159   |
| 2.0326        | 8.91  | 45   | 2.1075          | 53.1401 | 34.9721 | 42.2973 | 51.8454   |
| 2.0326        | 9.91  | 50   | 2.1123          | 52.5826 | 34.3861 | 41.8525 | 51.0015   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.9.1
- Datasets 2.0.0
- Tokenizers 0.10.3

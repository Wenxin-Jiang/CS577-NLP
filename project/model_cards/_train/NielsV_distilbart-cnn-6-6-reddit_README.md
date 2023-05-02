---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- reddit
metrics:
- rouge
model-index:
- name: distilbart-cnn-6-6-reddit
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: reddit
      type: reddit
      config: default
      split: train
      args: default
    metrics:
    - name: Rouge1
      type: rouge
      value: 0.1849
---

# distilbart-cnn-6-6-reddit

This model is a fine-tuned version of [sshleifer/distilbart-cnn-6-6](https://huggingface.co/sshleifer/distilbart-cnn-6-6) on the reddit dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9883
- Rouge1: 0.1849
- Rouge2: 0.0437
- Rougel: 0.1273
- Rougelsum: 0.1601

## More information and training script

You can find more information about how this model was trained, including the actual training script in [this github repository](https://github.com/VerleysenNiels/arxiv-summarizer).

## Training and evaluation data

I made a split in a train and test set. The test size is 1% of the total dataset, which comes down to about 38k samples.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:------:|:---------------:|:------:|:------:|:------:|:---------:|
| 3.13          | 1.0   | 238116 | 3.2736          | 0.1773 | 0.0392 | 0.1223 | 0.1539    |
| 2.8586        | 2.0   | 476232 | 3.0449          | 0.1846 | 0.0431 | 0.127  | 0.1601    |
| 2.7844        | 3.0   | 714348 | 2.9883          | 0.1849 | 0.0437 | 0.1273 | 0.1601    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

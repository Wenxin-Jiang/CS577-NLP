---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bart-base-News_Summarization_CNN
  results: []
---

# bart-base-News_Summarization_CNN

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1603

## Model description

Using the dataset from the following link, I trained a text summarization model.

https://www.kaggle.com/datasets/hadasu92/cnn-articles-after-basic-cleaning

## Intended uses & limitations

I used this to improve my skillset. I thank all of authors of the different technologies and dataset(s) for their contributions that have this possible. I am not too worried about getting credit for my part, but make sure to properly cite the authors of the different technologies and dataset(s) as they absolutely deserve credit for their contributions.

## Training and evaluation data

More information needed

## Training procedure
CPU trained on all samples where the article length is less than 820 words and the summary length is no more than 52 words in length. Additionally, any sample that was missing a new article or summarization was removed. In all, 24,911 out of the possible 42,025 samples were used for training/testing/evaluation.

Here is the link to the code that was used to train this model:
https://github.com/DunnBC22/NLP_Projects/blob/main/Text%20Summarization/CNN%20News%20Text%20Summarization.ipynb

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss |  rouge1  |  rouge2  |   rougeL   | rougeLsum  |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|:----------:|:----------:|
| 0.7491        | 1.0   | 1089 | 0.1618          |    N/A   |    N/A   |     N/A    |    N/A     |
| 0.1641        | 2.0   | 2178 | 0.1603          | 0.834343 | 0.793822 |  0.823824  |	0.823778  |

### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1

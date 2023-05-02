---
tags:
- generated_from_trainer
model-index:
- name: pegasus-multi_news-NewsSummarization_BBC
  results: []
---

# pegasus-multi_news-NewsSummarization_BBC

This model is a fine-tuned version of [google/pegasus-multi_news](https://huggingface.co/google/pegasus-multi_news) on the None dataset.

## Model description

More information needed

## Intended uses & limitations

I used this to improve my skillset. I thank all of authors of the different technologies and 
dataset(s) for their contributions that have this possible. I am not too worried about getting 
credit for my part, but make sure to properly cite the authors of the different technologies 
and dataset(s) as they absolutely deserve credit for their contributions.

## Training and evaluation data

Dataset Source: https://www.kaggle.com/datasets/pariza/bbc-news-summary

## Training procedure

Here is the link to the script that I created to train this project: 

https://github.com/DunnBC22/NLP_Projects/blob/main/Text%20Summarization/Text_Summarization_BBC_News-Pegasus.ipynb

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
- lr_scheduler_warmup_steps: 50
- num_epochs: 2

### Training results

Unfortunately, I did not set the metrics to automatically upload here. They are as follows:

| Training Loss | Epoch | Step |  rouge1  |  rouge2  |  rougeL  |  rougeLsum |
|:-------------:|:-----:|:----:|:--------:|:--------:|:--------:|:----------:|
|    6.41979    |  2.0  | 214  | 0.584474 | 0.463574 | 0.408729 |  0.408431  |

### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
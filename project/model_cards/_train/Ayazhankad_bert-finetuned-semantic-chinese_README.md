---
tags:
- generated_from_trainer
metrics:
- f1
- accuracy
model-index:
- name: bert-finetuned-sentiment-chinese
  results: []
---

# bert-finetuned-sentiment-chinese

This model is a fine-tuned version of [bert-base-chinese](https://huggingface.co/bert-base-chinese) on the 24000 samples of the [Douban Movies Short Comments](https://www.kaggle.com/datasets/utmhikari/doubanmovieshortcomments) from [Kaggle](https://www.kaggle.com).

[Douban.com](https://en.wikipedia.org/wiki/Douban#:~:text=Douban.com%20(Chinese%3A%20%E8%B1%86%E7%93%A3,and%20activities%20in%20Chinese%20cities.) (Chinese: 豆瓣; pinyin: Dòubàn), launched on 6 March 2005, is a Chinese social networking service website that allows registered users to record information and create content related to film, books, music, recent events, and activities in Chinese cities.

It achieves the following results on the evaluation set of 6000 samples:
- Loss: 0.4446
- F1: 0.5309
- Roc Auc: 0.7040
- Accuracy: 0.512

## **Using Hosted inference API**

Input text in Chinese and wait for the sentiment label assigned.
Example input: 连奥创都知道整容要去韩国 

-> "I like this very much", so it gives Star_5.

## Using in code

```
from transformers import pipeline

classifer = pipeline('sentiment-analysis',model='bert-finetuned-semantic-chinese/checkpoint-15000')
classifer('我非常喜歡這個')

```

## Model description

Multilabel Text Classification based on the semantics. 

Following Labels are assigned to the input text: ['Star_1', 'Star_2', 'Star_3', 'Star_4', 'Star_5'].

Star_1 - very negative

Star_2 - negative

Star_3 - neutral

Star_4 - positive.

Star_5 - very positive. 

## Intended uses & limitations

Limitations: may observe bias present in [bert-base-chinese](https://huggingface.co/bert-base-chinese) and the [Douban Movies Short Comments](https://www.kaggle.com/datasets/utmhikari/doubanmovieshortcomments) from [Kaggle](https://www.kaggle.com).

# Training procedures

Trained with PyTorch:
-Splitting dataframe to train and test 
-One hot encoding
-Setting AutoTokenizer as [bert-base-chinese](https://huggingface.co/bert-base-chinese)
-Encoding the dataset
-Setting AutoModelForSequenceClassification and setting problem type as "multi_label_classification"
-Setting Training arguments 
-Trainng with Hugging Face trainer
-pushing to hub

## Training and evaluation data

24000 - Training.
6000 - Evaluation

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | F1     | Roc Auc | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:-------:|:--------:|
| 0.3683        | 1.0   | 3000  | 0.3569          | 0.4709 | 0.6613  | 0.3848   |
| 0.3284        | 2.0   | 6000  | 0.3677          | 0.5179 | 0.6931  | 0.478    |
| 0.2874        | 3.0   | 9000  | 0.4007          | 0.5209 | 0.6967  | 0.4943   |
| 0.2309        | 4.0   | 12000 | 0.4446          | 0.5309 | 0.7040  | 0.512    |
| 0.1828        | 5.0   | 15000 | 0.5096          | 0.5298 | 0.7040  | 0.515    |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

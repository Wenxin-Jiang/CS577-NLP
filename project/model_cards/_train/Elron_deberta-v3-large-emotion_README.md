---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large
  results: []
---

# deberta-v3-large-sentiment

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on an [tweet_eval](https://huggingface.co/datasets/tweet_eval)  dataset.

## Model description

Test set results:

| Model                      | Emotion       | Hate          | Irony         | Offensive     | Sentiment     | 
| -------------              | ------------- | ------------- | ------------- | ------------- | ------------- | 
| deberta-v3-large           | **86.3**      | **61.3**      | **87.1**      | **86.4**      | **73.9**      | 
| BERTweet                   | 79.3          | -             | 82.1          | 79.5          | 73.4          | 
| RoB-RT                     | 79.5          | 52.3          | 61.7          | 80.5          | 69.3          | 

[source:papers_with_code](https://paperswithcode.com/sota/sentiment-analysis-on-tweeteval)


## Intended uses & limitations

Classifying attributes of interest on tweeter like data. 

## Training and evaluation data

[tweet_eval](https://huggingface.co/datasets/tweet_eval)  dataset.

## Training procedure

Fine tuned and evaluated with [run_glue.py]()
### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7e-06
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 50
- num_epochs: 10.0
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.2787        | 0.49  | 100  | 1.1127          | 0.4866   |
| 1.089         | 0.98  | 200  | 0.9668          | 0.7139   |
| 0.9134        | 1.47  | 300  | 0.8720          | 0.7834   |
| 0.8618        | 1.96  | 400  | 0.7726          | 0.7941   |
| 0.686         | 2.45  | 500  | 0.7337          | 0.8209   |
| 0.6333        | 2.94  | 600  | 0.7350          | 0.8235   |
| 0.5765        | 3.43  | 700  | 0.7561          | 0.8235   |
| 0.5502        | 3.92  | 800  | 0.7273          | 0.8476   |
| 0.5049        | 4.41  | 900  | 0.8137          | 0.8102   |
| 0.4695        | 4.9   | 1000 | 0.7581          | 0.8289   |
| 0.4657        | 5.39  | 1100 | 0.8404          | 0.8048   |
| 0.4549        | 5.88  | 1200 | 0.7800          | 0.8369   |
| 0.4305        | 6.37  | 1300 | 0.8575          | 0.8235   |
| 0.4209        | 6.86  | 1400 | 0.8572          | 0.8102   |
| 0.3983        | 7.35  | 1500 | 0.8392          | 0.8316   |
| 0.4139        | 7.84  | 1600 | 0.8152          | 0.8209   |
| 0.393         | 8.33  | 1700 | 0.8261          | 0.8289   |
| 0.3979        | 8.82  | 1800 | 0.8328          | 0.8235   |
| 0.3928        | 9.31  | 1900 | 0.8364          | 0.8209   |
| 0.3848        | 9.8   | 2000 | 0.8322          | 0.8235   |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.9.0
- Datasets 2.2.2
- Tokenizers 0.11.6

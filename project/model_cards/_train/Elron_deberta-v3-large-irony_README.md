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

# deberta-v3-large-irony

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
- learning_rate: 8e-06
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 50
- num_epochs: 10.0
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6478        | 1.12  | 100  | 0.5890          | 0.7529   |
| 0.5013        | 2.25  | 200  | 0.5873          | 0.7707   |
| 0.388         | 3.37  | 300  | 0.6993          | 0.7602   |
| 0.3169        | 4.49  | 400  | 0.6773          | 0.7874   |
| 0.2693        | 5.61  | 500  | 0.7172          | 0.7707   |
| 0.2396        | 6.74  | 600  | 0.7397          | 0.7801   |
| 0.2284        | 7.86  | 700  | 0.8096          | 0.7550   |
| 0.2207        | 8.98  | 800  | 0.7827          | 0.7654   |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.9.0
- Datasets 2.2.2
- Tokenizers 0.11.6

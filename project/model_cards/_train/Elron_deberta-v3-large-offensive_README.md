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
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 50
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6417        | 0.27  | 100  | 0.6283          | 0.6533   |
| 0.5105        | 0.54  | 200  | 0.4588          | 0.7915   |
| 0.4554        | 0.81  | 300  | 0.4500          | 0.7968   |
| 0.4212        | 1.08  | 400  | 0.4773          | 0.7938   |
| 0.4054        | 1.34  | 500  | 0.4311          | 0.7983   |
| 0.3922        | 1.61  | 600  | 0.4588          | 0.7998   |
| 0.3776        | 1.88  | 700  | 0.4367          | 0.8066   |
| 0.3535        | 2.15  | 800  | 0.4675          | 0.8074   |
| 0.33          | 2.42  | 900  | 0.4874          | 0.8021   |
| 0.3113        | 2.69  | 1000 | 0.4949          | 0.8044   |
| 0.3203        | 2.96  | 1100 | 0.4550          | 0.8059   |
| 0.248         | 3.23  | 1200 | 0.4858          | 0.8036   |
| 0.2478        | 3.49  | 1300 | 0.5299          | 0.8029   |
| 0.2371        | 3.76  | 1400 | 0.5013          | 0.7991   |
| 0.2388        | 4.03  | 1500 | 0.5520          | 0.8021   |
| 0.1744        | 4.3   | 1600 | 0.6687          | 0.7915   |
| 0.1788        | 4.57  | 1700 | 0.7560          | 0.7689   |
| 0.1652        | 4.84  | 1800 | 0.6985          | 0.7832   |
| 0.1596        | 5.11  | 1900 | 0.7191          | 0.7915   |
| 0.1214        | 5.38  | 2000 | 0.9097          | 0.7893   |
| 0.1432        | 5.64  | 2100 | 0.9184          | 0.7787   |
| 0.1145        | 5.91  | 2200 | 0.9620          | 0.7878   |
| 0.1069        | 6.18  | 2300 | 0.9489          | 0.7893   |
| 0.1012        | 6.45  | 2400 | 1.0107          | 0.7817   |
| 0.0942        | 6.72  | 2500 | 1.0021          | 0.7885   |
| 0.087         | 6.99  | 2600 | 1.1090          | 0.7915   |
| 0.0598        | 7.26  | 2700 | 1.1735          | 0.7795   |
| 0.0742        | 7.53  | 2800 | 1.1433          | 0.7817   |
| 0.073         | 7.79  | 2900 | 1.1343          | 0.7953   |
| 0.0553        | 8.06  | 3000 | 1.2258          | 0.7840   |
| 0.0474        | 8.33  | 3100 | 1.2461          | 0.7817   |
| 0.0515        | 8.6   | 3200 | 1.2996          | 0.7825   |
| 0.0551        | 8.87  | 3300 | 1.2819          | 0.7855   |
| 0.0541        | 9.14  | 3400 | 1.2808          | 0.7855   |
| 0.0465        | 9.41  | 3500 | 1.3398          | 0.7817   |
| 0.0407        | 9.68  | 3600 | 1.3231          | 0.7825   |
| 0.0343        | 9.94  | 3700 | 1.3330          | 0.7825   |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.9.0
- Datasets 2.2.2
- Tokenizers 0.11.6

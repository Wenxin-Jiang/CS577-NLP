---
language: sv
license: mit
---

## Swedish BERT models for sentiment analysis
 [Recorded Future](https://www.recordedfuture.com/) together with [AI Sweden](https://www.ai.se/en) releases two language models for sentiment analysis in Swedish. The two models are based on the [KB\/bert-base-swedish-cased](https://huggingface.co/KB/bert-base-swedish-cased) model and has been fine-tuned to solve a multi-label sentiment analysis task. 

The models have been fine-tuned for the sentiments fear and violence. The models output three floats corresponding to the labels "Negative", "Weak sentiment", and "Strong Sentiment" at the respective indexes. 
The models have been trained on Swedish data with a conversational focus, collected from various internet sources and forums.

The models are only trained on Swedish data and only supports inference of Swedish input texts. The models inference metrics for all non-Swedish inputs are not defined, these inputs are considered as out of domain data.

The current models are supported at Transformers version >= 4.3.3 and Torch version 1.8.0, compatibility with older versions are not verified. 

### Swedish-Sentiment-Fear

The model can be imported from the transformers library by running

    from transformers import BertForSequenceClassification, BertTokenizerFast
    
    tokenizer = BertTokenizerFast.from_pretrained("RecordedFuture/Swedish-Sentiment-Fear")
    classifier_fear= BertForSequenceClassification.from_pretrained("RecordedFuture/Swedish-Sentiment-Fear") 

When the model and tokenizer are initialized the model can be used for inference. 

#### Sentiment definitions
#### The strong sentiment includes but are not limited to
Texts that:

 - Hold an expressive emphasis on fear and/ or anxiety 

#### The weak sentiment includes but are not limited to
Texts that: 

- Express fear and/ or anxiety in a neutral way

#### Verification metrics 

During training, the model had maximized validation metrics at the following classification breakpoint. 



| Classification Breakpoint | F-score | Precision | Recall |
|:-------------------------:|:-------:|:---------:|:------:|
|               0.45 |  0.8754 |   0.8618  | 0.8895 |

#### Swedish-Sentiment-Violence
The model be can imported from the transformers library by running

    from transformers import BertForSequenceClassification, BertTokenizerFast
    
    tokenizer = BertTokenizerFast.from_pretrained("RecordedFuture/Swedish-Sentiment-Violence")
    classifier_violence = BertForSequenceClassification.from_pretrained("RecordedFuture/Swedish-Sentiment-Violence") 

When the model and tokenizer are initialized the model can be used for inference. 

### Sentiment definitions
#### The strong sentiment includes but are not limited to
Texts that:
 -  Referencing highly violent acts
-   Hold an aggressive tone
#### The weak sentiment includes but are not limited to
Texts that:
-   Include general violent statements that do not fall under the strong sentiment
#### Verification metrics 
During training, the model had maximized validation metrics at the following classification breakpoint. 

| Classification Breakpoint | F-score | Precision | Recall |
|:-------------------------:|:-------:|:---------:|:------:|
|            0.35           |  0.7677 |   0.7456  |  0.791 |
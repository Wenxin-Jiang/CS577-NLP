---
language: sv
license: mit
---

## Swedish BERT models for sentiment analysis, Sentiment targets. 
[Recorded Future](https://www.recordedfuture.com/) together with [AI Sweden](https://www.ai.se/en) releases two language models for target/role assignment in Swedish. The two models are based on the [KB/bert-base-swedish-cased](https://huggingface.co/KB/bert-base-swedish-cased), the models as has been fine tuned to solve a Named Entety Recognition(NER) token classification task.

This is a downstream model to be used in conjunction with the [Swedish violence sentiment classifier](https://huggingface.co/RecordedFuture/Swedish-Sentiment-Violence) or [Swedish violence sentiment classifier](https://huggingface.co/RecordedFuture/Swedish-Sentiment-Fear). The models are trained to tag parts of sentences that has recieved a positive classification from the upstream sentiment classifier. The model will tag parts of sentences that contains the targets that the upstream model has activated on. 

The NER sentiment target models do work as standalone models but their recommended application is downstreamfrom a sentence classification model.  

The models are only trained on Swedish data and only supports inference of Swedish input texts. The models inference metrics for all non-Swedish inputs are not defined, these inputs are considered as out of domain data.

The current models are supported at Transformers version >= 4.3.3 and Torch version 1.8.0, compatibility with older versions are not verified. 

### Fear targets

The model can be imported from the transformers library by running

    from transformers import BertForSequenceClassification, BertTokenizerFast
    
    tokenizer = BertTokenizerFast.from_pretrained("RecordedFuture/Swedish-Sentiment-Fear-Targets")
    classifier_fear_targets= BertForTokenClassification.from_pretrained("RecordedFuture/Swedish-Sentiment-Fear-Targets") 

When the model and tokenizer are initialized the model can be used for inference. 

#### Verification metrics 

During training the Fear target model had the following verification metrics when using "any overlap" as the evaluation metric.  


| F-score | Precision | Recall |
|:-------------------------:|:-------:|:---------:|:------:|
|  0.8361 |   0.7903  | 0.8876 |

#### Swedish-Sentiment-Violence
The model be can imported from the transformers library by running

    from transformers import BertForSequenceClassification, BertTokenizerFast
    
    tokenizer = BertTokenizerFast.from_pretrained("RecordedFuture/Swedish-Sentiment-Violence-Targets")
    classifier_violence_targets = BertForTokenClassification.from_pretrained("RecordedFuture/Swedish-Sentiment-Violence-Targets") 

When the model and tokenizer are initialized the model can be used for inference. 

#### Verification metrics 
During training the Violence target model had the following verification metrics when using "any overlap" as the evaluation metric.  

| F-score | Precision | Recall |
|:-------------------------:|:-------:|:---------:|:------:|
|  0.7831|   0.9155|  0.8442 |
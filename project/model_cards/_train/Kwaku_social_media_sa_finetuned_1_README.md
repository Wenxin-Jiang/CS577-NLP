---
language: eng
datasets:
- banking77
---

# Social Media Sentiment Analysis Model (Finetuned)
This is a fine-tuned version of the [Social Media Sentiment Analysis Model](https://huggingface.co/Kwaku/social_media_sa) which is a finetuned version of [Distilbert](https://huggingface.co/models?other=distilbert). It's best suited for sentiment-analysis.

## Model Description
Social Media Sentiment Analysis Model was trained on the [dataset consisting of tweets](https://www.kaggle.com/code/mohamednabill7/sentiment-analysis-of-twitter-data/data) obtained from Kaggle."

## Intended Uses and Limitations
This model is meant for sentiment-analysis. Because it was trained on a corpus of tweets, it is familiar with social media jargons.

### How to use

You can use this model directly with a pipeline for text generation:

```python
>>>from transformers import pipeline

>>> model_name = "Kwaku/social_media_sa_finetuned_1"
>>> generator = pipeline("sentiment-analysis", model=model_name)
>>> result = generator("I like this model")
>>> print(result)

Generated output: [{'label': 'positive', 'score': 0.9494990110397339}]
```

### Limitations and bias

This model inherits the bias of its parent, [Distilbert](https://huggingface.co/models?other=distilbert).
Besides that, it was trained on only 1000 randomly selected sequences, and thus does not achieve a high probability rate.
It does fairly well nonetheless.
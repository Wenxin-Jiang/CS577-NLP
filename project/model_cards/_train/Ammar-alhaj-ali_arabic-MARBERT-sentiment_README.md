---
language:
- ar
widget:
- text: "لقد كان الاحتفال رائع"
- text: "هناك بعض القوانين التي يجب تغيرها"
- text: "الخدمة كانت سيئة"
tags:
- text classification
- Sentiment
---
## Arabic-MARBERT-Sentiment Model
#### Model description
**Arabic-MARBERT-Sentiment Model** is a Sentiment analysis model that was built by fine-tuning the [MARBERT](https://huggingface.co/UBC-NLP/MARBERT) model. For the fine-tuning, I used [KAUST dataset](https://www.kaggle.com/competitions/arabic-sentiment-analysis-2021-kaust), which includes 3 labels(positive,negative,and neutral).


#### How to use
To use the model with a transformers pipeline:
```python
>>>from transformers import pipeline
>>>model = pipeline('text-classification', model='Ammar-alhaj-ali/arabic-MARBERT-sentiment')
>>>sentences = ['لقد استمتعت بالحفلة', 'خدمة المطعم كانت محبطة']
>>>model(sentences)
[{'label': 'positive', 'score': 0.9577557444572449},
{'label': 'negative', 'score': 0.9158180952072144}]
 

---
language:
- ar
widget:
- text: "ما شفت هدا العنوان هون"
- text: "مبقدرش احافظ علي المستوى الدراسي بتاعي"
- text: "منين تطلع بهاي السوالف كل يوم"
tags:
- text classification
---
## Arabic-MARBERT-dialect-Identification-City Model
#### Model description
**arabic-MARBERT-dialect-identification-city Model** is a dialect identification model that was built by fine-tuning the [MARBERT](https://huggingface.co/UBC-NLP/MARBERT) model. For the fine-tuning, I used [MADAR Corpus 26 dataset](https://camel.abudhabi.nyu.edu/madar-shared-task-2019/), which includes 26 labels(cities).

#### How to use
To use the model with a transformers pipeline:
```python
>>>from transformers import pipeline
>>>model = pipeline('text-classification', model='Ammar-alhaj-ali/arabic-MARBERT-dialect-identification-city')
>>>sentences = ['ناطرين البرنامج', 'اكلنا هوا بهل شروة']
>>>model(sentences)
[{'label': 'Beirut', 'score': 0.9731963276863098},
{'label': 'Aleppo', 'score': 0.4592577815055847}]
 

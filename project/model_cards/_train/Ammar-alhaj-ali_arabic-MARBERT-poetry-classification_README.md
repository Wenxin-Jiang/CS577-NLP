---
language:
- ar
widget:
- text: "قِفَا نَبْكِ مِنْ ذِكْرَى حَبِيبٍ ومَنْزِلِ [sep]بِسِقْطِ اللِّوَى بَيْنَ الدَّخُولِ فَحَوْمَلِ"
- text: "ليس الغريب غريب الشام واليمنُ[sep]إن الغريب غريب اللحد والكفن"
- text: "عَلى قَدْرِ أهْلِ العَزْم تأتي العَزائِمُ[sep] وَتأتي علَى قَدْرِ الكِرامِ المَكارمُ"
- text: "قم للمعلم وفّه التبجيلا[sep] كاد المعلم أن يكون رسولا"
tags:
- text classification
- arabic
- poetry
---
## Arabic MARBERT Poetry Classification Model
#### Model description
**arabic-MARBERT-poetry-classification Model** is a poetry classification model that was built by fine-tuning the [MARBERT](https://huggingface.co/UBC-NLP/MARBERT) model. For the fine-tuning, I used [APCD: Arabic Poem Comprehensive Dataset](https://hci-lab.github.io/ArabicPoetry-1-Private/) that includes 23 labels (البسيط,الطويل,الكامل,الوافر,الخفيف,السريع,..).

#### How to use
To use the model with a transformers pipeline:
```python
>>>from transformers import pipeline
>>>model = pipeline('text-classification', model='Ammar-alhaj-ali/arabic-MARBERT-poetry-classification')
>>>sentences = ['ويوم نلتقي فيه قصير[sep]يطول اليوم لا ألقاك فيه',
             'أما للهوى عليك نهي ولا أمر[sep]أراك عصيّ الدمع شيمتك الصبر']
>>>model(sentences)
[{'label': 'الوافر', 'score': 0.9979557991027832},
 {'label': 'الطويل', 'score': 0.9646275043487549}]
```
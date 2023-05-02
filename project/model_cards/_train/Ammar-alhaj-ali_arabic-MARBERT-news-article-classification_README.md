---
language:
- ar
widget:
- text: "أخطرت شركة أرامكو السعودية 4 على الأقل من المشترين في شمال آسيا بأنها ستورد إليهم الكميات المتعاقد عليها من النفط الخام كاملة في سبتمبرأيلول المقبل. وقالت مصادر مطلعة لرويترز إن السعودية، أكبر مصدر النفط في العالم، كانت قد رفعت سعر البيع الرسمي للمشترين الآسيويين إلى مستويات قياسية لذلك الشهر."
- text: "يرى المحلل العسكري والإستراتيجي اعياد الطوفان أن أحد أسباب الحرب الروسية الأوكرانية هو أن الولايات المتحدة تريد أن تقاتل كما يقال حتى آخر جندي أوكراني بمعنى أن واشنطن تسعى لاستنزاف الروس وكشف أسلحتهم السرية والإستراتيجية من دون أن تتحمل أي خسائر على الأرض."
tags:
- text classification
- news
---
## Arabic MARBERT News Article Classification Model
#### Model description
**arabic-MARBERT-news-article-classification Model** is a news article classification model that was built by fine-tuning the [MARBERT](https://huggingface.co/UBC-NLP/MARBERT) model. For the fine-tuning, I used [SANAD: Single-Label Arabic News Articles Dataset](https://data.mendeley.com/datasets/57zpx667y9) that includes 7 labels(Culture,Finance,Medical,Politics,Religion,Sports,and Tech).

#### How to use
To use the model with a transformers pipeline:
```python
>>>from transformers import pipeline
>>>model = pipeline('text-classification', model='Ammar-alhaj-ali/arabic-MARBERT-news-article-classification')
>>>sentences = ['أخطرت شركة أرامكو السعودية 4 على الأقل من المشترين في شمال آسيا بأنها ستورد إليهم الكميات المتعاقد عليها من النفط الخام كاملة في سبتمبرأيلول المقبل. وقالت مصادر مطلعة لرويترز إن السعودية، أكبر مصدر النفط في العالم، كانت قد رفعت سعر البيع الرسمي للمشترين الآسيويين إلى مستويات قياسية لذلك الشهر.']
>>>model(sentences)
[{'label': 'Finance', 'score': 0.9998553991317749}]
```
---
tags:
- ner
- token-classification
- berturk
- turkish
language: tr
datasets:
- MilliyetNER
widget:
- text: "Türkiye'nin başkenti Ankara'dır ve ilk cumhurbaşkanı Mustafa Kemal Atatürk'tür."
---

# DATASET
MilliyetNER dataset was collected from the Turkish Milliyet newspaper articles between 1997-1998. This dataset is presented by [Tür et al. (2003)](https://www.cambridge.org/core/journals/natural-language-engineering/article/abs/statistical-information-extraction-system-for-turkish/7C288FAFC71D5F0763C1F8CE66464017). It was collected from news articles and manually annotated with three different entity types: Person, Location, Organization. The authors did not provide training/validation/test splits for this dataset. Dataset splits used by [Yeniterzi et al. 2011](https://aclanthology.org/P11-3019).        
For more information: [tdd.ai - MilliyetNER](https://data.tdd.ai/#/effafb5f-ebfc-4e5c-9a63-4f709ec1a135)    
**Model is only trained using training set. Test set not included during the last training**.      

# USAGE
```python
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
model = AutoModelForTokenClassification.from_pretrained("alierenak/berturk-cased-ner")
tokenizer = AutoTokenizer.from_pretrained("alierenak/berturk-cased-ner")
ner_pipeline = pipeline('ner', model=model, tokenizer=tokenizer)
ner_pipeline("Türkiye'nin başkenti Ankara, ilk cumhurbaşkanı Mustafa Kemal Atatürk'tür.")
```

# RESULT
```bash
[{'entity': 'B-LOCATION',
  'score': 0.9966415,
  'index': 1,
  'word': 'Türkiye',
  'start': 0,
  'end': 7},
 {'entity': 'B-LOCATION',
  'score': 0.99456763,
  'index': 5,
  'word': 'Ankara',
  'start': 21,
  'end': 27},
 {'entity': 'B-PERSON',
  'score': 0.9958741,
  'index': 9,
  'word': 'Mustafa',
  'start': 47,
  'end': 54},
 {'entity': 'I-PERSON',
  'score': 0.98833394,
  'index': 10,
  'word': 'Kemal',
  'start': 55,
  'end': 60},
 {'entity': 'I-PERSON',
  'score': 0.9837286,
  'index': 11,
  'word': 'Atatürk',
  'start': 61,
  'end': 68}]
```

# BENCHMARKING
```bash
precision    recall  f1-score   support

    LOCATION       0.97      0.96      0.97       960
ORGANIZATION       0.95      0.92      0.94       863
      PERSON       0.97      0.97      0.97      1410

   micro avg       0.97      0.95      0.96      3233
   macro avg       0.96      0.95      0.96      3233
weighted avg       0.97      0.95      0.96      3233
```
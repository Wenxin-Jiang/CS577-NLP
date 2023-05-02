---
language:
- en
tags:
- text-classification

widget:
- text: "Please add a like button!"
  example_title: "Likely feature request"
- text: "The app crashed when I opened it this morning. Can you fix this please?"
  example_title: "Unlikely feature request"
---

How to use this classifier:

```
from transformers import pipeline

pipe = pipeline("text-classification", model="Peterard/distilbert_feature_classifier")

pipe("Please add a like button!")
# [{'label': 'feature_request', 'score': 0.8930749893188477}]

pipe("The app crashed when I opened it this morning. Can you fix this please?")
#[{'label': 'no_feature_request', 'score': 0.9971746206283569}]
```

N.B. The label will change depending on which is the likelier class
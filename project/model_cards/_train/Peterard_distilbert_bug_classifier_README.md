---
language:
- en
tags:
- text-classification

widget:
- text: "The app crashed when I opened it this morning. Can you fix this please?"
  example_title: "Likely bug report"
- text: "Please add a like button!"
  example_title: "Unlikely bug report"
---

How to use this classifier:

```
from transformers import pipeline

pipe = pipeline("text-classification", model="Peterard/distilbert_bug_classifier")

pipe("The app crashed when I opened it this morning. Can you fix this please?")
# [{'label': 'bug', 'score': 0.9042391180992126}]

pipe("Please add a like button!")
# [{'label': 'no_bug', 'score': 0.9977496266365051}]

```

N.B. The label will change depending on which is the likelier class
---
language: "id"
widget:
- text: "dia orang yang baik ya bunds."
---

## how to use

```python
from transformers import pipeline, set_seed

path = "akahana/indonesia-sentiment-roberta"
emotion = pipeline('text-classification', 
                     model=path,device=0)
set_seed(42)

kalimat = "dia orang yang baik ya bunds."
preds = emotion(kalimat)
preds
```
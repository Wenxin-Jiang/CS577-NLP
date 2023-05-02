---
thumbnail: https://huggingface.co/front/thumbnails/google.png
license: apache-2.0
---

# Question Answering model for Hindi and Tamil

This model is part of the ensemble that ranked 4/943 in the [Hindi and Tamil Question Answering](https://www.kaggle.com/c/chaii-hindi-and-tamil-question-answering) competition held by Google Research India at Kaggle.
```
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
  
tokenizer = AutoTokenizer.from_pretrained("Yuchen/muril-large-cased-hita-qa")

model = AutoModelForQuestionAnswering.from_pretrained("Yuchen/muril-large-cased-hita-qa")
```
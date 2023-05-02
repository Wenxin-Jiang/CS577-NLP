---
language:
- es
pipeline_tag: text-classification
---
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("MMG/xlm-roberta-base-sa-spanish")

model = AutoModelForSequenceClassification.from_pretrained("MMG/xlm-roberta-base-sa-spanish")

pipe = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

pipe(["Este bar es horrible", "Este bar es buenísimo"]))

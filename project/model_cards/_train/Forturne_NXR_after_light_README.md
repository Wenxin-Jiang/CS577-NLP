## How to use


```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

model = AutoModelForSequenceClassification.from_pretrained("Forturne/NXR_after_light")
tokenizer = AutoTokenizer.from_pretrained("Forturne/NXR_after_light")

pipe = pipeline(model=model, tokenizer=tokenizer)
pipe("환자분 성함이 어떻게 되세요?")
```
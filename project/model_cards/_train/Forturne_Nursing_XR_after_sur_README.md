## How to use


```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

model = AutoModelForSequenceClassification.from_pretrained("Forturne/Nursing_XR_after_sur")
tokenizer = AutoTokenizer.from_pretrained("Forturne/Nursing_XR_after_sur")

pipe = pipeline('text-classification', model=model, tokenizer=tokenizer)
pipe("환자분 성함이 어떻게 되세요?")
```
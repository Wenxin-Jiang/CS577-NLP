---
language:
- vi
- vn
- en
- multilingual
tags:
- question-answering
- pytorch
datasets:
- squad
metrics:
- squad
pipeline_tag: question-answering
widget:
- text: what is the capital of Vietnam ?
  context: Keeping an ageless charm through centuries, Hanoi - the capital of Vietnam
    is famous not only for the Old Quarter with narrow and crowded streets but also
    for the nostalgic feeling that it brings. While Saigon is a young and modern city,
    the ancient Hanoi is still a true beholder of history.
---

  
```python
from transformers import pipeline
model_checkpoint = "aicryptogroup/distill-xlm-mrc"
nlp = pipeline('question-answering', model=model_checkpoint,
                   tokenizer=model_checkpoint)
QA_input = {
  'question': "what is the capital of Vietnam",
  'context': "Keeping an ageless charm through centuries, Hanoi - the capital of Vietnam is famous not only for the Old Quarter with narrow and crowded streets but also for the nostalgic feeling that it brings. While Saigon is a young and modern city, the ancient Hanoi is still a true beholder of history."
}
res = nlp(QA_input)
print('pipeline: {}'.format(res))


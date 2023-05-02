---
license: mit
pipeline_tag: question-answering
widget:
    - context: "Пушкин родился 6 июля 1799 года"
    - text: "Когда родился Пушкин?"
      example_title: "test"
---
обученный rubert от cointegrated/rubert-tiny2.

размер выборки - 4.

Эпохи - 16.

```python
from transformers import pipeline
qa_pipeline = pipeline(
    "question-answering",
    model="Den4ikAI/rubert-tiny-squad",
    tokenizer="Den4ikAI/rubert-tiny-squad"
)
predictions = qa_pipeline({
    'context': "Пушкин родился 6 июля 1799 года",
    'question': "Когда родился Пушкин?"
})
print(predictions)
# output:
#{'score': 0.9413797664642334, 'start': 15, 'end': 31, 'answer': '6 июля 1799 года'}
```
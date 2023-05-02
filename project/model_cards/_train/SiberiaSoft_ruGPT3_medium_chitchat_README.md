---
license: mit
widget:
  - text: '[FIRST] В чем смысл жизни? [SECOND]'
    example_title: first_example
  - text: '[FIRST] Как твои дела? [SECOND]'
    example_title: second_example
pipeline_tag: text-generation
language:
- ru

---
Модель русскозычного чат бота, работающая в режиме чит-чат (без контекста предыдущих сообщений)

Пример работы с моделью:
```python
import torch
from transformers import AutoTokenizer, AutoModelWithLMHead
tokenizer = AutoTokenizer.from_pretrained('SiberiaSoft/ruGPT3_medium_chitchat')
model = AutoModelWithLMHead.from_pretrained('SiberiaSoft/ruGPT3_medium_chitchat')
inputs = tokenizer('[FIRST] Привет [SECOND]', return_tensors='pt')
generated_token_ids = model.generate(
    **inputs,
    top_k=10,
    top_p=0.95,
    num_beams=3,
    num_return_sequences=5,
    do_sample=True,
    no_repeat_ngram_size=2,
    temperature=1.0,
    repetition_penalty=1.2,
    length_penalty=1.0,
    eos_token_id=50257,
    max_length = 400
)
generation = [tokenizer.decode(sample_token_ids) for sample_token_ids in generated_token_ids]
print(generation)
```

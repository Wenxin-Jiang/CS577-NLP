---
language:
- ru
license: mit
datasets: Den4ikAI/fact_detection
widget:
- если вы хотите процитировать поэму или часть из нее, тогда вам следует придерживаться
  первоначального формата строк, чтобы передать первоначальный смысл
- ' резко вдавленный газ и знакомый свист шин унес машину прочь, превратив ее в маленькую
  постепенно движущуюся точку'
---

Модель rubert-base-cased от Deeppavlov. Обучена на датасете из предложений. В качестве фактов использовались предложения из Википедии, а в качестве негативных - худлит и новости

Датасет: [Den4ikAI/fact_detection](https://huggingface.co/datasets/Den4ikAI/fact_detection)

Простейший код инференса:

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

txt = 'Пулмен — бывший рабочий посёлок вагоностроительной компании «Пульман», построенный в 1880-е годы к югу от Чикаго.'
tokenizer = AutoTokenizer.from_pretrained('Den4ikAI/ruBert_base_fact_detection')
model = AutoModelForSequenceClassification.from_pretrained('Den4ikAI/ruBert_base_fact_detection')
inputs = tokenizer(txt, max_length=128, add_special_tokens=False, return_tensors='pt')
with torch.inference_mode():
    logits = model(**inputs).logits
    probas = torch.sigmoid(logits)[0].cpu().detach().numpy()
is_fact, no_fact = probas
print(f'[TEXT] --> {txt}')
print(f'[IS_FACT] --> {is_fact}')
print(f'[NO_FACT] --> {no_fact}')
```


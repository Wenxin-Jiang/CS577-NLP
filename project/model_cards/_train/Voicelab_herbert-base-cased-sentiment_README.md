---
pipeline_tag: text-classification
widget:
- text: "Pani Katarzyno z jakiej racji moja paczka przyszła do sąsiada zamiast do mnie? Nie można poprawnie nadać paczki?"
  example_title: "Sentiment"
license: cc-by-4.0
language: 
- pl
---

<img src="https://public.3.basecamp.com/p/rs5XqmAuF1iEuW6U7nMHcZeY/upload/download/VL-NLP-short.png" alt="logo voicelab nlp" style="width:300px;"/>

# Sentiment Classification in Polish

```python
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification

id2label = {0: "negative", 1: "neutral", 2: "positive"}
tokenizer = AutoTokenizer.from_pretrained("Voicelab/herbert-base-cased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("Voicelab/herbert-base-cased-sentiment")

input = ["Ale fajnie, spadł dzisiaj śnieg! Ulepimy dziś bałwana?"]

encoding = tokenizer(
          input,
          add_special_tokens=True,
          return_token_type_ids=True,
          truncation=True,
          padding='max_length',
          return_attention_mask=True,
          return_tensors='pt',
        )
output = model(**encoding).logits.to("cpu").detach().numpy()
prediction = id2label[np.argmax(output)]
print(input, "--->", prediction)

```

Predicted output:
```python
['Ale fajnie, spadł dzisiaj śnieg! Ulepimy dziś bałwana?'] ---> positive
```

### Overview
- **Language model:** [allegro/herbert-base-cased](https://huggingface.co/allegro/herbert-base-cased)   
- **Language:** pl
- **Training data:** Reviews + own data
- **Blog post:** [Sentiment analysis - COVID-19 – the source of the heated discussion](https://voicelab.ai/covid-19-the-source-of-the-heated-discussion)


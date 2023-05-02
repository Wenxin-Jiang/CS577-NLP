---
language: "en"
tags:
- financial-text-analysis
- forward-looking-statement
widget:
- text: "We expect the age of our fleet to enhance availability and reliability due to reduced downtime for repairs. "
---

Forward-looking statements (FLS) inform investors of managers’ beliefs and opinions about firm's future events or results. Identifying forward-looking statements from corporate reports can assist investors in financial analysis. FinBERT-FLS is a FinBERT model fine-tuned on 3,500 manually annotated sentences from Management Discussion and Analysis section of annual reports of Russell 3000 firms.  

**Input**: A financial text.

**Output**: Specific-FLS , Non-specific FLS, or Not-FLS.

# How to use 
You can use this model with Transformers pipeline for forward-looking statement classification.
```python
# tested in transformers==4.18.0 
from transformers import BertTokenizer, BertForSequenceClassification, pipeline

finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-fls',num_labels=3)
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-fls')
nlp = pipeline("text-classification", model=finbert, tokenizer=tokenizer)
results = nlp('We expect the age of our fleet to enhance availability and reliability due to reduced downtime for repairs.')
print(results)  # [{'label': 'Specific FLS', 'score': 0.77278733253479}]

```

Visit [FinBERT.AI](https://finbert.ai/) for more details on the recent development of FinBERT.
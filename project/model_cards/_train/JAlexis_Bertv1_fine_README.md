---
language: en
tags:
- pytorch
- question-answering
datasets:
- squad2
- cord19
metrics:
- f1

widget:
- text: "How can I protect myself against covid-19?"
  context: "Preventative measures consist of recommendations to wear a mask in public, maintain social distancing of at least six feet, wash hands regularly, and use hand sanitizer. To facilitate this aim, we adapt the conceptual model and measures of Liao et al. [6] to the current context of the COVID-19 pandemic and the culture of the USA. Applying this model in a different time and context provides an opportunity to make comparisons of reactions to information sources across a decade of evolving attitudes toward media and government, between two cultures (Hong Kong vs. the USA), and between two considerably different global pandemics (H1N1 vs. COVID-19)."
- text: "How can I protect myself against covid-19?"
  context: " "
  
---

## Model description 
This model was obtained by fine-tuning deepset/bert-base-cased-squad2 on Cord19 Dataset.

## How to use

```python
from transformers.pipelines import pipeline
model_name = "JAlexis/PruebaBert"
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
inputs = {
    'question': 'How can I protect myself against covid-19?',
    'context': 'Preventative measures consist of recommendations to wear a mask in public, maintain social distancing of at least six feet, wash hands regularly, and use hand sanitizer. To facilitate this aim, we adapt the conceptual model and measures of Liao et al. [6] to the current context of the COVID-19 pandemic and the culture of the USA. Applying this model in a different time and context provides an opportunity to make comparisons of reactions to information sources across a decade of evolving attitudes toward media and government, between two cultures (Hong Kong vs. the USA), and between two considerably different global pandemics (H1N1 vs. COVID-19). ',
    'question': 'How can I protect myself against covid-19?',
    'context': ' ',
}
nlp(inputs)
```

## Overview
```
Language model: deepset/bert-base-cased-squad2
Language: English
Downstream-task: Q&A
Datasets: CORD-19 from 31rd January 2022
Code: Haystack and FARM
Infrastructure: Tesla T4
```

## Hyperparameters
```
batch_size = 8
n_epochs = 7
max_seq_len = max_length
learning_rate = AdamW: 2e-5
```
 
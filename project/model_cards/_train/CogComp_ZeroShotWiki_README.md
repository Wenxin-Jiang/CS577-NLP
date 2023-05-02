---
license: apache-2.0
---

# Model description

A BertForSequenceClassification model that is finetuned on Wikipedia for zero-shot text classification. For details, see our NAACL'22 paper. 


# Usage

Concatenate the text sentence with each of the candidate labels as input to the model. The model will output a score for each label. Below is an example.

```
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("CogComp/ZeroShotWiki")
model = AutoModelForSequenceClassification.from_pretrained("CogComp/ZeroShotWiki")

labels = ["sports", "business", "politics"]
texts = ["As of the 2018 FIFA World Cup, twenty-one final tournaments have been held and a total of 79 national teams have competed."]

with torch.no_grad():
    for text in texts:
        label_score = {}
        for label in labels:
            inputs = tokenizer(text, label, return_tensors='pt')
            out = model(**inputs)
            label_score[label]=float(torch.nn.functional.softmax(out[0], dim=-1)[0][0])
        print(label_score)  # Predict the label with the highest score
```
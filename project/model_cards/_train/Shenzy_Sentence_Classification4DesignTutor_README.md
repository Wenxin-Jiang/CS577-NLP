---
tags: autotrain
language: en
widget:
- text: "An unusual hierarchy in the section near the top where the design seems to prioritise running time over a compacted artist name."
datasets:
- Shenzy/autotrain-data-sentence_classification
co2_eq_emissions: 0.00986494387043499
---

## Validation Metrics

- Loss: 0.6447726488113403
- Accuracy: 0.8263473053892215
- Macro F1: 0.7776555055392036
- Micro F1: 0.8263473053892215
- Weighted F1: 0.8161511591973788
- Macro Precision: 0.8273504273504274
- Micro Precision: 0.8263473053892215
- Weighted Precision: 0.8266697374481806
- Macro Recall: 0.7615518744551003
- Micro Recall: 0.8263473053892215
- Weighted Recall: 0.8263473053892215


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "An unusual hierarchy in the section near the top where the design seems to prioritise running time over a compacted artist name."}' https://api-inference.huggingface.co/models/Shenzy/Sentence_Classification4DesignTutor
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

import numpy as np

labdic ={ 0: "rationale", 1: "suggestion", 2: "specific_critique"}

model = AutoModelForSequenceClassification.from_pretrained("Shenzy/Sentence_Classification4DesignTutor")

tokenizer = AutoTokenizer.from_pretrained("Shenzy/Sentence_Classification4DesignTutor")

inputs = tokenizer("An unusual hierarchy in the section near the top where the design seems to prioritise running time over a compacted artist name.", return_tensors="pt")

outputs = model(**inputs)

print(labdic[np.argmax(outputs)])
```
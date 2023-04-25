---
tags:
- sentence-transformers
- feature-extraction
---

# TODO: Name of Model

TODO: Description

## Model Description
TODO: Add relevant content

(0) Base Transformer Type: DistilBertModel

(1) Pooling mean

(2) Dense 768x512


## Usage (Sentence-Transformers)

Using this model becomes more convenient when you have [sentence-transformers](https://github.com/UKPLab/sentence-transformers) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence"]

model = SentenceTransformer(TODO)
embeddings = model.encode(sentences)
print(embeddings)
```

## TODO: Training Procedure

## TODO: Evaluation Results

## TODO: Citing & Authors

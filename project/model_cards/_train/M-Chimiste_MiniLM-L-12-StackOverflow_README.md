---
license: apache-2.0
---
# Cross-Encoder for MS Marco

This model is a generic masked language model fine tuned on stack overflow data.  It's base pre-trained model was the cross-encoder/ms-marco-MiniLM-L-12-v2 model.

The model can be used for creating vectors for search applications.  It was trained to be used in conjunction with a knn search with OpenSearch for a pet project I've been working on.  It's easiest to create document embeddings with the flair package as shown below.


## Usage with Transformers

```python
from flair.data import Sentence
from flair.embeddings import TransformerDocumentEmbeddings

sentence = Sentence("Text to be embedded.")
model = TransformerDocumentEmbeddings("model-name")
model.embed(sentence)
embeddings = sentence.embedding
```

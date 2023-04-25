---
pipeline_tag: sentence-similarity
language: english
tags:
- sentence-transformers
- sentence-similarity
- transformers
---
# recobo/agri-sentence-transformer

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 512 dimensional dense vector space and can be used for tasks like clustering or semantic search.
This model was built using [recobo/agriculture-bert-uncased](https://huggingface.co/recobo/agriculture-bert-uncased), which is a BERT model trained on 6.5 million passages from the agricultural domain. Hence, this model is expected to perform well on sentence similarity tasks specifically for agricultural text data.
## Usage (Sentence-Transformers)
Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:
```
pip install -U sentence-transformers
```
Then you can use the model like this:
```python
from sentence_transformers import SentenceTransformer
sentences = ["A man is eating food.", "A man is eating a piece of bread"]

model = SentenceTransformer('recobo/agri-sentence-transformer')
embeddings = model.encode(sentences)
print(embeddings)

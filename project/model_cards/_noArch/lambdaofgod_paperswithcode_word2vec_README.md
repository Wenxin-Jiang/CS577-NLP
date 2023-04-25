---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
---

# lambdaofgod/paperswithcode_word2vec

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 200 dimensional dense vector space and can be used for tasks like clustering or semantic search.

## Training

This model was trained on PapersWithCode dataset on abstracts and READMEs using gensim.

<!--- Describe your model here -->

## Usage (Sentence-Transformers)


```python
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('lambdaofgod/paperswithcode_word2vec')
embeddings = model.encode(sentences)
print(embeddings)
```


## Full Model Architecture
```
SentenceTransformer(
  (0): WordEmbeddings(
    (emb_layer): Embedding(147043, 200)
  )
  (1): Pooling({'word_embedding_dimension': 200, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->
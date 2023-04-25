---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity

---

# lambdaofgod/query-dependencies-nbow-nbow-mnrl

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 200 dimensional dense vector space and can be used for tasks like clustering or semantic search.

<!--- Describe your model here -->

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('lambdaofgod/query-dependencies-nbow-nbow-mnrl')
embeddings = model.encode(sentences)
print(embeddings)
```



## Evaluation Results

<!--- Describe how your model was evaluated -->

For an automated evaluation of this model, see the *Sentence Embeddings Benchmark*: [https://seb.sbert.net](https://seb.sbert.net?model_name=lambdaofgod/query-dependencies-nbow-nbow-mnrl)



## Full Model Architecture
```
SentenceTransformer(
  (0): WordEmbeddings(
    (emb_layer): Embedding(4395, 200)
  )
  (1): WordWeights(
    (emb_layer): Embedding(4395, 1)
  )
  (2): Pooling({'word_embedding_dimension': 200, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->
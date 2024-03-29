---
pipeline_tag: sentence-similarity
license: apache-2.0
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
---

# average_word_embeddings_glove.6B.300d

**This model is a copy of [this model repository](https://huggingface.co/sentence-transformers/average_word_embeddings_glove.6B.300d) from sentence-transformers at the specific commit `5d2b7d1c127036ae98b9d487eca4d48744edc709`.**

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 300 dimensional dense vector space and can be used for tasks like clustering or semantic search.



## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/average_word_embeddings_glove.6B.300d')
embeddings = model.encode(sentences)
print(embeddings)
```



## Evaluation Results



For an automated evaluation of this model, see the *Sentence Embeddings Benchmark*: [https://seb.sbert.net](https://seb.sbert.net?model_name=sentence-transformers/average_word_embeddings_glove.6B.300d)



## Full Model Architecture
```
SentenceTransformer(
  (0): WordEmbeddings(
    (emb_layer): Embedding(400001, 300)
  )
  (1): Pooling({'word_embedding_dimension': 300, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

This model was trained by [sentence-transformers](https://www.sbert.net/). 
        
If you find this model helpful, feel free to cite our publication [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084):
```bibtex 
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "http://arxiv.org/abs/1908.10084",
}
```
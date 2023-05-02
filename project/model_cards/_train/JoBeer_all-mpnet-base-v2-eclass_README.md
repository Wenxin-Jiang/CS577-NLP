---
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
datasets: JoBeer/eclassTrainST
pipeline_tag: sentence-similarity
---

# all-mpnet-base-v2-eclass

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search.

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

model = SentenceTransformer('JoBeer/all-mpnet-base-v2-eclass')
embeddings = model.encode(sentences)
print(embeddings)
```



## Evaluation Results

<!--- Describe how your model was evaluated -->

For an automated evaluation of this model, see the *Sentence Embeddings Benchmark*: [https://seb.sbert.net](https://seb.sbert.net?model_name={MODEL_NAME})


## Training
The Model was trained with the eclass-dataset (https://huggingface.co/datasets/JoBeer/eclassTrainST). 


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 384, 'do_lower_case': False}) with Transformer model: MPNetModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
  (2): Normalize()
)
```

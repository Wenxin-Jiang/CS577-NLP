---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
datasets:
- code_search_net
---

# flax-sentence-embeddings/st-codesearch-distilroberta-base

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search.

It was trained on the [code_search_net](https://huggingface.co/datasets/code_search_net) dataset and can be used to search program code given text.

## Usage:

```python
from sentence_transformers import SentenceTransformer, util


#This list the defines the different programm codes
code = ["""def sort_list(x):
   return sorted(x)""",
"""def count_above_threshold(elements, threshold=0):
    counter = 0
    for e in elements:
        if e > threshold:
            counter += 1
    return counter""",
"""def find_min_max(elements):
    min_ele = 99999
    max_ele = -99999
    for e in elements:
        if e < min_ele:
            min_ele = e
        if e > max_ele:
            max_ele = e
    return min_ele, max_ele"""]
    

model = SentenceTransformer("flax-sentence-embeddings/st-codesearch-distilroberta-base")

# Encode our code into the vector space
code_emb = model.encode(code, convert_to_tensor=True)

# Interactive demo: Enter queries, and the method returns the best function from the 
# 3 functions we defined
while True:
    query = input("Query: ")
    query_emb = model.encode(query, convert_to_tensor=True)
    hits = util.semantic_search(query_emb, code_emb)[0]
    top_hit = hits[0]

    print("Cossim: {:.2f}".format(top_hit['score']))
    print(code[top_hit['corpus_id']])
    print("\n\n")
```

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('flax-sentence-embeddings/st-codesearch-distilroberta-base')
embeddings = model.encode(sentences)
print(embeddings)
```


## Training

The model was trained with a DistilRoBERTa-base model for 10k training steps on the codesearch dataset with batch_size 256 and MultipleNegativesRankingLoss. 

It is some preliminary model. It was neither tested nor was the trained quite sophisticated 


The model was trained with the parameters:

**DataLoader**:

`MultiDatasetDataLoader.MultiDatasetDataLoader` of length 5371 with parameters:
```
{'batch_size': 256}
```

**Loss**:

`sentence_transformers.losses.MultipleNegativesRankingLoss.MultipleNegativesRankingLoss` with parameters:
  ```
  {'scale': 20, 'similarity_fct': 'dot_score'}
  ```

Parameters of the fit()-Method:
```
{
    "callback": null,
    "epochs": 1,
    "evaluation_steps": 0,
    "evaluator": "NoneType",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'transformers.optimization.AdamW'>",
    "optimizer_params": {
        "lr": 2e-05
    },
    "scheduler": "warmupconstant",
    "steps_per_epoch": 10000,
    "warmup_steps": 500,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False}) with Transformer model: RobertaModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
  (2): Normalize()
)
```

## Citing & Authors

<!--- Describe where people can find more information -->
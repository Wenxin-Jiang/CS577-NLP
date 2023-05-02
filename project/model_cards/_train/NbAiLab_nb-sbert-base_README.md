---
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
datasets: NbAiLab/mnli-norwegian
pipeline_tag: sentence-similarity
widget:
- source_sentence: This is a Norwegian boy
  sentences:
  - Dette er en norsk gutt
  - This is an English boy
  - This is a dog
  example_title: Cross Language
- source_sentence: Det er noen dyr utenfor vinduet
  sentences:
  - På utsiden kan jeg høre noen hunder
  - Noen mennesker prater utenfor vinduet
  - Alle burde ha kjæledyr
  example_title: Paraphrases
- source_sentence: En kvinne sitter i en stol
  sentences:
  - A woman is sitting in a chair
  - Hun slapper av og leser i en bok
  - Hun løper maraton
  example_title: Paraphrases across language
---

# NB-SBERT-BASE
NB-SBERT-BASE is a [SentenceTransformers](https://www.SBERT.net) model trained on a [machine translated version of the MNLI dataset](https://huggingface.co/datasets/NbAiLab/mnli-norwegian), starting from [nb-bert-base](https://huggingface.co/NbAiLab/nb-bert-base). 

The model maps sentences & paragraphs to a 768 dimensional dense vector space. This vector can be used for tasks like clustering and semantic search. Below we give some examples on how to use the model. The easiest way is to simply measure the cosine distance between two sentences. Sentences that are close to each other in meaning, will have a small cosine distance and a similarity close to 1. The model is trained in such a way that similar sentences in different languages should also be close to each other. Ideally, an English-Norwegian sentence pair should have high similarity.

## Embeddings and Sentence Similarity (Sentence-Transformers)

As seen above, using the library [sentence-transformers](https://www.SBERT.net) makes the use of these models quite convenient:

```bash
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer, util
sentences = ["This is a Norwegian boy", "Dette er en norsk gutt"]

model = SentenceTransformer('NbAiLab/nb-sbert-base')
embeddings = model.encode(sentences)
print(embeddings)

# Compute cosine-similarities with sentence transformers
cosine_scores = util.cos_sim(embeddings[0],embeddings[1])
print(cosine_scores)

# Compute cosine-similarities with SciPy
from scipy import spatial
scipy_cosine_scores = 1 - spatial.distance.cosine(embeddings[0],embeddings[1])
print(scipy_cosine_scores)

# Both should give 0.8250 in the example above.

```


## Embeddings and Sentence Similarity (HuggingFace Transformers)
Without [sentence-transformers](https://www.SBERT.net), you can still use the model. First, you pass in your input through the transformer model, then you have to apply the right pooling-operation on top of the contextualized word embeddings.

```python
from transformers import AutoTokenizer, AutoModel
import torch


#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
sentences = ["This is a Norwegian boy", "Dette er en norsk gutt"]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('NbAiLab/nb-sbert-base')
model = AutoModel.from_pretrained('NbAiLab/nb-sbert-base')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, mean pooling.
embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

print(embeddings)

# Compute cosine-similarities with SciPy
from scipy import spatial
scipy_cosine_scores = 1 - spatial.distance.cosine(embeddings[0],embeddings[1])
print(scipy_cosine_scores)

# This should give 0.8250 in the example above.

```
## SetFit - Few Shot Classification
[SetFit](https://github.com/huggingface/setfit) is a method for using sentence-transformers to solve one of major problem that all NLP researchers are facing: Too few labeled training examples. The 'nb-sbert-base' can be plugged directly into the SetFit library. Please see [this tutorial](https://huggingface.co/blog/setfit) for how to use this technique.


## Keyword Extraction
The model can be used for extracting keywords from text. The basic technique is to find the words that are most similar to the document. There are various frameworks for doing this. An easy way is to use [KeyBERT](https://github.com/MaartenGr/KeyBERT). This example shows how this can be done.

```bash
pip install keybert
```

```python
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer
sentence_model = SentenceTransformer("NbAiLab/nb-sbert-base")
kw_model = KeyBERT(model=sentence_model)

doc = """
De første nasjonale bibliotek har sin opprinnelse i kongelige samlinger eller en annen framstående myndighet eller statsoverhode. 
Et av de første planene for et nasjonalbibliotek i England ble fremmet av den walisiske matematikeren og mystikeren John Dee som 
i 1556 presenterte en visjonær plan om et nasjonalt bibliotek for gamle bøker, manuskripter og opptegnelser for dronning Maria I 
av England. Hans forslag ble ikke tatt til følge.
"""
kw_model.extract_keywords(doc, stop_words=None)

# [('nasjonalbibliotek', 0.5242), ('bibliotek', 0.4342), ('samlinger', 0.3334), ('statsoverhode', 0.33), ('manuskripter', 0.3061)]
```

The [KeyBERT homepage](https://github.com/MaartenGr/KeyBERT) provides other several interesting examples: combining KeyBERT with stop words, extracting longer phrases, or directly producing highlighted text.

## Topic Modeling
To analyse a group of documents and determine the topics, has a lot of use cases. [BERTopic](https://github.com/MaartenGr/BERTopic) combines the power of sentence transformers with c-TF-IDF to create clusters for easily interpretable topics.

It would take too much time to explain topic modeling here. Instead we recommend that you take a look at the link above, as well as the [documentation](https://maartengr.github.io/BERTopic/index.html). The main adaptation you would need to do to use the Norwegian nb-sbert-base, is to add the following:

```python
topic_model = BERTopic(embedding_model='NbAiLab/nb-sbert-base').fit(docs)
```

## Similarity Search
Another common use case for a SentenceTransformers model is to find relevant documents or passages of documents given a certain query text. In this scenario, it is pretty common to have a vector database that stores the embedding vectors for all our documents. Then, at runtime, an embedding for the query text is generated and compared efficiently against the vector database.

While production vector databases exist, a quick way to experiment with them is by using [`autofaiss`](https://github.com/criteo/autofaiss):

```bash
pip install autofaiss sentence-transformers
```

```python
from autofaiss import build_index
import numpy as np

from sentence_transformers import SentenceTransformer, util
sentences = ["This is a Norwegian boy", "Dette er en norsk gutt", "A red house"]

model = SentenceTransformer('NbAiLab/nb-sbert-base')
embeddings = model.encode(sentences)
index, index_infos = build_index(embeddings, save_on_disk=False)

# Search for the closest matches
query = model.encode(["A young boy"])
_, index_matches = index.search(query, 1)
print(index_matches)
```




# Evaluation and Parameters

## Evaluation
Evaluation results on the sts-test dataset:
|                        | Pearson    | Spearman   |
|------------------------|------------|------------|
| Cosine Similarity      | **0.8275** | **0.8245** |
| Manhattan Distance     | 0.8193     | 0.8182     |
| Euclidean Distance     | 0.8190     | 0.8180     |
| Dot Product Similarity | 0.8039     | 0.7951     |

## Training
The model was trained with the parameters:

**DataLoader**:

`sentence_transformers.datasets.NoDuplicatesDataLoader.NoDuplicatesDataLoader` of length 16471 with parameters:
```
{'batch_size': 32}
```

**Loss**:

`sentence_transformers.losses.MultipleNegativesRankingLoss.MultipleNegativesRankingLoss` with parameters:
  ```
  {'scale': 20.0, 'similarity_fct': 'cos_sim'}
  ```

Parameters of the fit()-Method:
```
{
    "epochs": 1,
    "evaluation_steps": 1647,
    "evaluator": "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator.EmbeddingSimilarityEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'torch.optim.adamw.AdamW'>",
    "optimizer_params": {
        "lr": 2e-05
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 1648,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 75, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors
The model was trained by Rolv-Arild Braaten and Per Egil Kummervold. Documentation written by Javier de la Rosa, Rov-Arild Braaten and Per Egil Kummervold.
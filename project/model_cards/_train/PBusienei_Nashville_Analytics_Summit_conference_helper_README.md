---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
---

# Conference Helper
This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 384 dimensional dense vector space and was designed for **semantic search**. It has been trained on 215M (question, answer) pairs from diverse sources. 


## Usage (Sentence-Transformers)
The usage of this model is easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Thus the model can be used as:
```python
from sentence_transformers import SentenceTransformer, util

query = "Health Analytics?"
docs = ["The output is 3 top most similar sessions from the summit"]

#Load the model
model = SentenceTransformer('sentence-transformers/multi-qa-MiniLM-L6-cos-v1')

#Encode query and documents
query_emb = model.encode(query)
doc_emb = model.encode(docs)

#Compute dot score between query and all document embeddings
scores = util.dot_score(query_emb, doc_emb)[0].cpu().tolist()

#Combine docs & scores
doc_score_pairs = list(zip(docs, scores))

#Sort by decreasing score
doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)

#Output passages & scores
for doc, score in doc_score_pairs:
    print(score, doc)
```


## Usage (HuggingFace Transformers)
Without [sentence-transformers](https://www.SBERT.net), you can take the following steps: 
1. Pass input through the transformer model, 
2. Apply the correct pooling-operation on-top of the contextualized word embeddings.

```python

from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

#Mean Pooling - Take average of all tokens
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output.last_hidden_state #The first element of model_output containing all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


#Encode text
def encode(texts):
    # Tokenize sentences
    encoded_input = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')

    # Compute token embeddings
    with torch.no_grad():
        model_output = model(**encoded_input, return_dict=True)

    # Perform pooling
    embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

    # Normalize embeddings
    embeddings = F.normalize(embeddings, p=2, dim=1)
	
    return embeddings


# Sentences we want sentence embeddings for
query = "Health Analytics?"
docs = ["The output is 3 top most similar sessions from the summit"]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/multi-qa-MiniLM-L6-cos-v1")
model = AutoModel.from_pretrained("sentence-transformers/multi-qa-MiniLM-L6-cos-v1")

#Encode query and docs
query_emb = encode(query)
doc_emb = encode(docs)

#Compute dot score between query and all document embeddings
scores = torch.mm(query_emb, doc_emb.transpose(0, 1))[0].cpu().tolist()

#Combine docs & scores
doc_score_pairs = list(zip(docs, scores))

#Sort by decreasing score
doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)

#Output passages & scores
for doc, score in doc_score_pairs:
    print(score, doc)
```

## Technical Details

In the following some technical details how this model must be used:

| Setting | Value |
| --- | :---: |
| Dimensions | 384 |
| Produces normalized embeddings | Yes |
| Pooling-Method | Mean pooling |
| Suitable score functions | dot-product (`util.dot_score`), cosine-similarity (`util.cos_sim`), or euclidean distance |

Note: When loaded with `sentence-transformers`, this model produces normalized embeddings with length 1. In that case, dot-product and cosine-similarity are equivalent. dot-product is preferred as it is faster. Euclidean distance is proportional to dot-product and can also be used.

----


## Background

The project aims to train sentence embedding models on very large sentence level datasets using a self-supervised 
contrastive learning objective. We use a contrastive learning objective: given a sentence from the pair, the model should predict which out of a set of randomly sampled other sentences, was actually paired with it in our dataset.



## Intended uses

The model is intended to be used for semantic search at Nashville Analytics Summit: It encodes queries / questions and text paragraphs in a dense vector space. It finds relevant documents for the given passages.

Note that there is a limit of 512 word pieces: Text longer than that will be truncated. Further note that the model was just trained on input text up to 250 word pieces. It might not work well for longer text. 



## Training procedure

The full training script is accessible in: `train_script.py`.

### Pre-training 

The pretrained [`nreimers/MiniLM-L6-H384-uncased`](https://huggingface.co/nreimers/MiniLM-L6-H384-uncased) model. 

#### Training

We use the concatenation from multiple datasets to fine-tune our model. In total we have about 215M (question, answer) pairs.
We sampled each dataset given a weighted probability which configuration is detailed in the `data_config.json` file.

The model was trained with [MultipleNegativesRankingLoss](https://www.sbert.net/docs/package_reference/losses.html#multiplenegativesrankingloss) using Mean-pooling, cosine-similarity as similarity function, and a scale of 20.




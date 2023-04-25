---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
language: 
  - it
---

# sentence-BERTino-3-64

This is a distilled [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 64 dimensional dense vector space and can be used for tasks like clustering or semantic search.

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

model = SentenceTransformer('efederici/sentence-BERTino-3-64')
embeddings = model.encode(sentences)
print(embeddings)
```


## Training
The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 1724 with parameters:
```
{'batch_size': 64, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.MSELoss.MSELoss` 


## Full Model Architecture
```
SentenceTransformer(
  (0): SentenceTransformer(
    (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: DistilBertModel 
    (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
  )
  (1): Dense({'in_features': 768, 'out_features': 64, 'bias': True, 'activation_function': 'torch.nn.modules.activation.Tanh'})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->
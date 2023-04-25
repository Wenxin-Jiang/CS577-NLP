---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
---

# This model is superseded by [https://github.com/ORNL/affinity_pred](https://github.com/ORNL/affinity_pred)

# jglaser/protein-ligand-mlp-1

This is a [sentence-transformers](https://www.SBERT.net) model: It maps pairs of protein and chemical sequences (canonical SMILES) onto binding affinities (pIC50 values).

Each member of the ensemble has been trained using a different seed and you can use the different models as independent samples to estimate the uncertainty.

<!--- Describe your model here -->

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
#pip install -U sentence-transformers
pip install git+https://github.com/jglaser/sentence-transformers.git@enable_mixed
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = [{'protein': ["SEQVENCE"], 'ligand': ["c1ccccc1"]}]

model = SentenceTransformer('jglaser/protein-ligand-mlp-1')
embeddings = model.encode(sentences)
print(embeddings)
```


## Evaluation Results

<!--- Describe how your model was evaluated -->

## Full Model Architecture
```
SentenceTransformer(
  (0): Asym(
    (protein-0): Transformer({'max_seq_length': 2048, 'do_lower_case': False}) with Transformer model: BertModel 
    (protein-1): Pooling({'word_embedding_dimension': 1024, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
    (protein-2): Dense({'in_features': 1024, 'out_features': 1024, 'bias': True, 'activation_function': 'torch.nn.modules.activation.Tanh'})
    (ligand-0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
    (ligand-1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
    (ligand-2): Dense({'in_features': 768, 'out_features': 768, 'bias': True, 'activation_function': 'torch.nn.modules.activation.Tanh'})
  )
  (1): Dense({'in_features': 1792, 'out_features': 1000, 'bias': True, 'activation_function': 'torch.nn.modules.activation.GELU'})
  (2): Dense({'in_features': 1000, 'out_features': 1000, 'bias': True, 'activation_function': 'torch.nn.modules.activation.GELU'})
  (3): Dense({'in_features': 1000, 'out_features': 1000, 'bias': True, 'activation_function': 'torch.nn.modules.activation.GELU'})
  (4): Dense({'in_features': 1000, 'out_features': 1, 'bias': True, 'activation_function': 'torch.nn.modules.linear.Identity'})
  (5): Dense({'in_features': 1, 'out_features': 1, 'bias': True, 'activation_function': 'torch.nn.modules.linear.Identity'})
)
```

## Citing & Authors
- [Andrew E Blanchard](https://github.com/blnchrd)
- [John Gounley](https://github.com/gounley)
- [Debsindhu Bhowmik](https://github.com/debsindhu)
- [Mayanka Chandra Shekar](https://github.com/mayankachandrashekar)
- [Isaac Lyngaas](https://github.com/irlyngaas)
- Shang Gao
- Junqi Yin
- Aristeidis Tsaris
- Feiyi Wang
- [Jens Glaser](https://github.com/jglaser)

Find more information in our [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2021.12.10.471928v1)
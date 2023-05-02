---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
language:
- ro
language_creators:
- machine-generated
dataset:
- ro_sts

---

# stsb-xlm-r-multilingual-ro

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search. Fine Tune of stsb-xlm-r-multilingual for romanian language

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

model = SentenceTransformer('BlackKakapo/stsb-xlm-r-multilingual-ro')
embeddings = model.encode(sentences)
print(embeddings)
```



## Usage (HuggingFace Transformers)
Without [sentence-transformers](https://www.SBERT.net), you can use the model like this: First, you pass your input through the transformer model, then you have to apply the right pooling-operation on-top of the contextualized word embeddings.

```python
from transformers import AutoTokenizer, AutoModel
import torch


#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
sentences = ['This is an example sentence', 'Each sentence is converted']

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('BlackKakapo/stsb-xlm-r-multilingual-ro')
model = AutoModel.from_pretrained('BlackKakapo/stsb-xlm-r-multilingual-ro')
```

## Training
**DataSet**:
[STS-ro](https://www.SBERT.net)
The text dataset is in Romanian (ro). Score is from 0 to 5, that why I divide score by 5, becouse the score for  EmbeddingSimilarityEvaluator (evaluator for finetune) need  to be from 0 to 1.
Dataset Structure:
```
{
'score': 1.5,
 'sentence1': 'Un bărbat cântă la harpă.',
 'sentence2': 'Un bărbat cântă la claviatură.',
}
```


**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 223 with parameters:
```
{'batch_size': 32, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.CosineSimilarityLoss.CosineSimilarityLoss` 

Parameters of the fit()-Method:
```
{
    "epochs": 10,
    "evaluation_steps": 0,
    "evaluator": "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator.EmbeddingSimilarityEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'torch.optim.adamw.AdamW'>",
    "optimizer_params": {
        "lr": 2e-05
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 100,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False}) with Transformer model: XLMRobertaModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

# BlackKakapo

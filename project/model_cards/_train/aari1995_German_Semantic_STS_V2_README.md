---
pipeline_tag: sentence-similarity
language:
- de
datasets:
- stsb_multi_mt
tags:
- gBERT-large
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers

---

# gBERT-large-sts-v2

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 1024 dimensional dense vector space and can be used for tasks like clustering or semantic search.

Special thanks to [deepset](https://huggingface.co/deepset/) for providing the model gBERT-large and also to [Philip May](https://huggingface.co/philipMay) for the Translation of the dataset and chats about the topic.

Model score after fine-tuning according to CSV:

**STS-B Test: 0.8626 (Spearman)**

This is the best result achieved that I know of.

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

model = SentenceTransformer('aari1995/gBERT-large-sts-v2')
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
tokenizer = AutoTokenizer.from_pretrained('aari1995/gBERT-large-sts-v2')
model = AutoModel.from_pretrained('aari1995/gBERT-large-sts-v2')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, mean pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

print("Sentence embeddings:")
print(sentence_embeddings)
```



## Evaluation Results

<!--- Describe how your model was evaluated -->

For an automated evaluation of this model, see the *Sentence Embeddings Benchmark*: [https://seb.sbert.net](https://seb.sbert.net?model_name={MODEL_NAME})


## Training
The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 1438 with parameters:
```
{'batch_size': 4, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.ContrastiveLoss.ContrastiveLoss` with parameters:
  ```
  {'distance_metric': 'SiameseDistanceMetric.COSINE_DISTANCE', 'margin': 0.5, 'size_average': True}
  ```

Parameters of the fit()-Method:
```
{
    "epochs": 4,
    "evaluation_steps": 500,
    "evaluator": "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator.EmbeddingSimilarityEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'torch.optim.adamw.AdamW'>",
    "optimizer_params": {
        "lr": 5e-06
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 576,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 1024, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->
The base model is trained by deepset.
The dataset was published / translated by Philip May.
The model was fine-tuned by Aaron Chibb.
---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
- german
- nli
- text-classification


---

# airnicco8/xlm-roberta-de

This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search. It is trained on the [Ted talks transcripts](https://www.kaggle.com/datasets/rounakbanik/ted-talks) filtered only by German language, the training setting is described [here](https://towardsdatascience.com/a-complete-guide-to-transfer-learning-from-english-to-other-languages-using-sentence-embeddings-8c427f8804a9). It can be used straight-forwardly for sentence similarity, but can also be fine-tuned for NLI and Text-Classification, examples coming soon.

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["das ist eine glückliche Frau", "das ist ein glücklicher Mann", "das ist ein glücklicher Hund"]

model = SentenceTransformer('airnicco8/xlm-roberta-de')
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
sentences = ["das ist eine glückliche Frau", "das ist ein glücklicher Mann", "das ist ein glücklicher Hund"]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('airnicco8/xlm-roberta-de')
model = AutoModel.from_pretrained('airnicco8/xlm-roberta-de')

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

For an automated evaluation of this model, see the *Sentence Embeddings Benchmark*: [https://seb.sbert.net](https://seb.sbert.net?model_name=airnicco8/xlm-roberta-de)


## Training
The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 3071 with parameters:
```
{'batch_size': 16, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.MSELoss.MSELoss` 

Parameters of the fit()-Method:
```
{
    "epochs": 10,
    "evaluation_steps": 1000,
    "evaluator": "sentence_transformers.evaluation.SequentialEvaluator.SequentialEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'torch.optim.adamw.AdamW'>",
    "optimizer_params": {
        "eps": 1e-06,
        "lr": 2e-05
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 1000,
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

<!--- Describe where people can find more information -->
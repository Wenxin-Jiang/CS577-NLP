---
pipeline_tag: sentence-similarity
language: en
tags:
- sentence-similarity
- transformers
- en
- bert
- sentence-transformers
- feature-extraction
datasets:
- nli
- stsb
---

It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search.

## Details

This model is based on the English bert-base-uncased pre-trained model [1, 2]. 


Model was trained  on a natural language inference task (NLI). This task consists in training the model to recognize relations between sentences (contradiction, neutral, implication).

It was then trained on a text semantic similarity task (on STS data) [3]. This task consists in training the model to estimate the similarity between two sentences.

This fine-tuning process allows our model to have a semantic representation of words that is much better than the one proposed by the base model.

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["How is air traffic controlled?", "How do you become an air traffic controller?"]

model = SentenceTransformer('Shobhank-iiitdwd/BERT-BU-nli-sts-sent')
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
sentences = ["Learn to code in python", "Become an expert in accounting"]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('Shobhank-iiitdwd/BERT-BU-nli-sts-sent')
model = AutoModel.from_pretrained('Shobhank-iiitdwd/BERT-BU-nli-sts-sent')

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

STS (en) score: 84.61%


## Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': True}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## References

[1] https://huggingface.co/bert-base-uncased <br>
[2] https://arxiv.org/abs/1810.04805 <br>
[3] https://huggingface.co/datasets/stsb_multi_mt <br>
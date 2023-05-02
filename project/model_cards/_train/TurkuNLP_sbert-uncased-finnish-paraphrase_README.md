---
language:
- fi
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
widget:
- text: "Minusta täällä on ihana asua!"
---


# Uncased Finnish Sentence BERT model

Finnish Sentence BERT trained from FinBERT. A demo on retrieving the most similar sentences from a dataset of 400 million sentences *using [the cased model](https://huggingface.co/TurkuNLP/sbert-cased-finnish-paraphrase)* can be found [here](http://epsilon-it.utu.fi/sbert400m).

## Training

- Library: [sentence-transformers](https://www.sbert.net/)
- FinBERT model: TurkuNLP/bert-base-finnish-uncased-v1
- Data: The data provided [here](https://turkunlp.org/paraphrase.html), including the Finnish Paraphrase Corpus and the automatically collected paraphrase candidates (500K positive and 5M negative)
- Pooling: mean pooling
- Task: Binary prediction, whether two sentences are paraphrases or not. Note: the labels 3 and 4 are considered paraphrases, and labels 1 and 2 non-paraphrases. [Details on labels](https://aclanthology.org/2021.nodalida-main.29/)

## Usage

The same as in [HuggingFace documentation](https://huggingface.co/sentence-transformers/bert-base-nli-mean-tokens). Either through `SentenceTransformer` or `HuggingFace Transformers`

### SentenceTransformer

```python
from sentence_transformers import SentenceTransformer
sentences = ["Tämä on esimerkkilause.", "Tämä on toinen lause."]

model = SentenceTransformer('TurkuNLP/sbert-uncased-finnish-paraphrase')
embeddings = model.encode(sentences)
print(embeddings)
```

### HuggingFace Transformers

```python
from transformers import AutoTokenizer, AutoModel
import torch


# Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
sentences = ["Tämä on esimerkkilause.", "Tämä on toinen lause."]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('TurkuNLP/sbert-uncased-finnish-paraphrase')
model = AutoModel.from_pretrained('TurkuNLP/sbert-uncased-finnish-paraphrase')

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

A publication detailing the evaluation results is currently being drafted.

## Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': True}) with Transformer model: BertModel
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
    )
```

## Citing & Authors
While the publication is being drafted, please cite [this page](https://turkunlp.org/paraphrase.html).

## References

- J. Kanerva, F. Ginter, LH. Chang, I. Rastas, V. Skantsi, J. Kilpeläinen, HM. Kupari, J. Saarni, M. Sevón, and O. Tarkka. Finnish Paraphrase Corpus. In *NoDaLiDa 2021*, 2021.
- N. Reimers and I. Gurevych. Sentence-BERT: Sentence embeddings using Siamese BERT-networks. In *EMNLP-IJCNLP*, pages 3982–3992, 2019.
- A. Virtanen, J. Kanerva, R. Ilo, J. Luoma, J. Luotolahti, T. Salakoski, F. Ginter, and S. Pyysalo. Multilingual is not enough: BERT for Finnish. *arXiv preprint arXiv:1912.07076*, 2019.

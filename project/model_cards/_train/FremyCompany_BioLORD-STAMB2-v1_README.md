---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
language: en
license: other
datasets:
- FremyCompany/BioLORD-Dataset
widget:
  source_sentence: bartonellosis
  sentences:
  - cat scratch disease
  - cat scratch wound
  - tick-borne orbivirus fever
  - cat fur

---

# FremyCompany/BioLORD-STAMB2-v1
This model was trained using BioLORD, a new pre-training strategy for producing meaningful representations for clinical sentences and biomedical concepts. 

State-of-the-art methodologies operate by maximizing the similarity in representation of names referring to the same concept, and preventing collapse through contrastive learning. However, because biomedical names are not always self-explanatory, it sometimes results in non-semantic representations. 

BioLORD overcomes this issue by grounding its concept representations using definitions, as well as short descriptions derived from a multi-relational knowledge graph consisting of biomedical ontologies. Thanks to this grounding, our model produces more semantic concept representations that match more closely the hierarchical structure of ontologies. BioLORD establishes a new state of the art for text similarity on both clinical sentences (MedSTS) and biomedical concepts (MayoSRS).

This model is based on [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) and was further finetuned on the [BioLORD-Dataset](https://huggingface.co/datasets/FremyCompany/BioLORD-Dataset).
<img width="640" src="https://s3.amazonaws.com/moonup/production/uploads/1665568401241-5f04e8865d08220171a0ad3f.png" />


## General purpose
This is a [sentence-transformers](https://www.SBERT.net) model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search. This model has been finentuned for the biomedical domain. While it preserves a good ability to produce embeddings for general-purpose text, it will be more useful to you if you are trying to process medical documents such as EHR records or clinical notes. Both sentences and phrases can be embedded in the same latent space.

## Citation
This model accompanies the [BioLORD: Learning Ontological Representations from Definitions](https://arxiv.org/abs/2210.11892) paper, accepted in the EMNLP 2022 Findings. When you use this model, please cite the original paper as follows:

```latex
@inproceedings{remy-etal-2022-biolord,
    title = "{B}io{LORD}: Learning Ontological Representations from Definitions for Biomedical Concepts and their Textual Descriptions",
    author = "Remy, François  and
      Demuynck, Kris  and
      Demeester, Thomas",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2022",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-emnlp.104",
    pages = "1454--1465",
    abstract = "This work introduces BioLORD, a new pre-training strategy for producing meaningful representations for clinical sentences and biomedical concepts. State-of-the-art methodologies operate by maximizing the similarity in representation of names referring to the same concept, and preventing collapse through contrastive learning. However, because biomedical names are not always self-explanatory, it sometimes results in non-semantic representations. BioLORD overcomes this issue by grounding its concept representations using definitions, as well as short descriptions derived from a multi-relational knowledge graph consisting of biomedical ontologies. Thanks to this grounding, our model produces more semantic concept representations that match more closely the hierarchical structure of ontologies. BioLORD establishes a new state of the art for text similarity on both clinical sentences (MedSTS) and biomedical concepts (MayoSRS).",
}
```

## Usage (Sentence-Transformers)
Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:
```
pip install -U sentence-transformers
```
Then you can use the model like this:
```python
from sentence_transformers import SentenceTransformer
sentences = ["Cat scratch injury", "Cat scratch disease", "Bartonellosis"]

model = SentenceTransformer('FremyCompany/BioLORD-STAMB2-v1')
embeddings = model.encode(sentences)
print(embeddings)
```
## Usage (HuggingFace Transformers)
Without [sentence-transformers](https://www.SBERT.net), you can use the model like this: First, you pass your input through the transformer model, then you have to apply the right pooling-operation on-top of the contextualized word embeddings.
```python
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

# Sentences we want sentence embeddings for
sentences = ["Cat scratch injury", "Cat scratch disease", "Bartonellosis"]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('FremyCompany/BioLORD-STAMB2-v1')
model = AutoModel.from_pretrained('FremyCompany/BioLORD-STAMB2-v1')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)
# Perform pooling
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
# Normalize embeddings
sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)
print("Sentence embeddings:")
print(sentence_embeddings)
```

## License
My own contributions for this model are covered by the MIT license.
However, given the data used to train this model originates from UMLS, you will need to ensure you have proper licensing of UMLS before using this model. UMLS is free of charge in most countries, but you might have to create an account and report on your usage of the data yearly to keep a valid license.
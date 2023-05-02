---
language: 
  - en
thumbnail: "https://www.fusion.uni-jena.de/fusionmedia/fusionpictures/fusion-service/fusion-transp.png?height=383&width=680"
tags:
- bert-base-cased
- biodiversity
license: cc-by-nc-4.0
---

# BiodivBERT

## Model description
* BiodivBERT is a domain-specific BERT based cased model for the biodiversity literature.
* It uses the tokenizer from BERTT base cased model.
* BiodivBERT is pre-trained on abstracts and full text from biodiversity literature.
* BiodivBERT is fine-tuned on two down stream tasks for Named Entity Recognition and Relation Extraction in the biodiversity domain.
* Please visit our [GitHub Repo](https://github.com/fusion-jena/BiodivBERT) for more details.

## How to use
* You can use BiodivBERT via huggingface library as follows:

1. Masked Language Model 

````
>>> from transformers import AutoTokenizer, AutoModelForMaskedLM

>>> tokenizer = AutoTokenizer.from_pretrained("NoYo25/BiodivBERT")

>>> model = AutoModelForMaskedLM.from_pretrained("NoYo25/BiodivBERT")
````

2. Token Classification - Named Entity Recognition

````
>>> from transformers import AutoTokenizer, AutoModelForTokenClassification

>>> tokenizer = AutoTokenizer.from_pretrained("NoYo25/BiodivBERT")

>>> model = AutoModelForTokenClassification.from_pretrained("NoYo25/BiodivBERT")
````

3. Sequence Classification - Relation Extraction

````
>>> from transformers import AutoTokenizer, AutoModelForSequenceClassification

>>> tokenizer = AutoTokenizer.from_pretrained("NoYo25/BiodivBERT")

>>> model = AutoModelForSequenceClassification.from_pretrained("NoYo25/BiodivBERT")
````

## Training data

* BiodivBERT is pre-trained on abstracts and full text from biodiversity domain-related publications.
* We used both Elsevier and Springer APIs to crawl such data.
* We covered publications over the duration of 1990-2020.

## Evaluation results
BiodivBERT overperformed both ``BERT_base_cased``, ``biobert_v1.1``, and ``BiLSTM`` as a baseline approach on the down stream tasks.

## License 
license: cc-by-nc-4.0



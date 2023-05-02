
---
language:
- da
license: cc-by-sa-4.0
---

# XLM-Roberta fine-tuned for Named Entity Disambiguation

Given a sentence and a knowledge graph context, the model detects whether a specific entity (represented by the knowledge graph context) is mentioned in the sentence (binary classification). 
The base language model used is the [xlm-roberta-base](https://huggingface.co/xlm-roberta-base). 

Here is how to use the model: 

```python
from transformers import XLMRobertaTokenizer, XLMRobertaForSequenceClassification

model = XLMRobertaForSequenceClassification.from_pretrained("alexandrainst/da-ned-base")
tokenizer = XLMRobertaTokenizer.from_pretrained("alexandrainst/da-ned-base")
```

The tokenizer takes 2 strings has input: the sentence and the knowledge graph (KG) context. 
Here is an example:
```python
sentence = "Karen Blixen vendte tilbage til Danmark, hvor hun boede resten af sit liv på Rungstedlund, som hun arvede efter sin mor i 1939"
kg_context = "udmærkelser modtaget Kritikerprisen udmærkelser modtaget Tagea Brandts Rejselegat udmærkelser modtaget Ingenio et arti udmærkelser modtaget Holbergmedaljen udmærkelser modtaget De Gyldne Laurbær mor Ingeborg Dinesen ægtefælle Bror von Blixen-Finecke køn kvinde Commons-kategori Karen Blixen LCAuth no95003722 VIAF 90663542 VIAF 121643918 GND-identifikator 118637878 ISNI 0000 0001 2096 6265 ISNI 0000 0003 6863 4408 ISNI 0000 0001 1891 0457 fødested Rungstedlund fødested Rungsted dødssted Rungstedlund dødssted København statsborgerskab Danmark NDL-nummer 00433530 dødsdato +1962-09-07T00:00:00Z dødsdato +1962-01-01T00:00:00Z fødselsdato +1885-04-17T00:00:00Z fødselsdato +1885-01-01T00:00:00Z AUT NKC jn20000600905 AUT NKC jo2015880827 AUT NKC xx0196181 emnets hovedkategori Kategori:Karen Blixen tilfælde af menneske billede Karen Blixen cropped from larger original.jpg IMDb-identifikationsnummer nm0227598 Freebase-ID /m/04ymd8w BNF 118857710 beskæftigelse skribent beskæftigelse selvbiograf beskæftigelse novelleforfatter ..."
```

A KG context, for a specific entity, can be generated from its Wikidata page. 
In the previous example, the KG context is a string representation of the Wikidata page of [Karen Blixen (QID=Q182804)](https://www.wikidata.org/wiki/Q182804). 
See the [DaNLP documentation](https://danlp-alexandra.readthedocs.io/en/latest/docs/tasks/ned.html#xlmr) for more details about how to generate a KG context. 


## Training Data 

The model has been trained on the [DaNED](https://danlp-alexandra.readthedocs.io/en/latest/docs/datasets.html#daned) and [DaWikiNED](https://danlp-alexandra.readthedocs.io/en/latest/docs/datasets.html#dawikined) datasets. 
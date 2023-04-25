---
language:
- en
tags:
- ner
- chemical
- bionlp
- bc4cdr
- bioinfomatics
license: apache-2.0
datasets:
- bionlp
- bc4cdr
widget:
- text: "Serotonin receptor 2A (HTR2A) gene polymorphism predicts treatment response to venlafaxine XR in generalized anxiety disorder."

---

# NER to find Gene & Gene products
> The model was trained on bionlp and bc4cdr dataset, pretrained on this [pubmed-pretrained roberta model](/raynardj/roberta-pubmed)
All the labels, the possible token classes.
```json
{"label2id":
  {
    "O": 0,
    "Chemical": 1,
  }
 }
```
 
Notice, we removed the 'B-','I-' etc from data label.🗡
 
## This is the template we suggest for using the model
Of course I'm well aware of the ```aggregation_strategy``` arguments offered by hf, but by the way of training, I discard any entropy loss for appending subwords, like only the label for the 1st subword token is not -100, after many search effort, I can't find a way to achieve that with default pipeline, hence I fancy an inference class myself.
```python
!pip install forgebox
from forgebox.hf.train import NERInference
ner = NERInference.from_pretrained("raynardj/ner-chemical-bionlp-bc5cdr-pubmed")
a_df = ner.predict(["text1", "text2"])
```

> check our NER model on
* [gene and gene products](/raynardj/ner-gene-dna-rna-jnlpba-pubmed)
* [chemical substance](/raynardj/ner-chemical-bionlp-bc5cdr-pubmed).
* [disease](/raynardj/ner-disease-ncbi-bionlp-bc5cdr-pubmed)
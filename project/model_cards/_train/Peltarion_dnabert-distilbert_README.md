---
tags:
  - DNA
license: mit
---

## DistilDNA model

This is a distilled version of [DNABERT](https://github.com/jerryji1993/DNABERT) by using DistilBERT technique. It has a BERT architecture with 6 layers and 768 hidden units, pre-trained on 6-mer DNA sequences. For more details on the pre-training scheme and methods, please check the original [thesis report](http://www.diva-portal.org/smash/record.jsf?dswid=846&pid=diva2%3A1676068&c=1&searchType=SIMPLE&language=en&query=joana+palés&af=%5B%5D&aq=%5B%5B%5D%5D&aq2=%5B%5B%5D%5D&aqe=%5B%5D&noOfRows=50&sortOrder=author_sort_asc&sortOrder2=title_sort_asc&onlyFullText=false&sf=all).


## How to Use  

The model can be used to fine-tune on a downstream genomic task, e.g. promoter identification.

```python
import torch
from transformers import DistilBertForSequenceClassification

model = DistilBertForSequenceClassification.from_pretrained('Peltarion/dnabert-distilbert')
```

More details on how to fine-tune the model, dataset and additional source codes are available on [github.com/joanaapa/Distillation-DNABERT-Promoter](https://github.com/joanaapa/Distillation-DNABERT-Promoter).

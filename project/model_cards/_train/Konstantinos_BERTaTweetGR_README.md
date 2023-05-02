---
language: el
widget:
 - text: "μπαινω στο <mask> και τι να δω."
---

#  Α lite RoBERTa fill mask model trained mostly in greek tweets


The training dataset of this model  consists of 23 million tweets in Greek, of approximately 5000 users in total, spanning from 2008 to 2018.
The model has been trained to support the work for the paper [Multimodal Hate Speech Detection in Greek Social Media](https://www.mdpi.com/2414-4088/5/7/34) 


## Load the pretrained model

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("Konstantinos/BERTaTweetGR")
model = AutoModel.from_pretrained("Konstantinos/BERTaTweetGR")
```

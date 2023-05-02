---
language: ar
widget:
 - text: " جاب ليا [MASK] ."
 - text: "مشيت نجيب[MASK] فالفرماسيان ."
---


AIOX Lab and  SI2M Lab INSEA have joined forces to offer researchers, industrialists and the NLP (Natural Language Processing) community the first intelligent Open Source system that understands Moroccan dialectal language "Darija".


**DarijaBERT** is the first BERT model for the Moroccan Arabic dialect called “Darija”. It is based on the same architecture as BERT-base, but without the Next Sentence Prediction (NSP) objective. This model was trained on a total of ~3 Million sequences of Darija dialect representing 691MB of text or a total of ~100M tokens.

The model was trained on a dataset issued from three different sources:
*  Stories written in Darija scrapped from a dedicated website
*  Youtube comments from 40 different Moroccan channels
*  Tweets crawled based on a list of Darija keywords. 

More details about DarijaBert are available in the dedicated GitHub [repository](https://github.com/AIOXLABS/DBert) 

**Loading the model**

The model can be loaded directly using the Huggingface library:

```python
from transformers import AutoTokenizer, AutoModel
DarijaBERT_tokenizer = AutoTokenizer.from_pretrained("SI2M-Lab/DarijaBERT")
DarijaBert_model = AutoModel.from_pretrained("SI2M-Lab/DarijaBERT")
```
 
**Acknowledgments**

We gratefully acknowledge Google’s TensorFlow Research Cloud (TRC) program for providing us with free Cloud TPUs.



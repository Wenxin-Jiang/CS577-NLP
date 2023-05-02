---
language: ar
widget:
 - text: " Mchit njib [MASK] ."
 - text: " Yak nta li [MASK] lih dik lhedra."
 - text: " Ach [MASK] daba."
 - text: " Lmghrib ajmal [MASK] fl3alam."
---
AIOX Lab and  SI2M Lab INSEA have joined forces to offer researchers, industrialists and the NLP (Natural Language Processing) community the first intelligent Open Source system that understands Moroccan dialectal language "Darija".
**DarijaBERT** is the first BERT model for the Moroccan Arabic dialect called “Darija”. It is based on the same architecture as BERT-base, but without the Next Sentence Prediction (NSP) objective. This model is the Arabizi specific version of DarijaBERT and it was trained on a total of ~4.6 Million sequences of Darija dialect written in Latin letters.

The model was trained on a dataset issued from Youtube comments.

More details about DarijaBert are available in the dedicated GitHub [repository](https://github.com/AIOXLABS/DBert) 
**Loading the model**
The model can be loaded directly using the Huggingface library:
```python
from transformers import AutoTokenizer, AutoModel
DarijaBERT_tokenizer = AutoTokenizer.from_pretrained("Kamel/DarijaBERT-arabizi")
DarijaBert_model = AutoModel.from_pretrained("Kamel/DarijaBERT-arabizi")
```
 
**Acknowledgments**
We gratefully acknowledge Google’s TensorFlow Research Cloud (TRC) program for providing us with free Cloud TPUs.

<font size =2>**Warning**
This model being trained on texts from social networks, it can unfortunately generate toxic outputs reflecting part of the learned data</font>

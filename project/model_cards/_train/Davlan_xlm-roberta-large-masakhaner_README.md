Hugging Face's logo
---
language: 
- amh
- hau
- ibo
- kin
- lug
- luo
- pcm
- swa
- wol
- yor
- multilingual


datasets:
- masakhaner
---
# xlm-roberta-large-masakhaner
## Model description
**xlm-roberta-large-masakhaner** is the first **Named Entity Recognition** model for 10 African languages (Amharic, Hausa, Igbo, Kinyarwanda, Luganda, Nigerian Pidgin, Swahili, Wolof, and Yorùbá) based on a fine-tuned  XLM-RoBERTa large model.  It achieves the **state-of-the-art performance** for the NER task. It has been trained to recognize four types of entities: dates & times (DATE), location (LOC), organizations (ORG), and person (PER). 
Specifically, this model is a *xlm-roberta-large* model that was fine-tuned on an aggregation of African language datasets obtained from Masakhane [MasakhaNER](https://github.com/masakhane-io/masakhane-ner) dataset. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for NER.
```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
tokenizer = AutoTokenizer.from_pretrained("Davlan/xlm-roberta-large-masakhaner")
model = AutoModelForTokenClassification.from_pretrained("Davlan/xlm-roberta-large-masakhaner")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "Emir of Kano turban Zhang wey don spend 18 years for Nigeria"
ner_results = nlp(example)
print(ner_results)
```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains.  
## Training data
This model was fine-tuned on 10 African NER datasets (Amharic, Hausa, Igbo, Kinyarwanda, Luganda, Nigerian Pidgin, Swahili, Wolof, and Yorùbá) Masakhane [MasakhaNER](https://github.com/masakhane-io/masakhane-ner) dataset

The training dataset distinguishes between the beginning and continuation of an entity so that if there are back-to-back entities of the same type, the model can output where the second entity begins. As in the dataset, each token will be classified as one of the following classes:
Abbreviation|Description
-|-
O|Outside of a named entity
B-DATE |Beginning of a DATE entity right after another DATE entity
I-DATE |DATE entity
B-PER |Beginning of a person’s name right after another person’s name
I-PER |Person’s name
B-ORG |Beginning of an organisation right after another organisation
I-ORG |Organisation
B-LOC |Beginning of a location right after another location
I-LOC |Location
## Training procedure
This model was trained on a single NVIDIA V100 GPU with recommended hyperparameters from the [original MasakhaNER paper](https://arxiv.org/abs/2103.11811) which trained & evaluated the model on MasakhaNER corpus. 
## Eval results on Test set (F-score)
language|F1-score
-|-
amh |75.76
hau |91.75
ibo |86.26
kin |76.38
lug |84.64
luo |80.65
pcm |89.55
swa |89.48
wol |70.70
yor |82.05

### BibTeX entry and citation info
```
@article{adelani21tacl,
    title = {Masakha{NER}: Named Entity Recognition for African Languages},
    author = {David Ifeoluwa Adelani and Jade Abbott and Graham Neubig and Daniel D'souza and Julia Kreutzer and Constantine Lignos and Chester Palen-Michel and Happy Buzaaba and Shruti Rijhwani and Sebastian Ruder and Stephen Mayhew and Israel Abebe Azime and Shamsuddeen Muhammad and Chris Chinenye Emezue and Joyce Nakatumba-Nabende and Perez Ogayo and Anuoluwapo Aremu and Catherine Gitau and Derguene Mbaye and Jesujoba Alabi and Seid Muhie Yimam and Tajuddeen Gwadabe and Ignatius Ezeani and Rubungo Andre Niyongabo and Jonathan Mukiibi and Verrah Otiende and Iroro Orife and Davis David and Samba Ngom and Tosin Adewumi and Paul Rayson and Mofetoluwa Adeyemi and Gerald Muriuki and Emmanuel Anebi and Chiamaka Chukwuneke and Nkiruka Odu and Eric Peter Wairagala and Samuel Oyerinde and Clemencia Siro and Tobius Saul Bateesa and Temilola Oloyede and Yvonne Wambui and Victor Akinode and Deborah Nabagereka and Maurice Katusiime and Ayodele Awokoya and Mouhamadane MBOUP and Dibora Gebreyohannes and Henok Tilaye and Kelechi Nwaike and Degaga Wolde and Abdoulaye Faye and Blessing Sibanda and Orevaoghene Ahia and Bonaventure F. P. Dossou and Kelechi Ogueji and Thierno Ibrahima DIOP and Abdoulaye Diallo and Adewale Akinfaderin and Tendai Marengereke and Salomey Osei},
    journal = {Transactions of the Association for Computational Linguistics (TACL)},
    month = {},
    url = {https://arxiv.org/abs/2103.11811},
    year = {2021}
}
```


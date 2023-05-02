Hugging Face's logo
---
language: 
- ar
- de
- en
- es
- fr
- it
- lv
- nl
- pt
- zh
- multilingual

---
# distilbert-base-multilingual-cased-ner-hrl
## Model description
**distilbert-base-multilingual-cased-ner-hrl** is a **Named Entity Recognition** model for 10 high resourced languages (Arabic, German, English, Spanish, French, Italian, Latvian, Dutch, Portuguese and Chinese) based on a fine-tuned  Distiled BERT base model. It has been trained to recognize three types of entities: location (LOC), organizations (ORG), and person (PER). 
Specifically, this model is a *distilbert-base-multilingual-cased* model that was fine-tuned on an aggregation of 10 high-resourced languages
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for NER.
```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
tokenizer = AutoTokenizer.from_pretrained("Davlan/distilbert-base-multilingual-cased-ner-hrl")
model = AutoModelForTokenClassification.from_pretrained("Davlan/distilbert-base-multilingual-cased-ner-hrl")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "Nader Jokhadar had given Syria the lead with a well-struck header in the seventh minute."
ner_results = nlp(example)
print(ner_results)
```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains.  
## Training data
The training data for the 10 languages are from: 

Language|Dataset
-|-
Arabic | [ANERcorp](https://camel.abudhabi.nyu.edu/anercorp/)
German | [conll 2003](https://www.clips.uantwerpen.be/conll2003/ner/)
English | [conll 2003](https://www.clips.uantwerpen.be/conll2003/ner/)
Spanish | [conll 2002](https://www.clips.uantwerpen.be/conll2002/ner/)
French | [Europeana Newspapers](https://github.com/EuropeanaNewspapers/ner-corpora/tree/master/enp_FR.bnf.bio)
Italian | [Italian I-CAB](https://ontotext.fbk.eu/icab.html)
Latvian | [Latvian NER](https://github.com/LUMII-AILab/FullStack/tree/master/NamedEntities)
Dutch | [conll 2002](https://www.clips.uantwerpen.be/conll2002/ner/)
Portuguese |[Paramopama + Second Harem](https://github.com/davidsbatista/NER-datasets/tree/master/Portuguese)
Chinese | [MSRA](https://huggingface.co/datasets/msra_ner)

The training dataset distinguishes between the beginning and continuation of an entity so that if there are back-to-back entities of the same type, the model can output where the second entity begins. As in the dataset, each token will be classified as one of the following classes:
Abbreviation|Description
-|-
O|Outside of a named entity
B-PER |Beginning of a person’s name right after another person’s name
I-PER |Person’s name
B-ORG |Beginning of an organisation right after another organisation
I-ORG |Organisation
B-LOC |Beginning of a location right after another location
I-LOC |Location
## Training procedure
This model was trained on NVIDIA V100 GPU with recommended hyperparameters from HuggingFace code.



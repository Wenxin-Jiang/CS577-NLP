Hugging Face's logo
---
language: 
- ar
- as
- bn
- ca
- en
- es
- eu
- fr
- gu
- hi
- id
- ig
- mr
- pa
- pt
- sw
- ur
- vi
- yo
- zh
- multilingual


datasets:
- wikiann
---
# xlm-roberta-base-wikiann-ner
## Model description
**xlm-roberta-base-wikiann-ner** is the first **Named Entity Recognition** model for 20 languages (Arabic, Assamese, Bengali, Catalan, English, Spanish, Basque, French, Gujarati, Hindi, Indonesia, Igbo, Marathi, Punjabi,  Portugues and Swahili, Urdu, Vietnamese, Yoruba, Chinese) based on a fine-tuned  XLM-RoBERTa large model.  It achieves the **state-of-the-art performance** for the NER task. It has been trained to recognize three types of entities: location (LOC), organizations (ORG), and person (PER). 
Specifically, this model is a *xlm-roberta-large* model that was fine-tuned on an aggregation of  languages datasets obtained from  [WikiANN](https://huggingface.co/datasets/wikiann) dataset. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for NER.
```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
tokenizer = AutoTokenizer.from_pretrained("xlm-roberta-base-wikiann-ner")
model = AutoModelForTokenClassification.from_pretrained("xlm-roberta-base-wikiann-ner")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "Ìbọn ń ró kù kù gẹ́gẹ́ bí ọwọ́ ọ̀pọ̀ aráàlù ṣe tẹ ìbọn ní Kyiv láti dojú kọ Russia"
ner_results = nlp(example)
print(ner_results)
```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains.  
## Training data
This model was fine-tuned on 20 NER datasets (Arabic, Assamese, Bengali, Catalan, English, Spanish, Basque, French, Gujarati, Hindi, Indonesia, Igbo, Marathi, Punjabi,  Portugues and Swahili, Urdu, Vietnamese, Yoruba, Chinese)[wikiann](https://huggingface.co/datasets/wikiann). 

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

### BibTeX entry and citation info

```




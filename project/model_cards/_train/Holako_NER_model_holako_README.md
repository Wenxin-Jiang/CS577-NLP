
#### How to use
You can use this model with Transformers *pipeline* for NER.
```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
tokenizer = AutoTokenizer.from_pretrained("Holako/NER_model_holako")
model = AutoModelForTokenClassification.from_pretrained("Holako/NER_model_holako")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "اسمي احمد"
ner_results = nlp(example)
print(ner_results)
```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains.  

=======
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains.  
## Training data

Language|Dataset
-|-
Arabic | [ANERcorp](https://camel.abudhabi.nyu.edu/anercorp/)

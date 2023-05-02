---
language: en
datasets:
- Satellite-Instrument-NER
widget:
- text: "Centroid Moment Tensor Global Navigation Satellite System GNSS"
- text: "This paper describes the latest version of the algorithm MAIAC used for processing the MODIS Collection 6 data record."
- text: "We derive tropospheric column BrO during the ARCTAS and ARCPAC field campaigns in spring 2008 using retrievals of total column BrO from the satellite UV nadir sensors OMI and GOME - 2 using a radiative transfer model and stratospheric column BrO from a photochemical simulation."
license: mit

---
# bert-base-NER

## Model description

**bert-base-NER** is a fine-tuned BERT model that is ready to use for **Named Entity Recognition** and achieves **F1 0.61** for the NER task. It has been trained to recognize two types of entities: instrument and satellite. 

Specifically, this model is a *bert-base-cased* model that was fine-tuned on Satellite-Instrument-NER dataset. 



## Intended uses & limitations

#### How to use

You can use this model with Transformers *pipeline* for NER.

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
tokenizer = AutoTokenizer.from_pretrained("NahedAbdelgaber/ner_base_model")
model = AutoModelForTokenClassification.from_pretrained("NahedAbdelgaber/ner_base_model")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "Centroid Moment Tensor Global Navigation Satellite System GNSS"
ner_results = nlp(example)
print(ner_results)
```
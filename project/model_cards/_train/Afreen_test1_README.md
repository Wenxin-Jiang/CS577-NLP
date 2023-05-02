---
language:
- en
tags:
- Text Classification
co2_eq_emissions: 0.1069
widget:
- text: "At the every month post-injection monitoring event, TCE, carbon tetrachloride, and chloroform concentrations were above CBSGs in three of the wells"
  example_title: "Remediation Standards"
- text: "TRPH exceedances were observed in the subsurface soils immediately above the water table and there are no TRPH exceedances in surface soils."
  example_title: "Extent of Contamination"
- text: "weathered shale was encountered below the surface area with fluvial deposits. Sediments in the coastal plain region are found above and below the bedrock with sandstones and shales that form the basement rock"
  example_title: "Geology"

---

## About the Model
An Environmental due diligence classification model, trained on customized environmental Dataset to detect contamination and remediation activities (both prevailing as well as planned) as a part of site assessment process.  This model can identify the source of contamination, the extent of contamination, the types of contaminants present at the site, the flow of contaminants and their interaction with ground water, surface water and other surrounding water bodies .

This model was built on top of distilbert-base-uncased model and trained for 10 epochs with a batch size of 16, a learning rate of 5e-5, and a maximum sequence length of 512.

- Dataset : Open Source News data + Custom data
- Carbon emission 0.1069 Kg

## Usage
The easiest way is to load through the pipeline object offered by transformers library.
```python
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from transformers import pipeline
tokenizer = AutoTokenizer.from_pretrained("d4data/environmental-due-diligence-model")
model = TFAutoModelForSequenceClassification.from_pretrained("d4data/environmental-due-diligence-model")

classifier = pipeline('text-classification', model=model, tokenizer=tokenizer) # cuda = 0,1 based on gpu availability
classifier("At the every month post-injection monitoring event, TCE, carbon tetrachloride, and chloroform concentrations were above CBSGs in three of the wells")
```

## Author
This model is part of the Research topic "Environmental Due Diligence" conducted by Deepak John Reji, Afreen Aman, Shaina Raza. If you use this work (code, model or dataset), please cite as:
> Environmental Due Diligence, (2020), GitHub repository https://github.com/dreji18/environmental-due-diligence


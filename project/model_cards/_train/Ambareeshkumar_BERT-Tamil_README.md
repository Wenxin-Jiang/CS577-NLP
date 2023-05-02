---
language: ta
datasets:
- wikiann
examples:
widget:
- text: "இந்திய"
  example_title: "Sentence_1"
- text: "இந்தியா வளர்ந்து வரும் வல்லரசு"
  example_title: "Sentence_2"
- text: "2050ல் இந்தியா உலகின் மிகப்பெரிய பொருளாதார நாடாக மாறும்"
  example_title: "Sentence_3"
- text: "இந்தியாவின் வெளியுறவுத்துறை அமைச்சர் திரு.ஜெய் சங்கர், ரஷ்யா-உக்ரைன் மோதலில் இந்தியாவின் நிலைப்பாட்டை தெளிவாக எடுத்துரைத்தார்."
  example_title: "Sentence_4"
- text: "ஜி20 நாடுகளின் தலைவர் பதவி இந்திய பிரதமர் நரேந்திர மோடியிடம் ஒப்படைக்கப்பட்டுள்ளது"
  example_title: "Sentence_5"
- text: "ரஷ்யாவிடம் இருந்து எண்ணெய் வாங்க வேண்டாம் என ஐரோப்பிய நாடுகளுக்கு ஐரோப்பிய ஒன்றியம் அறிவுறுத்தியுள்ளது"
---

<h1>Tamil Named Entity Recognition</h1>
Fine-tuning bert-base-multilingual-cased on Wikiann dataset for performing NER on Tamil language.


## Label ID and its corresponding label name

| Label ID | Label Name|
| -------- | ----- |
|0 | O |
| 1 | B-PER |
| 2 | I-PER |
| 3 | B-ORG|
| 4 | I-ORG | 
| 5 | B-LOC |
| 6 | I-LOC |

<h1>Results</h1>

| Step | Training Loss|	Validation Loss|Overall Precision|Overall Recall|Overall F1|Overall Accuracy| Loc F1  | Org F1  | Per F1  | 
|----- |--------------|----------------|-----------------|--------------|----------|----------------|---------|---------|---------|
| 1000 |    0.386900  |	    0.300006   |   0.833469	     |   0.824748	| 0.829086 |   0.912857	    | 0.835343|	0.781625| 0.867752|
| 2000 |	0.210200  |	    0.251389   |   0.845455	     |   0.842052	| 0.843750 |   0.924861	    | 0.851711|	0.790198| 0.886515|
| 3000 |	0.140000  |	    0.264964   |   0.866952	     |   0.856137   | 0.861510 |   0.930141	    | 0.874872|	0.818150| 0.885203|
| 4000 |	0.095400  | 	0.298542   |   0.860871	     |   0.882696   | 0.871647 |   0.935692	    | 0.881348|	0.829285| 0.899245|
| 5000 |	0.062200  |	    0.296011   |   0.871805	     |   0.878471   | 0.875125 |   0.938806	    | 0.875434|	0.850889| 0.898148|
| 6000 |	0.042200  |     0.320418   |   0.868416	     |   0.879074   | 0.873713 |   0.937497	    | 0.877588|	0.833611| 0.907737|

Example
```py
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
tokenizer = AutoTokenizer.from_pretrained("Ambareeshkumar/BERT-Tamil")
model = AutoModelForTokenClassification.from_pretrained("Ambareeshkumar/BERT-Tamil")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "இந்திய"
ner_results = nlp(example)
ner_results
```
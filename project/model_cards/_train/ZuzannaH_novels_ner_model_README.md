---
language:
- pl
pipeline_tag: token-classification
widget:
- text: "– Najświętsza Mario! – krzyknęła Maria i chwyciła za książkę Dostojewskiego, bo tak spodobały jej się słowa Tomasza, która czytał pisma św. Tomasza, mówił o Jezusie, Żeromskim i o swojej koleżance Annie."
---
# Model Card for Novels_NER_model
NER model trained on custom dataset of 58 annotated Polish novels, with the aim to recognize only relevant characters.
## Model description
* finetuned from: Davlan/bert-base-multilingual-cased-ner-hrl 
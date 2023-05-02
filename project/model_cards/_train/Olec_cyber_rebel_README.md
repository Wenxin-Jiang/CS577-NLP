---
pipeline_tag: text2text-generation
tags:
- STIX
- NER
- RE
- CTI
- cyber threat intelligence
metrics:
- f1: 0.4064894147513486
- recall : 0.4463734567901234
- precision : 0.37314814814814806
---
# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->


## Model Details

### Model Description

- Model to extract Relations from cyber threat intelligence(CTI) text.
- This model needs a pre/postprocessing pipeline https://github.com/l0renor/Relation-Extraction-and-Knowledge-Graph-Generation-on-MISP-Event-Reports
- Standalone Model: Olec/cyber_rebel_no_pipe


- **Developed by:** Leon Lukas

- **Model type:** seq2seq
- **Language(s) (NLP): English
- **Finetuned from model : mrmoor/cti-t5-RE-NYT (T5 model trained on NYT RE)

### Metrics test set

- precision: 0.37314814814814806
- recall: 0.4463734567901234,
- f1 : 0.4064894147513486

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/l0renor/Relation-Extraction-and-Knowledge-Graph-Generation-on-MISP-Event-Reports
- **Paper [optional]:** https://github.com/l0renor/Relation-Extraction-and-Knowledge-Graph-Generation-on-MISP-Event-Reports
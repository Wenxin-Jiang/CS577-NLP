---
language:
- en

license: mit

datasets:
- MIMIC-III

widget:
- text: "Due to shortness of breath, the patient is diagnosed with [MASK], and other respiratory problems."
  example_title: "Example 1"
---

# ClinicalPubMedBERT
## Description

A BERT model pre-trained on PubMed abstracts, and continual pre-trained on clinical notes ([MIMIC-III](https://mimic.physionet.org/)). We try combining two domains that have fewer overlaps with general knowledge text corpora: EHRs and biomedical papers. We hope this model can serve better results on clinical-related downstream tasks such as readmissions. 

This model is trained on 500000 clinical notes randomly sampled from MIMIC datasets, with 120k steps of training. We also used whole word masking to enhance the coherence of the language model. All notes are chunked into a length of 128 tokens.

Pre-trained model: https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract
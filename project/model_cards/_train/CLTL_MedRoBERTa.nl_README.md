---
language: nl
license: mit

---

# MedRoBERTa.nl

## Description
This model is a RoBERTa-based model pre-trained from scratch on Dutch hospital notes sourced from Electronic Health Records. The model is not fine-tuned. All code used for the creation of MedRoBERTa.nl can be found at https://github.com/cltl-students/verkijk_stella_rma_thesis_dutch_medical_language_model.

## Intended use
The model can be fine-tuned on any type of task. Since it is a domain-specific model trained on medical data, it is meant to be used on medical NLP tasks for Dutch.  

## Data
The model was trained on nearly 10 million hospital notes from the Amsterdam University Medical Centres. The training data was anonymized before starting the pre-training procedure. 

## Privacy
By anonymizing the training data we made sure the model did not learn any representative associations linked to names. Apart from the training data, the model's vocabulary was also anonymized. This ensures that the model can not predict any names in the generative fill-mask task. 

## Authors
Stella Verkijk, Piek Vossen

## Reference
Paper: Verkijk, S. & Vossen, P. (2022) MedRoBERTa.nl: A Language Model for Dutch Electronic Health Records. Computational Linguistics in the Netherlands Journal, 11.
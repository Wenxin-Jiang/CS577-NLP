---
language:
- en

---
# Model Card for Password-Model

 
# Model Details
 
## Model Description
 
 
The Password Model is intended to be used with [Credential Digger](https://github.com/SAP/credential-digger) in order to automatically filter false positive password discoveries.
 
- **Developed by:** SAP OSS
- **Shared by [Optional]:** Hugging Face
- **Model type:** Text Classification
- **Language(s) (NLP):** en
- **License:** Apache-2.0
- **Related Models:** 
  - **Parent Model:** RoBERTa
- **Resources for more information:**
  - [GitHub Repo](https://github.com/SAP/credential-digger) 
  - [Associated Paper](https://www.scitepress.org/Papers/2021/102381/102381.pdf) 
 
# Uses
 
 
## Direct Use
The model is directly integrated into [Credential Digger]((https://github.com/SAP/credential-digger) and can be used to filter the false positive password discoveries of a scan.
 

## Out-of-Scope Use
 
The model should not be used to intentionally create hostile or alienating environments for people. 
 
 
# Training Details
 
## Training Data
 
[CodeBERT-base-mlm](https://huggingface.co/microsoft/codebert-base-mlm) fine-tuned on a dataset for leak detection.
 
 
## Training Procedure
 
 
### Preprocessing
 
More information needed
 
### Speeds, Sizes, Times
 
More information needed
 
# Evaluation
 
More information needed
 
## Testing Data, Factors & Metrics
 
### Testing Data
 
More information needed
 
### Factors
 
More information needed
 
### Metrics
 
More information needed
 
## Results 
 
More information needed
 
 
# Model Examination
More information needed
 
# Environmental Impact
 
Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).
 
- **Hardware Type:** More information needed
- **Hours used:** More information needed
- **Cloud Provider:** More information needed
- **Compute Region:** More information needed
- **Carbon Emitted:** More information needed
 
# Technical Specifications [optional]
 
## Model Architecture and Objective
 
More information needed
 
## Compute Infrastructure
More information needed
 
### Hardware
 
More information needed
 
### Software
 
More information needed
 
 
# Citation
 
**BibTeX:**
 
```
TBD
```
 
# Model Card Authors [optional]
 
SAP OSS in collaboration with Ezi Ozoani and the Hugging Face team.
 
# Model Card Contact
 
More information needed

# How to Get Started with the Model
 
The model is directly integrated into Credential Digger and can be used to filter the false positive discoveries of a scan
 
<details>
<summary> Click to expand </summary>

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
 
tokenizer = AutoTokenizer.from_pretrained("SAPOSS/password-model")
 
model = AutoModelForSequenceClassification.from_pretrained("SAPOSS/password-model")
 
 ```
</details>

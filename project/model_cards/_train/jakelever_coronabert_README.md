---
language: en
thumbnail: https://coronacentral.ai/logo-with-name.png?1
tags:
- coronavirus
- covid
- bionlp
datasets:
- cord19
- pubmed
license: mit
widget:
- text: "Pre-existing T-cell immunity to SARS-CoV-2 in unexposed healthy controls in Ecuador, as detected with a COVID-19 Interferon-Gamma Release Assay."
- text: "Lifestyle and mental health disruptions during COVID-19."
- text: "More than 50 Long-term effects of COVID-19: a systematic review and meta-analysis"
---
# CoronaCentral BERT Model for Topic / Article Type Classification

This is the topic / article type multi-label classification for the [CoronaCentral website](https://coronacentral.ai). This forms part of the pipeline for downloading and processing coronavirus literature described in the [corona-ml repo](https://github.com/jakelever/corona-ml) with available [step-by-step descriptions](https://github.com/jakelever/corona-ml/blob/master/stepByStep.md). The method is described in the [preprint](https://doi.org/10.1101/2020.12.21.423860) and detailed performance results can be found in the [machine learning details](https://github.com/jakelever/corona-ml/blob/master/machineLearningDetails.md) document.

This model was derived by fine-tuning the [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract) model on this coronavirus sequence (document) classification task.

## Usage

Below are two Google Colab notebooks with example usage of this sequence classification model using HuggingFace transformers and KTrain.

- [HuggingFace example on Google Colab](https://colab.research.google.com/drive/1cBNgKd4o6FNWwjKXXQQsC_SaX1kOXDa4?usp=sharing)
- [KTrain example on Google Colab](https://colab.research.google.com/drive/1h7oJa2NDjnBEoox0D5vwXrxiCHj3B1kU?usp=sharing)

## Training Data

The model is trained on ~3200 manually-curated articles sampled at various stages during the coronavirus pandemic. The code for training is available in the [category\_prediction](https://github.com/jakelever/corona-ml/tree/master/category_prediction) directory of the main Github Repo. The data is available in the [annotated_documents.json.gz](https://github.com/jakelever/corona-ml/blob/master/category_prediction/annotated_documents.json.gz) file.

## Inputs and Outputs

The model takes in a tokenized title and abstract (combined into a single string and separated by a new line). The outputs are topics and article types, broadly called categories in the pipeline code. The types are listed below. Some others are managed by hand-coded rules described in the [step-by-step descriptions](https://github.com/jakelever/corona-ml/blob/master/stepByStep.md).

### List of Article Types 

- Comment/Editorial
- Meta-analysis
- News
- Review

### List of Topics

- Clinical Reports
- Communication
- Contact Tracing
- Diagnostics
- Drug Targets
- Education
- Effect on Medical Specialties
- Forecasting & Modelling
- Health Policy
- Healthcare Workers
- Imaging
- Immunology
- Inequality
- Infection Reports
- Long Haul
- Medical Devices
- Misinformation
- Model Systems & Tools
- Molecular Biology
- Non-human
- Non-medical
- Pediatrics
- Prevalence
- Prevention
- Psychology
- Recommendations
- Risk Factors
- Surveillance
- Therapeutics
- Transmission
- Vaccines

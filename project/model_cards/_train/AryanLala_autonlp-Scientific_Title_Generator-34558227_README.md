---
tags: autonlp
language: en
widget: 
- text: "The scale, variety, and quantity of publicly-available NLP datasets has grown rapidly as researchers propose new tasks, larger models, and novel benchmarks. Datasets is a community library for contemporary NLP designed to support this ecosystem. Datasets aims to standardize end-user interfaces, versioning, and documentation, while providing a lightweight front-end that behaves similarly for small datasets as for internet-scale corpora. The design of the library incorporates a distributed, community-driven approach to adding datasets and documenting usage. After a year of development, the library now includes more than 650 unique datasets, has more than 250 contributors, and has helped support a variety of novel cross-dataset research projects and shared tasks. The library is available at https://github.com/huggingface/datasets."
datasets:
- AryanLala/autonlp-data-Scientific_Title_Generator
co2_eq_emissions: 137.60574081887984
---

# Model Trained Using AutoNLP
- Model: Google's Pegasus (https://huggingface.co/google/pegasus-xsum)
- Problem type: Summarization
- Model ID: 34558227
- CO2 Emissions (in grams): 137.60574081887984
- Spaces: https://huggingface.co/spaces/TitleGenerators/ArxivTitleGenerator
- Dataset: arXiv Dataset (https://www.kaggle.com/Cornell-University/arxiv)
- Data subset used: https://huggingface.co/datasets/AryanLala/autonlp-data-Scientific_Title_Generator

## Validation Metrics

- Loss: 2.578599214553833
- Rouge1: 44.8482
- Rouge2: 24.4052
- RougeL: 40.1716
- RougeLsum: 40.1396
- Gen Len: 11.4675

## Social
- LinkedIn: https://www.linkedin.com/in/aryanlala/
- Twitter: https://twitter.com/AryanLala20

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/AryanLala/autonlp-Scientific_Title_Generator-34558227
```
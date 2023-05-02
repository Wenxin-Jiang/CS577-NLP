
---
language:
- en
tags:
- table-question-answering
license: apache-2.0
datasets:
- sqa
metrics:
- bleu

---

# TABLE QUESTION ANSWERING

## TAPAS model
TAPAS, the model learns an inner representation of the English language used in tables and associated texts, which can then be used to extract features useful for downstream tasks such as answering questions about a table, or determining whether a sentence is entailed or refuted by the contents of a table.

## Model description
- It is a BERT-based model specifically designed (and pre-trained) for answering questions about tabular data
- TAPAS uses relative position embeddings and has 7 token types that encode tabular structure.
- It is pre-trained on the masked language modeling (MLM) objective on a large dataset comprising millions of tables from English Wikipedia and corresponding texts.

The model has been fine-tuned on several datasets

1. SQA (Sequential Question Answering by Microsoft) 
2. WTQ (Wiki Table Questions by Stanford University) 
3. WikiSQL (by Salesforce). 

## Limitations

Unable to deal with large input files



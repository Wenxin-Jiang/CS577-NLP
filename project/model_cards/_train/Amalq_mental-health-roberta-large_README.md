---
language: en
tags:
- Transformers
license: mit
datasets:
- SMHD
---

# MentalHealth-RoBERTa model:
MentalHealth-RoBERTa is a roberta-large model (https://huggingface.co/roberta-large ) fine-tuned on a SMHD corpus.  
[SMHD: A Large-Scale Resource for Exploring Online Language Usage for Multiple Mental Health Conditions] (https://ir.cs.georgetown.edu/resources/smhd.html). 
We follow the standard pretraining protocols of RoBERTa with [Huggingface’s Transformers library](https://github.com/huggingface/transformers).    

## Usage Load the model via [Huggingface’s Transformers library](https://github.com/huggingface/transformers):   

from transformers import AutoTokenizer,    
AutoModel tokenizer = AutoTokenizer.from_pretrained("Amalq/mental-health-roberta-large")    
model = AutoModel.from_pretrained("Amalq/mental-health-roberta-large")   


Perplexity of this model is: 3.88
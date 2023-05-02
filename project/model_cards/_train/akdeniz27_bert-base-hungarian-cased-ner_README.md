---
language: hu
widget:
- text: "Karikó Katalin megkapja Szeged díszpolgárságát."
---
# Hungarian Named Entity Recognition (NER) Model
This model is the fine-tuned model of "SZTAKI-HLT/hubert-base-cc" 
using the famous WikiANN dataset presented
in the "Cross-lingual Name Tagging and Linking for 282 Languages" [paper](https://aclanthology.org/P17-1178.pdf).

# Fine-tuning parameters:
```
task = "ner"
model_checkpoint = "SZTAKI-HLT/hubert-base-cc"
batch_size = 8 
label_list = ['O', 'B-PER', 'I-PER', 'B-ORG', 'I-ORG', 'B-LOC', 'I-LOC']
max_length = 512 
learning_rate = 2e-5 
num_train_epochs = 3 
weight_decay = 0.01 
```
# How to use: 
```
model = AutoModelForTokenClassification.from_pretrained("akdeniz27/bert-base-hungarian-cased-ner")
tokenizer = AutoTokenizer.from_pretrained("akdeniz27/bert-base-hungarian-cased-ner")
ner = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="first")
ner("<your text here>")
```
Pls refer "https://huggingface.co/transformers/_modules/transformers/pipelines/token_classification.html" for entity grouping with aggregation_strategy parameter.

# Reference test results:
* accuracy: 0.9774538310923768
* f1: 0.9462099085573904
* precision: 0.9425718667406271
* recall: 0.9498761426661113
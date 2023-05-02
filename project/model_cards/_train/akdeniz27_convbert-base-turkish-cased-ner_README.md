---
language: tr
widget:
- text: "Almanya, koronavirüs aşısını geliştiren Dr. Özlem Türeci ve eşi Prof. Dr. Uğur Şahin'e liyakat nişanı verdi"
---
# Turkish Named Entity Recognition (NER) Model
This model is the fine-tuned model of dbmdz/convbert-base-turkish-cased (ConvBERTurk)
using a reviewed version of well known Turkish NER dataset
 
(https://github.com/stefan-it/turkish-bert/files/4558187/nerdata.txt).

The ConvBERT architecture is presented in the ["ConvBERT: Improving BERT with Span-based Dynamic Convolution"](https://arxiv.org/abs/2008.02496) paper.

# Fine-tuning parameters:
```
task = "ner"
model_checkpoint = "dbmdz/convbert-base-turkish-cased"
batch_size = 8 
label_list = ['O', 'B-PER', 'I-PER', 'B-ORG', 'I-ORG', 'B-LOC', 'I-LOC']
max_length = 512 
learning_rate = 2e-5 
num_train_epochs = 3 
weight_decay = 0.01 
```
# How to use: 
```
model = AutoModelForTokenClassification.from_pretrained("akdeniz27/convbert-base-turkish-cased-ner")
tokenizer = AutoTokenizer.from_pretrained("akdeniz27/convbert-base-turkish-cased-ner")
ner = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="first")
ner("<your text here>")

# Pls refer "https://huggingface.co/transformers/_modules/transformers/pipelines/token_classification.html" for entity grouping with aggregation_strategy parameter.
```
# Reference test results:
* accuracy: 0.9937648915431506
* f1: 0.9610945644080416
* precision: 0.9619899385131359
* recall: 0.9602008554956295
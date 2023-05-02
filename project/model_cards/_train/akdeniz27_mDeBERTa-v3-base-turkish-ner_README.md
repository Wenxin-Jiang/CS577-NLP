---
language: tr
widget:
- text: "Mustafa Kemal Atatürk 19 Mayıs 1919'da Samsun'a çıktı."
---
# Turkish Named Entity Recognition (NER) Model
This model is the fine-tuned version of "microsoft/mDeBERTa-v3-base"
(a multilingual version of DeBERTa V3) 
using a reviewed version of well known Turkish NER dataset 
(https://github.com/stefan-it/turkish-bert/files/4558187/nerdata.txt).
# Fine-tuning parameters:
```
task = "ner"
model_checkpoint = "microsoft/mdeberta-v3-base"
batch_size = 8 
label_list = ['O', 'B-PER', 'I-PER', 'B-ORG', 'I-ORG', 'B-LOC', 'I-LOC']
max_length = 512 
learning_rate = 2e-5 
num_train_epochs = 2 
weight_decay = 0.01 
```
# How to use: 
```
model = AutoModelForTokenClassification.from_pretrained("akdeniz27/mDeBERTa-v3-base-turkish-ner")
tokenizer = AutoTokenizer.from_pretrained("akdeniz27/mDeBERTa-v3-base-turkish-ner")
ner = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
ner("<your text here>")
```
Pls refer "https://huggingface.co/transformers/_modules/transformers/pipelines/token_classification.html" for entity grouping with aggregation_strategy parameter.
# Reference test results:
* f1: 0.95
* precision: 0.94
* recall: 0.96
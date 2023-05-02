---
language: tr
widget:
- text: "Mustafa Kemal Atatürk 19 Mayıs 1919'da Samsun'a çıktı."
---

# Turkish Named Entity Recognition (NER) Model

This model is the fine-tuned model of "dbmdz/bert-base-turkish-cased" 
using a reviewed version of well known Turkish NER dataset 
(https://github.com/stefan-it/turkish-bert/files/4558187/nerdata.txt).

# Fine-tuning parameters:
```
task = "ner"
model_checkpoint = "dbmdz/bert-base-turkish-cased"
batch_size = 8 
label_list = ['O', 'B-PER', 'I-PER', 'B-ORG', 'I-ORG', 'B-LOC', 'I-LOC']
max_length = 512 
learning_rate = 2e-5 
num_train_epochs = 3 
weight_decay = 0.01 
```

# How to use: 
```
model = AutoModelForTokenClassification.from_pretrained("akdeniz27/bert-base-turkish-cased-ner")
tokenizer = AutoTokenizer.from_pretrained("akdeniz27/bert-base-turkish-cased-ner")
ner = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="first")
ner("your text here")
```
Pls refer "https://huggingface.co/transformers/_modules/transformers/pipelines/token_classification.html" for entity grouping with aggregation_strategy parameter.

# Reference test results:
* accuracy: 0.9933935699477056
* f1: 0.9592969472710453
* precision: 0.9543530277931161
* recall: 0.9642923563325274

Evaluation results with the test sets proposed in ["Küçük, D., Küçük, D., Arıcı, N. 2016. Türkçe Varlık İsmi Tanıma için bir Veri Kümesi ("A Named Entity Recognition Dataset for Turkish"). IEEE Sinyal İşleme, İletişim ve Uygulamaları Kurultayı. Zonguldak, Türkiye."](https://ieeexplore.ieee.org/document/7495744) paper.

* Test Set	Acc.	Prec.	Rec.	F1-Score
* 20010000	0.9946  0.9871  0.9463	0.9662
* 20020000	0.9928	0.9134	0.9206	0.9170
* 20030000	0.9942	0.9814	0.9186	0.9489
* 20040000	0.9943	0.9660	0.9522	0.9590
* 20050000	0.9971	0.9539	0.9932	0.9732
* 20060000	0.9993	0.9942	0.9942	0.9942
* 20070000	0.9970	0.9806	0.9439	0.9619
* 20080000	0.9988	0.9821	0.9649	0.9735
* 20090000	0.9977	0.9891	0.9479	0.9681
* 20100000	0.9961	0.9684	0.9293	0.9485
* Overall 	0.9961	0.9720	0.9516	0.9617
---
license: lgpl-lr
language: 
  - "uk"
datasets:
 - UberText
max_length:
- 120
tags:
- summarization
widget:
- text: "15 листопада чисельність населення Землі досягла восьми мільярдів, повідомляє ООН. Зазначають, що нашій планеті знадобилося лише 11 років, щоб вирости з семи до восьми мільярдів. Таке зростання ООН пояснила поступовим збільшенням тривалості життя людини завдяки поліпшенню охорони здоров'я, харчування, особистої гігієни та медицини. Це також результат високого та постійного рівня народжуваності в деяких країнах."

---
The mt5-large model has been finetuned with the data from [Uber](https://lang.org.ua/en/corpora/) corpus in Ukrainian.

The dataset contains around 40K articles about politics, science, technology, social life collected until December 2021 from Hromadske.ua.

##### Load the model and mt tokenizer :
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("google/mt5-large")

model = AutoModelForSeq2SeqLM.from_pretrained("SGaleshchuk/t5-large-ua-news")

summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, framework="pt")
##### Try on your example

summary = summarizer("15 листопада чисельність населення Землі досягла восьми мільярдів, повідомляє ООН. Зазначають, що нашій планеті знадобилося лише 11 років, щоб вирости з семи до восьми мільярдів. Таке зростання ООН пояснила поступовим збільшенням тривалості життя людини завдяки поліпшенню охорони здоров'я, харчування, особистої гігієни та медицини. Це також результат високого та постійного рівня народжуваності в деяких країнах.", min_length=3, max_length = 128)
print(summary)
[{'summary_text': 'Чисельність населення Землі зросла до восьми мільярдів. '}]
```




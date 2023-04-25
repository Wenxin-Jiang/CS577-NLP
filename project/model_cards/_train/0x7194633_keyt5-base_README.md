---
language:
- ru
license: mit
inference:
  parameters:
    top_p: 0.9
widget:
- text: "В России может появиться новый штамм коронавируса «омикрон», что может привести к подъему заболеваемости в январе, заявил доцент кафедры инфекционных болезней РУДН Сергей Вознесенский. Он отметил, что вариант «дельта» вызывал больше летальных случаев, чем омикрон, именно на фоне «дельты» была максимальная летальность."
  example_title: "Коронавирус"
- text: "Начальника штаба обороны Великобритании адмирала Тони Радакина заставили имитировать активность во время визита в ангар с тяжелым вооружением, сообщила британская пресса. В приказе говорилось, что военнослужащим было велено подбегать к автомобилям, открывать все люки, затворы, листать руководство по эксплуатации и осматриваться машины, будто проводится функциональный тест для обеспечения правильной работы оборудования."
  example_title: "Британия"
- text: "Для воспроизведения музыки достаточно нажимать на кнопки клавиатуры. Каждой клавише соответствует определенный семпл — есть маракасы и футуристичные звуки, напоминающие выстрелы бластеров. Из всего многообразия можно формировать собственные паттерны и наблюдать за визуализацией с анимированными геометрическими фигурами. Что интересно, нажатием клавиши пробел можно полностью переменить оформление, цвета на экране и звучание семплов."
  example_title: "Технологии"
---
## keyT5. Base (small) version
[![0x7o - text2keywords](https://img.shields.io/static/v1?label=0x7o&message=text2keywords&color=blue&logo=github)](https://github.com/0x7o/text2keywords "Go to GitHub repo")
[![stars - text2keywords](https://img.shields.io/github/stars/0x7o/text2keywords?style=social)](https://github.com/0x7o/text2keywords)
[![forks - text2keywords](https://img.shields.io/github/forks/0x7o/text2keywords?style=social)](https://github.com/0x7o/text2keywords)

Supported languages: ru

Github - [text2keywords](https://github.com/0x7o/text2keywords)


[Pretraining Large version](https://huggingface.co/0x7194633/keyt5-large)
|
[Pretraining Base version](https://huggingface.co/0x7194633/keyt5-base)

# Usage
Example usage (the code returns a list with keywords. duplicates are possible):

[![Try Model Training In Colab!](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/0x7o/text2keywords/blob/main/example/keyT5_use.ipynb)

```
pip install transformers sentencepiece
```

```python
from itertools import groupby
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
model_name = "0x7194633/keyt5-large" # or 0x7194633/keyt5-base
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def generate(text, **kwargs):
    inputs = tokenizer(text, return_tensors='pt')
    with torch.no_grad():
        hypotheses = model.generate(**inputs, num_beams=5, **kwargs)
    s = tokenizer.decode(hypotheses[0], skip_special_tokens=True)
    s = s.replace('; ', ';').replace(' ;', ';').lower().split(';')[:-1]
    s = [el for el, _ in groupby(s)]
    return s

article = """Reuters сообщил об отмене 3,6 тыс. авиарейсов из-за «омикрона» и погоды
Наибольшее число отмен авиарейсов 2 января пришлось на американские авиакомпании 
SkyWest и Southwest, у каждой — более 400 отмененных рейсов. При этом среди 
отмененных 2 января авиарейсов — более 2,1 тыс. рейсов в США. Также свыше 6400 
рейсов были задержаны."""

print(generate(article, top_p=1.0, max_length=64))  
# ['авиаперевозки', 'отмена авиарейсов', 'отмена рейсов', 'отмена авиарейсов', 'отмена рейсов', 'отмена авиарейсов']
```
# Training
Go to the training notebook and learn more about it:

[![Try Model Training In Colab!](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/0x7o/text2keywords/blob/main/example/keyT5_train.ipynb)

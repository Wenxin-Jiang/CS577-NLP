---
language:
- ru
tags:
- summarization
- token-classification
- t5
datasets:
- IlyaGusev/gazeta
license: apache-2.0
inference: false
widget:
- text: "С 1 сентября в России вступают в силу поправки в закон «О банкротстве» — теперь должники смогут освобождаться от непосильных обязательств во внесудебном порядке, если сумма задолженности составляет не менее 50 тыс. рублей и не превышает 500 тыс. рублей без учета штрафов, пени, процентов за просрочку платежа и прочих имущественных или финансовых санкций.[SEP]У физлиц и индивидуальных предпринимателей появилась возможность пройти процедуру банкротства без участия суда и финансового управляющего — достаточно подать соответствующее заявление через МФЦ.[SEP]Сумму задолженности и список всех известных заявителю кредиторов нужно предоставить самостоятельно.[SEP]Если все условия соблюдены, сведения внесут в Единый федеральный реестр в течение трех рабочих дней.[SEP]При этом на момент подачи заявления в отношении заявителя должно быть окончено исполнительное производство с возвращением исполнительного документа взыскателю.[SEP]Это значит, что у потенциального банкрота не должно быть имущества, которое можно взыскать.[SEP]Кроме того, в отношении гражданина не должно быть возбуждено другое исполнительное производство.[SEP]В период всей процедуры заявитель не сможет брать займы, кредиты, выдавать поручительства, совершать иные обеспечительные сделки.[SEP]Внесудебное банкротство будет длиться шесть месяцев, в течение которых также будет действовать мораторий на удовлетворение требований кредиторов, отмеченных в заявлении должника, и мораторий об уплате обязательных платежей.[SEP]Кроме того, прекращается начисление неустоек и иных финансовых санкций; имущественные взыскания (кроме алиментов) также будут приостановлены.[SEP]По завершению процедуры заявителя освободят от дальнейшего выполнения требований кредиторов, указанных в заявлении о признании его банкротом, а эта задолженность признается безнадежной.[SEP]В прошлом месяце стало известно, что за первое полугодие 2020 года российские суды признали банкротами 42,7 тыс. граждан (в том числе индивидуальных предпринимателей) — по данным единого реестра «Федресурс», это на 47,2% больше показателя аналогичного периода 2019 года.[SEP]Рост числа обанкротившихся граждан во втором квартале по сравнению с первым замедлился — такая динамика обусловлена тем, что в период ограничений с 19 марта по 11 мая суды редко рассматривали банкротные дела компаний и меньше, чем обычно, в отношении граждан, объяснял руководитель проекта «Федресурс» Алексей Юхнин.[SEP]"
  example_title: "Новости"
  
---

# RuBERTExtSumGazeta

## Model description

Model for extractive summarization based on [rubert-base-cased](DeepPavlov/rubert-base-cased)

## Intended uses & limitations

#### How to use

Colab: [link](https://colab.research.google.com/drive/1Q8_v3H-kxdJhZIiyLYat7Kj02qDq7M1L)

```python
import razdel
from transformers import AutoTokenizer, BertForTokenClassification

model_name = "IlyaGusev/rubert_ext_sum_gazeta"

tokenizer = AutoTokenizer.from_pretrained(model_name)
sep_token = tokenizer.sep_token
sep_token_id = tokenizer.sep_token_id

model = BertForTokenClassification.from_pretrained(model_name)

article_text = "..."
sentences = [s.text for s in razdel.sentenize(article_text)]
article_text = sep_token.join(sentences)

inputs = tokenizer(
    [article_text],
    max_length=500,
    padding="max_length",
    truncation=True,
    return_tensors="pt",
)
sep_mask = inputs["input_ids"][0] == sep_token_id

# Fix token_type_ids
current_token_type_id = 0 
for pos, input_id in enumerate(inputs["input_ids"][0]):
    inputs["token_type_ids"][0][pos] = current_token_type_id
    if input_id == sep_token_id:
        current_token_type_id = 1 - current_token_type_id

# Infer model
with torch.no_grad(): 
    outputs = model(**inputs) 
logits = outputs.logits[0, :, 1]

# Choose sentences 
logits = logits[sep_mask]
logits, indices = logits.sort(descending=True)
logits, indices = logits.cpu().tolist(), indices.cpu().tolist()
pairs = list(zip(logits, indices))
pairs = pairs[:3]
indices = list(sorted([idx for _, idx in pairs]))
summary = " ".join([sentences[idx] for idx in indices])
print(summary)
```

#### Limitations and bias

- The model should work well with Gazeta.ru articles, but for any other agencies it can suffer from domain shift


## Training data

- Dataset: [Gazeta](https://huggingface.co/datasets/IlyaGusev/gazeta)

## Training procedure

TBD

## Eval results

TBD

Evaluation: https://github.com/IlyaGusev/summarus/blob/master/evaluate.py

Flags: --language ru --tokenize-after --lower

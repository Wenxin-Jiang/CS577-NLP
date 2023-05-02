---
widget:
- text: "El dólar se dispara tras la reunión de la Fed"
---


# Spanish News Classification Headlines

SNCH: this model was developed by [M47Labs](https://www.m47labs.com/es/)  the goal is text classification, the base model use was [BETO](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased), however this model has not been fine-tuned on any dataset. The objective is to show the performance of this model when is used with the objective of inference without training at all.


## Dataset validation Sample

Dataset size : 1000

Columns: idTask,task content 1,idTag,tag.

|task content|tag|
|------|------|
|Alcalá de Guadaíra celebra la IV Semana de la Diversidad Sexual con acciones de sensibilización|sociedad|
|El Archipiélago Chinijo Graciplus se impone en el Trofeo Centro Comercial Rubicón|deportes|
|Un total de 39 personas padecen ELA actualmente en la provincia|sociedad|
|Eurocopa 2021 : Italia vence a Gales y pasa a octavos con su candidatura reforzada|deportes|
|Resolución de 10 de junio de 2021, del Ayuntamiento de Tarazona de La Mancha (Albacete), referente a la convocatoria para proveer una plaza.|sociedad|
|El primer ministro sueco pierde una moción de censura|politica|
|El dólar se dispara tras la reunión de la Fed|economia|


## Labels:

 * ciencia_tecnologia
 
 * clickbait
 
 * cultura 
 
 * deportes
 
 * economia
 
 * educacion
 
 * medio_ambiente
 
 * opinion
 
 * politica
 
 * sociedad
 


## Example of Use

### Pipeline

```{python}

import torch
from transformers import AutoTokenizer, BertForSequenceClassification,TextClassificationPipeline


review_text = 'los vehiculos que esten esperando pasajaeros deberan estar apagados para reducir emisiones'
path = "M47Labs/spanish_news_classification_headlines_untrained"
tokenizer = AutoTokenizer.from_pretrained(path)
model = BertForSequenceClassification.from_pretrained(path)


nlp = TextClassificationPipeline(task = "text-classification",
                model = model,
                tokenizer = tokenizer)

print(nlp(review_text))

```

```[{'label': 'medio_ambiente', 'score': 0.2834321384291023}]```

### Pytorch

```{python}

import torch
from transformers import AutoTokenizer, BertForSequenceClassification,TextClassificationPipeline
from numpy import np

model_name  = 'M47Labs/spanish_news_classification_headlines_untrained'
MAX_LEN = 32


tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSequenceClassification.from_pretrained(model_name)

texto = "las emisiones estan bajando, debido a las medidas ambientales tomadas por el gobierno"


encoded_review = tokenizer.encode_plus(
  texto,
  max_length=MAX_LEN,
  add_special_tokens=True,
  #return_token_type_ids=False,
  pad_to_max_length=True,
  return_attention_mask=True,
  return_tensors='pt',
)

input_ids = encoded_review['input_ids']
attention_mask = encoded_review['attention_mask']
output = model(input_ids, attention_mask)

_, prediction = torch.max(output['logits'], dim=1)
print(f'Review text: {texto}')

print(f'Sentiment  : {model.config.id2label[prediction.detach().cpu().numpy()[0]]}')

```

```Review text: las emisiones estan bajando, debido a las medidas ambientales tomadas por el gobierno```


```Sentiment  : opinion```


A more in depth example on how to use the model can be found in this colab notebook: https://colab.research.google.com/drive/1XsKea6oMyEckye2FePW_XN7Rf8v41Cw_?usp=sharing
 

## Validation Results
 
|Full Dataset||
|------|------|
|Accuracy Score|0.362|
|Precision (Macro)|0.21|
|Recall (Macro)|0.22|



 ![alt text](https://media-exp1.licdn.com/dms/image/C4D0BAQHpfgjEyhtE1g/company-logo_200_200/0/1625210573748?e=1638403200&v=beta&t=toQNpiOlyim5Ja4f7Ejv8yKoCWifMsLWjkC7XnyXICI "Logo M47")

---
widget:
- text: "El dólar se dispara tras la reunión de la Fed"
---


# Spanish News Classification Headlines

SNCH: this model was develop by [M47Labs](https://www.m47labs.com/es/)  the goal is text classification, the base model use was [BETO](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased), it was fine-tuned on 1000 example dataset.


## Dataset Sample

Dataset size : 1000

Columns: idTask,task content 1,idTag,tag.

|idTask|task content 1|idTag|tag|
|------|------|------|------|
|3637d9ac-119c-4a8f-899c-339cf5b42ae0|Alcalá de Guadaíra celebra la IV Semana de la Diversidad Sexual con acciones de sensibilización|81b36360-6cbf-4ffa-b558-9ef95c136714|sociedad|
|d56bab52-0029-45dd-ad90-5c17d4ed4c88|El Archipiélago Chinijo Graciplus se impone en el Trofeo Centro Comercial Rubicón|ed198b6d-a5b9-4557-91ff-c0be51707dec|deportes|
|dec70bc5-4932-4fa2-aeac-31a52377be02|Un total de 39 personas padecen ELA actualmente en la provincia|81b36360-6cbf-4ffa-b558-9ef95c136714|sociedad|
|fb396ba9-fbf1-4495-84d9-5314eb731405|Eurocopa 2021 : Italia vence a Gales y pasa a octavos con su candidatura reforzada|ed198b6d-a5b9-4557-91ff-c0be51707dec|deportes|
|bc5a36ca-4e0a-422e-9167-766b41008c01|Resolución de 10 de junio de 2021, del Ayuntamiento de Tarazona de La Mancha (Albacete), referente a la convocatoria para proveer una plaza.|81b36360-6cbf-4ffa-b558-9ef95c136714|sociedad|
|a87f8703-ce34-47a5-9c1b-e992c7fe60f6|El primer ministro sueco pierde una moción de censura|209ae89e-55b4-41fd-aac0-5400feab479e|politica|
|d80bdaad-0ad5-43a0-850e-c473fd612526|El dólar se dispara tras la reunión de la Fed|11925830-148e-4890-a2bc-da9dc059dc17|economia|


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
path = "M47Labs/spanish_news_classification_headlines"
tokenizer = AutoTokenizer.from_pretrained(path)
model = BertForSequenceClassification.from_pretrained(path)


nlp = TextClassificationPipeline(task = "text-classification",
                model = model,
                tokenizer = tokenizer)

print(nlp(review_text))

```

```[{'label': 'medio_ambiente', 'score': 0.5648820996284485}]```

### Pytorch

```{python}

import torch
from transformers import AutoTokenizer, BertForSequenceClassification,TextClassificationPipeline
from numpy import np

model_name  = 'M47Labs/spanish_news_classification_headlines'
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


```Sentiment  : medio_ambiente```


A more in depth example on how to use the model can be found in this colab notebook: https://colab.research.google.com/drive/1XsKea6oMyEckye2FePW_XN7Rf8v41Cw_?usp=sharing


## Finetune Hyperparameters


 * MAX_LEN = 32
 * TRAIN_BATCH_SIZE = 8
 * VALID_BATCH_SIZE = 4
 * EPOCHS = 5
 * LEARNING_RATE = 1e-05
 
## Train Results

|n_example|epoch|loss|acc|
|------|------|------|------|
|100|0|2.286327266693115|12.5|
|100|1|2.018876111507416|40.0|
|100|2|1.8016730904579163|43.75|
|100|3|1.6121837735176086|46.25|
|100|4|1.41565443277359|68.75|
 
|n_example|epoch|loss|acc|
|------|------|------|------|
|500|0|2.0770938420295715|24.5|
|500|1|1.6953029704093934|50.25|
|500|2|1.258900796175003|64.25|
|500|3|0.8342628020048142|78.25|
|500|4|0.5135736921429634|90.25|
 
|n_example|epoch|loss|acc|
|------|------|------|------|
|1000|0|1.916002897115854|36.1997226074896|
|1000|1|1.2941598492664295|62.2746185852982|
|1000|2|0.8201534710415117|76.97642163661581|
|1000|3|0.524806430051615|86.9625520110957|
|1000|4|0.30662027455784463|92.64909847434119|

## Validation Results
 
|n_examples|100|
|------|------|
|Accuracy Score|0.35|
|Precision (Macro)|0.35|
|Recall (Macro)|0.16|

|n_examples|500|
|------|------|
|Accuracy Score|0.62|
|Precision (Macro)|0.60|
|Recall (Macro)|0.47|

|n_examples|1000|
|------|------|
|Accuracy Score|0.68|
|Precision(Macro)|0.68|
|Recall (Macro)|0.64|



 ![alt text](https://media-exp1.licdn.com/dms/image/C4D0BAQHpfgjEyhtE1g/company-logo_200_200/0/1625210573748?e=1638403200&v=beta&t=toQNpiOlyim5Ja4f7Ejv8yKoCWifMsLWjkC7XnyXICI "Logo M47")


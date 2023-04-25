---
language:
- en

pipeline_tag: text-classification

---



# bert-base-cased-sentiment

Es un modelo de BERT (bert-base-cased) afinado para el analisis de sentimientos para dos clases.

El sentimiento solo se define como positivo negativo según sea el caso de la oración suministrada.

## Training data

El set de datos utilizado para el entrenamiento del modelo fue a traves de una recopilación de reseñas de amazón, el cual se puede descargar desde el autor original en Kaggle [Adam Bittlingmayer](https://www.kaggle.com/bittlingmayer/amazonreviews) Amazon Reviews for Sentiment Analysis.

El numero de datos fue solo de 40 000 oraciones de las cuales solo se tomaron las primeras 100 palabras para conformar cada una de las oraciones.

## Accuaracy
El modelo afinado fue sometido a 3 pruebas para conocer su precisión.

- La primera prueba fue en un set de datos de Reseñas de hoteles
| Accuracy (Precisión) |
| -------- | 
|  95% | 

- La segunda prueba fue en un set de datos de Reseñas de comida
| Accuracy (Precisión) |
| -------- | 
|  88% | 

- La tercera prueba fue en un set de datos de Sentimientos generales
| Accuracy (Precisión) |
| -------- |
| 65%  | 

## Contact

Contacto a traves de github [Murdoocc7](https://github.com/murdoocc)
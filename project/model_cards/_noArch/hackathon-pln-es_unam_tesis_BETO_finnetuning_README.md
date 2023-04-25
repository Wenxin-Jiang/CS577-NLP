---
annotations_creators: 
- inoid
- MajorIsaiah
- Ximyer
- clavel
tags: 
- "transformers"
- "text-classification"
languages: "es"
license: "apache-2.0"
datasets: "unam_tesis"
metrics: "accuracy"
widget: 
- text: "Introducción al análisis de riesgos competitivos bajo el enfoque de la función de incidencia acumulada (FIA) y su aplicación con R"
- text: "Asociación del polimorfismo rs1256031 del receptor beta de estrógenos en pacientes con diabetes tipo 2"
---

# Unam_tesis_beto_finnetuning: Unam's thesis classification with BETO 

This model is created from the finetuning of the pre-model
for Spanish [BETO](https://huggingface.co/dccuchile/bert-base-spanish-wwm-uncased), using PyTorch framework, 
and trained with a set of theses of the National Autonomous University of Mexico [(UNAM)](https://tesiunam.dgb.unam.mx/F?func=find-b-0&local_base=TES01). 
The model classifies a text into for five (Psicología, Derecho, Química Farmacéutico Biológica, Actuaría, Economía) 
possible careers at the UNAM.

## Training Dataset 

1000 documents (Thesis introduction, Author´s first name, Author´s last name, Thesis title, Year, Career)

|     Careers |  Size         | 
|--------------|----------------------|
|  Actuaría   |  200    | 
|  Derecho|   200    | 
|  Economía|   200    | 
|  Psicología|   200    | 
|  Química Farmacéutico Biológica|   200    | 

## Example of use

For further details on how to use unam_tesis_BETO_finnetuning you can visit the Hugging Face Transformers library, starting with the Quickstart section. The UNAM tesis model can be accessed simply as 'hackathon-pln-e/unam_tesis_BETO_finnetuning' by using the Transformers library. An example of how to download and use the model can be found next. 

```python

 tokenizer = AutoTokenizer.from_pretrained('hiiamsid/BETO_es_binary_classification', use_fast=False)
 model = AutoModelForSequenceClassification.from_pretrained(
                   'hackathon-pln-es/unam_tesis_BETO_finnetuning', num_labels=5, output_attentions=False,
                  output_hidden_states=False)
 pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, return_all_scores=True)
 
 classificationResult = pipe("Análisis de las condiciones del aprendizaje desde casa en los alumnos de preescolar y primaria del municipio de Nicolás Romero")

```


## Citation

To cite this resource in a publication please use the following:

[UNAM's Tesis with BETO finetuning classify] (https://huggingface.co/hackathon-pln-es/unam_tesis_BETO_finnetuning)

To cite this resource in a publication please use the following:

```
@inproceedings{SpanishNLPHackaton2022,
  title={UNAM's Theses with BETO fine-tuning classify},
  author={López López, Isaac Isaías; Clavel Quintero, Yisel; López Ramos, Dionis & López López, Ximena Yeraldin},
  booktitle={Somos NLP Hackaton 2022},
  year={2022}
}
```

## Team members
- Isaac Isaías López López ([MajorIsaiah](https://huggingface.co/MajorIsaiah))
- Dionis López Ramos ([inoid](https://huggingface.co/inoid))
- Yisel Clavel Quintero ([clavel](https://huggingface.co/clavel))
- Ximena Yeraldin López López ([Ximyer](https://huggingface.co/Ximyer))
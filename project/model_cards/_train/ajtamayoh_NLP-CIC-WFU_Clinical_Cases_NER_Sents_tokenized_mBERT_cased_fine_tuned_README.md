---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: NLP-CIC-WFU_Clinical_Cases_NER_Sents_tokenized_mBERT_cased_fine_tuned
  results: []
  
widget:

- text: 'Se hospitalizó un hombre de 42 años, al que se le había diagnosticado recientemente un carcinoma renal sarcomatoide de células claras metastásico, con fiebre, manejo del dolor por metástasis óseas sintomáticas y para decisiones de tratamiento sistémico de primera línea. El paciente no tenía otros antecedentes. Inicialmente presentó fiebre de 39,0 °C el 12 de marzo de 2020, para la cual recibió ceftriaxona fuera de nuestro centro. El día 6, presentó tos leve y fiebre (38,3°C), lo que llevó a realizar una prueba de PCR en tiempo real para SARS-CoV-2; el resultado fue positivo. El paciente fue ingresado en la sala de COVID-19 de nuestro hospital y se monitorizó estrechamente. La TAC torácica mostró opacidades de vidrio esmerilado bilaterales parcheadas, asociadas al COVID-19 (figura 1). El D7 se le empezó a administrar terapia antivírica con lopinavir y ritonavir (400mg/100mg por vía oral), que se mantuvo durante 5 días, según las directrices locales. El día 8, una disnea súbita y una caída de la saturación obligaron a aumentar el oxígeno a 6 l/min, sin necesidad de ventilación mecánica. Se le administraron dos dosis de tocilizumab, con 8 mg/kg i.v. en cada dosis, separadas 8 horas, con buena tolerancia. Después mostró una mejora clínica, pasando a afebril rápidamente y con un consumo de oxígeno decreciente, que fue retirado por completo el día 12. Una TAC torácica del día 12 confirmó la mejora mostrando regresión parcial de los infiltrados pulmonares y de las opacidades de vidrio esmerilado. La proteína C-reactiva, un marcador indirecto de liberación de citocinas, disminuyó de 225 mg/L a 33 mg/L en 4 días (figura 1). Tras la administración de tocilizumab no se observaron cambios relevantes en las subpoblaciones linfocíticas circulantes y el porcentaje de CD4 + CD25 + linfocitos era alto, antes y después del tocilizumab. Finalmente, el paciente se recuperó totalmente de los síntomas de la COVID-19.'
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NLP-CIC-WFU_Clinical_Cases_NER_Sents_tokenized_mBERT_cased_fine_tuned

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the LivingNER shared task 2022 dataset. It is available at: https://temu.bsc.es/livingner/category/data/

It achieves the following results on the evaluation set:
- Loss: 0.0546
- Precision: 0.8574
- Recall: 0.7366
- F1: 0.7924
- Accuracy: 0.9893

## Model description

For a complete description of our system, please go to: https://ceur-ws.org/Vol-3202/livingner-paper13.pdf


## Training and evaluation data

Dataset provided by LivingNER shared task, it is available at: https://temu.bsc.es/livingner/category/data/

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 7

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0505        | 1.0   | 2568  | 0.0434          | 0.9399    | 0.6781 | 0.7878 | 0.9886   |
| 0.0393        | 2.0   | 5136  | 0.0450          | 0.9384    | 0.6947 | 0.7984 | 0.9892   |
| 0.0306        | 3.0   | 7704  | 0.0451          | 0.9497    | 0.6951 | 0.8027 | 0.9897   |
| 0.0266        | 4.0   | 10272 | 0.0422          | 0.9646    | 0.6904 | 0.8048 | 0.9900   |
| 0.0208        | 5.0   | 12840 | 0.0494          | 0.9576    | 0.6969 | 0.8067 | 0.9902   |
| 0.0141        | 6.0   | 15408 | 0.0506          | 0.8407    | 0.7352 | 0.7844 | 0.9890   |
| 0.0093        | 7.0   | 17976 | 0.0546          | 0.8574    | 0.7366 | 0.7924 | 0.9893   |

### How to cite this work:

Tamayo, A., Burgos, D., & Gelbukh, A. (2022). ParTNER: Paragraph Tuning for Named Entity Recognition on Clinical Cases in Spanish using mBERT+ Rules. In CEUR Workshop Proceedings (Vol. 3202). CEUR-WS.

@inproceedings{tamayo2022partner,
  title={ParTNER: Paragraph Tuning for Named Entity Recognition on Clinical Cases in Spanish using mBERT+ Rules},
  author={Tamayo, Antonio and Burgos, Diego and Gelbukh, Alexander}
}

### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

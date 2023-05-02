---
language: "pt"
widget:
- text: "Dispneia importante aos esforços + dor tipo peso no peito no esforço."
- text: "Obeso, has, icc  c # cintilografia miocardica para avaliar angina. Discreto edema mmii pricn a esquerda."
- text: "Plastia Mitral ( Insuficiencia ), CRM Saf-2Mg e e Saf-3MG ).(09/03/16). Nega palpitação."
- text: "Uso: AAS 100  -1xd; Metoprolol  25 -1xd; FSM -1xd ; Levotiroxina 175  -1xd; Sinva 40 -1xd; Fluoxetina 20-1xd."
- text: "Refere melhora da dispneia depois da cx porem mantem aos mdoeardos-leves esforço."

datasets: 
- TempClinBr
---

# Portuguese NER- TempClinBr - BioBERTpt(clin)

Treinado com BioBERTpt(clin), com o corpus TempClinBr.

Metricas:

```
              precision    recall  f1-score   support

           0       1.00      0.85      0.92        33
           1       0.73      0.69      0.71        78
           2       0.75      0.55      0.63        11
           3       0.70      0.70      0.70        10
           4       0.90      1.00      0.95        71
           5       0.75      0.90      0.82       503
           6       0.83      0.90      0.87       112
           7       0.93      0.90      0.92      2236
           8       0.78      0.50      0.61        28
           9       0.82      0.84      0.83       291
          10       0.79      0.96      0.87       124
          11       0.82      0.73      0.77       420

    accuracy                           0.87      3917
   macro avg       0.82      0.79      0.80      3917
weighted avg       0.88      0.87      0.87      3917

```

Parâmetros:

```
device = cuda (Colab)
nclasses = len(tag2id)
nepochs = 50 => parou na 16
batch_size = 16
batch_status = 32
learning_rate = 3e-5

early_stop = 5
max_length = 256
write_path = 'model'
```

Eval no conjunto de teste - TempClinBr
OBS: Avaliação com tag "O" (label 7), se necessário fazer a média sem essa tag.

```
tag2id ={'<pad>': 12,
 'B-DepartamentoClinico': 2,
 'B-Evidencia': 4,
 'B-Ocorrencia': 10,
 'B-Problema': 5,
 'B-Teste': 6,
 'B-Tratamento': 9,
 'I-DepartamentoClinico': 3,
 'I-Ocorrencia': 8,
 'I-Problema': 11,
 'I-Teste': 0,
 'I-Tratamento': 1,
 'O': 7}

              precision    recall  f1-score   support

           0       0.70      0.30      0.42        99
           1       0.84      0.75      0.79       146
           2       1.00      0.90      0.95        30
           3       0.93      0.93      0.93        14
           4       1.00      0.95      0.98       128
           5       0.83      0.97      0.89       713
           6       0.80      0.80      0.80       194
           7       0.93      0.93      0.93      2431
           8       0.56      0.20      0.29        51
           9       0.86      0.85      0.85       261
          10       0.77      0.88      0.82       146
          11       0.85      0.82      0.83       645
          12       0.00      0.00      0.00         0

    accuracy                           0.88      4858
   macro avg       0.77      0.71      0.73      4858
weighted avg       0.88      0.88      0.88      4858
 ```


Como citar: **em breve**
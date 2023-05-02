---
tags:
- generated_from_trainer
datasets:
- nerde
widget:
- text: "Considerando-se os argumentos elencados pela Peticionária, infere-se que a CNH Industrial detém legítimo interesse pelo caso em epígrafe, visto que pode ser afetada pela decisão a ser adotada pelo Cade sobre a Operação, constatação que autoriza o enquadramento do pleito nas hipóteses previstas no artigo 50 da Lei nº 12.529/2011."
- text: "Em análise dos autos verifica-se a existência de documentos contra Aurélio de Paula, datados de 04 de março de 2010, 19 de março de 2010 e 05 de outubro de 2010; contra Bianchini Indústria de Plásticos Ltda., Igon Bernardelli, datados de 19 de março de 2010; contra a Nasato Indústria de Plásticos Eireli e Osmair Nasato, datados de 04 de março de 2010 e 05 de outubro de 2010; contra TWB Indústria e Comércio de Produtos Plásticos Ltda. e Waldir Dezotti, datados de 04 de março de 2010 e 05 de outubro de 2010, podendo-se concluir que a conduta ocorreu de forma contínua na maioria dos casos, pelo menos ao longo do ano de 2010, questões que serão melhor analisadas após o fim da instrução processual."
inference:
  parameters:
    aggregation_strategy: "max"
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: NERDE-base
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: nerde
      type: nerde
      args: NERDE
    metrics:
    - name: Precision
      type: precision
      value: 0.9118601747815231
    - name: Recall
      type: recall
      value: 0.9152882205513785
    - name: F1
      type: f1
      value: 0.9135709818636648
    - name: Accuracy
      type: accuracy
      value: 0.9841962132484992
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NERDE-base

This model is a fine-tuned version of [pierreguillou/bert-base-cased-pt-lenerbr](https://huggingface.co/pierreguillou/bert-base-cased-pt-lenerbr) on the nerde dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1246
- Precision: 0.9119
- Recall: 0.9153
- F1: 0.9136
- Accuracy: 0.9842

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2466        | 1.0   | 541  | 0.1003          | 0.8515    | 0.8822 | 0.8666 | 0.9782   |
| 0.0608        | 2.0   | 1082 | 0.0855          | 0.8990    | 0.9083 | 0.9036 | 0.9837   |
| 0.0411        | 3.0   | 1623 | 0.1006          | 0.9078    | 0.9103 | 0.9090 | 0.9837   |
| 0.0266        | 4.0   | 2164 | 0.1052          | 0.9023    | 0.9163 | 0.9092 | 0.9828   |
| 0.0191        | 5.0   | 2705 | 0.1060          | 0.9112    | 0.9183 | 0.9147 | 0.9847   |
| 0.0153        | 6.0   | 3246 | 0.1152          | 0.9052    | 0.9098 | 0.9075 | 0.9831   |
| 0.0124        | 7.0   | 3787 | 0.1209          | 0.9029    | 0.9185 | 0.9107 | 0.9835   |
| 0.0083        | 8.0   | 4328 | 0.1176          | 0.9072    | 0.9163 | 0.9117 | 0.9844   |
| 0.0077        | 9.0   | 4869 | 0.1240          | 0.9080    | 0.9201 | 0.9140 | 0.9844   |
| 0.0051        | 10.0  | 5410 | 0.1246          | 0.9119    | 0.9153 | 0.9136 | 0.9842   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

---
tags:
- spacy
- token-classification
language:
- pt
datasets:
- lener_br
model-index:
- name: pt_lg_pipeline
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8397790055
    - name: NER Recall
      type: recall
      value: 0.8360836084
    - name: NER F Score
      type: f_score
      value: 0.8379272326
widget:
- text: >-
    Que causaram evidente transtorno e evidencia a má prestação de serviço, com
    violação ao princípio da transparência, da confiaça e da boa-fé objetiva
    insertos nos artigos 4º e 6º do CDC. Por todo o acima exposto, na forma do
    artigo 269, I do Código de Processo Civil, conhecido e apelação não
    promovida. (Apelação Cível 2009 01 1 075609-5 APC Relator Desembargador JAIR
    SOARE.) Em relação ao CONTRATO BANCÁRIO INVERSÃO DO ÔNUS DA PROVA CDC
    Possibilidade da inversão do ônus da prova com base no artigo 6º, VIII, do
    CDC Reconhecido que o cliente tem direito de postular a exibição de
    documentos - Possibilidade de determinação pelo juiz incidentalmente.
- text: >-
    Evidenciado que a citação somente foi aperfeiçoada após o
    decurso do prazo prescricional, tem-se por correta a extinção
    da demanda monitória, com resolução do mérito, nos termos do
    artigo 485, inciso II, do Código de Processo Civil.
- text: >-
    O Senhor Ministro Ricardo Lewandowski (Relator): Trata-se de
    agravo regimental interposto pela União contra decisão monocrática que
    julgou procedente Ação Cível Originária ajuizada pelo Estado do Mato
    Grosso, determinando-se à União que renove o Certificado de
    Regularidade Previdenciária do Estado de Mato Grosso, retirando-o do
    conceito de irregular do Cadastro de Regime Próprio de Previdência
    Social-CADPREV ou retirando-o de qualquer outro cadastro de
    inadimplentes pelo mesmo motivo (CADIN, CA UC, SIAFI, SICONV),
    declarando-se ainda, incidenter tantum, a inconstitucionalidade do Decreto
    3.788/2001 e da Portaria MPS n° 204/2008 e de suas posteriores
    alterações.
library_name: spacy
pipeline_tag: text-classification
---

## Modelo para Reconhecimento de Entidade Nomeadas em português utilizando o modelo spaCy pt_core_news_lg

Link do trabalho no Kaggle: https://www.kaggle.com/datasets/flaviagg/lenerbr .

Criei um Web App que proporciona a comparação dos modelos sm e lg: https://huggingface.co/spaces/flaviaggp/Streamlit_Lener .

## Métricas por entidade

![Screenshot](scorer_lg.png)

| Feature | Description |
| --- | --- |
| **Name** | `pt_lg_pipeline` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.4,<3.5.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 500000 keys, 500000 unique vectors (300 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (6 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `JURISPRUDENCIA`, `LEGISLACAO`, `LOCAL`, `ORGANIZACAO`, `PESSOA`, `TEMPO` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 83.79 |
| `ENTS_P` | 83.98 |
| `ENTS_R` | 83.61 |
| `TOK2VEC_LOSS` | 23620.33 |
| `NER_LOSS` | 127975.46 |
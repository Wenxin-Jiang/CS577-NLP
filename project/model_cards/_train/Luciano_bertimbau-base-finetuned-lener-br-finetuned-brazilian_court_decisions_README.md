---
language:
- pt
license: mit
tags:
- generated_from_trainer
datasets:
- joelito/brazilian_court_decisions
metrics:
- accuracy
train-eval-index:
- config: joelito--brazilian_court_decisions
  task: text-classification
  task_id: multi_class_classification
  splits:
    eval_split: test
  col_mapping:
    decision_description: text
    judgment_label: target
widget:
- text: 'AGRAVO DE INSTRUMENTO. AÇÃO REVISIONAL DE CONTRATO. DEPÓSITO DO VALOR INCONTROVERSO.
    IMPOSSIBILIDADE. NÃO PREENCHIMENTO DOS REQUISITOS PELO DEVEDOR. MANUTENÇÃO NA
    POSSE DO BEM E VEDAÇÃO DE INSCRIÇÃO NOS ÓRGÃOS DE PROTEÇÃO AO CRÉDITO MEDIANTE
    O DEPÓSITO DO VALOR ORIGINALMENTE CONTRATADO. 1. O autor requereu a sua manutenção
    na posse do bem, o depósito em juízo dos valores que entende incontroversos, a
    proibição de inscrição de seu nome nos órgãos de proteção ao crédito e a suspensão
    de eventual ação de busca e apreensão do veículo. 2. O artigo 330, PARAGRAFO 2
    e PARAGRAFO 3 do CODIGO DE PROCESSO CIVIL autoriza expressamente o depósito do
    valor incontroverso nas ações revisionais de contrato mediante presença de três
    requisitos concomitantes: a) propositura de ação contestando a existência integral
    ou parcial do débito; b) efetiva demonstração de que a contestação da cobrança
    indevida se funda na aparência do bom direito; e, c) que a parte efetue o depósito
    do valor incontroverso ou preste caução idônea. Contudo, tal conduta não afastará
    a incidência das restrições legais decorrentes da dívida, porquanto os valores
    considerados incontroversos são inferiores àqueles contratados. 3. A jurisprudência
    é pacífica no sentido de ser necessário o depósito do valor integral da parcela
    da dívida para inibir os efeitos da mora e suas consequências. 4. Nos termos da
    jurisprudência consolidada nesta Corte, deverá o devedor depositar os valores
    pactuados originalmente no contrato, tanto para as parcelas vencidas, quanto para
    as vincendas, nas datas pactuadas, se desejar se manter na posse do bem e obstacular
    sua inscrição de seu nome nos cadastros restritivos de crédito.'
- text: O constrangimento ilegal deve ser aferido segundo as circunstancias do caso
    concreto, especialmente diante da complexidade e das diligências necessárias,
    ainda mais quando tais elementos são necessários para embasar a própria denúncia
    em si. Intensa movimentação processual no sentido de angariar as informações necessárias.
    Prazo que merece ser mitigado. Denúncia oferecida nos autos da ação penal 0800162-9820188020001.
    II - Presentes a materialidade dos delitos e seus indícios de autoria, mormente
    diante das colaborações premiadas colhidas durante as investigações, não há falar
    em embasamento abstrato da decisão especialmente quando esta expressamente apontou
    que o paciente era proprietário de empresas supostamente fantasmas, que recebiam
    benefícios de diversas prefeituras. III - Ausência de constrangimento ilegal,
    tanto pela presença dos requisitos para a prisão preventiva em questão, quanto
    pelo fato de que resta evidenciado que o paciente ficou foragido. Precedentes.
    IV - Especificamente em relação ao pedido de extensão dos efeitos dos benefícios
    concedidos a outros investigados (Josimar Campos, Raphael de Barros Lima e Raulene
    Karoline Barros e Gabriel Brandão), entendo, a partir do narrado pela própria
    petição inicial, que a situação do paciente é diferente dos demais investigados,
    uma vez que, além de ele ter foragido do distrito da culpa e responder a outras
    ações penais, aparentemente não está colaborando com as investigações (os outros
    investigados firmaram acordo de colaboração premiada). V - No que tange ao pedido
    relacionado aos ex-prefeitos (Márcia Coutinho Nogueira de Albuquerque, José Jacob
    Gomes Brandão, Fábio Rangel Nunes de Oliveira) que se encontram em liberdade,
    entendo que a situação do paciente também é diferente, uma vez que a decisão de
    origem da conta que existem indicativos de que o esquema tenha ocorrido em 80
    (oitenta) prefeituras. VI - A partir da leitura da decisão prolatada pelos juízes
    impetrados, verifica-se que o decreto de prisão não é fundamentado apenas no risco
    de a liberdade do paciente atrapalhar as investigações, mas também, para, sobretudo,
    garantir a aplicação da lei penal pelo fato de o paciente ter foragido do distrito
    da culpa.
- text: APELAÇÃO CÍVEL. AÇÃO ORIGINÁRIA DE USUCAPIÃO. JULGAMENTO ANTECIPADO DA LIDE.
    SENTENÇA DE IMPROCEDÊNCIA AO PLEITO AUTORAL ANTE A AUSÊNCIA DOS REQUISITOS DO
    ARTIGO 1238 DO CÓDIGO CIVIL/02. AUSÊNCIA DE CITAÇÃO DO PROPRIETÁRIO DO BEM A SER
    USUCAPIDO. AUTOR COMPROVA POR DOCUMENTO EXPEDIDO PELA MUNICIPALIDADE O REGISTRO
    DO IMÓVEL USUCAPIENDO EM SEU NOME DESDE 1990. POSSIBILIDADE DO PREENCHIMENTO DO
    REQUISITO TEMPORAL (PRAZO PARA USUCAPIR) PREVISTO EM LEI A SER IMPLEMENTADO NO
    CURSO DA DEMANDA. OFENSA AO DEVIDO PROCESSO LEGAL MATÉRIA DE ORDEM PÚBLICA, RECONHECIDA
    DE OFÍCIO NO JUÍZO AD QUEM. NULIDADE DA SENTENÇA COM RETORNO DOS AUTOS À ORIGEM
    PARA DAR SEGUIMENTO A INSTRUÇÃO COM PROLAÇÃO DE NOVA DECISÃO.
model-index:
- name: bertimbau-base-finetuned-lener-br-finetuned-brazilian_court_decisions
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: joelito/brazilian_court_decisions
      type: joelito/brazilian_court_decisions
      config: joelito--brazilian_court_decisions
      split: test
    metrics:
    - type: accuracy
      value: 0.7925925925925926
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNGYwNzJiZjE0ZjE1NzM5ZWI2ZWQ3MDZiNTkxNDMzY2IwODJmNjRjMGFjYWNjMzg0MWM0YjZmNjNlODJiMzZiZCIsInZlcnNpb24iOjF9.yuzroeBIxzMUISrKslpXl6mw_pdmZ5rsx1_yBRvneBF5Y18NIwbaSidUJ4A_AsR91yrHStvCi2LV9mi0pSUSBg
    - type: precision
      value: 0.7561026936026934
      name: Precision Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZTU1YTMxOGQ3MjcxZjViNTYxOTFmN2MwYzk1YjAwMTU4NjVmNzEwODBlNWZlN2EzNWI5Y2FmZjE5NmNjODQ4NSIsInZlcnNpb24iOjF9.NC1NGFneaJFl-aA0veGNiaHXhZ7_7Xp14DoCRQkqNuDbjmcEqARaT2zvcfmUlC1KFafqGdA9zGxPyPvLYGD9Dg
    - type: precision
      value: 0.7925925925925926
      name: Precision Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTIwMzg2ZjkwNzNiZTNjMTg1MTExY2E3NmNhYWM5MGQxYjlkMGNkOTFjMjU5YWRlZGJkOGRmNzUyOTI1MGE4MSIsInZlcnNpb24iOjF9.e-2no4ZzEQh_o2IZLwqAgKnandZ60gkLQwkHQ1chblFJldFJVeiD_VuYPG6oYxT0i6olPZob3soV1qRLOMBOAw
    - type: precision
      value: 0.7913112607557052
      name: Precision Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNGQ3YTE5Y2YzYzQzYjllMDMxMTQ3ODRmNzI1ZWZkZTNmMGFkMjAxZTE3M2FhZGEzMjM3OTcwODg4NjBmMWU2ZSIsInZlcnNpb24iOjF9.uLD9Bqp5E6S0vZSc82RUtB49jOxMWPwqCp18YjDqJQRBpRgm7kyQwxmtenDci9UieuJ0d1DtD2b8sPYyPQ7dDA
    - type: recall
      value: 0.7408785957173055
      name: Recall Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTM2YTVkNmM1ZGRhNzY0OWYyYTg2NmIxYWRkOWYyMTc4ZWVlYjdmNDliMDlhOTk2MGVjNjJlMjFhZGJmMGYxYyIsInZlcnNpb24iOjF9.KsRzS_NH6bbyIyhKD-P2BPKKtAZjdOXrwZrq_U9zensLOY7C5RZCFGuYESqm0vQwpQf0ZKqKEYCUL9WRwONhBg
    - type: recall
      value: 0.7925925925925926
      name: Recall Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYWUxMzM5OWQwMDg3ZjIxMTFiNzg0MmJkMzYwODU5MjNmMDllZWFjYmMzNTRlNWRhY2NkNmJiNGZkYmU0MjVhNSIsInZlcnNpb24iOjF9.AtDYhA7T8793on76uVa0tbzCKfq1UD4U_pU1Q0vFRST8lDjQYyw6_Q6JzY3Jh9qw1gSU6qA52zMlesb8ANckDw
    - type: recall
      value: 0.7925925925925926
      name: Recall Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTBiYTYwZmRiZjY3YjM4YmFlMjkwNDVlN2JiOTY2MDgxOWNmYmE1YmJkZGY1NGU5ZDA1MjdjZDgyMzI3NDhlMCIsInZlcnNpb24iOjF9.uXSLCN14oZb6mP0hLTH8RxD6Og6OYrS7OSxRbIqsx_JauIXdca4RFZcXptzeq190gbRWT0lNz5GEhzjeT7qmAA
    - type: f1
      value: 0.7466596343178621
      name: F1 Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMzMzNDIwZGMzNmVjZmUxNGVhZGRhOWZkNzI3OWViYmNiOGZkNGI4ZjE5M2U2MjA1OGRjMzE2YzEyODFjNDE3NiIsInZlcnNpb24iOjF9.GHA7gAvoIQQuhhoXMeGuMdGo0f4Pma5AUgCA9T6qDKeXMeuRs6gqumLzi3lXgMBB4RuPxE49NOgVLLyrq-J2Aw
    - type: f1
      value: 0.7925925925925926
      name: F1 Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMzFkNTU5NTM1NjhjNjAwMzQ1ZTNjYzczNDc5MzI1NjI3ODkyMzk5OTExMTBlZDlhYzAzNTkzYzM3ZjU2MTJjMSIsInZlcnNpb24iOjF9.Gw1w7Fsv--XRx0Hxuw6pYAzyhd9vb-n31Y5Mwgh6lbQKEDsBMauztkT3rqPIIqqCLVI3LsaVoLk4ECTAIngwBA
    - type: f1
      value: 0.7908149710892328
      name: F1 Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMDVkNTU3MmUxYjY0NmFiMGU2ZTM1M2YzYmUxMGM3NDNjOTkxMGY2NzU5ODkwYTc3YTRhMWIwMjE4YzVhMzU0YSIsInZlcnNpb24iOjF9.KrMgoICICm8QeS6usYrHMhQ7PoscE6wyLz9QGnUPpQa0LOr0EcasCpgeK_yyVytBCIR3lT1doYAvKH8mTf9lBA
    - type: loss
      value: 1.6538628339767456
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiODZkMWEzODY5ZTA2N2MzMjJkYmQ2NWE4MWJmZWIxMmNjZmVmZTA3Yjk2ZTdjNzFmODIyMThkY2NhOWIzYTgwMCIsInZlcnNpb24iOjF9.IyEKEBbdbNYTcUzOF09r2vp7umxYSIeTGN_muWNujaSbibd6uSooNRWzSfZOS37L0S4_GPdMvDXQuMsUeybWAQ
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bertimbau-base-finetuned-lener-br-finetuned-brazilian_court_decisions

This model is a fine-tuned version of [Luciano/bertimbau-base-finetuned-lener-br](https://huggingface.co/Luciano/bertimbau-base-finetuned-lener-br) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8017
- Accuracy: 0.7698

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 405  | 0.7790          | 0.6535   |
| 0.8276        | 2.0   | 810  | 0.6739          | 0.7277   |
| 0.5818        | 3.0   | 1215 | 0.8767          | 0.7302   |
| 0.4147        | 4.0   | 1620 | 0.8229          | 0.7896   |
| 0.287         | 5.0   | 2025 | 0.9874          | 0.7921   |
| 0.287         | 6.0   | 2430 | 1.2301          | 0.7772   |
| 0.1727        | 7.0   | 2835 | 1.2864          | 0.7946   |
| 0.1179        | 8.0   | 3240 | 1.5097          | 0.7772   |
| 0.0709        | 9.0   | 3645 | 1.4772          | 0.7921   |
| 0.0437        | 10.0  | 4050 | 1.5581          | 0.7797   |
| 0.0437        | 11.0  | 4455 | 1.6317          | 0.7896   |
| 0.0318        | 12.0  | 4860 | 1.7295          | 0.7822   |
| 0.0158        | 13.0  | 5265 | 1.7333          | 0.7797   |
| 0.0108        | 14.0  | 5670 | 1.8008          | 0.7772   |
| 0.0137        | 15.0  | 6075 | 1.8017          | 0.7698   |


### Framework versions

- Transformers 4.22.0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

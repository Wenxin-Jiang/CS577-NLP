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
- name: bertimbau-base-finetuned-brazilian_court_decisions
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
      value: 0.7753086419753087
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiN2Q0N2I5ZThjOTdmYjJmNjQ2M2EwYzllOGZlZmUzMzQ3ZTNmMDYwN2Y4NTk3MjA4NTBiYzBkNGRmMDVjMWE0YiIsInZlcnNpb24iOjF9.azo0rnA6IBxWvLcVuY37hgCQ2Krss0pqrqzHJ_cu4y6hb5IHupoPUzvkAXpv5_U_iOVAq_xPS8Ow9CU9YLDjAg
    - type: precision
      value: 0.7250426732752088
      name: Precision Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDFlNGMzM2VlMGNkOGYwNWU1N2U1NDVmNjlmMjZmYTI1YzVmNTJkZTVlMmY1NTQ3NDkzOWRlMjBmZDZlMDlkMiIsInZlcnNpb24iOjF9.2xet0XJ9AzIF4WvH-QPborSKwNYxrnjI88yYbx5rmt82Uw5_KutBG_LLHl-H7ZDLcBmbLrCGq9kAz7FsDR8DDg
    - type: precision
      value: 0.7753086419753087
      name: Precision Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTRmYTY2MWZhY2ZlZjYwMmQ5NzBkZjNkYzZiMGU0NmI5OTA5MDZjMGZkNDczNzc1OWVjNDE0YzFlMDE3MjU5YyIsInZlcnNpb24iOjF9.2smiUGVwRxTXdTcWm9wT_7HfYMQBGtNGiRECC-VqDgJalFiJL8z42RhaL0PpX29P9Gs2AqHj_CC2yOpcF9-dBQ
    - type: precision
      value: 0.772642124493271
      name: Precision Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMGYwN2I2MzcwODBjZTI0MjRjZjZmYzg5OGQyYzI3MzNiNDg3OTRlOGY0ZjBhM2NkMzdmM2Q1MGY1OTg3NGQ4YyIsInZlcnNpb24iOjF9.alVSoPTd0sN2WnlwUsvjMB3FMwgq4idmBg61VvZEGGjMheq-gantO2LEjghOLvyqV2ykHKZ3HtsaBZg3MFh1BQ
    - type: recall
      value: 0.7165701681830714
      name: Recall Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMzdhMGFlOTk1ZDY5NmNkMjQ0ZDJjOWI1NzMxYmFiNTZiNzM3N2ZhY2ZmZGRkYjBlMmY1ZjM4MDAzYWRhZmYxYyIsInZlcnNpb24iOjF9.iOY4HQhYtb0j4Aj0Q1pohB39QNNzBfeF3KjMeN33hgaRrK5BgoL_6VH_g_-n7oY00Pmw5sXbaLdO7obCpQooAQ
    - type: recall
      value: 0.7753086419753087
      name: Recall Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDFlY2ViMjdmM2MzNDVkNGVjM2UxMzk5N2MyOWM3NTE5ZjQ2ZTJjMGMzNDViNmYzNWZiN2E0MmM3MTFhZmJhNCIsInZlcnNpb24iOjF9.MrfbjuTh4fNTjeNz6SNJ9L5bAxOQYtfXFArg0lMN7dzji8BtpSep_pVwb-27A6Bem7V2xlc27PdCMayVu08oCw
    - type: recall
      value: 0.7753086419753087
      name: Recall Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTFkOGJhODNjZWI3OWM2ZDQwNWNkNWViYjZmOWQ3NDAzNWIzMjM1ZmRlNThiMjhkYjhkMDM0ZGU5MTdhOWYyOSIsInZlcnNpb24iOjF9.sxK_3TdQnAcCttSHzVvPOGxGlOfpeKYBZ9z6rTEAUw2G6HlC09jcxhlcl5nQRvpfMcMAzgVTrL6X3kgRjB9VBg
    - type: f1
      value: 0.7202933364810833
      name: F1 Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZWZkMzNmZjJmNDhjZWU3MWM3ODdjNDA1OTY3ZGY3MmJmM2VjOTk2YTdkYzk2NWYxMGVjYjNmZTA1YTAxYjdjZiIsInZlcnNpb24iOjF9.tJ0qIvWo2pz1nzxCx-nCXm9BQPP94VV7cOEVQLPE2U3YRgOuIFMO99CW4a_Ge70XPLyFTIRCbr2-xDpMrC03Cw
    - type: f1
      value: 0.7753086419753087
      name: F1 Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOGJiZDA4ZWU3NzA3OWU0N2YzNTU1NTQ1MmI2MzdlNWMwYTFhYjk1ZTQ5NDA0NzIyYTEwYWU2NGYxMDg5MzE5NyIsInZlcnNpb24iOjF9.HrC1_am-qUC4HboPtIanE1np2faZVqSPy58VlY3oK-nTPHYyEt_6FfgJoP2M6roVGKLjiXDs7gVljplAAG1XBQ
    - type: f1
      value: 0.7736389495276883
      name: F1 Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYjgzYjc2Y2JjYTI0MDFhYWZmOGY1YTc5ZTQ1NzI3ZDUxNWY5NzdhZmIyYzE1MTA5NTEyOTA4NjFkMmQ4ODI5ZCIsInZlcnNpb24iOjF9.TCvj3Rqei3q2ajB6L9dqIxTyKXhNFQuQrU4ymc7kWnEyPuKgB9ty2JTqjeRYPWpY2RicABU9UFDXEhrdcfbKCw
    - type: loss
      value: 0.6030029058456421
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMmUyZjdjMTNiOGQ4OGJmZTg3MjU2MjczNDY0OWNhODNjZTIzYjhhOWFmZWI2M2Q4NTI3MjU1YzcwOWNiMDI0MCIsInZlcnNpb24iOjF9.DZoUcmXU7RWW_AGR5ezU7ZbM9YobJ5nzQSgrtLVJtZjd6bELzCyafbsCCJE1Uia7Uz0HcW1B1J6mbev_z6TlAg
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bertimbau-base-finetuned-brazilian_court_decisions

This model is a fine-tuned version of [neuralmind/bert-base-portuguese-cased](https://huggingface.co/neuralmind/bert-base-portuguese-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6424
- Accuracy: 0.7921

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 203  | 0.7726          | 0.6683   |
| No log        | 2.0   | 406  | 0.5948          | 0.7673   |
| 0.7112        | 3.0   | 609  | 0.6424          | 0.7723   |
| 0.7112        | 4.0   | 812  | 0.6376          | 0.7772   |
| 0.3383        | 5.0   | 1015 | 0.6424          | 0.7921   |


### Framework versions

- Transformers 4.22.0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

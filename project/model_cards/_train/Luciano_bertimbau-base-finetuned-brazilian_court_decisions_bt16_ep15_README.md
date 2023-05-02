---
language:
- pt
license: mit
datasets:
- joelito/brazilian_court_decisions
train-eval-index:
- config: joelito--brazilian_court_decisions
  task: text-classification
  task_id: multi_class_classification
  splits:
    eval_split: test
  col_mapping:
    decision_description: text
    judgment_label: target
tags:
- generated_from_trainer
metrics:
- accuracy
widget:
- text: "AGRAVO DE INSTRUMENTO. A\xC7\xC3O REVISIONAL DE CONTRATO. DEP\xD3SITO DO\
    \ VALOR INCONTROVERSO. IMPOSSIBILIDADE. N\xC3O PREENCHIMENTO DOS REQUISITOS PELO\
    \ DEVEDOR. MANUTEN\xC7\xC3O NA POSSE DO BEM E VEDA\xC7\xC3O DE INSCRI\xC7\xC3\
    O NOS \xD3RG\xC3OS DE PROTE\xC7\xC3O AO CR\xC9DITO MEDIANTE O DEP\xD3SITO DO VALOR\
    \ ORIGINALMENTE CONTRATADO. 1. O autor requereu a sua manuten\xE7\xE3o na posse\
    \ do bem, o dep\xF3sito em ju\xEDzo dos valores que entende incontroversos, a\
    \ proibi\xE7\xE3o de inscri\xE7\xE3o de seu nome nos \xF3rg\xE3os de prote\xE7\
    \xE3o ao cr\xE9dito e a suspens\xE3o de eventual a\xE7\xE3o de busca e apreens\xE3\
    o do ve\xEDculo. 2. O artigo 330, PARAGRAFO 2 e PARAGRAFO 3 do CODIGO DE PROCESSO\
    \ CIVIL autoriza expressamente o dep\xF3sito do valor incontroverso nas a\xE7\xF5\
    es revisionais de contrato mediante presen\xE7a de tr\xEAs requisitos concomitantes:\
    \ a) propositura de a\xE7\xE3o contestando a exist\xEAncia integral ou parcial\
    \ do d\xE9bito; b) efetiva demonstra\xE7\xE3o de que a contesta\xE7\xE3o da cobran\xE7\
    a indevida se funda na apar\xEAncia do bom direito; e, c) que a parte efetue o\
    \ dep\xF3sito do valor incontroverso ou preste cau\xE7\xE3o id\xF4nea. Contudo,\
    \ tal conduta n\xE3o afastar\xE1 a incid\xEAncia das restri\xE7\xF5es legais decorrentes\
    \ da d\xEDvida, porquanto os valores considerados incontroversos s\xE3o inferiores\
    \ \xE0queles contratados. 3. A jurisprud\xEAncia \xE9 pac\xEDfica no sentido de\
    \ ser necess\xE1rio o dep\xF3sito do valor integral da parcela da d\xEDvida para\
    \ inibir os efeitos da mora e suas consequ\xEAncias. 4. Nos termos da jurisprud\xEA\
    ncia consolidada nesta Corte, dever\xE1 o devedor depositar os valores pactuados\
    \ originalmente no contrato, tanto para as parcelas vencidas, quanto para as vincendas,\
    \ nas datas pactuadas, se desejar se manter na posse do bem e obstacular sua inscri\xE7\
    \xE3o de seu nome nos cadastros restritivos de cr\xE9dito."
- text: "O constrangimento ilegal deve ser aferido segundo as circunstancias do caso\
    \ concreto, especialmente diante da complexidade e das dilig\xEAncias necess\xE1\
    rias, ainda mais quando tais elementos s\xE3o necess\xE1rios para embasar a pr\xF3\
    pria den\xFAncia em si. Intensa movimenta\xE7\xE3o processual no sentido de angariar\
    \ as informa\xE7\xF5es necess\xE1rias. Prazo que merece ser mitigado. Den\xFA\
    ncia oferecida nos autos da a\xE7\xE3o penal 0800162-9820188020001. II - Presentes\
    \ a materialidade dos delitos e seus ind\xEDcios de autoria, mormente diante das\
    \ colabora\xE7\xF5es premiadas colhidas durante as investiga\xE7\xF5es, n\xE3\
    o h\xE1 falar em embasamento abstrato da decis\xE3o especialmente quando esta\
    \ expressamente apontou que o paciente era propriet\xE1rio de empresas supostamente\
    \ fantasmas, que recebiam benef\xEDcios de diversas prefeituras. III - Aus\xEA\
    ncia de constrangimento ilegal, tanto pela presen\xE7a dos requisitos para a pris\xE3\
    o preventiva em quest\xE3o, quanto pelo fato de que resta evidenciado que o paciente\
    \ ficou foragido. Precedentes. IV - Especificamente em rela\xE7\xE3o ao pedido\
    \ de extens\xE3o dos efeitos dos benef\xEDcios concedidos a outros investigados\
    \ (Josimar Campos, Raphael de Barros Lima e Raulene Karoline Barros e Gabriel\
    \ Brand\xE3o), entendo, a partir do narrado pela pr\xF3pria peti\xE7\xE3o inicial,\
    \ que a situa\xE7\xE3o do paciente \xE9 diferente dos demais investigados, uma\
    \ vez que, al\xE9m de ele ter foragido do distrito da culpa e responder a outras\
    \ a\xE7\xF5es penais, aparentemente n\xE3o est\xE1 colaborando com as investiga\xE7\
    \xF5es (os outros investigados firmaram acordo de colabora\xE7\xE3o premiada).\
    \ V - No que tange ao pedido relacionado aos ex-prefeitos (M\xE1rcia Coutinho\
    \ Nogueira de Albuquerque, Jos\xE9 Jacob Gomes Brand\xE3o, F\xE1bio Rangel Nunes\
    \ de Oliveira) que se encontram em liberdade, entendo que a situa\xE7\xE3o do\
    \ paciente tamb\xE9m \xE9 diferente, uma vez que a decis\xE3o de origem da conta\
    \ que existem indicativos de que o esquema tenha ocorrido em 80 (oitenta) prefeituras.\
    \ VI - A partir da leitura da decis\xE3o prolatada pelos ju\xEDzes impetrados,\
    \ verifica-se que o decreto de pris\xE3o n\xE3o \xE9 fundamentado apenas no risco\
    \ de a liberdade do paciente atrapalhar as investiga\xE7\xF5es, mas tamb\xE9m,\
    \ para, sobretudo, garantir a aplica\xE7\xE3o da lei penal pelo fato de o paciente\
    \ ter foragido do distrito da culpa."
- text: "APELA\xC7\xC3O C\xCDVEL. A\xC7\xC3O ORIGIN\xC1RIA DE USUCAPI\xC3O. JULGAMENTO\
    \ ANTECIPADO DA LIDE. SENTEN\xC7A DE IMPROCED\xCANCIA AO PLEITO AUTORAL ANTE A\
    \ AUS\xCANCIA DOS REQUISITOS DO ARTIGO 1238 DO C\xD3DIGO CIVIL/02. AUS\xCANCIA\
    \ DE CITA\xC7\xC3O DO PROPRIET\xC1RIO DO BEM A SER USUCAPIDO. AUTOR COMPROVA POR\
    \ DOCUMENTO EXPEDIDO PELA MUNICIPALIDADE O REGISTRO DO IM\xD3VEL USUCAPIENDO EM\
    \ SEU NOME DESDE 1990. POSSIBILIDADE DO PREENCHIMENTO DO REQUISITO TEMPORAL (PRAZO\
    \ PARA USUCAPIR) PREVISTO EM LEI A SER IMPLEMENTADO NO CURSO DA DEMANDA. OFENSA\
    \ AO DEVIDO PROCESSO LEGAL MAT\xC9RIA DE ORDEM P\xDABLICA, RECONHECIDA DE OF\xCD\
    CIO NO JU\xCDZO AD QUEM. NULIDADE DA SENTEN\xC7A COM RETORNO DOS AUTOS \xC0 ORIGEM\
    \ PARA DAR SEGUIMENTO A INSTRU\xC7\xC3O COM PROLA\xC7\xC3O DE NOVA DECIS\xC3O."
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bertimbau-base-finetuned-brazilian_court_decisions_bt16_ep15

This model is a fine-tuned version of [neuralmind/bert-base-portuguese-cased](https://huggingface.co/neuralmind/bert-base-portuguese-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.523958
- Accuracy: 0.772277

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

| Epoch | Training Loss | Validation Loss | Accuracy |
|:-------------:|:-----:|:---------------:|:--------:|
| 1	| No log	 | 0.852318| 	0.603960
| 2	| No log	 | 0.728222	| 0.660891
| 3	| 0.781100	 | 0.662818	| 0.742574
| 4	| 0.781100	 | 0.687966	| 0.742574
| 5	| 0.399400	|  0.727256	| 0.762376
| 6	| 0.399400	| 0.843507	| 0.762376
| 7	| 0.399400	| 0.936927	| 0.759901
| 8	| 0.182400	| 1.065885	| 0.769802
| 9	| 0.182400	| 1.154641	| 0.754950
| 10 | 	0.082200	 | 1.375061| 	0.745050
| 11 | 	0.082200	 | 1.377540| 	0.757426
| 12 | 	0.082200	 | 1.465057| 	0.759901
| 13 | 	0.033800	 | 1.497934| 	0.762376
| 14 | 	0.033800	 | 1.504722| 	0.769802
| 15 | 	0.017900	| 1.523958| 	0.772277

### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

---
language: 
- pt
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bertimbau-base-finetuned-lener-br-finetuned-peticoes-assuntos
  results: []
widget:
- text: "A parte agravada alega ter firmado contratos junto à agravante, porém, alega que os juros estão muito altos. Requer a revisão do contrato, repetição do indébito, descaracterização da mora, suspensão dos descontos, não inclusão em órgãos restritivos de crédito e depósito da parcela incontroversa."
- text: "A parte Agravada propôs ação de busca e apreensão contra a parte Agravante com base no Decreto-lei nº 911/69, sob a alegação de estar a parte recorrente estar em mora com relação ao pagamento das prestações de financiamento firmado entre as partes, para aquisição de bem mediante consórcio. O M.M. Juiz de Direito da 2ª Vara Cível de Cachoeira do Sul concedeu liminarmente a busca e apreensão do veículo alienado, medida essa cumprida em 06/08/2020."
- text: "AMANDA DA SILVA e PEDRO DA SILVA, ambos representados pela mãe, Larissa da Silva, todos já qualificados nos autos da “ação revisional de alimentos” que lhes move MARCELO SOUZA, também qualificado, vêm, respeitosamente, à presença de Vossa Excelência, por seus procuradores, interpor o presente AGRAVO DE INSTRUMENTO em face da decisão interlocutória que, nos autos de origem, dentre outras matérias, em saneamento ao processo, rejeitou a preliminar de inadequação do valor da causa e deferiu parcialmente tutela antecipada para fixar alimentos prestados por Marcelo aos filhos Amanda e Pedro no equivalente a 20% de seus rendimentos líquidos, do que recorre pelos fundamentos de fato e de direito que seguem anexo e justificam a súplica ao final. Outrossim, requer a dispensa do recolhimento das custas, eis que os menores não têm condições de arcar com as despesas do processo sem prejuízo ao próprio sustento."
- text: "ANA MARIA DE SOUZA, brasileira, solteira, Advogada, inscrita na OAB/RS sob o nº 12.345, residente e domiciliada na Estrada ABC, 123, Bairro X, Viamão, RS, e-mail dra@gmail.com, Telefone 51 987654321, vem, respeitosamente, à presença de Vossa Excelência, impetrar HABEAS CORPUS Com fundamento legal no art. 5º, LXVIII, da Constituição Federal e nos artigos 647 e 648 do Código de Processo Penal, em favor da MARIA DA SILVA, já qualificada nos presentes autos, atualmente recolhida na PENITENCIÁRIA MADRE PELETIER, PORTO ALEGRE, por estar sofrendo flagrante constrangimento ilegal perpetrado pelo Excelentíssima Senhora Doutora Juíza de Direito da 2ª Vara Criminal da Comarca de Canoas, nos autos em epígrafe, como será demonstrado a seguir: I - DOS FATOS E DO DIREITO A paciente  encontra-se presa desde 31 de agosto de 2020. Decretada a prisão em flagrante da paciente, foi convertida pela juíza plantonista a prisão em preventiva, no dia seguinte."  
  
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bertimbau-base-finetuned-lener-br-finetuned-peticoes-assuntos

This model is a fine-tuned version of [Luciano/bertimbau-base-finetuned-lener-br](https://huggingface.co/Luciano/bertimbau-base-finetuned-lener-br) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9930
- Accuracy: 0.3575

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
| 4.7305        | 1.0   | 898  | 3.6586          | 0.2533   |
| 3.4793        | 2.0   | 1796 | 3.2827          | 0.3029   |
| 3.0791        | 3.0   | 2694 | 3.0938          | 0.3427   |
| 2.83          | 4.0   | 3592 | 3.0101          | 0.3477   |
| 2.7427        | 5.0   | 4490 | 2.9930          | 0.3575   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1

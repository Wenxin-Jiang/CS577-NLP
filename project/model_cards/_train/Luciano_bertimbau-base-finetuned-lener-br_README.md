---
license: mit
language: 
- pt
tags:
- generated_from_trainer
datasets:
- Luciano/lener_br_text_to_lm
model-index:
- name: bertimbau-base-finetuned-lener-br
  results: []
widget:
- text: "Com efeito, se tal fosse possível, o Poder [MASK] – que não dispõe de função legislativa – passaria a desempenhar atribuição que lhe é institucionalmente estranha (a de legislador positivo), usurpando, desse modo, no contexto de um sistema de poderes essencialmente limitados, competência que não lhe pertence, com evidente transgressão ao princípio constitucional da separação de poderes."
- text: "O autor sustenta que a lei é formal e materialmente inconstitucional, em violação aos arts. 15, XIV e XV, 19, caput, 53, 71, §1º, I , e 100, VI e X, da Lei Orgânica do DF, uma vez que, ( i ) originou-se de iniciativa parlamentar quando necessáriainiciativa privativa do Chefe do Poder Executivo, suscitando, inclusive, violação ao postulado constitucional da `` reserva de administração '', a qual impede a ingerência normativa do Poder [MASK] em matérias de competência executiva ; ( ii ) autoriza a delegação de poder de polícia , atividade típica e exclusiva de Estado , na medida em que permite ao Distrito Federal firmar convênios com o Conselho Regional de Engenharia e Agronomia do Distrito Federal - CREA-DF e com o Conselho de Arquitetura e Urbanismo do Distrito Federal - CAU-DF para, por meio do seu corpo técnico e credenciados, atuarem na análise de processos de concessão de Alvará de Construção e de Carta de Habite-se."

---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bertimbau-base-finetuned-lener-br

This model is a fine-tuned version of [neuralmind/bert-base-portuguese-cased](https://huggingface.co/neuralmind/bert-base-portuguese-cased) on the [Luciano/lener_br_text_to_lm](https://huggingface.co/datasets/Luciano/lener_br_text_to_lm) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8132

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 1.3167        | 1.0   | 2079  | 1.1163          |
| 1.1683        | 2.0   | 4158  | 1.0594          |
| 1.0648        | 3.0   | 6237  | 1.0501          |
| 1.0228        | 4.0   | 8316  | 0.9693          |
| 0.9662        | 5.0   | 10395 | 0.9847          |
| 0.9422        | 6.0   | 12474 | 0.9556          |
| 0.8696        | 7.0   | 14553 | 0.8978          |
| 0.7856        | 8.0   | 16632 | nan             |
| 0.7849        | 9.0   | 18711 | 0.9192          |
| 0.7559        | 10.0  | 20790 | 0.8536          |
| 0.7564        | 11.0  | 22869 | 0.9230          |
| 0.7641        | 12.0  | 24948 | 0.8852          |
| 0.7007        | 13.0  | 27027 | 0.8616          |
| 0.7139        | 14.0  | 29106 | 0.8419          |
| 0.6543        | 15.0  | 31185 | 0.8460          |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

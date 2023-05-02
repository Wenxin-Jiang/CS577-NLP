---
language: sv
license: mit
datasets:
- "Gabriel/citesum_swe"
tags:
- summarization

widget:
- text: 'Många samtidiga programmeringsmodeller möjliggör både transaktionsminne och meddelandepassage. För sådana modeller har forskare byggt upp allt effektivare implementeringar och fastställt rimliga korrekthetskriterier, samtidigt som det fortfarande är ett öppet problem att få det bästa av båda världarna. Vi presenterar en programmeringsmodell som är den första som har ogenomskinliga transaktioner, säkert asynkront meddelande som passerar, och ett effektivt genomförande. Våra semantik använder preliminärt meddelande passerar och håller reda på beroenden för att möjliggöra ångra meddelande passerar om en transaktion avbryter. Vi kan programmera kommunikation idiomer som barriär och mötesplats som inte dödläge när de används i ett atomblock. Våra experiment visar att vår modell tillför lite overhead till rena transaktioner, och att den är betydligt effektivare än Transaktionshändelser. Vi använder en ny definition av säkert meddelande som kan vara av oberoende intresse.'

inference:
  parameters:
    temperature: 0.7
    min_length: 30
    max_length: 120
      
model-index:
- name: Gabriel/bart-base-cnn-xsum-cite-swe
  results:
    - task: 
        type: summarization
        name: summarization
      dataset:
        name: Gabriel/citesum_swe
        type: Gabriel/citesum_swe
        split: validation
      metrics:
           - name: Validation ROGUE-1.    
             type: rouge-1
             value: 29.6279
             verified: true
           - name: Validation ROGUE-2
             type: rouge-2
             value: 11.5697
             verified: true
           - name: Validation ROGUE-L
             type: rouge-l
             value: 24.2429
             verified: true
           - name: Validation ROGUE-L-SUM
             type: rouge-l-sum
             value: 24.4557
             verified: true

             
train-eval-index:
- config: Gabriel--citesum_swe
  task: summarization
  task_id: summarization
  splits:
    eval_split: test
  col_mapping:
    document: text
    summary: target
    
co2_eq_emissions:
  emissions: 0.0334
  source: Google Colab
  training_type: fine-tuning
  geographical_location: Fredericia, Denmark
  hardware_used: Tesla P100-PCIE-16GB
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-base-cnn-xsum-cite-swe

This model is a fine-tuned version of [Gabriel/bart-base-cnn-xsum-swe](https://huggingface.co/Gabriel/bart-base-cnn-xsum-swe) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4203
- Rouge1: 29.6279
- Rouge2: 11.5697
- Rougel: 24.2429
- Rougelsum: 24.4557
- Gen Len: 19.9371

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
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.4833        | 1.0   | 2558 | 2.4203          | 29.6279 | 11.5697 | 24.2429 | 24.4557   | 19.9371 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1

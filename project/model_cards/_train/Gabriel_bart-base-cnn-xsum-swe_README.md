---
language: sv
license: mit
tags:
- summarization
datasets:
- Gabriel/xsum_swe
widget:
- text: 'Jordan Hill, Bretagne Covington och Tesfaye Cooper, alla 18, och Tanishia
    Covington, 24, dök upp i en Chicagodomstol på fredag. De fyra har åtalats för
    hatbrott och grov kidnappning och misshandel, bland annat. En insamling på nätet
    till deras offer har hittills samlat in $51.000 (=42.500 pund). Domare Maria Kuriakos
    Ciesil förnekade borgen och frågade: Var fanns din anständighetskänsla? Åklagarna
    berättade för domstolen att misshandeln började i en skåpbil och fortsatte i ett
    hus, där de misstänkta påstås ha tvingat det 18-åriga vita offret, som lider av
    schizofreni och problem med uppmärksamhetsbrist, att dricka toalettvatten och
    kyssa golvet. Polisen hävdar att skåpbilen tidigare stals av Mr Hill, som också
    anklagas för att ha krävt 300 dollar av offrets mor medan de höll honom fången,
    enligt Chicago Tribune. Rätten fick också veta att de misstänkta stoppade en strumpa
    i munnen, tejpade igen munnen och band händerna med ett bälte. I en video gjord
    för Facebook Live som har setts miljontals gånger, kan angriparna höras göra nedsättande
    uttalanden mot vita människor och Donald Trump. Offret hade släppts av på en McDonalds
    för att träffa Mr Hill - som var en av hans vänner - den 31 december. Han hittades
    av en polis tisdagen den 3 januari, en dag efter att han anmäldes saknad av sina
    föräldrar. Åklagarna säger att de misstänkta möter två hatbrott räknas, en på
    grund av offrets ras och den andra på grund av hans funktionshinder.'
inference:
  parameters:
    temperature: 0.7
    min_length: 30
    max_length: 120
train-eval-index:
- config: Gabriel--xsum_swe
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
model-index:
- name: bart-base-cnn-xsum-swe
  results:
  - task:
      type: summarization
      name: summarization
    dataset:
      name: Gabriel/xsum_swe
      type: Gabriel/xsum_swe
      split: validation
    metrics:
    - type: rouge-1
      value: 30.9467
      name: Validation ROGUE-1.
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNWJmOWRhNjgzNjNhY2U3Y2VjY2Y0MzU3MmQyNzVlNzE0NmZjY2YxM2EzZmUxMzA3YTQ1MjU0ZGI3ZjU2OTllNCIsInZlcnNpb24iOjF9.vs305ofbXaHXU-APAdgvvMjJgI7Eb2xpNih3yt9lgFzG5EhDmVm2la62vLgiW_ypvc3v-95CFw2RDvX4GjqQDA
    - type: rouge-2
      value: 12.2589
      name: Validation ROGUE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNGI4NzFhZDBjZmJhYmFhMmYwZTQ3ZTdkYTY3OWU1MDk2MDNjNDAyODg3Yzc2YjY0MmE1ZGZlYjIyODdiYTZjZCIsInZlcnNpb24iOjF9.Xm9uAyUR_QsOKtw7GM0J6jduoL1-qUVra07cpIGQve8au8T8r94pzvb_r5f5YFKioa1rsG8fT8xCHecV2yPjAg
    - type: rouge-l
      value: 25.4487
      name: Validation ROGUE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDdmMjEyNDRhODI5MWJmNGYyMGRiMzlkOGMwODIyZjgyNDg2M2NjMTAwZTlkYWVkZjUxNjRmNzgzZWU0MGMyNCIsInZlcnNpb24iOjF9.Wx0RQwcx4-rJ2K3EG-RwWxvfTpSYii-DW2Wi9TTre6HkByDHNImzesP7sPJ3AcIoHZzt1kw30652nUpmMW5zDg
    - type: rouge-l-sum
      value: 25.4792
      name: Validation ROGUE-L-SUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTFiMDE5YThmNGM5YjMwNThkNzQ1MWUzMGFjNmNiNzE0ZWU0N2I2OTk0MTU4YzkwNzhlNzkzZjI0MjcxNTQ4OSIsInZlcnNpb24iOjF9.uU9p925R6K3m9w-SrfTFb7pbXEfP8T38tsOG9iKiLiLPexQ1sJTTold1oTTWiYOs8oDBIqF1w2eRit4Q7U90Dg
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-base-cnn-xsum-swe

This model is a fine-tuned version of [Gabriel/bart-base-cnn-swe](https://huggingface.co/Gabriel/bart-base-cnn-swe) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1027
- Rouge1: 30.9467
- Rouge2: 12.2589
- Rougel: 25.4487
- Rougelsum: 25.4792
- Gen Len: 19.7379

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.3076        | 1.0   | 6375  | 2.1986          | 29.7041 | 10.9883 | 24.2149 | 24.2406   | 19.7193 |
| 2.0733        | 2.0   | 12750 | 2.1246          | 30.4521 | 11.8107 | 24.9519 | 24.9745   | 19.6592 |
| 1.8933        | 3.0   | 19125 | 2.0989          | 30.9407 | 12.2682 | 25.4135 | 25.4378   | 19.7195 |
| 1.777         | 4.0   | 25500 | 2.1027          | 30.9467 | 12.2589 | 25.4487 | 25.4792   | 19.7379 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1

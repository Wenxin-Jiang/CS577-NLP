---
language: sv
license: mit
tags:
- summarization
datasets:
- Gabriel/cnn_daily_swe
widget:
- text: 'Frankrike lås Sebastien Chabal har nämnts för en farlig tackling på Englands
    Simon Shaw under lördagens VM semifinal i Paris. Simon Shaw lastar av trots att
    Raphael Ibanez, vänster, och Sebastien Chabal. Sale Sharks framåt kommer att ställas
    inför en disciplinär utfrågning på måndag efter hans tackling på motsatt andra-rower
    Shaw noterades genom att citera kommissionär Dennis Wheelahan. Chabal började
    matchen på ersättningsbänken, men kom i 26: e minuten att ersätta den skadade
    Fabien Pelous under värd Frankrikes 14-9 nederlag. Om han blir avstängd missar
    Chabal fredagens tredje och fjärde match på Parc des Princes. Samtidigt, Frankrike
    tränare Bernard Laporte sade att nederlaget var svårare att ta än Englands 24-7
    seger i 2003 semifinalen. "År 2003 var de bättre än oss. I själva verket var de
    bättre än alla", sade Laporte, som lämnar sin roll att tillträda posten som junior
    idrottsminister i den franska regeringen. "De var som Nya Zeeland i denna turnering
    - favoriten, förutom att de gick hela vägen. Den här gången är det svårare för
    igår var det 50-50." Samtidigt, England -- försöker bli den första nationen att
    försvara VM-titeln -- avslöjade att stjärna kicker Jonny Wilkinson återigen hade
    problem med matchbollarna under semifinalen. Flughalvan, som uttryckte sin oro
    efter att ha kämpat med stöveln mot Australien, avvisade en boll innan han sparkade
    en vital trepoängare mot Frankrike. "Vi sa det inte förra veckan men en icke-match
    bollen kom ut på fältet i Marseille som Jonny sparkade," chef för rugby Rob Andrew
    sade. "Han tänkte inte på det när han sparkade det. Matchbollarna är märkta, numrerade
    ett till sex. Igår kväll hade de "World Cup semifinal England vs Frankrike" skrivet
    på dem. På matchkvällen var Jonny vaksam när han sparkade för mål att de faktiskt
    var matchbollar han sparkade. "Träningsbollarna förlorar tryck och form. Hela
    frågan förra veckan, arrangörerna accepterade alla sex matchbollar bör användas
    av båda sidor på torsdagen före matchen. " E-post till en vän.'
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
- name: bart-base-cnn-swe
  results:
  - task:
      type: summarization
      name: summarization
    dataset:
      name: Gabriel/cnn_daily_swe
      type: Gabriel/cnn_daily_swe
      split: validation
    metrics:
    - type: rouge-1
      value: 22.2046
      name: Validation ROGUE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiY2U4YjhhNzhjYmQ2ODY2YWU1NzY5Y2RkYzIzNTUxOTA0MmUwZjNmYTdjNmE5OWNkODhhYWExOGNkOGJkNTBkZiIsInZlcnNpb24iOjF9.lEMnUJOeoa5LepNmjsRflkQmtJAaVo03ocSs9JJuxbLeu4x0oY-XsML3O1IfDJQuvlO4WHZviykRLabkhTtbBQ
    - type: rouge-2
      value: 10.4332
      name: Validation ROGUE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiODkzOGYxNTNiMjc1MGIyODAzY2Q2MjA0NTg1N2NjODc5YWZlZGI5Y2Q3ZDAwNTQyMjA4MmJjOGUxYzVlOGFlNyIsInZlcnNpb24iOjF9.lpn8VP1_AvHXvyYDJHEfMoIpb-_B5fXvMaMQ249Tngo3HBPrexPmhEvGqj1HVnVGxVFyDFhF2tYh4AhThguoBQ
    - type: rouge-l
      value: 18.1753
      name: Validation ROGUE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMWRkM2ViZjRmYmNkZTI1NWE1ODUzNGMwZTYzNzU1Yjk1ODM3NDNkZWMwMjc1ZGJmZGZkNWQxYThmN2ZiZDhjZCIsInZlcnNpb24iOjF9.6ENOPrpZ245V0jcZtiSOmWwdr06W9prPAyE9Qjnn5meiE7yoc0T0oquE9d8SLOfFqYcIbCb6vVUSVxFewj_VAA
    - type: rouge-l-sum
      value: 20.846
      name: Validation ROGUE-L-SUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMDJjODc0MTQwYTM5OGRmMjE2ODUxNGM4YmYxMTJlNDE1MzI0M2Q2ZGJkZDlkOWE2NTMxNjI0YjZjMDQwYjNjNyIsInZlcnNpb24iOjF9.FvNGRVWTCJSafucQKp3eW1B__SAHCL7qHBzooe8ufYIijnNuope0W7AIphex1WMT_9o_Unni2vPGFUvT2o9qAg
---

# bart-base-cnn-swe
This model is a W.I.P

## Model description
BART is a transformer encoder-encoder (seq2seq) model with a bidirectional (BERT-like) encoder and an autoregressive (GPT-like) decoder. BART is pre-trained by (1) corrupting text with an arbitrary noising function, and (2) learning a model to reconstruct the original text. This model is a fine-tuned version of [KBLab/bart-base-swedish-cased](https://huggingface.co/KBLab/bart-base-swedish-cased) on the [Gabriel/bart-base-cnn-swe](https://huggingface.co/datasets/Gabriel/cnn_daily_swe) dataset and can be used for summarization tasks.


## Intended uses & limitations

This model should only be used to fine-tune further on and summarization tasks.


```python
from transformers import pipeline
summarizer = pipeline("summarization", model="Gabriel/bart-base-cnn-swe")
ARTICLE = """
Frankrike lås Sebastien Chabal har nämnts för en farlig tackling på Englands Simon Shaw under lördagens VM semifinal i Paris. Simon Shaw lastar av trots att Raphael Ibanez, vänster, och Sebastien Chabal. Sale Sharks framåt kommer att ställas inför en disciplinär utfrågning på måndag efter hans tackling på motsatt andra-rower Shaw noterades genom att citera kommissionär Dennis Wheelahan. Chabal började matchen på ersättningsbänken, men kom i 26: e minuten att ersätta den skadade Fabien Pelous under värd Frankrikes 14-9 nederlag. Om han blir avstängd missar Chabal fredagens tredje och fjärde match på Parc des Princes. Samtidigt, Frankrike tränare Bernard Laporte sade att nederlaget var svårare att ta än Englands 24-7 seger i 2003 semifinalen. "År 2003 var de bättre än oss. I själva verket var de bättre än alla", sade Laporte, som lämnar sin roll att tillträda posten som junior idrottsminister i den franska regeringen. "De var som Nya Zeeland i denna turnering - favoriten, förutom att de gick hela vägen. Den här gången är det svårare för igår var det 50-50." Samtidigt, England -- försöker bli den första nationen att försvara VM-titeln -- avslöjade att stjärna kicker Jonny Wilkinson återigen hade problem med matchbollarna under semifinalen. Flughalvan, som uttryckte sin oro efter att ha kämpat med stöveln mot Australien, avvisade en boll innan han sparkade en vital trepoängare mot Frankrike. "Vi sa det inte förra veckan men en icke-match bollen kom ut på fältet i Marseille som Jonny sparkade," chef för rugby Rob Andrew sade. "Han tänkte inte på det när han sparkade det. Matchbollarna är märkta, numrerade ett till sex. Igår kväll hade de "World Cup semifinal England vs Frankrike" skrivet på dem. På matchkvällen var Jonny vaksam när han sparkade för mål att de faktiskt var matchbollar han sparkade. "Träningsbollarna förlorar tryck och form. Hela frågan förra veckan, arrangörerna accepterade alla sex matchbollar bör användas av båda sidor på torsdagen före matchen. " E-post till en vän.
"""
print(summarizer(ARTICLE, max_length=130, min_length=30, num_beams=10 ,do_sample=False))
>>> [{'summary_text': """ Frankrike lås Sebastien Chabal har nämnts för en farlig tackling på Englands Simon Shaw under VM semifinal i Paris. Sale Sharks framåt kommer att ställas inför en disciplinär utfrågning på måndag efter hans tackling på motsatt andra - rower Shaw noterades genom att citera kommissionär Dennis Wheelahan. Om Chabal blir avstängd missar Chabal fredagens tredje och fjärde match på Parc des Princes."""}]
```

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2*2 = 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.2349        | 1.0   | 17944 | 2.0643          | 21.9564 | 10.2133 | 17.9958 | 20.6502   | 19.9992 |
| 2.0726        | 2.0   | 35888 | 2.0253          | 22.0568 | 10.3302 | 18.0648 | 20.7482   | 19.9996 |
| 1.8658        | 3.0   | 53832 | 2.0333          | 22.0871 | 10.2902 | 18.0577 | 20.7082   | 19.998  |
| 1.8121        | 4.0   | 71776 | 1.9759          | 22.2046 | 10.4332 | 18.1753 | 20.846    | 19.9971 |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

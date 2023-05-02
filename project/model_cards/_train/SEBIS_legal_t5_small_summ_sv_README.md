
---
language: Swedish   
tags:
- summarization Swedish model
datasets:
- jrc-acquis
widget:
- text: "EUROPEISKA GEMENSKAPERNAS RÅD HAR ANTAGIT DENNA FÖRORDNING med beaktande av Fördraget om upprättandet av Europeiska ekonomiska gemenskapen, särskilt artiklarna 43 och 100a i detta, med beaktande av kommissionens förslag(1), i samarbete med Europaparlamentet(2), med beaktande av Ekonomiska och sociala kommitténs yttrande(3), och med beaktande av följande: Det bör införas förbud mot användning av blybaserade kapsyler eller blybaserad folie i förslutningar på förpackningar som används då aromatiserade viner, aromatiserade vinbaserade drycker och aromatiserade drinkar baserade på vinprodukter släpps ut på marknaden i syfte att undvika risken för kontaminering, särskilt vid oavsiktlig kontakt med sådana produkter, samt risken för miljöförorening på grund av avfall som innehåller bly från kapsyler och folie av detta slag. Tillverkarna och användarna av kapsylerna och folien i fråga bör dock ges tid att anpassa sig genom att förbudet inte tillämpas förrän från och med den 1 januari 1993. Det är även nödvändigt att tillåta att produkter som före detta datum tappats på buteljer med blybaserade kapsyler eller blybaserad folie får säljas till dess att lagren är uttömda. Vissa definitioner av aromatiserade vinbaserade drycker bör anpassas så att större hänsyn tas till traditionella framställningsmetoder. Förordning (EEG) nr 1601/91(4) bör därför ändras. HÄRIGENOM FÖRESKRIVS FÖLJANDE. Artikel 1 Förordning (EEG) nr 1601/91 ändras på följande sätt: 1. Artikel 2.3 a första stycket skall ersättas med följande: %quot%a) Sangria: en dryck som framställs av vin - som smaksatts genom tillsats av naturliga extrakt eller essenser av citrusfrukt, - med eller utan saft av sådan frukt, - eventuellt: - med tillsats av kryddor, - sötat, - med tillsats av CO2, och med en slutlig alkoholstyrka på under 12 volymprocent.%quot% 2. Artikel 2.3 e skall ersättas med följande: %quot%e) Kalte Ente: Smaksatt vinbaserad dryck som framställs genom att vin, pärlande vin eller pärlande vin med tillsatt CO2 blandas med mousserande vin eller mousserande vin med tillsatt CO2 och tillsätts naturlig citronsubstans eller extrakt av detta som måste ge en tydligt framträdande smak. Slutprodukten måste innehålla minst 25 volymprocent mousserande vin eller mousserande vin med tillsatt CO2.%quot% 3. Följande punkt skall införas i artikel 8: %quot%4.a Från och med den 1 januari 1993 får buteljerade produkter som omfattas av denna förordning inte saluhållas eller släppas ut på marknaden i förpackningar med förslutningar som täckts med blybaserade kapsyler eller blybaserad folie. Dock får produkter som före detta datum tappats på flaskor med detta slag av kapsyler eller folie avyttras till dess att lagren tömts.%quot% Artikel 2 Denna förordning träder i kraft den tredje dagen efter det att den har offentliggjorts i Europeiska gemenskapernas officiella tidning. Denna förordning är till alla delar bindande och direkt tillämplig i alla medlemsstater. Utfärdad i Bryssel den 9 november 1992. På rådets vägnar D. HURD Ordförande (1) EGT nr C 69, 18.3.1992, s. 11. (2) EGT nr C 241, 21.9.1992, s. 97 och beslut av den 28 oktober 1992. (3) EGT nr C 169, 6.7.1992, s. 1. (4) EGT nr L 149, 14.6.1991, s. 1. "

---

# legal_t5_small_summ_sv model

Model for Summarization of legal text written in Swedish. It was first released in
[this repository](https://github.com/agemagician/LegalTrans). This model is trained on three parallel corpus from jrc-acquis.


## Model description

legal_t5_small_summ_sv is based on the `t5-small` model and was trained on a large corpus of parallel text. This is a smaller model, which scales the baseline model of t5 down by using `dmodel = 512`, `dff = 2,048`, 8-headed attention, and only 6 layers each in the encoder and decoder. This variant has about 60 million parameters.

## Intended uses & limitations

The model could be used for summarization of legal texts written in Swedish.

### How to use

Here is how to use this model to summarize legal text written in Swedish in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, TranslationPipeline

pipeline = TranslationPipeline(
model=AutoModelWithLMHead.from_pretrained("SEBIS/legal_t5_small_summ_sv"),
tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path = "SEBIS/legal_t5_small_summ_sv", do_lower_case=False, 
                                            skip_special_tokens=True),
    device=0
)

sv_text = "EUROPEISKA GEMENSKAPERNAS RÅD HAR ANTAGIT DENNA FÖRORDNING med beaktande av Fördraget om upprättandet av Europeiska ekonomiska gemenskapen, särskilt artiklarna 43 och 100a i detta, med beaktande av kommissionens förslag(1), i samarbete med Europaparlamentet(2), med beaktande av Ekonomiska och sociala kommitténs yttrande(3), och med beaktande av följande: Det bör införas förbud mot användning av blybaserade kapsyler eller blybaserad folie i förslutningar på förpackningar som används då aromatiserade viner, aromatiserade vinbaserade drycker och aromatiserade drinkar baserade på vinprodukter släpps ut på marknaden i syfte att undvika risken för kontaminering, särskilt vid oavsiktlig kontakt med sådana produkter, samt risken för miljöförorening på grund av avfall som innehåller bly från kapsyler och folie av detta slag. Tillverkarna och användarna av kapsylerna och folien i fråga bör dock ges tid att anpassa sig genom att förbudet inte tillämpas förrän från och med den 1 januari 1993. Det är även nödvändigt att tillåta att produkter som före detta datum tappats på buteljer med blybaserade kapsyler eller blybaserad folie får säljas till dess att lagren är uttömda. Vissa definitioner av aromatiserade vinbaserade drycker bör anpassas så att större hänsyn tas till traditionella framställningsmetoder. Förordning (EEG) nr 1601/91(4) bör därför ändras. HÄRIGENOM FÖRESKRIVS FÖLJANDE. Artikel 1 Förordning (EEG) nr 1601/91 ändras på följande sätt: 1. Artikel 2.3 a första stycket skall ersättas med följande: %quot%a) Sangria: en dryck som framställs av vin - som smaksatts genom tillsats av naturliga extrakt eller essenser av citrusfrukt, - med eller utan saft av sådan frukt, - eventuellt: - med tillsats av kryddor, - sötat, - med tillsats av CO2, och med en slutlig alkoholstyrka på under 12 volymprocent.%quot% 2. Artikel 2.3 e skall ersättas med följande: %quot%e) Kalte Ente: Smaksatt vinbaserad dryck som framställs genom att vin, pärlande vin eller pärlande vin med tillsatt CO2 blandas med mousserande vin eller mousserande vin med tillsatt CO2 och tillsätts naturlig citronsubstans eller extrakt av detta som måste ge en tydligt framträdande smak. Slutprodukten måste innehålla minst 25 volymprocent mousserande vin eller mousserande vin med tillsatt CO2.%quot% 3. Följande punkt skall införas i artikel 8: %quot%4.a Från och med den 1 januari 1993 får buteljerade produkter som omfattas av denna förordning inte saluhållas eller släppas ut på marknaden i förpackningar med förslutningar som täckts med blybaserade kapsyler eller blybaserad folie. Dock får produkter som före detta datum tappats på flaskor med detta slag av kapsyler eller folie avyttras till dess att lagren tömts.%quot% Artikel 2 Denna förordning träder i kraft den tredje dagen efter det att den har offentliggjorts i Europeiska gemenskapernas officiella tidning. Denna förordning är till alla delar bindande och direkt tillämplig i alla medlemsstater. Utfärdad i Bryssel den 9 november 1992. På rådets vägnar D. HURD Ordförande (1) EGT nr C 69, 18.3.1992, s. 11. (2) EGT nr C 241, 21.9.1992, s. 97 och beslut av den 28 oktober 1992. (3) EGT nr C 169, 6.7.1992, s. 1. (4) EGT nr L 149, 14.6.1991, s. 1. "

pipeline([sv_text], max_length=512)
```

## Training data

The legal_t5_small_summ_sv model was trained on [JRC-ACQUIS](https://wt-public.emm4u.eu/Acquis/index_2.2.html) dataset consisting of 19 Thousand texts.

## Training procedure

The model was trained on a single TPU Pod V3-8 for 250K steps in total, using sequence length 512 (batch size 64). It has a total of approximately 220M parameters and was trained using the encoder-decoder architecture. The optimizer used is AdaFactor with inverse square root learning rate schedule for pre-training.
### Preprocessing

An unigram model trained with 88M lines of text from the parallel corpus (of all possible language pairs) to get the vocabulary (with byte pair encoding), which is used with this model.

### Pretraining



## Evaluation results

When the model is used for classification test dataset, achieves the following results:

Test results :

| Model | Rouge1  | Rouge2 | Rouge Lsum |
|:-----:|:-----:|:-----:|:-----:|
|   legal_t5_small_summ_sv | 78.84|69.97 |77.59|


### BibTeX entry and citation info

> Created by [Ahmed Elnaggar/@Elnaggar_AI](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/)

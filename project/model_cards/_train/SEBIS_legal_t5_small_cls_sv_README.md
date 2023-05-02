
---
language: Swedish   
tags:
- classification Swedish model
datasets:
- jrc-acquis
widget:
- text: "Rådets förordning (EG) nr 1973/2002 av den 5 november 2002 om ändring av förordning (EG) nr 2026/97 om skydd mot subventionerad import från länder som inte är medlemmar i Europeiska gemenskapen EUROPEISKA UNIONENS RÅD HAR ANTAGIT DENNA FÖRORDNING med beaktande av Fördraget om upprättandet av Europeiska gemenskapen, särskilt artikel 133 i detta, med beaktande av kommissionens förslag, och av följande skäl: (1) Rådet antog genom förordning (EG) nr 2026/97(1) gemensamma regler för skydd mot subventionerad import från länder som inte är medlemmar i Europeiska gemenskapen. (2) I artikel 6 i förordning (EG) nr 2026/97 anges vissa riktlinjer för beräkning av förmånen för mottagaren, inbegripet det riktmärke för marknaden enligt vilket förmånens storlek beräknas. Det bör klargöras vilka bestämmelser som bör följas i de fall ett sådant riktmärke för marknaden inte finns i det berörda landet. I en sådan situation bör riktmärket fastställas genom anpassning av de villkor som råder i det berörda landet på grundval av de faktiska uppgifter som är tillgängliga där. Om detta inte är praktiskt genomförbart på grund av att det inte finns några uppgifter om sådana priser och kostnader eller på grund av att dessa är otillförlitliga, bör riktmärket fastställas med hjälp av de villkor som gäller på andra marknader. (3) I artikel 4 i förordning (EG) nr 2026/97 anges att vissa subventioner som rör miljö, forskning och regional utveckling inte är utjämningsbara. I artikel 10.5 och 10.6 i den förordningen anges vidare att undersökningar kan inledas för att avgöra om subventioner är icke-utjämningsbara och att de inte bör inledas om de rör vissa icke-utjämningsbara subventioner. Motsvarande bestämmelser i WTO-avtalet beträffande subventioner och utjämningsåtgärder var avsedda att löpa ut den 31 december 1999, såvida inte WTO-medlemsstaterna beslutade annat. Inget sådant beslut har fattats och de relevanta bestämmelserna är därför inte längre tillämpliga. Det är därför nödvändigt att fastställa huruvida bestämmelserna rörande icke-utjämningsbara subventioner i förordning (EG) nr 2026/97 bör fortsätta att gälla. Gemenskapens viktigaste handelspartner tillämpar inte längre dessa bestämmelser i sina utjämningsundersökningar. Av denna anledning och i syfte att upprätthålla balansen mellan rättigheter och skyldigheter enligt nämnda WTO-avtal bör de bestämmelser i förordning (EG) nr 2026/97 som rör icke-utjämningsbara subventioner upphöra att gälla. (4) I artikel 28.5 i förordning (EG) nr 2026/97 anges att om tillgängliga uppgifter används skall upplysningarna kontrolleras genom att jämföras med uppgifter från flera källor. Det bör specificeras att dessa källor också kan utgöras av uppgifter om världsmarknaden eller andra representativa marknader. (5) Ur rättssäkerhetssynpunkt är det lämpligt att dessa ändringar tillämpas så snart som möjligt i samband med alla nya undersökningar. HÄRIGENOM FÖRESKRIVS FÖLJANDE. Artikel 1 Förordning (EG) nr 2026/97 ändras enligt följande: 1. I artikel 6 d skall följande text läggas till: %quot%Om det inte finns några sådana rådande marknadsvillkor för produkterna eller tjänsterna i fråga i det land som tillhandahåller eller köper dem, som kan användas som lämpliga riktmärken, skall en av följande bestämmelser tillämpas: i) De villkor som råder i landet i fråga skall justeras på grundval av de faktiska kostnader, priser och andra faktorer som är tillgängliga i det landet med hjälp av ett lämpligt belopp som avspeglar normala marknadsvillkor. ii) I tillämpliga fall skall de villkor användas som råder på marknaden i ett annat land eller på världsmarknaden och som är tillgängliga för mottagaren.%quot% 2. Artikel 4 och artikel 10.5 och 10.6 skall utgå. 3. I artikel 28.5 skall följande mening läggas till: %quot%Sådana uppgifter kan, i tillämpliga fall, inbegripa relevanta upplysningar om världsmarknaden eller andra representativa marknader.%quot% Artikel 2 Denna förordning träder i kraft dagen efter det att den har offentliggjorts i Europeiska gemenskapernas officiella tidning. Den skall tillämpas i samband med alla undersökningar som inleds i enlighet med förordning (EG) nr 2026/97 efter dagen för ikraftträdandet av denna förordning. Denna förordning är till alla delar bindande och direkt tillämplig i alla medlemsstater. Utfärdad i Bryssel den 5 november 2002. På rådets vägnar T. Pedersen Ordförande (1) EGT L 288, 21.10.1997, s. 1."

---

# legal_t5_small_cls_sv model

Model for classification of legal text written in Swedish. It was first released in
[this repository](https://github.com/agemagician/LegalTrans). This model is trained on three parallel corpus from jrc-acquis.


## Model description

legal_t5_small_cls_sv is based on the `t5-small` model and was trained on a large corpus of parallel text. This is a smaller model, which scales the baseline model of t5 down by using `dmodel = 512`, `dff = 2,048`, 8-headed attention, and only 6 layers each in the encoder and decoder. This variant has about 60 million parameters.

## Intended uses & limitations

The model could be used for classification of legal texts written in Swedish.

### How to use

Here is how to use this model to classify legal text written in Swedish in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, TranslationPipeline

pipeline = TranslationPipeline(
model=AutoModelWithLMHead.from_pretrained("SEBIS/legal_t5_small_cls_sv"),
tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path = "SEBIS/legal_t5_small_cls_sv", do_lower_case=False, 
                                            skip_special_tokens=True),
    device=0
)

sv_text = "Rådets förordning (EG) nr 1973/2002 av den 5 november 2002 om ändring av förordning (EG) nr 2026/97 om skydd mot subventionerad import från länder som inte är medlemmar i Europeiska gemenskapen EUROPEISKA UNIONENS RÅD HAR ANTAGIT DENNA FÖRORDNING med beaktande av Fördraget om upprättandet av Europeiska gemenskapen, särskilt artikel 133 i detta, med beaktande av kommissionens förslag, och av följande skäl: (1) Rådet antog genom förordning (EG) nr 2026/97(1) gemensamma regler för skydd mot subventionerad import från länder som inte är medlemmar i Europeiska gemenskapen. (2) I artikel 6 i förordning (EG) nr 2026/97 anges vissa riktlinjer för beräkning av förmånen för mottagaren, inbegripet det riktmärke för marknaden enligt vilket förmånens storlek beräknas. Det bör klargöras vilka bestämmelser som bör följas i de fall ett sådant riktmärke för marknaden inte finns i det berörda landet. I en sådan situation bör riktmärket fastställas genom anpassning av de villkor som råder i det berörda landet på grundval av de faktiska uppgifter som är tillgängliga där. Om detta inte är praktiskt genomförbart på grund av att det inte finns några uppgifter om sådana priser och kostnader eller på grund av att dessa är otillförlitliga, bör riktmärket fastställas med hjälp av de villkor som gäller på andra marknader. (3) I artikel 4 i förordning (EG) nr 2026/97 anges att vissa subventioner som rör miljö, forskning och regional utveckling inte är utjämningsbara. I artikel 10.5 och 10.6 i den förordningen anges vidare att undersökningar kan inledas för att avgöra om subventioner är icke-utjämningsbara och att de inte bör inledas om de rör vissa icke-utjämningsbara subventioner. Motsvarande bestämmelser i WTO-avtalet beträffande subventioner och utjämningsåtgärder var avsedda att löpa ut den 31 december 1999, såvida inte WTO-medlemsstaterna beslutade annat. Inget sådant beslut har fattats och de relevanta bestämmelserna är därför inte längre tillämpliga. Det är därför nödvändigt att fastställa huruvida bestämmelserna rörande icke-utjämningsbara subventioner i förordning (EG) nr 2026/97 bör fortsätta att gälla. Gemenskapens viktigaste handelspartner tillämpar inte längre dessa bestämmelser i sina utjämningsundersökningar. Av denna anledning och i syfte att upprätthålla balansen mellan rättigheter och skyldigheter enligt nämnda WTO-avtal bör de bestämmelser i förordning (EG) nr 2026/97 som rör icke-utjämningsbara subventioner upphöra att gälla. (4) I artikel 28.5 i förordning (EG) nr 2026/97 anges att om tillgängliga uppgifter används skall upplysningarna kontrolleras genom att jämföras med uppgifter från flera källor. Det bör specificeras att dessa källor också kan utgöras av uppgifter om världsmarknaden eller andra representativa marknader. (5) Ur rättssäkerhetssynpunkt är det lämpligt att dessa ändringar tillämpas så snart som möjligt i samband med alla nya undersökningar. HÄRIGENOM FÖRESKRIVS FÖLJANDE. Artikel 1 Förordning (EG) nr 2026/97 ändras enligt följande: 1. I artikel 6 d skall följande text läggas till: %quot%Om det inte finns några sådana rådande marknadsvillkor för produkterna eller tjänsterna i fråga i det land som tillhandahåller eller köper dem, som kan användas som lämpliga riktmärken, skall en av följande bestämmelser tillämpas: i) De villkor som råder i landet i fråga skall justeras på grundval av de faktiska kostnader, priser och andra faktorer som är tillgängliga i det landet med hjälp av ett lämpligt belopp som avspeglar normala marknadsvillkor. ii) I tillämpliga fall skall de villkor användas som råder på marknaden i ett annat land eller på världsmarknaden och som är tillgängliga för mottagaren.%quot% 2. Artikel 4 och artikel 10.5 och 10.6 skall utgå. 3. I artikel 28.5 skall följande mening läggas till: %quot%Sådana uppgifter kan, i tillämpliga fall, inbegripa relevanta upplysningar om världsmarknaden eller andra representativa marknader.%quot% Artikel 2 Denna förordning träder i kraft dagen efter det att den har offentliggjorts i Europeiska gemenskapernas officiella tidning. Den skall tillämpas i samband med alla undersökningar som inleds i enlighet med förordning (EG) nr 2026/97 efter dagen för ikraftträdandet av denna förordning. Denna förordning är till alla delar bindande och direkt tillämplig i alla medlemsstater. Utfärdad i Bryssel den 5 november 2002. På rådets vägnar T. Pedersen Ordförande (1) EGT L 288, 21.10.1997, s. 1."

pipeline([sv_text], max_length=512)
```

## Training data

The legal_t5_small_cls_sv model was trained on [JRC-ACQUIS](https://wt-public.emm4u.eu/Acquis/index_2.2.html) dataset consisting of 23 Thousand texts.

## Training procedure


The model was trained on a single TPU Pod V3-8 for 250K steps in total, using sequence length 512 (batch size 64). It has a total of approximately 220M parameters and was trained using the encoder-decoder architecture. The optimizer used is AdaFactor with inverse square root learning rate schedule for pre-training.

### Preprocessing

An unigram model trained with 88M lines of text from the parallel corpus (of all possible language pairs) to get the vocabulary (with byte pair encoding), which is used with this model.

### Pretraining



## Evaluation results

When the model is used for classification test dataset, achieves the following results:

Test results :

| Model | F1 score |
|:-----:|:-----:|
|   legal_t5_small_cls_sv | 0.6449|


### BibTeX entry and citation info

> Created by [Ahmed Elnaggar/@Elnaggar_AI](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/)

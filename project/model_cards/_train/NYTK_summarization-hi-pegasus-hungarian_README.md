---
language: 
  - hu
tags:
- summarization
metrics:
- rouge
widget:
- text: "A Tisza-parti város állatkertjében régóta tartanak szurikátákat ( Suricata suricatta ) , de tavaly tavaszig nem sikerült szaporítani őket , annak ellenére , hogy tágas ház és kifutó épült számukra - közölte Veprik Róbert igazgató . 2010-ben alakult ki az új - három Amszterdamból származó nőstényből és egy budapesti fiatal hímből álló - csapat , amely szaporodni kezdett . 2011-ben három , idén pedig egy utóddal örvendeztették meg a gondozókat és az állatbarátokat . A szurikáták utódai - tizenegy hetes vemhesség után - október és március között vakon és szőrtelenül jönnek a világra . A kicsinyek háromhetesen bújnak elő az üregből , és nevelésükben mindkét szülő részt vesz . A szurikátacsapatokban a család tagjai nagyon szoros kapcsolatban állnak egymással , viszont nagyon harciasan fellépnek az idegenekkel szemben , akár meg is ölhetik azt az állatot , amelyet betolakodónak tekintenek . Bár a Dél-Afrikában , a Kalahári sivatagban őshonos cibetmacskaféle ragadozókat a szegedi állatkertben természetes élőhelyükhöz képest kevesebb veszély fenyegeti , a vadasparki erdőben ragadozó madarak is élnek , amelyek akár zsákmányként is tekinthetnének a szurikátákra . A szegedi csapatnál azonban szigorú őrség van , mindig lesi valaki két lábra állva a veszélyforrásokat . Az őrszemek figyelmét még a sárkányrepülők is felkeltik , és felbukkanásakor valamennyi egyed biztos helyre menekül . A szurikáták a Kalahári sivatag bozótos , sziklás területein csapatokban élnek . A 700 gramm körüli testtömegű ragadozók rovarokkal , lárvákkal , skorpiókkal táplálkoznak , de néha elfogyasztják a kisebb gerinceseket , tojásokat és növényi gumókat is . A nappal aktív állatok földalatti üregrendszert ásnak , amelynek több bejárata is van . Ha a szurikáták idegen csapattal vagy ragadozóval kerülnek szembe , azonnal elkezdenek ásni , nagy porfelhőt kavarva . Az is gyakorta előfordul , hogy szorosan egymáshoz bújnak , felborzolják szőrüket , megnyújtják testüket , hogy minél nagyobbnak látszódjanak . Az előadásuk csúcspontján pedig az egész csapat a levegőbe ugrik , közben pedig morog . A hangadás egyébként is fontos a szurikáták kapcsolatában , az egyedek legalább tízféle jelzést használnak a kolónián belül ."

---

# Hungarian Abstractive Summarization with finetuned Pegasus model

For further details, see or [our demo site](https://juniper.nytud.hu/demo/nlp).

- Finetuned on Pegasus model
- Finetuned on HI corpus (hvg.hu + index.hu)
  - Segments: 559162
  	
## Limitations

- tokenized input text (tokenizer: [HuSpaCy](https://huggingface.co/huspacy))
- max_source_length = 1024
- max_target_length = 256
- because of modified vocab, only PegasusTokenizerFast can be used

## Results

| Model | HI | 
| ------------- | ------------- |
| mBART | 35.17/16.46/25.61 |
| mT5 | 33.30/15.97/24.65 |
| PEGASUS | 30.36/13.11/21.57 |

## Usage

```python
from transformers import PegasusForConditionalGeneration, PegasusTokenizerFast
model_name = 'NYTK/summarization-hi-pegasus-hungarian'

tokenizer = PegasusTokenizerFast.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name)
input_text = "A Tisza-parti város állatkertjében régóta tartanak szurikátákat ( Suricata suricatta ) , de tavaly tavaszig nem sikerült szaporítani őket , annak ellenére , hogy tágas ház és kifutó épült számukra - közölte Veprik Róbert igazgató . 2010-ben alakult ki az új - három Amszterdamból származó nőstényből és egy budapesti fiatal hímből álló - csapat , amely szaporodni kezdett . 2011-ben három , idén pedig egy utóddal örvendeztették meg a gondozókat és az állatbarátokat . A szurikáták utódai - tizenegy hetes vemhesség után - október és március között vakon és szőrtelenül jönnek a világra . A kicsinyek háromhetesen bújnak elő az üregből , és nevelésükben mindkét szülő részt vesz . A szurikátacsapatokban a család tagjai nagyon szoros kapcsolatban állnak egymással , viszont nagyon harciasan fellépnek az idegenekkel szemben , akár meg is ölhetik azt az állatot , amelyet betolakodónak tekintenek . Bár a Dél-Afrikában , a Kalahári sivatagban őshonos cibetmacskaféle ragadozókat a szegedi állatkertben természetes élőhelyükhöz képest kevesebb veszély fenyegeti , a vadasparki erdőben ragadozó madarak is élnek , amelyek akár zsákmányként is tekinthetnének a szurikátákra . A szegedi csapatnál azonban szigorú őrség van , mindig lesi valaki két lábra állva a veszélyforrásokat ."

tokenized_text = tokenizer(input_text, truncation=True, max_length=1024, return_tensors="pt")
summarization = model.generate(**tokenized_text, max_length=256)

print(tokenizer.batch_decode(summarization, skip_special_tokens=True))
```


## Citation
If you use this model, please cite the following paper:

```
@inproceedings {yang-multi-sum,
    title = {{Többnyelvű modellek és PEGASUS finomhangolása magyar nyelvű absztraktív összefoglalás feladatára}},
	booktitle = {XIX. Magyar Számítógépes Nyelvészeti Konferencia (MSZNY 2023)},
	year = {2023},
	publisher = {Szegedi Tudományegyetem, Informatikai Intézet},
	address = {Szeged, Magyarország},
	author = {Yang, Zijian Győző},
	pages = {381--393}
}

```
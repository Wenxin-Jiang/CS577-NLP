---
language:
- hu
tags:
- summarization
license: apache-2.0
metrics:
- rouge
widget:
- text: >-
    A Tisza-parti város állatkertjében régóta tartanak szurikátákat ( Suricata
    suricatta ) , de tavaly tavaszig nem sikerült szaporítani őket , annak
    ellenére , hogy tágas ház és kifutó épült számukra - közölte Veprik Róbert
    igazgató . 2010-ben alakult ki az új - három Amszterdamból származó
    nőstényből és egy budapesti fiatal hímből álló - csapat , amely szaporodni
    kezdett . 2011-ben három , idén pedig egy utóddal örvendeztették meg a
    gondozókat és az állatbarátokat . A szurikáták utódai - tizenegy hetes
    vemhesség után - október és március között vakon és szőrtelenül jönnek a
    világra . A kicsinyek háromhetesen bújnak elő az üregből , és nevelésükben
    mindkét szülő részt vesz . A szurikátacsapatokban a család tagjai nagyon
    szoros kapcsolatban állnak egymással , viszont nagyon harciasan fellépnek az
    idegenekkel szemben , akár meg is ölhetik azt az állatot , amelyet
    betolakodónak tekintenek . Bár a Dél-Afrikában , a Kalahári sivatagban
    őshonos cibetmacskaféle ragadozókat a szegedi állatkertben természetes
    élőhelyükhöz képest kevesebb veszély fenyegeti , a vadasparki erdőben
    ragadozó madarak is élnek , amelyek akár zsákmányként is tekinthetnének a
    szurikátákra . A szegedi csapatnál azonban szigorú őrség van , mindig lesi
    valaki két lábra állva a veszélyforrásokat . Az őrszemek figyelmét még a
    sárkányrepülők is felkeltik , és felbukkanásakor valamennyi egyed biztos
    helyre menekül . A szurikáták a Kalahári sivatag bozótos , sziklás
    területein csapatokban élnek . A 700 gramm körüli testtömegű ragadozók
    rovarokkal , lárvákkal , skorpiókkal táplálkoznak , de néha elfogyasztják a
    kisebb gerinceseket , tojásokat és növényi gumókat is . A nappal aktív
    állatok földalatti üregrendszert ásnak , amelynek több bejárata is van . Ha
    a szurikáták idegen csapattal vagy ragadozóval kerülnek szembe , azonnal
    elkezdenek ásni , nagy porfelhőt kavarva . Az is gyakorta előfordul , hogy
    szorosan egymáshoz bújnak , felborzolják szőrüket , megnyújtják testüket ,
    hogy minél nagyobbnak látszódjanak . Az előadásuk csúcspontján pedig az
    egész csapat a levegőbe ugrik , közben pedig morog . A hangadás egyébként is
    fontos a szurikáták kapcsolatában , az egyedek legalább tízféle jelzést
    használnak a kolónián belül .
---

# Hungarian Abstractive Summarization BART model

For further models, scripts and details, see [our repository](https://github.com/nytud/neural-models) or [our demo site](https://juniper.nytud.hu/demo/nlp).

- BART base model (see Results Table - bold):
  - Pretrained on Webcorpus 2.0
  - Finetuned NOL corpus (nol.hu)
  	- Segments: 397,343
  	
## Limitations

- tokenized input text (tokenizer: [HuSpaCy](https://huggingface.co/huspacy))
- max_source_length = 512
- max_target_length = 256

## Results

| Model | HI | NOL |
| ------------- | ------------- | ------------- |
| BART-base-512 | 30.18/13.86/22.92 | **46.48/32.40/39.45**  |
| BART-base-1024| 31.86/14.59/23.79 | 47.01/32.91/39.97 |

## Citation
If you use this model, please cite the following paper:

```
@inproceedings {yang-bart,
    title = {{BARTerezzünk! - Messze, messze, messze a világtól, - BART kísérleti modellek magyar nyelvre}},
	booktitle = {XVIII. Magyar Számítógépes Nyelvészeti Konferencia},
	year = {2022},
	publisher = {Szegedi Tudományegyetem, Informatikai Intézet},
	address = {Szeged, Magyarország},
	author = {Yang, Zijian Győző},
	pages = {15--29}
}

```
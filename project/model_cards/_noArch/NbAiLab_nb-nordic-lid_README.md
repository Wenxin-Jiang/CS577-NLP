---
license: openrail
language:
- dan
- eng
- fao
- fin
- isl
- nno
- nob
- sma
- sme
- smj
- smn
- sms
- swe
tags:
- fasttext
- text-classification
- language-detection
- language-identification
datasets:
- tatoeba
library_name: fasttext
inference: false
pipeline_tag: text-classification
---

# NB-NORDIC-LID

This repo contains models for the identification of language in text (also referred to as language detection). It is based on Fasttext and designed with the Nordic languages in mind, including several Sámi languages. It comes in two flavours, `nb-nordic-lid`, a model that identifies between the 12 most common languages in the Nordic countries (plus English), and `nb-nordic-lid.159`, a model that extends that list to 159 languages of the world. Moreover, each of them come in large and small (quantized) versions.

| Model                       | Size              |   Precision |   Recall |   F1-Score |   Support |
|:----------------------------|:------------------|------------:|---------:|-----------:|----------:|
| [`nb-nordic-lid.bin`](https://huggingface.co/NbAiLab/nb-nordic-lid/resolve/main/nb-nordic-lid.bin) (large)    | 274 MB            |      0.9901 |   0.9900 |     0.9900 |      5500 |
| [`nb-nordic-lid.ftz`](https://huggingface.co/NbAiLab/nb-nordic-lid/resolve/main/nb-nordic-lid.ftz) (small)    | 1.87 MB           |      0.9889 |   0.9890 |     0.9890 |      5500 |
| [`nb-nordic-lid.159.bin`](https://huggingface.co/NbAiLab/nb-nordic-lid/resolve/main/nb-nordic-lid.159.bin) (large)| 9.63 GB           |      0.9434 |   0.9528 |     0.9476 |     44049 |
| [`nb-nordic-lid.159.ftz`](https://huggingface.co/NbAiLab/nb-nordic-lid/resolve/main/nb-nordic-lid.159.ftz) (small)| 11.2 MB           |      0.9275 |   0.9399 |     0.9327 |     44049 |


## Usage

After download, the models can be used through the Fasttext library:

```python
from huggingface_hub import hf_hub_download
import fasttext

model_name = "nb-nordic-lid.ftz"
model = fasttext.load_model(hf_hub_download("NbAiLab/nb-nordic-lid", model_name))

model.predict("Debatt er bra og sunt for demokratier, og en forutsetning for politikkutvikling.", threshold=0.25)
# (('__label__nob',), array([0.95482141]))
```

Alternatively, these models are also integrated into the the experimental `nbailab` CLI application:

```bash
$ echo "Jeg leser en bok" | nbailab langid --model-name  nb-nordic-lid.ftz
nob,0.9999788999557495
```


## Languages

### `nb-nordic-lid.bin`

Trained on sentences from the [GiellaT's Translation Memories](https://giellalt.github.io/tm/TranslationMemories.html) and [Wortschatz's corpora](https://wortschatz.uni-leipzig.de/en/download).

| ISO-639-3    | Language          |   Precision |   Recall |   F1-Score |   Support |
|:-------------|:------------------|------------:|---------:|-----------:|----------:|
| dan          | Danish            |      0.9720 |   0.9838 |     0.9779 |       494 |
| eng          | English           |      0.9980 |   0.9940 |     0.9960 |       502 |
| fao          | Faroese           |      0.9920 |   0.9940 |     0.9930 |       499 |
| fin          | Finnish           |      1.0000 |   1.0000 |     1.0000 |       500 |
| isl          | Icelandic         |      0.9900 |   0.9920 |     0.9910 |       499 |
| nno          | Norwegian Nynorsk |      0.9920 |   0.9861 |     0.9890 |       503 |
| nob          | Norwegian Bokmål  |      0.9840 |   0.9743 |     0.9791 |       505 |
| sma          | Southern Sami     |      0.9800 |   0.9703 |     0.9751 |       101 |
| sme          | Northern Sami     |      1.0000 |   0.9921 |     0.9960 |       504 |
| smj          | Lule Sami         |      0.9920 |   0.9960 |     0.9940 |       498 |
| smn          | Inari Sami        |      0.9950 |   1.0000 |     0.9975 |       199 |
| sms          | Skolt Sami        |      0.9900 |   0.9950 |     0.9925 |       199 |
| swe          | Swedish           |      0.9860 |   0.9920 |     0.9890 |       497 |
| Accuracy     |                   |             |          |     0.9905 |      5500 |
| Weighted avg |                   |      0.9906 |   0.9905 |     0.9905 |      5500 |
| Macro avg    |                   |      0.9901 |   0.9900 |     0.9900 |      5500 |

### `nb-nordic-lid.159.bin`

<details>
  <summary>Scores for the 159 languages</summary>
  
Additionally trained on sentences from [Taoteba](https://tatoeba.org/en/).

| ISO-639-3    | Language                    |   Precision |   Recall |   F1-Score |   Support |
|:-------------|:----------------------------|------------:|---------:|-----------:|----------:|
| afr          | Afrikaans                   |      0.9634 |   0.9485 |     0.9558 |       194 |
| ara          | Arabic                      |      0.9771 |   0.9533 |     0.9650 |       492 |
| arq          | Algerian Arabic             |      0.9478 |   0.9316 |     0.9397 |       117 |
| arz          | Egyptian Arabic             |      0.7193 |   0.8542 |     0.7810 |        48 |
| asm          | Assamese                    |      0.9828 |   0.9884 |     0.9856 |       173 |
| avk          | Kotava                      |      0.9895 |   0.9844 |     0.9869 |       192 |
| aze          | Azerbaijani                 |      0.9707 |   0.9831 |     0.9768 |       236 |
| bel          | Belarusian                  |      0.9864 |   0.9785 |     0.9825 |       372 |
| ben          | Bengali                     |      0.9915 |   0.9873 |     0.9894 |       236 |
| ber          | Berber                      |      0.8991 |   0.8507 |     0.8742 |       576 |
| bos          | Bosnian                     |      0.1548 |   0.1781 |     0.1656 |        73 |
| bre          | Breton                      |      0.9613 |   0.9681 |     0.9647 |       282 |
| bua          | Buryat                      |      0.9333 |   0.9130 |     0.9231 |        46 |
| bul          | Bulgarian                   |      0.9530 |   0.9660 |     0.9595 |       441 |
| cat          | Catalan                     |      0.9604 |   0.9510 |     0.9557 |       306 |
| cbk          | Chavacano                   |      0.9627 |   0.9923 |     0.9773 |       130 |
| ceb          | Cebuano                     |      0.8974 |   0.9091 |     0.9032 |        77 |
| ces          | Czech                       |      0.9684 |   0.9665 |     0.9675 |       508 |
| chv          | Chuvash                     |      0.9878 |   0.9643 |     0.9759 |        84 |
| ckb          | Central Kurdish (Soranî)    |      0.9751 |   0.9944 |     0.9846 |       354 |
| ckt          | Chukchi                     |      0.9615 |   1.0000 |     0.9804 |        25 |
| cmn          | Mandarin Chinese            |      0.9726 |   0.8674 |     0.9170 |       573 |
| cor          | Cornish                     |      1.0000 |   0.9733 |     0.9864 |       187 |
| csb          | Kashubian                   |      0.9787 |   1.0000 |     0.9892 |        46 |
| cym          | Welsh                       |      0.9625 |   0.9625 |     0.9625 |        80 |
| dan          | Danish                      |      0.9401 |   0.9345 |     0.9373 |      1007 |
| deu          | German                      |      0.9908 |   0.9765 |     0.9836 |       553 |
| dsb          | Lower Sorbian               |      0.8704 |   0.8246 |     0.8468 |        57 |
| dtp          | Central Dusun               |      0.9161 |   0.9562 |     0.9357 |       137 |
| ell          | Greek                       |      1.0000 |   0.9979 |     0.9989 |       476 |
| eng          | English                     |      0.9914 |   0.9886 |     0.9900 |      1052 |
| epo          | Esperanto                   |      0.9817 |   0.9853 |     0.9835 |       544 |
| est          | Estonian                    |      0.9659 |   0.9770 |     0.9714 |       174 |
| eus          | Basque                      |      0.9883 |   0.9585 |     0.9732 |       265 |
| fao          | Faroese                     |      0.9840 |   0.9899 |     0.9870 |       497 |
| fin          | Finnish                     |      0.9932 |   0.9817 |     0.9874 |      1041 |
| fkv          | Kven Finnish                |      0.5769 |   0.7500 |     0.6522 |        20 |
| fra          | French                      |      0.9890 |   0.9890 |     0.9890 |       544 |
| frr          | North Frisian               |      0.9784 |   0.9784 |     0.9784 |       139 |
| fry          | Frisian                     |      0.7419 |   0.9200 |     0.8214 |        25 |
| gcf          | Guadeloupean Creole French  |      0.9810 |   0.9904 |     0.9856 |       104 |
| gla          | Scottish Gaelic             |      0.9608 |   0.9800 |     0.9703 |        50 |
| gle          | Irish                       |      0.9781 |   0.9853 |     0.9817 |       136 |
| glg          | Galician                    |      0.9198 |   0.9330 |     0.9264 |       209 |
| gos          | Gronings                    |      0.9631 |   0.9671 |     0.9651 |       243 |
| grc          | Ancient Greek               |      0.9828 |   1.0000 |     0.9913 |        57 |
| grn          | Guarani                     |      0.9810 |   0.9936 |     0.9873 |       156 |
| guc          | Wayuu                       |      0.9556 |   1.0000 |     0.9773 |        43 |
| hau          | Hausa                       |      0.9930 |   0.9930 |     0.9930 |       431 |
| heb          | Hebrew                      |      1.0000 |   1.0000 |     1.0000 |       536 |
| hin          | Hindi                       |      1.0000 |   0.9974 |     0.9987 |       391 |
| hoc          | Ho                          |      0.9143 |   1.0000 |     0.9552 |        32 |
| hrv          | Croatian                    |      0.6085 |   0.5652 |     0.5861 |       253 |
| hrx          | Hunsrik                     |      0.8727 |   0.9231 |     0.8972 |        52 |
| hsb          | Upper Sorbian               |      0.8533 |   0.8312 |     0.8421 |        77 |
| hun          | Hungarian                   |      0.9853 |   0.9889 |     0.9871 |       541 |
| hye          | Armenian                    |      1.0000 |   1.0000 |     1.0000 |       225 |
| ido          | Ido                         |      0.9731 |   0.9560 |     0.9645 |       341 |
| ile          | Interlingue                 |      0.9386 |   0.9450 |     0.9418 |       291 |
| ilo          | Ilocano                     |      0.9917 |   0.9677 |     0.9796 |       124 |
| ina          | Interlingua                 |      0.9602 |   0.9775 |     0.9688 |       444 |
| ind          | Indonesian                  |      0.8550 |   0.8305 |     0.8426 |       419 |
| isl          | Icelandic                   |      0.9874 |   0.9931 |     0.9902 |       869 |
| ita          | Italian                     |      0.9835 |   0.9746 |     0.9791 |       552 |
| jav          | Javanese                    |      0.9400 |   0.9792 |     0.9592 |        48 |
| jbo          | Lojban                      |      1.0000 |   1.0000 |     1.0000 |       402 |
| jpn          | Japanese                    |      0.9870 |   1.0000 |     0.9935 |       531 |
| kab          | Kabyle                      |      0.8382 |   0.9012 |     0.8686 |       506 |
| kat          | Georgian                    |      1.0000 |   0.9885 |     0.9942 |       260 |
| kaz          | Kazakh                      |      0.9896 |   0.9896 |     0.9896 |       192 |
| kha          | Khasi                       |      0.9038 |   0.9400 |     0.9216 |       100 |
| khm          | Khmer                       |      1.0000 |   1.0000 |     1.0000 |        75 |
| kmr          | Northern Kurdish (Kurmancî) |      0.9881 |   0.9793 |     0.9837 |       338 |
| knc          | Central Kanuri              |      0.9775 |   1.0000 |     0.9886 |       174 |
| kor          | Korean                      |      1.0000 |   0.9806 |     0.9902 |       360 |
| kzj          | Coastal Kadazan             |      0.9744 |   0.9580 |     0.9661 |       238 |
| lad          | Ladino                      |      0.8154 |   0.8281 |     0.8217 |        64 |
| lat          | Latin                       |      0.9756 |   0.9677 |     0.9717 |       496 |
| lfn          | Lingua Franca Nova          |      0.9745 |   0.9768 |     0.9757 |       431 |
| lij          | Ligurian                    |      0.9556 |   0.9556 |     0.9556 |        90 |
| lin          | Lingala                     |      0.9859 |   0.9859 |     0.9859 |       213 |
| lit          | Lithuanian                  |      0.9903 |   0.9942 |     0.9922 |       513 |
| ltz          | Luxembourgish               |      0.9773 |   0.9149 |     0.9451 |        47 |
| lvs          | Latvian                     |      0.9732 |   0.9797 |     0.9764 |       148 |
| lzh          | Literary Chinese            |      0.7473 |   0.9444 |     0.8344 |        72 |
| mal          | Malayalam                   |      1.0000 |   1.0000 |     1.0000 |        44 |
| mar          | Marathi                     |      0.9961 |   1.0000 |     0.9980 |       509 |
| mhr          | Meadow Mari                 |      0.9899 |   0.9801 |     0.9850 |       201 |
| mkd          | Macedonian                  |      0.9630 |   0.9447 |     0.9538 |       524 |
| mon          | Mongolian                   |      0.9781 |   0.9710 |     0.9745 |       138 |
| mus          | Muskogee (Creek)            |      0.9333 |   0.9655 |     0.9492 |        29 |
| mya          | Burmese                     |      1.0000 |   1.0000 |     1.0000 |        27 |
| nds          | Low German (Low Saxon)      |      0.9829 |   0.9805 |     0.9817 |       410 |
| nld          | Dutch                       |      0.9681 |   0.9810 |     0.9745 |       526 |
| nnb          | Nande                       |      0.9896 |   0.9845 |     0.9870 |       387 |
| nno          | Norwegian Nynorsk           |      0.9551 |   0.9685 |     0.9617 |       571 |
| nob          | Norwegian Bokmål            |      0.9280 |   0.9168 |     0.9224 |       914 |
| nst          | Naga (Tangshang)            |      1.0000 |   1.0000 |     1.0000 |        39 |
| nus          | Nuer                        |      0.9903 |   1.0000 |     0.9951 |       102 |
| oci          | Occitan                     |      0.9795 |   0.9598 |     0.9696 |       249 |
| orv          | Old East Slavic             |      0.9846 |   1.0000 |     0.9922 |        64 |
| oss          | Ossetian                    |      0.9891 |   0.9963 |     0.9927 |       272 |
| ota          | Ottoman Turkish             |      0.9469 |   0.9727 |     0.9596 |       110 |
| pam          | Kapampangan                 |      0.9865 |   0.9733 |     0.9799 |        75 |
| pcd          | Picard                      |      0.9552 |   0.9697 |     0.9624 |        66 |
| pes          | Persian                     |      0.9934 |   0.9956 |     0.9945 |       454 |
| pms          | Piedmontese                 |      0.9268 |   0.9744 |     0.9500 |        39 |
| pol          | Polish                      |      0.9886 |   0.9886 |     0.9886 |       525 |
| por          | Portuguese                  |      0.9669 |   0.9686 |     0.9677 |       542 |
| prg          | Old Prussian                |      0.9800 |   0.9608 |     0.9703 |        51 |
| rhg          | Rohingya                    |      0.9890 |   1.0000 |     0.9945 |       180 |
| rom          | Romani                      |      0.9535 |   0.8913 |     0.9213 |        46 |
| ron          | Romanian                    |      0.9870 |   0.9785 |     0.9827 |       465 |
| run          | Kirundi                     |      0.9871 |   0.9746 |     0.9808 |       236 |
| rus          | Russian                     |      0.9671 |   0.9796 |     0.9733 |       540 |
| sah          | Yakut                       |      1.0000 |   1.0000 |     1.0000 |        48 |
| sat          | Santali                     |      1.0000 |   1.0000 |     1.0000 |       171 |
| sdh          | Southern Kurdish            |      0.9808 |   0.9107 |     0.9444 |        56 |
| shi          | Tashelhit                   |      0.9779 |   0.9172 |     0.9466 |       145 |
| slk          | Slovak                      |      0.9235 |   0.9421 |     0.9327 |       397 |
| slv          | Slovenian                   |      0.7544 |   0.8958 |     0.8190 |        48 |
| sma          | Southern Sami               |      0.9600 |   0.9600 |     0.9600 |       100 |
| sme          | Northern Sami               |      1.0000 |   0.9901 |     0.9950 |       505 |
| smj          | Lule Sami                   |      0.9860 |   1.0000 |     0.9930 |       493 |
| smn          | Inari Sami                  |      0.9950 |   0.9950 |     0.9950 |       200 |
| sms          | Skolt Sami                  |      0.9850 |   0.9899 |     0.9875 |       199 |
| spa          | Spanish                     |      0.9779 |   0.9619 |     0.9698 |       551 |
| sqi          | Albanian                    |      0.9683 |   0.9839 |     0.9760 |       124 |
| srp          | Serbian                     |      0.8347 |   0.8313 |     0.8330 |       492 |
| swc          | Congo Swahili               |      0.8750 |   0.8594 |     0.8671 |       448 |
| swe          | Swedish                     |      0.9809 |   0.9839 |     0.9824 |       991 |
| swg          | Swabian                     |      0.9898 |   0.9604 |     0.9749 |       101 |
| swh          | Swahili                     |      0.6946 |   0.7382 |     0.7157 |       191 |
| tat          | Tatar                       |      0.9817 |   0.9843 |     0.9830 |       382 |
| tgl          | Tagalog                     |      0.9830 |   0.9830 |     0.9830 |       412 |
| tha          | Thai                        |      1.0000 |   1.0000 |     1.0000 |       220 |
| thv          | Tahaggart Tamahaq           |      0.7241 |   0.8400 |     0.7778 |        25 |
| tig          | Tigre                       |      1.0000 |   1.0000 |     1.0000 |       181 |
| tlh          | Klingon                     |      1.0000 |   1.0000 |     1.0000 |       439 |
| tok          | Toki Pona                   |      1.0000 |   1.0000 |     1.0000 |       495 |
| tpw          | Old Tupi                    |      0.8929 |   0.9615 |     0.9259 |        26 |
| tuk          | Turkmen                     |      0.9890 |   0.9711 |     0.9800 |       277 |
| tur          | Turkish                     |      0.9872 |   0.9659 |     0.9764 |       558 |
| uig          | Uyghur                      |      0.9966 |   0.9933 |     0.9950 |       299 |
| ukr          | Ukrainian                   |      0.9813 |   0.9850 |     0.9831 |       532 |
| urd          | Urdu                        |      1.0000 |   0.9914 |     0.9957 |       116 |
| uzb          | Uzbek                       |      0.8200 |   0.9762 |     0.8913 |        42 |
| vie          | Vietnamese                  |      0.9977 |   0.9977 |     0.9977 |       426 |
| vol          | Volapük                     |      0.9862 |   0.9908 |     0.9885 |       217 |
| war          | Waray                       |      0.9505 |   0.9796 |     0.9648 |        98 |
| wuu          | Shanghainese                |      0.8364 |   0.9275 |     0.8796 |       193 |
| xal          | Kalmyk                      |      0.9302 |   0.9756 |     0.9524 |        41 |
| xmf          | Mingrelian                  |      0.7419 |   0.8519 |     0.7931 |        27 |
| yid          | Yiddish                     |      0.9971 |   1.0000 |     0.9986 |       348 |
| yue          | Cantonese                   |      0.9195 |   0.9877 |     0.9524 |       243 |
| zgh          | Standard Moroccan Tamazight |      0.9873 |   0.9873 |     0.9873 |       158 |
| zlm          | Malay (Vernacular)          |      0.8605 |   0.9024 |     0.8810 |        82 |
| zsm          | Malay                       |      0.7782 |   0.7921 |     0.7851 |       279 |
| zza          | Zaza                        |      0.9294 |   0.9294 |     0.9294 |        85 |
| Accuracy     |                             |             |          |     0.9620 |     44049 |
| Weighted avg |                             |      0.9627 |   0.9620 |     0.9621 |     44049 |
| Macro avg    |                             |      0.9434 |   0.9528 |     0.9476 |     44049 |

</details>

### `nb-nordic-lid.ftz`

The small models are quantized versions of the large versions using a cutoff of 50,000 words and ngrams and quantizing the norm separately.

| ISO-639-3    | Language          |   Precision |   Recall |   F1-Score |   Support |
|:-------------|:------------------|------------:|---------:|-----------:|----------:|
| dan          | Danish            |      0.9700 |   0.9838 |     0.9768 |       493 |
| eng          | English           |      0.9980 |   0.9940 |     0.9960 |       502 |
| fao          | Faroese           |      0.9920 |   0.9920 |     0.9920 |       500 |
| fin          | Finnish           |      1.0000 |   1.0000 |     1.0000 |       500 |
| isl          | Icelandic         |      0.9880 |   0.9920 |     0.9900 |       498 |
| nno          | Norwegian Nynorsk |      0.9880 |   0.9841 |     0.9860 |       502 |
| nob          | Norwegian Bokmål  |      0.9860 |   0.9705 |     0.9782 |       508 |
| sma          | Southern Sami     |      0.9800 |   0.9703 |     0.9751 |       101 |
| sme          | Northern Sami     |      1.0000 |   0.9921 |     0.9960 |       504 |
| smj          | Lule Sami         |      0.9920 |   0.9940 |     0.9930 |       499 |
| smn          | Inari Sami        |      0.9950 |   1.0000 |     0.9975 |       199 |
| sms          | Skolt Sami        |      0.9850 |   0.9949 |     0.9899 |       198 |
| swe          | Swedish           |      0.9820 |   0.9899 |     0.9859 |       496 |
| Accuracy     |                   |             |          |     0.9895 |      5500 |
| Weighted avg |                   |      0.9895 |   0.9895 |     0.9895 |      5500 |
| Macro avg    |                   |      0.9889 |   0.9890 |     0.9890 |      5500 |


### `nb-nordic-lid.159.ftz`

<details>
  <summary>Scores for the 159 languages (compressed model)</summary>

| ISO-639-3    | Language                    |   Precision |   Recall |   F1-Score |   Support |
|:-------------|:----------------------------|------------:|---------:|-----------:|----------:|
| afr          | Afrikaans                   |      0.9529 |   0.9333 |     0.9430 |       195 |
| ara          | Arabic                      |      0.9708 |   0.9191 |     0.9443 |       507 |
| arq          | Algerian Arabic             |      0.8783 |   0.8783 |     0.8783 |       115 |
| arz          | Egyptian Arabic             |      0.5439 |   0.8378 |     0.6596 |        37 |
| asm          | Assamese                    |      0.9828 |   0.9448 |     0.9634 |       181 |
| avk          | Kotava                      |      0.9843 |   0.9792 |     0.9817 |       192 |
| aze          | Azerbaijani                 |      0.9582 |   0.9828 |     0.9703 |       233 |
| bel          | Belarusian                  |      0.9919 |   0.9683 |     0.9799 |       378 |
| ben          | Bengali                     |      0.9574 |   0.9868 |     0.9719 |       228 |
| ber          | Berber                      |      0.8495 |   0.7928 |     0.8202 |       584 |
| bos          | Bosnian                     |      0.1429 |   0.2264 |     0.1752 |        53 |
| bre          | Breton                      |      0.9507 |   0.9712 |     0.9609 |       278 |
| bua          | Buryat                      |      0.9333 |   0.9333 |     0.9333 |        45 |
| bul          | Bulgarian                   |      0.9351 |   0.9457 |     0.9404 |       442 |
| cat          | Catalan                     |      0.9406 |   0.9406 |     0.9406 |       303 |
| cbk          | Chavacano                   |      0.9552 |   0.9624 |     0.9588 |       133 |
| ceb          | Cebuano                     |      0.8718 |   0.8500 |     0.8608 |        80 |
| ces          | Czech                       |      0.9586 |   0.9548 |     0.9567 |       509 |
| chv          | Chuvash                     |      1.0000 |   0.9647 |     0.9820 |        85 |
| ckb          | Central Kurdish (Soranî)    |      0.9640 |   0.9748 |     0.9694 |       357 |
| ckt          | Chukchi                     |      0.9615 |   1.0000 |     0.9804 |        25 |
| cmn          | Mandarin Chinese            |      0.9667 |   0.8165 |     0.8853 |       605 |
| cor          | Cornish                     |      0.9780 |   0.9674 |     0.9727 |       184 |
| csb          | Kashubian                   |      0.9574 |   1.0000 |     0.9783 |        45 |
| cym          | Welsh                       |      0.9625 |   0.9506 |     0.9565 |        81 |
| dan          | Danish                      |      0.9281 |   0.9355 |     0.9318 |       993 |
| deu          | German                      |      0.9853 |   0.9781 |     0.9817 |       549 |
| dsb          | Lower Sorbian               |      0.8889 |   0.8276 |     0.8571 |        58 |
| dtp          | Central Dusun               |      0.8741 |   0.9470 |     0.9091 |       132 |
| ell          | Greek                       |      0.9958 |   0.9937 |     0.9947 |       476 |
| eng          | English                     |      0.9886 |   0.9876 |     0.9881 |      1050 |
| epo          | Esperanto                   |      0.9853 |   0.9818 |     0.9835 |       548 |
| est          | Estonian                    |      0.9489 |   0.9766 |     0.9625 |       171 |
| eus          | Basque                      |      0.9844 |   0.9583 |     0.9712 |       264 |
| fao          | Faroese                     |      0.9780 |   0.9819 |     0.9800 |       498 |
| fin          | Finnish                     |      0.9922 |   0.9724 |     0.9822 |      1050 |
| fkv          | Kven Finnish                |      0.5385 |   0.7368 |     0.6222 |        19 |
| fra          | French                      |      0.9871 |   0.9728 |     0.9799 |       552 |
| frr          | North Frisian               |      0.9640 |   0.9640 |     0.9640 |       139 |
| fry          | Frisian                     |      0.7097 |   0.8462 |     0.7719 |        26 |
| gcf          | Guadeloupean Creole French  |      0.9714 |   0.9808 |     0.9761 |       104 |
| gla          | Scottish Gaelic             |      0.9608 |   0.9608 |     0.9608 |        51 |
| gle          | Irish                       |      0.9489 |   0.9924 |     0.9701 |       131 |
| glg          | Galician                    |      0.8868 |   0.9082 |     0.8974 |       207 |
| gos          | Gronings                    |      0.9426 |   0.9544 |     0.9485 |       241 |
| grc          | Ancient Greek               |      0.9483 |   0.9483 |     0.9483 |        58 |
| grn          | Guarani                     |      0.9684 |   0.9935 |     0.9808 |       154 |
| guc          | Wayuu                       |      0.9333 |   1.0000 |     0.9655 |        42 |
| hau          | Hausa                       |      0.9861 |   0.9884 |     0.9872 |       430 |
| heb          | Hebrew                      |      0.9981 |   0.9907 |     0.9944 |       540 |
| hin          | Hindi                       |      0.9974 |   0.9898 |     0.9936 |       393 |
| hoc          | Ho                          |      0.8571 |   1.0000 |     0.9231 |        30 |
| hrv          | Croatian                    |      0.6766 |   0.5911 |     0.6310 |       269 |
| hrx          | Hunsrik                     |      0.8545 |   0.9216 |     0.8868 |        51 |
| hsb          | Upper Sorbian               |      0.8400 |   0.8182 |     0.8289 |        77 |
| hun          | Hungarian                   |      0.9816 |   0.9852 |     0.9834 |       541 |
| hye          | Armenian                    |      1.0000 |   1.0000 |     1.0000 |       225 |
| ido          | Ido                         |      0.9672 |   0.9501 |     0.9586 |       341 |
| ile          | Interlingue                 |      0.9352 |   0.9547 |     0.9448 |       287 |
| ilo          | Ilocano                     |      0.9917 |   0.9600 |     0.9756 |       125 |
| ina          | Interlingua                 |      0.9580 |   0.9558 |     0.9569 |       453 |
| ind          | Indonesian                  |      0.8231 |   0.8034 |     0.8131 |       417 |
| isl          | Icelandic                   |      0.9805 |   0.9885 |     0.9845 |       867 |
| ita          | Italian                     |      0.9817 |   0.9555 |     0.9684 |       562 |
| jav          | Javanese                    |      0.9400 |   0.9792 |     0.9592 |        48 |
| jbo          | Lojban                      |      1.0000 |   0.9975 |     0.9988 |       403 |
| jpn          | Japanese                    |      0.9684 |   0.9981 |     0.9830 |       522 |
| kab          | Kabyle                      |      0.7702 |   0.8516 |     0.8089 |       492 |
| kat          | Georgian                    |      1.0000 |   0.9847 |     0.9923 |       261 |
| kaz          | Kazakh                      |      0.9792 |   0.9843 |     0.9817 |       191 |
| kha          | Khasi                       |      0.8942 |   0.9300 |     0.9118 |       100 |
| khm          | Khmer                       |      1.0000 |   0.9868 |     0.9934 |        76 |
| kmr          | Northern Kurdish (Kurmancî) |      0.9791 |   0.9647 |     0.9719 |       340 |
| knc          | Central Kanuri              |      0.9775 |   0.9943 |     0.9858 |       175 |
| kor          | Korean                      |      0.9972 |   0.9778 |     0.9874 |       360 |
| kzj          | Coastal Kadazan             |      0.9658 |   0.9378 |     0.9516 |       241 |
| lad          | Ladino                      |      0.7538 |   0.8033 |     0.7778 |        61 |
| lat          | Latin                       |      0.9614 |   0.9594 |     0.9604 |       493 |
| lfn          | Lingua Franca Nova          |      0.9722 |   0.9611 |     0.9666 |       437 |
| lij          | Ligurian                    |      0.8778 |   0.9753 |     0.9240 |        81 |
| lin          | Lingala                     |      0.9859 |   0.9677 |     0.9767 |       217 |
| lit          | Lithuanian                  |      0.9864 |   0.9864 |     0.9864 |       515 |
| ltz          | Luxembourgish               |      0.9773 |   0.9149 |     0.9451 |        47 |
| lvs          | Latvian                     |      0.9597 |   0.9662 |     0.9630 |       148 |
| lzh          | Literary Chinese            |      0.6593 |   0.8108 |     0.7273 |        74 |
| mal          | Malayalam                   |      1.0000 |   1.0000 |     1.0000 |        44 |
| mar          | Marathi                     |      0.9902 |   0.9980 |     0.9941 |       507 |
| mhr          | Meadow Mari                 |      0.9899 |   0.9752 |     0.9825 |       202 |
| mkd          | Macedonian                  |      0.9397 |   0.9253 |     0.9324 |       522 |
| mon          | Mongolian                   |      0.9781 |   0.9571 |     0.9675 |       140 |
| mus          | Muskogee (Creek)            |      0.9000 |   0.9643 |     0.9310 |        28 |
| mya          | Burmese                     |      1.0000 |   1.0000 |     1.0000 |        27 |
| nds          | Low German (Low Saxon)      |      0.9829 |   0.9687 |     0.9757 |       415 |
| nld          | Dutch                       |      0.9644 |   0.9735 |     0.9689 |       528 |
| nnb          | Nande                       |      0.9870 |   0.9896 |     0.9883 |       384 |
| nno          | Norwegian Nynorsk           |      0.9499 |   0.9632 |     0.9565 |       571 |
| nob          | Norwegian Bokmål            |      0.9324 |   0.9073 |     0.9197 |       928 |
| nst          | Naga (Tangshang)            |      1.0000 |   0.9750 |     0.9873 |        40 |
| nus          | Nuer                        |      0.9903 |   1.0000 |     0.9951 |       102 |
| oci          | Occitan                     |      0.9631 |   0.9476 |     0.9553 |       248 |
| orv          | Old East Slavic             |      0.9538 |   0.9254 |     0.9394 |        67 |
| oss          | Ossetian                    |      0.9818 |   0.9926 |     0.9872 |       271 |
| ota          | Ottoman Turkish             |      0.9204 |   0.9455 |     0.9327 |       110 |
| pam          | Kapampangan                 |      0.9730 |   0.9600 |     0.9664 |        75 |
| pcd          | Picard                      |      0.9254 |   0.9688 |     0.9466 |        64 |
| pes          | Persian                     |      0.9846 |   0.9868 |     0.9857 |       454 |
| pms          | Piedmontese                 |      0.9024 |   0.9487 |     0.9250 |        39 |
| pol          | Polish                      |      0.9867 |   0.9885 |     0.9876 |       524 |
| por          | Portuguese                  |      0.9595 |   0.9577 |     0.9586 |       544 |
| prg          | Old Prussian                |      0.9800 |   0.9423 |     0.9608 |        52 |
| rhg          | Rohingya                    |      0.9835 |   0.9835 |     0.9835 |       182 |
| rom          | Romani                      |      0.9302 |   0.8511 |     0.8889 |        47 |
| ron          | Romanian                    |      0.9783 |   0.9762 |     0.9772 |       462 |
| run          | Kirundi                     |      0.9871 |   0.9426 |     0.9644 |       244 |
| rus          | Russian                     |      0.9561 |   0.9757 |     0.9658 |       536 |
| sah          | Yakut                       |      0.9792 |   1.0000 |     0.9895 |        47 |
| sat          | Santali                     |      0.9942 |   1.0000 |     0.9971 |       170 |
| sdh          | Southern Kurdish            |      0.8462 |   0.8627 |     0.8544 |        51 |
| shi          | Tashelhit                   |      0.9706 |   0.8980 |     0.9329 |       147 |
| slk          | Slovak                      |      0.9111 |   0.9318 |     0.9213 |       396 |
| slv          | Slovenian                   |      0.7018 |   0.9302 |     0.8000 |        43 |
| sma          | Southern Sami               |      0.9500 |   0.9406 |     0.9453 |       101 |
| sme          | Northern Sami               |      1.0000 |   0.9843 |     0.9921 |       508 |
| smj          | Lule Sami                   |      0.9840 |   0.9980 |     0.9909 |       493 |
| smn          | Inari Sami                  |      0.9850 |   0.9949 |     0.9899 |       198 |
| sms          | Skolt Sami                  |      0.9700 |   0.9848 |     0.9773 |       197 |
| spa          | Spanish                     |      0.9613 |   0.9560 |     0.9586 |       545 |
| sqi          | Albanian                    |      0.9603 |   0.9680 |     0.9641 |       125 |
| srp          | Serbian                     |      0.8122 |   0.8106 |     0.8114 |       491 |
| swc          | Congo Swahili               |      0.8500 |   0.8367 |     0.8433 |       447 |
| swe          | Swedish                     |      0.9759 |   0.9778 |     0.9768 |       992 |
| swg          | Swabian                     |      0.9796 |   0.9320 |     0.9552 |       103 |
| swh          | Swahili                     |      0.6650 |   0.7068 |     0.6853 |       191 |
| tat          | Tatar                       |      0.9739 |   0.9816 |     0.9777 |       380 |
| tgl          | Tagalog                     |      0.9709 |   0.9732 |     0.9721 |       411 |
| tha          | Thai                        |      1.0000 |   1.0000 |     1.0000 |       220 |
| thv          | Tahaggart Tamahaq           |      0.6552 |   0.7600 |     0.7037 |        25 |
| tig          | Tigre                       |      1.0000 |   1.0000 |     1.0000 |       181 |
| tlh          | Klingon                     |      0.9977 |   0.9955 |     0.9966 |       440 |
| tok          | Toki Pona                   |      1.0000 |   1.0000 |     1.0000 |       495 |
| tpw          | Old Tupi                    |      0.8214 |   0.8846 |     0.8519 |        26 |
| tuk          | Turkmen                     |      0.9779 |   0.9708 |     0.9744 |       274 |
| tur          | Turkish                     |      0.9780 |   0.9604 |     0.9691 |       556 |
| uig          | Uyghur                      |      0.9933 |   0.9900 |     0.9916 |       299 |
| ukr          | Ukrainian                   |      0.9682 |   0.9700 |     0.9691 |       533 |
| urd          | Urdu                        |      1.0000 |   0.9914 |     0.9957 |       116 |
| uzb          | Uzbek                       |      0.8000 |   0.9756 |     0.8791 |        41 |
| vie          | Vietnamese                  |      0.9977 |   0.9977 |     0.9977 |       426 |
| vol          | Volapük                     |      0.9862 |   0.9817 |     0.9840 |       219 |
| war          | Waray                       |      0.9208 |   0.9688 |     0.9442 |        96 |
| wuu          | Shanghainese                |      0.8037 |   0.9053 |     0.8515 |       190 |
| xal          | Kalmyk                      |      0.9070 |   0.9512 |     0.9286 |        41 |
| xmf          | Mingrelian                  |      0.6774 |   0.8400 |     0.7500 |        25 |
| yid          | Yiddish                     |      0.9828 |   0.9942 |     0.9885 |       345 |
| yue          | Cantonese                   |      0.8314 |   0.9688 |     0.8948 |       224 |
| zgh          | Standard Moroccan Tamazight |      0.9873 |   0.9873 |     0.9873 |       158 |
| zlm          | Malay (Vernacular)          |      0.8488 |   0.8588 |     0.8538 |        85 |
| zsm          | Malay                       |      0.7465 |   0.7544 |     0.7504 |       281 |
| zza          | Zaza                        |      0.8824 |   0.9146 |     0.8982 |        82 |
| Accuracy     |                             |             |          |     0.9513 |     44049 |
| Weighted avg |                             |      0.9529 |   0.9513 |     0.9518 |     44049 |
| Macro avg    |                             |      0.9275 |   0.9399 |     0.9327 |     44049 |

</details>


## Citing & Authors

The model was trained by Javier de la Rosa. Data was prepared by Per Egil Kummervold and Javier de la Rosa. Documentation written by Javier de la Rosa.
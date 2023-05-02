---
language:
- dsb
- cs
- csb_Latn
- hsb
- pl
- zlw
- hu
- vro
- fi
- liv_Latn
- mdf
- krl
- fkv_Latn
- mhr
- et
- sma
- udm
- vep
- myv
- kpv
- se
- izh
- fiu

tags:
- translation

license: apache-2.0
---
### zlw-fiu
* source language name: West Slavic languages
* target language name: Finno-Ugrian languages
* OPUS readme: [README.md](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-fiu/README.md)
* model: transformer
* source language codes: dsb, cs, csb_Latn, hsb, pl, zlw
* target language codes: hu, vro, fi, liv_Latn, mdf, krl, fkv_Latn, mhr, et, sma, udm, vep, myv, kpv, se, izh, fiu
* dataset: opus 
* release date: 2021-02-18
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2021-02-18.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-fiu/opus-2021-02-18.zip/zlw-fiu/opus-2021-02-18.zip)
* a sentence-initial language token is required in the form of >>id<<(id = valid, usually three-letter target language ID)
* Training data: 
  * ces-fin: Tatoeba-train (1000000)
  * ces-hun: Tatoeba-train (1000000)
  * pol-est: Tatoeba-train (1000000)
  * pol-fin: Tatoeba-train (1000000)
  * pol-hun: Tatoeba-train (1000000)
* Validation data: 
  * ces-fin: Tatoeba-dev, 1000
  * ces-hun: Tatoeba-dev, 1000
  * est-pol: Tatoeba-dev, 1000
  * fin-pol: Tatoeba-dev, 1000
  * hun-pol: Tatoeba-dev, 1000
  * mhr-pol: Tatoeba-dev, 461
  * total-size-shuffled: 5426
  * devset-selected: top 5000  lines of Tatoeba-dev.src.shuffled!
* Test data: 
  * newssyscomb2009.ces-hun: 502/9733
  * newstest2009.ces-hun: 2525/54965
  * Tatoeba-test.ces-fin: 88/408
  * Tatoeba-test.ces-hun: 1911/10336
  * Tatoeba-test.multi-multi: 4562/25497
  * Tatoeba-test.pol-chm: 5/36
  * Tatoeba-test.pol-est: 15/98
  * Tatoeba-test.pol-fin: 609/3293
  * Tatoeba-test.pol-hun: 1934/11285
* test set translations file: [test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-fiu/opus-2021-02-18.zip/zlw-fiu/opus-2021-02-18.test.txt)
* test set scores file: [eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-fiu/opus-2021-02-18.zip/zlw-fiu/opus-2021-02-18.eval.txt)
* BLEU-scores
|Test set|score|
|---|---|
|Tatoeba-test.ces-fin|57.2|
|Tatoeba-test.ces-hun|42.6|
|Tatoeba-test.multi-multi|39.4|
|Tatoeba-test.pol-hun|36.6|
|Tatoeba-test.pol-fin|36.1|
|Tatoeba-test.pol-est|20.9|
|newssyscomb2009.ces-hun|13.9|
|newstest2009.ces-hun|13.9|
|Tatoeba-test.pol-chm|2.0|
* chr-F-scores
|Test set|score|
|---|---|
|Tatoeba-test.ces-fin|0.71|
|Tatoeba-test.ces-hun|0.637|
|Tatoeba-test.multi-multi|0.616|
|Tatoeba-test.pol-hun|0.605|
|Tatoeba-test.pol-fin|0.592|
|newssyscomb2009.ces-hun|0.449|
|newstest2009.ces-hun|0.443|
|Tatoeba-test.pol-est|0.372|
|Tatoeba-test.pol-chm|0.007|

### System Info: 
* hf_name: zlw-fiu
* source_languages: dsb,cs,csb_Latn,hsb,pl,zlw
* target_languages: hu,vro,fi,liv_Latn,mdf,krl,fkv_Latn,mhr,et,sma,udm,vep,myv,kpv,se,izh,fiu
* opus_readme_url: https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-fiu/opus-2021-02-18.zip/README.md
* original_repo: Tatoeba-Challenge
* tags: ['translation']
* languages: ['dsb', 'cs', 'csb_Latn', 'hsb', 'pl', 'zlw', 'hu', 'vro', 'fi', 'liv_Latn', 'mdf', 'krl', 'fkv_Latn', 'mhr', 'et', 'sma', 'udm', 'vep', 'myv', 'kpv', 'se', 'izh', 'fiu']
* src_constituents: ['dsb', 'ces', 'csb_Latn', 'hsb', 'pol']
* tgt_constituents: ['hun', 'vro', 'fin', 'liv_Latn', 'mdf', 'krl', 'fkv_Latn', 'mhr', 'est', 'sma', 'udm', 'vep', 'myv', 'kpv', 'sme', 'izh']
* src_multilingual: True
* tgt_multilingual: True
* helsinki_git_sha: a0966db6db0ae616a28471ff0faf461b36fec07d
* transformers_git_sha: 3857f2b4e34912c942694489c2b667d9476e55f5
* port_machine: bungle
* port_time: 2021-06-29-15:24
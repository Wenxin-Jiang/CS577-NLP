---
language: 
- be
- hr
- mk
- cs
- ru
- pl
- bg
- uk
- sl
- sla

tags:
- translation

license: apache-2.0
---

### sla-sla

* source group: Slavic languages 
* target group: Slavic languages 
*  OPUS readme: [sla-sla](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/sla-sla/README.md)

*  model: transformer
* source language(s): bel bel_Latn bos_Latn bul bul_Latn ces dsb hrv hsb mkd orv_Cyrl pol rus slv srp_Cyrl srp_Latn ukr
* target language(s): bel bel_Latn bos_Latn bul bul_Latn ces dsb hrv hsb mkd orv_Cyrl pol rus slv srp_Cyrl srp_Latn ukr
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/sla-sla/opus-2020-07-27.zip)
* test set translations: [opus-2020-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/sla-sla/opus-2020-07-27.test.txt)
* test set scores: [opus-2020-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/sla-sla/opus-2020-07-27.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newstest2012-cesrus.ces.rus 	| 15.9 	| 0.437 |
| newstest2012-rusces.rus.ces 	| 13.6 	| 0.403 |
| newstest2013-cesrus.ces.rus 	| 19.8 	| 0.473 |
| newstest2013-rusces.rus.ces 	| 17.9 	| 0.449 |
| Tatoeba-test.bel-bul.bel.bul 	| 100.0 	| 1.000 |
| Tatoeba-test.bel-ces.bel.ces 	| 33.5 	| 0.630 |
| Tatoeba-test.bel-hbs.bel.hbs 	| 45.4 	| 0.644 |
| Tatoeba-test.bel-mkd.bel.mkd 	| 19.3 	| 0.531 |
| Tatoeba-test.bel-pol.bel.pol 	| 46.9 	| 0.681 |
| Tatoeba-test.bel-rus.bel.rus 	| 58.5 	| 0.767 |
| Tatoeba-test.bel-ukr.bel.ukr 	| 55.1 	| 0.743 |
| Tatoeba-test.bul-bel.bul.bel 	| 10.7 	| 0.423 |
| Tatoeba-test.bul-ces.bul.ces 	| 36.9 	| 0.585 |
| Tatoeba-test.bul-hbs.bul.hbs 	| 53.7 	| 0.807 |
| Tatoeba-test.bul-mkd.bul.mkd 	| 31.9 	| 0.715 |
| Tatoeba-test.bul-pol.bul.pol 	| 38.6 	| 0.607 |
| Tatoeba-test.bul-rus.bul.rus 	| 44.8 	| 0.655 |
| Tatoeba-test.bul-ukr.bul.ukr 	| 49.9 	| 0.691 |
| Tatoeba-test.ces-bel.ces.bel 	| 30.9 	| 0.585 |
| Tatoeba-test.ces-bul.ces.bul 	| 75.8 	| 0.859 |
| Tatoeba-test.ces-hbs.ces.hbs 	| 50.0 	| 0.661 |
| Tatoeba-test.ces-hsb.ces.hsb 	| 7.9 	| 0.246 |
| Tatoeba-test.ces-mkd.ces.mkd 	| 24.6 	| 0.569 |
| Tatoeba-test.ces-pol.ces.pol 	| 44.3 	| 0.652 |
| Tatoeba-test.ces-rus.ces.rus 	| 50.8 	| 0.690 |
| Tatoeba-test.ces-slv.ces.slv 	| 4.9 	| 0.240 |
| Tatoeba-test.ces-ukr.ces.ukr 	| 52.9 	| 0.687 |
| Tatoeba-test.dsb-pol.dsb.pol 	| 16.3 	| 0.367 |
| Tatoeba-test.dsb-rus.dsb.rus 	| 12.7 	| 0.245 |
| Tatoeba-test.hbs-bel.hbs.bel 	| 32.9 	| 0.531 |
| Tatoeba-test.hbs-bul.hbs.bul 	| 100.0 	| 1.000 |
| Tatoeba-test.hbs-ces.hbs.ces 	| 40.3 	| 0.626 |
| Tatoeba-test.hbs-mkd.hbs.mkd 	| 19.3 	| 0.535 |
| Tatoeba-test.hbs-pol.hbs.pol 	| 45.0 	| 0.650 |
| Tatoeba-test.hbs-rus.hbs.rus 	| 53.5 	| 0.709 |
| Tatoeba-test.hbs-ukr.hbs.ukr 	| 50.7 	| 0.684 |
| Tatoeba-test.hsb-ces.hsb.ces 	| 17.9 	| 0.366 |
| Tatoeba-test.mkd-bel.mkd.bel 	| 23.6 	| 0.548 |
| Tatoeba-test.mkd-bul.mkd.bul 	| 54.2 	| 0.833 |
| Tatoeba-test.mkd-ces.mkd.ces 	| 12.1 	| 0.371 |
| Tatoeba-test.mkd-hbs.mkd.hbs 	| 19.3 	| 0.577 |
| Tatoeba-test.mkd-pol.mkd.pol 	| 53.7 	| 0.833 |
| Tatoeba-test.mkd-rus.mkd.rus 	| 34.2 	| 0.745 |
| Tatoeba-test.mkd-ukr.mkd.ukr 	| 42.7 	| 0.708 |
| Tatoeba-test.multi.multi 	| 48.5 	| 0.672 |
| Tatoeba-test.orv-pol.orv.pol 	| 10.1 	| 0.355 |
| Tatoeba-test.orv-rus.orv.rus 	| 10.6 	| 0.275 |
| Tatoeba-test.orv-ukr.orv.ukr 	| 7.5 	| 0.230 |
| Tatoeba-test.pol-bel.pol.bel 	| 29.8 	| 0.533 |
| Tatoeba-test.pol-bul.pol.bul 	| 36.8 	| 0.578 |
| Tatoeba-test.pol-ces.pol.ces 	| 43.6 	| 0.626 |
| Tatoeba-test.pol-dsb.pol.dsb 	| 0.9 	| 0.097 |
| Tatoeba-test.pol-hbs.pol.hbs 	| 42.4 	| 0.644 |
| Tatoeba-test.pol-mkd.pol.mkd 	| 19.3 	| 0.535 |
| Tatoeba-test.pol-orv.pol.orv 	| 0.7 	| 0.109 |
| Tatoeba-test.pol-rus.pol.rus 	| 49.6 	| 0.680 |
| Tatoeba-test.pol-slv.pol.slv 	| 7.3 	| 0.262 |
| Tatoeba-test.pol-ukr.pol.ukr 	| 46.8 	| 0.664 |
| Tatoeba-test.rus-bel.rus.bel 	| 34.4 	| 0.577 |
| Tatoeba-test.rus-bul.rus.bul 	| 45.5 	| 0.657 |
| Tatoeba-test.rus-ces.rus.ces 	| 48.0 	| 0.659 |
| Tatoeba-test.rus-dsb.rus.dsb 	| 10.7 	| 0.029 |
| Tatoeba-test.rus-hbs.rus.hbs 	| 44.6 	| 0.655 |
| Tatoeba-test.rus-mkd.rus.mkd 	| 34.9 	| 0.617 |
| Tatoeba-test.rus-orv.rus.orv 	| 0.1 	| 0.073 |
| Tatoeba-test.rus-pol.rus.pol 	| 45.2 	| 0.659 |
| Tatoeba-test.rus-slv.rus.slv 	| 30.4 	| 0.476 |
| Tatoeba-test.rus-ukr.rus.ukr 	| 57.6 	| 0.751 |
| Tatoeba-test.slv-ces.slv.ces 	| 42.5 	| 0.604 |
| Tatoeba-test.slv-pol.slv.pol 	| 39.6 	| 0.601 |
| Tatoeba-test.slv-rus.slv.rus 	| 47.2 	| 0.638 |
| Tatoeba-test.slv-ukr.slv.ukr 	| 36.4 	| 0.549 |
| Tatoeba-test.ukr-bel.ukr.bel 	| 36.9 	| 0.597 |
| Tatoeba-test.ukr-bul.ukr.bul 	| 56.4 	| 0.733 |
| Tatoeba-test.ukr-ces.ukr.ces 	| 52.1 	| 0.686 |
| Tatoeba-test.ukr-hbs.ukr.hbs 	| 47.1 	| 0.670 |
| Tatoeba-test.ukr-mkd.ukr.mkd 	| 20.8 	| 0.548 |
| Tatoeba-test.ukr-orv.ukr.orv 	| 0.2 	| 0.058 |
| Tatoeba-test.ukr-pol.ukr.pol 	| 50.1 	| 0.695 |
| Tatoeba-test.ukr-rus.ukr.rus 	| 63.9 	| 0.790 |
| Tatoeba-test.ukr-slv.ukr.slv 	| 14.5 	| 0.288 |


### System Info: 
- hf_name: sla-sla

- source_languages: sla

- target_languages: sla

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/sla-sla/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['be', 'hr', 'mk', 'cs', 'ru', 'pl', 'bg', 'uk', 'sl', 'sla']

- src_constituents: {'bel', 'hrv', 'orv_Cyrl', 'mkd', 'bel_Latn', 'srp_Latn', 'bul_Latn', 'ces', 'bos_Latn', 'csb_Latn', 'dsb', 'hsb', 'rus', 'srp_Cyrl', 'pol', 'rue', 'bul', 'ukr', 'slv'}

- tgt_constituents: {'bel', 'hrv', 'orv_Cyrl', 'mkd', 'bel_Latn', 'srp_Latn', 'bul_Latn', 'ces', 'bos_Latn', 'csb_Latn', 'dsb', 'hsb', 'rus', 'srp_Cyrl', 'pol', 'rue', 'bul', 'ukr', 'slv'}

- src_multilingual: True

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/sla-sla/opus-2020-07-27.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/sla-sla/opus-2020-07-27.test.txt

- src_alpha3: sla

- tgt_alpha3: sla

- short_pair: sla-sla

- chrF2_score: 0.672

- bleu: 48.5

- brevity_penalty: 1.0

- ref_len: 59320.0

- src_name: Slavic languages

- tgt_name: Slavic languages

- train_date: 2020-07-27

- src_alpha2: sla

- tgt_alpha2: sla

- prefer_old: False

- long_pair: sla-sla

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41
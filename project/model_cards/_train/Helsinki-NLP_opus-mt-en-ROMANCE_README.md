---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-ROMANCE

* source languages: en
* target languages: fr,fr_BE,fr_CA,fr_FR,wa,frp,oc,ca,rm,lld,fur,lij,lmo,es,es_AR,es_CL,es_CO,es_CR,es_DO,es_EC,es_ES,es_GT,es_HN,es_MX,es_NI,es_PA,es_PE,es_PR,es_SV,es_UY,es_VE,pt,pt_br,pt_BR,pt_PT,gl,lad,an,mwl,it,it_IT,co,nap,scn,vec,sc,ro,la
*  OPUS readme: [en-fr+fr_BE+fr_CA+fr_FR+wa+frp+oc+ca+rm+lld+fur+lij+lmo+es+es_AR+es_CL+es_CO+es_CR+es_DO+es_EC+es_ES+es_GT+es_HN+es_MX+es_NI+es_PA+es_PE+es_PR+es_SV+es_UY+es_VE+pt+pt_br+pt_BR+pt_PT+gl+lad+an+mwl+it+it_IT+co+nap+scn+vec+sc+ro+la](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-fr+fr_BE+fr_CA+fr_FR+wa+frp+oc+ca+rm+lld+fur+lij+lmo+es+es_AR+es_CL+es_CO+es_CR+es_DO+es_EC+es_ES+es_GT+es_HN+es_MX+es_NI+es_PA+es_PE+es_PR+es_SV+es_UY+es_VE+pt+pt_br+pt_BR+pt_PT+gl+lad+an+mwl+it+it_IT+co+nap+scn+vec+sc+ro+la/README.md)

*  dataset: opus
* model: transformer
* pre-processing: normalization + SentencePiece
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-04-21.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-fr+fr_BE+fr_CA+fr_FR+wa+frp+oc+ca+rm+lld+fur+lij+lmo+es+es_AR+es_CL+es_CO+es_CR+es_DO+es_EC+es_ES+es_GT+es_HN+es_MX+es_NI+es_PA+es_PE+es_PR+es_SV+es_UY+es_VE+pt+pt_br+pt_BR+pt_PT+gl+lad+an+mwl+it+it_IT+co+nap+scn+vec+sc+ro+la/opus-2020-04-21.zip)
* test set translations: [opus-2020-04-21.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-fr+fr_BE+fr_CA+fr_FR+wa+frp+oc+ca+rm+lld+fur+lij+lmo+es+es_AR+es_CL+es_CO+es_CR+es_DO+es_EC+es_ES+es_GT+es_HN+es_MX+es_NI+es_PA+es_PE+es_PR+es_SV+es_UY+es_VE+pt+pt_br+pt_BR+pt_PT+gl+lad+an+mwl+it+it_IT+co+nap+scn+vec+sc+ro+la/opus-2020-04-21.test.txt)
* test set scores: [opus-2020-04-21.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-fr+fr_BE+fr_CA+fr_FR+wa+frp+oc+ca+rm+lld+fur+lij+lmo+es+es_AR+es_CL+es_CO+es_CR+es_DO+es_EC+es_ES+es_GT+es_HN+es_MX+es_NI+es_PA+es_PE+es_PR+es_SV+es_UY+es_VE+pt+pt_br+pt_BR+pt_PT+gl+lad+an+mwl+it+it_IT+co+nap+scn+vec+sc+ro+la/opus-2020-04-21.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba.en.la 	| 50.1 	| 0.693 |


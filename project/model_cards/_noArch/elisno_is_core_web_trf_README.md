---
tags:
- spacy
- token-classification
language:
- is
model-index:
- name: is_core_web_trf
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9193318395
    - name: NER Recall
      type: recall
      value: 0.9217728758
    - name: NER F Score
      type: f_score
      value: 0.9205507394
---
| Feature | Description |
| --- | --- |
| **Name** | `is_core_web_trf` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.1.1,<3.2.0` |
| **Default Pipeline** | `transformer`, `ner`, `tagger`, `parser` |
| **Components** | `transformer`, `ner`, `tagger`, `parser` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (591 labels for 3 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `Date`, `Location`, `Miscellaneous`, `Money`, `Organization`, `Percent`, `Person`, `Time` |
| **`tagger`** | `aa`, `aae`, `aam`, `af`, `afe`, `afm`, `au`, `c`, `cn`, `ct`, `e`, `fahee`, `fahen`, `faheo`, `faheþ`, `fahfe`, `fahfn`, `fahfo`, `fahfþ`, `fakee`, `faken`, `fakeo`, `fakeþ`, `fakfe`, `fakfn`, `fakfo`, `fakfþ`, `favee`, `faven`, `faveo`, `faveþ`, `favfe`, `favfn`, `favfo`, `favfþ`, `fbhee`, `fbhen`, `fbheo`, `fbheþ`, `fbhfe`, `fbhfn`, `fbhfo`, `fbhfþ`, `fbkee`, `fbken`, `fbkeo`, `fbkeþ`, `fbkfe`, `fbkfn`, `fbkfo`, `fbkfþ`, `fbvee`, `fbven`, `fbveo`, `fbveþ`, `fbvfe`, `fbvfn`, `fbvfo`, `fbvfþ`, `fehee`, `fehen`, `feheo`, `feheþ`, `fehfe`, `fehfn`, `fehfo`, `fehfþ`, `fekee`, `feken`, `fekeo`, `fekeþ`, `fekfe`, `fekfn`, `fekfo`, `fekfþ`, `fevee`, `feven`, `feveo`, `feveþ`, `fevfe`, `fevfn`, `fevfo`, `fevfþ`, `fohee`, `fohen`, `foheo`, `foheþ`, `fohfe`, `fohfn`, `fohfo`, `fohfþ`, `fokee`, `foken`, `fokeo`, `fokeþ`, `fokfe`, `fokfn`, `fokfo`, `fokfþ`, `fovee`, `foven`, `foveo`, `foveþ`, `fovfe`, `fovfn`, `fovfo`, `fovfþ`, `fp1ee`, `fp1en`, `fp1eo`, `fp1eþ`, `fp1fe`, `fp1fn`, `fp1fo`, `fp1fþ`, `fp2ee`, `fp2en`, `fp2eo`, `fp2eþ`, `fp2fe`, `fp2fn`, `fp2fo`, `fp2fþ`, `fphee`, `fphen`, `fpheo`, `fpheþ`, `fphfe`, `fphfn`, `fphfo`, `fphfþ`, `fpkee`, `fpken`, `fpkeo`, `fpkeþ`, `fpkfe`, `fpkfn`, `fpkfo`, `fpkfþ`, `fpvee`, `fpven`, `fpveo`, `fpveþ`, `fpvfe`, `fpvfn`, `fpvfo`, `fpvfþ`, `fshee`, `fshen`, `fsheo`, `fsheþ`, `fshfe`, `fshfn`, `fshfo`, `fshfþ`, `fskee`, `fsken`, `fskeo`, `fskeþ`, `fskfe`, `fskfn`, `fskfo`, `fskfþ`, `fsvee`, `fsven`, `fsveo`, `fsveþ`, `fsvfe`, `fsvfn`, `fsvfo`, `fsvfþ`, `ghee`, `ghen`, `gheo`, `gheþ`, `ghfe`, `ghfn`, `ghfo`, `ghfþ`, `gkee`, `gken`, `gkeo`, `gkeþ`, `gkfe`, `gkfn`, `gkfo`, `gkfþ`, `gvee`, `gven`, `gveo`, `gveþ`, `gvfe`, `gvfn`, `gvfo`, `gvfþ`, `ks`, `kt`, `lheeof`, `lheesf`, `lheeve`, `lheevf`, `lheevm`, `lhenof`, `lhense`, `lhensf`, `lhenve`, `lhenvf`, `lhenvm`, `lheoof`, `lheose`, `lheosf`, `lheosm`, `lheove`, `lheovf`, `lheovm`, `lheþof`, `lheþse`, `lheþsf`, `lheþve`, `lheþvf`, `lheþvm`, `lhfeof`, `lhfese`, `lhfesf`, `lhfeve`, `lhfevf`, `lhfevm`, `lhfnof`, `lhfnse`, `lhfnsf`, `lhfnve`, `lhfnvf`, `lhfnvm`, `lhfoof`, `lhfose`, `lhfosf`, `lhfove`, `lhfovf`, `lhfovm`, `lhfþof`, `lhfþse`, `lhfþsf`, `lhfþve`, `lhfþvf`, `lhfþvm`, `lkeeof`, `lkeesf`, `lkeeve`, `lkeevf`, `lkeevm`, `lkenof`, `lkense`, `lkensf`, `lkenve`, `lkenvf`, `lkenvm`, `lkeoof`, `lkeose`, `lkeosf`, `lkeove`, `lkeovf`, `lkeovm`, `lkeþof`, `lkeþse`, `lkeþsf`, `lkeþve`, `lkeþvf`, `lkeþvm`, `lkfeof`, `lkfese`, `lkfesf`, `lkfeve`, `lkfevf`, `lkfevm`, `lkfnof`, `lkfnse`, `lkfnsf`, `lkfnve`, `lkfnvf`, `lkfnvm`, `lkfoof`, `lkfose`, `lkfosf`, `lkfove`, `lkfovf`, `lkfovm`, `lkfþof`, `lkfþse`, `lkfþsf`, `lkfþsm`, `lkfþve`, `lkfþvf`, `lkfþvm`, `lveeof`, `lveese`, `lveesf`, `lveeve`, `lveevf`, `lveevm`, `lvenof`, `lvense`, `lvensf`, `lvenve`, `lvenvf`, `lvenvm`, `lveoof`, `lveose`, `lveosf`, `lveove`, `lveovf`, `lveovm`, `lveþof`, `lveþse`, `lveþsf`, `lveþve`, `lveþvf`, `lveþvm`, `lvfeof`, `lvfese`, `lvfesf`, `lvfeve`, `lvfevf`, `lvfevm`, `lvfnof`, `lvfnse`, `lvfnsf`, `lvfnve`, `lvfnvf`, `lvfnvm`, `lvfoof`, `lvfose`, `lvfosf`, `lvfove`, `lvfovf`, `lvfovm`, `lvfþof`, `lvfþse`, `lvfþsf`, `lvfþsm`, `lvfþve`, `lvfþvf`, `lvfþvm`, `m`, `n----s`, `n-ee`, `n-ee-s`, `n-en`, `n-en-s`, `n-eng`, `n-eo`, `n-eo-s`, `n-eþ`, `n-eþ-s`, `n-fn`, `nhee`, `nhee-s`, `nheeg`, `nheegs`, `nhen`, `nhen-s`, `nheng`, `nhengs`, `nheo`, `nheo-s`, `nheog`, `nheogs`, `nheþ`, `nheþ-s`, `nheþg`, `nheþgs`, `nhfe`, `nhfe-s`, `nhfeg`, `nhfegs`, `nhfn`, `nhfn-s`, `nhfng`, `nhfngs`, `nhfo`, `nhfo-s`, `nhfog`, `nhfogs`, `nhfþ`, `nhfþ-s`, `nhfþg`, `nhfþgs`, `nkee`, `nkee-s`, `nkeeg`, `nkeegs`, `nken`, `nken-s`, `nkeng`, `nkengs`, `nkeo`, `nkeo-s`, `nkeog`, `nkeogs`, `nkeþ`, `nkeþ-s`, `nkeþg`, `nkeþgs`, `nkfe`, `nkfe-s`, `nkfeg`, `nkfegs`, `nkfn`, `nkfn-s`, `nkfng`, `nkfngs`, `nkfo`, `nkfo-s`, `nkfog`, `nkfogs`, `nkfþ`, `nkfþ-s`, `nkfþg`, `nkfþgs`, `nvee`, `nvee-s`, `nveeg`, `nveegs`, `nven`, `nven-s`, `nveng`, `nvengs`, `nveo`, `nveo-s`, `nveog`, `nveogs`, `nveþ`, `nveþ-s`, `nveþg`, `nveþgs`, `nvfe`, `nvfe-s`, `nvfeg`, `nvfegs`, `nvfn`, `nvfn-s`, `nvfng`, `nvfngs`, `nvfo`, `nvfo-s`, `nvfog`, `nvfogs`, `nvfþ`, `nvfþ-s`, `nvfþg`, `nvfþgs`, `pa`, `pg`, `pk`, `pl`, `sbg2en`, `sbg2fn`, `sbm2en`, `sbm2fn`, `sfg1en`, `sfg1eþ`, `sfg1fn`, `sfg1fþ`, `sfg2en`, `sfg2eþ`, `sfg2fn`, `sfg2fþ`, `sfg3en`, `sfg3eþ`, `sfg3fn`, `sfg3fþ`, `sfm1en`, `sfm1eþ`, `sfm1fn`, `sfm1fþ`, `sfm2en`, `sfm2eþ`, `sfm2fn`, `sfm2fþ`, `sfm3en`, `sfm3eþ`, `sfm3fn`, `sfm3fþ`, `slg`, `sng`, `snm`, `svg1en`, `svg1eþ`, `svg1fn`, `svg1fþ`, `svg2en`, `svg2eþ`, `svg2fn`, `svg2fþ`, `svg3en`, `svg3eþ`, `svg3fn`, `svg3fþ`, `svm1en`, `svm1eþ`, `svm1fn`, `svm1fþ`, `svm2en`, `svm2eþ`, `svm2fn`, `svm3en`, `svm3eþ`, `svm3fn`, `svm3fþ`, `sþghen`, `sþgheo`, `sþghfn`, `sþghfo`, `sþgken`, `sþgkeo`, `sþgkfn`, `sþgkfo`, `sþgven`, `sþgveo`, `sþgvfn`, `sþgvfo`, `sþgvfþ`, `sþmhen`, `sþmheo`, `sþmken`, `sþmven`, `ta`, `tfhee`, `tfhen`, `tfheo`, `tfheþ`, `tfhfe`, `tfhfn`, `tfhfo`, `tfhfþ`, `tfkee`, `tfken`, `tfkeo`, `tfkeþ`, `tfkfe`, `tfkfn`, `tfkfo`, `tfkfþ`, `tfvee`, `tfven`, `tfveo`, `tfveþ`, `tfvfe`, `tfvfn`, `tfvfo`, `tfvfþ`, `to`, `tp`, `v`, `x` |
| **`parser`** | `ROOT`, `acl`, `acl:relcl`, `advcl`, `advmod`, `amod`, `appos`, `aux`, `case`, `cc`, `ccomp`, `compound:prt`, `conj`, `cop`, `dep`, `det`, `fixed`, `flat:name`, `mark`, `nmod`, `nmod:poss`, `nsubj`, `nummod`, `obj`, `obl`, `obl:arg`, `parataxis`, `punct`, `xcomp` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 92.06 |
| `ENTS_P` | 91.93 |
| `ENTS_R` | 92.18 |
| `TRANSFORMER_LOSS` | 248325.98 |
| `NER_LOSS` | 120059.07 |
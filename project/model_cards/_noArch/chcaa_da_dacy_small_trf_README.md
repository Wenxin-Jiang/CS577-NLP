---
tags:
- spacy
- token-classification
language:
- da
license: apache-2.0
model-index:
- name: da_dacy_small_trf
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.81724846
    - name: NER Recall
      type: recall
      value: 0.8291666667
    - name: NER F Score
      type: f_score
      value: 0.8231644261
  - task:
      name: SENTER
      type: token-classification
    metrics:
    - name: SENTER Precision
      type: precision
      value: 0.8603839442
    - name: SENTER Recall
      type: recall
      value: 0.8741134752
    - name: SENTER F Score
      type: f_score
      value: 0.8671943712
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Dependencies Accuracy
      type: accuracy
      value: 0.8492442546
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Dependencies Accuracy
      type: accuracy
      value: 0.8492442546
---

<a href="https://github.com/centre-for-humanities-computing/Dacy"><img src="https://centre-for-humanities-computing.github.io/DaCy/_static/icon.png" width="175" height="175" align="right" /></a>

# DaCy small transformer

DaCy is a Danish language processing framework with state-of-the-art pipelines as well as functionality for analysing Danish pipelines.
DaCy's largest pipeline has achieved State-of-the-Art performance on Named entity recognition, part-of-speech tagging and dependency 
parsing for Danish on the DaNE dataset. Check out the [DaCy repository](https://github.com/centre-for-humanities-computing/DaCy) for material on how to use DaCy and reproduce the results. 
DaCy also contains guides on usage of the package as well as behavioural test for biases and robustness of Danish NLP pipelines.
    

| Feature | Description |
| --- | --- |
| **Name** | `da_dacy_small_trf` |
| **Version** | `0.1.0` |
| **spaCy** | `>=3.1.1,<3.2.0` |
| **Default Pipeline** | `transformer`, `morphologizer`, `parser`, `attribute_ruler`, `lemmatizer`, `ner` |
| **Components** | `transformer`, `morphologizer`, `parser`, `attribute_ruler`, `lemmatizer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [UD Danish DDT v2.5](https://github.com/UniversalDependencies/UD_Danish-DDT) (Johannsen, Anders; Martínez Alonso, Héctor; Plank, Barbara)<br />[DaNE](https://github.com/alexandrainst/danlp/blob/master/docs/datasets.md#danish-dependency-treebank-dane) (Rasmus Hvingelby, Amalie B. Pauli, Maria Barrett, Christina Rosted, Lasse M. Lidegaard, Anders Søgaard)<br />[Maltehb/-l-ctra-danish-electra-small-cased](https://huggingface.co/Maltehb/-l-ctra-danish-electra-small-cased) (Malte Højmark-Bertelsen) |
| **License** | `Apache-2.0 License` |
| **Author** | [Centre for Humanities Computing Aarhus](https://chcaa.io/#/) |

### Label Scheme

<details>

<summary>View label scheme (192 labels for 3 components)</summary>

| Component | Labels |
| --- | --- |
| **`morphologizer`** | `AdpType=Prep\|POS=ADP`, `Definite=Ind\|Gender=Com\|Number=Sing\|POS=NOUN`, `Mood=Ind\|POS=AUX\|Tense=Pres\|VerbForm=Fin\|Voice=Act`, `POS=PROPN`, `Definite=Ind\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=SCONJ`, `Definite=Def\|Gender=Com\|Number=Sing\|POS=NOUN`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin\|Voice=Act`, `POS=ADV`, `Number=Plur\|POS=DET\|PronType=Dem`, `Degree=Pos\|Number=Plur\|POS=ADJ`, `Definite=Ind\|Gender=Com\|Number=Plur\|POS=NOUN`, `POS=PUNCT`, `POS=CCONJ`, `Definite=Ind\|Degree=Cmp\|Number=Sing\|POS=ADJ`, `Degree=Cmp\|POS=ADJ`, `POS=PRON\|PartType=Inf`, `Gender=Com\|Number=Sing\|POS=DET\|PronType=Ind`, `Definite=Ind\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Case=Acc\|Gender=Neut\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Definite=Def\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `Degree=Pos\|POS=ADV`, `Definite=Def\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=PRON\|PronType=Dem`, `NumType=Card\|POS=NUM`, `Definite=Ind\|Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Case=Acc\|Gender=Com\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Degree=Pos\|Gender=Com\|Number=Sing\|POS=ADJ`, `Case=Nom\|Gender=Com\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `NumType=Ord\|POS=ADJ`, `Gender=Com\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `Mood=Ind\|POS=AUX\|Tense=Past\|VerbForm=Fin\|Voice=Act`, `POS=VERB\|VerbForm=Inf\|Voice=Act`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin\|Voice=Act`, `POS=NOUN`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin\|Voice=Pass`, `POS=ADP\|PartType=Inf`, `Degree=Pos\|POS=ADJ`, `Definite=Def\|Gender=Com\|Number=Plur\|POS=NOUN`, `Number[psor]=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Com\|Number=Sing\|POS=NOUN`, `POS=AUX\|VerbForm=Inf\|Voice=Act`, `Definite=Ind\|Degree=Pos\|Gender=Com\|Number=Sing\|POS=ADJ`, `Gender=Com\|Number=Sing\|POS=DET\|PronType=Dem`, `Number=Plur\|POS=DET\|PronType=Ind`, `Gender=Com\|Number=Sing\|POS=PRON\|PronType=Ind`, `Case=Acc\|POS=PRON\|Person=3\|PronType=Prs\|Reflex=Yes`, `POS=PART\|PartType=Inf`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Ind`, `Case=Acc\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `Case=Nom\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Case=Nom\|Gender=Com\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Nom\|Gender=Com\|POS=PRON\|PronType=Ind`, `Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Ind`, `Mood=Imp\|POS=VERB`, `Gender=Com\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Definite=Ind\|Number=Sing\|POS=AUX\|Tense=Past\|VerbForm=Part`, `POS=X`, `Case=Nom\|Gender=Com\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Com\|Number=Plur\|POS=NOUN`, `POS=VERB\|Tense=Pres\|VerbForm=Part`, `Number=Plur\|POS=PRON\|PronType=Int,Rel`, `POS=VERB\|VerbForm=Inf\|Voice=Pass`, `Case=Gen\|Definite=Ind\|Gender=Com\|Number=Sing\|POS=NOUN`, `Degree=Cmp\|POS=ADV`, `POS=ADV\|PartType=Inf`, `Degree=Sup\|POS=ADV`, `Number=Plur\|POS=PRON\|PronType=Dem`, `Number=Plur\|POS=PRON\|PronType=Ind`, `Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Case=Acc\|Gender=Com\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Gen\|POS=PROPN`, `POS=ADP`, `Degree=Cmp\|Number=Plur\|POS=ADJ`, `Definite=Def\|Degree=Sup\|POS=ADJ`, `Gender=Neut\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Degree=Pos\|Number=Sing\|POS=ADJ`, `Number=Plur\|Number[psor]=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `Gender=Com\|Number=Sing\|Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs\|Style=Form`, `Number=Plur\|POS=PRON\|PronType=Rcp`, `Case=Gen\|Degree=Cmp\|POS=ADJ`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Number[psor]=Plur\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `POS=INTJ`, `Number=Plur\|Number[psor]=Sing\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Gender=Neut\|Number=Sing\|Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs\|Style=Form`, `Case=Acc\|Gender=Com\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Gender=Com\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Number=Sing\|POS=PRON\|PronType=Int,Rel`, `Number=Plur\|Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs\|Style=Form`, `Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Int,Rel`, `Definite=Def\|Degree=Sup\|Number=Plur\|POS=ADJ`, `Case=Nom\|Gender=Com\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Gender=Neut\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `Definite=Ind\|Number=Sing\|POS=NOUN`, `Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Number=Plur\|Number[psor]=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `POS=SYM`, `Case=Nom\|Gender=Com\|POS=PRON\|Person=2\|Polite=Form\|PronType=Prs`, `Degree=Sup\|POS=ADJ`, `Number=Plur\|POS=DET\|PronType=Ind\|Style=Arch`, `Case=Gen\|Gender=Com\|Number=Sing\|POS=DET\|PronType=Dem`, `Foreign=Yes\|POS=X`, `POS=DET\|Person=2\|Polite=Form\|Poss=Yes\|PronType=Prs`, `Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Dem`, `Case=Acc\|Gender=Com\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `Case=Gen\|POS=PRON\|PronType=Int,Rel`, `Gender=Com\|Number=Sing\|POS=PRON\|PronType=Dem`, `Abbr=Yes\|POS=X`, `Case=Gen\|Definite=Ind\|Gender=Com\|Number=Plur\|POS=NOUN`, `Definite=Def\|Degree=Abs\|POS=ADJ`, `Definite=Ind\|Degree=Sup\|Number=Sing\|POS=ADJ`, `Definite=Ind\|POS=NOUN`, `Gender=Com\|Number=Plur\|POS=NOUN`, `Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Gender=Com\|POS=PRON\|PronType=Int,Rel`, `Case=Nom\|Gender=Com\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Degree=Abs\|POS=ADV`, `POS=VERB\|VerbForm=Ger`, `POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Def\|Degree=Sup\|Number=Sing\|POS=ADJ`, `Number=Plur\|Number[psor]=Plur\|POS=PRON\|Person=1\|Poss=Yes\|PronType=Prs\|Style=Form`, `Case=Gen\|Definite=Def\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Case=Gen\|Degree=Pos\|Number=Plur\|POS=ADJ`, `Case=Acc\|Gender=Com\|POS=PRON\|Person=2\|Polite=Form\|PronType=Prs`, `Gender=Com\|Number=Sing\|POS=PRON\|PronType=Int,Rel`, `POS=VERB\|Tense=Pres`, `Case=Gen\|Number=Plur\|POS=DET\|PronType=Ind`, `Number[psor]=Plur\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `POS=PRON\|Person=2\|Polite=Form\|Poss=Yes\|PronType=Prs`, `Gender=Neut\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `POS=AUX\|Tense=Pres\|VerbForm=Part`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin\|Voice=Pass`, `Gender=Com\|Number=Sing\|Number[psor]=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `Degree=Sup\|Number=Plur\|POS=ADJ`, `Case=Acc\|Gender=Com\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Gender=Neut\|Number=Sing\|Number[psor]=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `Definite=Ind\|Number=Plur\|POS=NOUN`, `Case=Gen\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Mood=Imp\|POS=AUX`, `Gender=Com\|Number=Sing\|Number[psor]=Sing\|POS=PRON\|Person=1\|Poss=Yes\|PronType=Prs`, `Number[psor]=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `Definite=Def\|Gender=Com\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Number=Plur\|Number[psor]=Sing\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `Case=Gen\|Gender=Com\|Number=Sing\|POS=DET\|PronType=Ind`, `Case=Gen\|POS=NOUN`, `Number[psor]=Plur\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `POS=DET\|PronType=Dem`, `Definite=Def\|Number=Plur\|POS=NOUN` |
| **`parser`** | `ROOT`, `acl:relcl`, `advcl`, `advmod`, `amod`, `appos`, `aux`, `case`, `cc`, `ccomp`, `compound:prt`, `conj`, `cop`, `dep`, `det`, `expl`, `fixed`, `flat`, `iobj`, `list`, `mark`, `nmod`, `nmod:poss`, `nsubj`, `nummod`, `obj`, `obl`, `obl:loc`, `obl:tmod`, `punct`, `xcomp` |
| **`ner`** | `LOC`, `MISC`, `ORG`, `PER` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `POS_ACC` | 95.83 |
| `MORPH_ACC` | 95.70 |
| `DEP_UAS` | 84.92 |
| `DEP_LAS` | 81.76 |
| `SENTS_P` | 86.04 |
| `SENTS_R` | 87.41 |
| `SENTS_F` | 86.72 |
| `LEMMA_ACC` | 84.91 |
| `ENTS_F` | 82.32 |
| `ENTS_P` | 81.72 |
| `ENTS_R` | 82.92 |
| `TRANSFORMER_LOSS` | 41746686.63 |
| `MORPHOLOGIZER_LOSS` | 3458966.49 |
| `PARSER_LOSS` | 15104898.38 |
| `NER_LOSS` | 546098.45 |


## Bias and Robustness

Besides the validation done by SpaCy on the DaNE testset, DaCy also provides a series of augmentations to the DaNE test set to see how well the models deal with these types of augmentations.
The can be seen as behavioural probes akinn to the NLP checklist.

### Deterministic Augmentations
Deterministic augmentations are augmentation which always yield the same result.

| Augmentation | Part-of-speech tagging (Accuracy) | Morphological tagging (Accuracy) | Dependency Parsing (UAS) | Dependency Parsing (LAS) | Sentence segmentation (F1) | Lemmatization (Accuracy) | Named entity recognition (F1) |
| --- | --- | --- | --- |  --- | --- | --- |  --- |
| No augmentation | 0.98 | 0.974 | 0.868 |  0.836 | 0.936 | 0.844 | 0.765 |
| Æøå Augmentation | 0.955 | 0.948 | 0.823 |  0.783 | 0.922 | 0.754 | 0.718 |
| Lowercase | 0.974 | 0.97 | 0.862 |  0.828 | 0.905 | 0.848 | 0.681 |
| No Spacing | 0.229 | 0.229 | 0.004 |  0.003 | 0.824 | 0.225 | 0.048 |
| Abbreviated first names | 0.979 | 0.973 | 0.864 |  0.832 | 0.94 | 0.845 | 0.699 |
| Input size augmentation 5 sentences | 0.956 | 0.956 | 0.851 |  0.818 | 0.883 | 0.844 | 0.743 |
| Input size augmentation 10 sentences | 0.959 | 0.958 | 0.853 |  0.821 | 0.897 | 0.844 | 0.755 |



### Stochastic Augmentations
Stochastic augmentations are augmentation which are repeated mulitple times to estimate the effect of the augmentation.

| Augmentation | Part-of-speech tagging (Accuracy) | Morphological tagging (Accuracy) | Dependency Parsing (UAS) | Dependency Parsing (LAS) | Sentence segmentation (F1) | Lemmatization (Accuracy) | Named entity recognition (F1) |
| --- | --- | --- | --- |  --- | --- | --- |  --- |
| Keystroke errors 2% | 0.931 (0.003) | 0.929 (0.003) | 0.797 (0.003) |  0.753 (0.003) | 0.884 (0.003) | 0.772 (0.003) | 0.657 (0.003) |
| Keystroke errors 5% | 0.859 (0.003) | 0.863 (0.003) | 0.699 (0.003) |  0.641 (0.003) | 0.824 (0.003) | 0.681 (0.003) | 0.53 (0.003) |
| Keystroke errors 15% | 0.633 (0.006) | 0.662 (0.006) | 0.439 (0.006) |  0.358 (0.006) | 0.688 (0.006) | 0.459 (0.006) | 0.293 (0.006) |
| Danish names | 0.979 (0.0) | 0.974 (0.0) | 0.867 (0.0) |  0.835 (0.0) | 0.943 (0.0) | 0.847 (0.0) | 0.748 (0.0) |
| Muslim names | 0.979 (0.0) | 0.974 (0.0) | 0.865 (0.0) |  0.833 (0.0) | 0.94 (0.0) | 0.847 (0.0) | 0.732 (0.0) |
| Female names | 0.979 (0.0) | 0.974 (0.0) | 0.867 (0.0) |  0.835 (0.0) | 0.946 (0.0) | 0.847 (0.0) | 0.754 (0.0) |
| Male names | 0.979 (0.0) | 0.974 (0.0) | 0.867 (0.0) |  0.835 (0.0) | 0.943 (0.0) | 0.847 (0.0) | 0.748 (0.0) |
| Spacing Augmention 5% | 0.941 (0.002) | 0.936 (0.002) | 0.755 (0.002) |  0.725 (0.002) | 0.907 (0.002) | 0.811 (0.002) | 0.699 (0.002) |

<details>

<summary> Description of Augmenters </summary>

    

**No augmentation:**
Applies no augmentation to the DaNE test set.

**Æøå Augmentation:**
This augmentation replace the æ,ø, and å with their spelling variations ae, oe and aa respectively.

**Lowercase:**
This augmentation lowercases all text.

**No Spacing:**
This augmentation removed all spacing from the text.

**Abbreviated first names:**
This agmentation abbreviates the first names of entities. For instance 'Kenneth Enevoldsen' would turn to 'K. Enevoldsen'.

**Keystroke errors 2%:**
This agmentation simulate keystroke errors by replacing 2% of keys with a neighbouring key on a Danish QWERTY keyboard. As this agmentation is stochastic it is repeated 20 times to obtain a consistent estimate and the mean is provided with its standard deviation in parenthesis.

**Keystroke errors 5%:**
This agmentation simulate keystroke errors by replacing 5% of keys with a neighbouring key on a Danish QWERTY keyboard. As this agmentation is stochastic it is repeated 20 times to obtain a consistent estimate and the mean is provided with its standard deviation in parenthesis.

**Keystroke errors 15%:**
This agmentation simulate keystroke errors by replacing 15% of keys with a neighbouring key on a Danish QWERTY keyboard. As this agmentation is stochastic it is repeated 20 times to obtain a consistent estimate and the mean is provided with its standard deviation in parenthesis.

**Danish names:**
This agmentation replace all names with Danish names derived from Danmarks Statistik (2021). As this agmentation is stochastic it is repeated 20 times to obtain a consistent estimate and the mean is provided with its standard deviation in parenthesis.

**Muslim names:**
This agmentation replace all names with Muslim names derived from  Meldgaard (2005). As this agmentation is stochastic it is repeated 20 times to obtain a consistent estimate and the mean is provided with its standard deviation in parenthesis.

**Female names:**
This agmentation replace all names with Danish female names derived from Danmarks Statistik (2021). As this agmentation is stochastic it is repeated 20 times to obtain a consistent estimate and the mean is provided with its standard deviation in parenthesis.

**Male names:**
This agmentation replace all names with Danish male names derived from Danmarks Statistik (2021). As this agmentation is stochastic it is repeated 20 times to obtain a consistent estimate and the mean is provided with its standard deviation in parenthesis.

**Spacing Augmention 5%:**
This agmentation replace all names with Danish male names derived from Danmarks Statistik (2021). As this agmentation is stochastic it is repeated 20 times to obtain a consistent estimate and the mean is provided with its standard deviation in parenthesis.
 </details> 
 <br /> 


### Hardware
This was run an trained on a Quadro RTX 8000 GPU.

---
language: en
datasets:
 - ccdv/pubmed-summarization
  
license: apache-2.0
---

## Introduction

[Google's LongT5: Efficient Text-To-Text Transformer for Long Sequences](https://arxiv.org/pdf/2112.07916.pdf) introduced as an extension of a successful [T5 model](https://arxiv.org/pdf/1910.10683.pdf).

This is an unofficial *longt5-large-16384-pubmed-3k_steps* checkpoint. I.e., this is a large configuration of the LongT5 model with a `transient-global` attention fine-tuned on [pubmed summarization dataset](https://huggingface.co/datasets/ccdv/pubmed-summarization) for 3,000 training steps. It may be worth continuing in the fine-tuning as we did not train the model until the convergence.

## Results and Fine-tuning Details 

The fine-tuned model achieves the following results on the evaluation set using `beam_search=3` and without any specific calibration of generation parameters are presented below, altogether with the results from the original paper (the original scores are higher, very likely due to a higher number of training steps).

| Metric | Score | Score (original paper)
| --- | --- | --- |
| Rouge-1 | 47.44 | 49.98 |
| Rouge-2 | 22.68 | 24.69 |
| Rouge-L | 29.83 | x |
| Rouge-Lsum | 43.13 | 46.46 |

The training parameters follow the ones specified in the paper. We accumulated batch size to 128 examples and used `Adafactor` optimizer with a constant learning rate `0.001`. The full training hyper-parameters and logs can be found via the following [W&B run](https://wandb.ai/stancld/LongT5/runs/1lwncl8a?workspace=user-stancld). The model was trained using the [HuggingFace's trainer](https://github.com/huggingface/transformers/blob/main/src/transformers/trainer_seq2seq.py).

The only specific adjustment, I made for the training, was dropping very short input articles (less than 16 words (a bit of mistake, should be less than 16 tokens)) as this sequences do not contribute to gradient creation in the *transient-global* attention, which resulted in training crashes when DDP used.

## Usage

```python 
LONG_ARTICLE = """"anxiety affects quality of life in those living
with parkinson 's disease ( pd ) more so than
overall cognitive status , motor deficits , apathy
, and depression [ 13 ] . although anxiety and
depression are often related and coexist in pd
patients , recent research suggests that anxiety
rather than depression is the most prominent and
prevalent mood disorder in pd [ 5 , 6 ] . yet ,
our current understanding of anxiety and its
impact on cognition in pd , as well as its neural
basis and best treatment practices , remains
meager and lags far behind that of depression .
overall , neuropsychiatric symptoms in pd have
been shown to be negatively associated with
cognitive performance . for example , higher
depression scores have been correlated with lower
scores on the mini - mental state exam ( mmse ) [
8 , 9 ] as well as tests of memory and executive
functions ( e.g. , attention ) [ 1014 ] . likewise
, apathy and anhedonia in pd patients have been
associated with executive dysfunction [ 10 , 1523
] . however , few studies have specifically
investigated the relationship between anxiety and
cognition in pd . one study showed a strong
negative relationship between anxiety ( both state
and trait ) and overall cognitive performance (
measured by the total of the repeatable battery
for the assessment of neuropsychological status
index ) within a sample of 27 pd patients .
furthermore , trait anxiety was negatively
associated with each of the cognitive domains
assessed by the rbans ( i.e. , immediate memory ,
visuospatial construction , language , attention ,
and delayed memory ) . two further studies have
examined whether anxiety differentially affects
cognition in patients with left - sided dominant
pd ( lpd ) versus right - sided dominant pd ( rpd
) ; however , their findings were inconsistent .
the first study found that working memory
performance was worse in lpd patients with anxiety
compared to rpd patients with anxiety , whereas
the second study reported that , in lpd , apathy
but not anxiety was associated with performance on
nonverbally mediated executive functions and
visuospatial tasks ( e.g. , tmt - b , wms - iii
spatial span ) , while in rpd , anxiety but not
apathy significantly correlated with performance
on verbally mediated tasks ( e.g. , clock reading
test and boston naming test ) . furthermore ,
anxiety was significantly correlated with
neuropsychological measures of attention and
executive and visuospatial functions . taken
together , it is evident that there are limited
and inconsistent findings describing the
relationship between anxiety and cognition in pd
and more specifically how anxiety might influence
particular domains of cognition such as attention
and memory and executive functioning . it is also
striking that , to date , no study has examined
the influence of anxiety on cognition in pd by
directly comparing groups of pd patients with and
without anxiety while excluding depression . given
that research on healthy young adults suggests
that anxiety reduces processing capacity and
impairs processing efficiency , especially in the
central executive and attentional systems of
working memory [ 26 , 27 ] , we hypothesized that
pd patients with anxiety would show impairments in
attentional set - shifting and working memory
compared to pd patients without anxiety .
furthermore , since previous work , albeit limited
, has focused on the influence of symptom
laterality on anxiety and cognition , we also
explored this relationship . seventeen pd patients
with anxiety and thirty - three pd patients
without anxiety were included in this study ( see
table 1 ) . the cross - sectional data from these
participants was taken from a patient database
that has been compiled over the past 8 years (
since 2008 ) at the parkinson 's disease research
clinic at the brain and mind centre , university
of sydney . inclusion criteria involved a
diagnosis of idiopathic pd according to the united
kingdom parkinson 's disease society brain bank
criteria   and were confirmed by a neurologist (
sjgl ) . patients also had to have an adequate
proficiency in english and have completed a full
neuropsychological assessment . ten patients in
this study ( 5 pd with anxiety ; 5 pd without
anxiety ) were taking psychotropic drugs ( i.e. ,
benzodiazepine or selective serotonin reuptake
inhibitor ) . patients were also excluded if they
had other neurological disorders , psychiatric
disorders other than affective disorders ( such as
anxiety ) , or if they reported a score greater
than six on the depression subscale of the
hospital anxiety and depression scale ( hads ) .
thus , all participants who scored within a
depressed  ( hads - d > 6 ) range were excluded
from this study , in attempt to examine a refined
sample of pd patients with and without anxiety in
order to determine the independent effect of
anxiety on cognition . this research was approved
by the human research ethics committee of the
university of sydney , and written informed
consent was obtained from all participants . self
- reported hads was used to assess anxiety in pd
and has been previously shown to be a useful
measure of clinical anxiety in pd . a cut - off
score of > 8 on the anxiety subscale of the hads (
hads - a ) was used to identify pd cases with
anxiety ( pda+ ) , while a cut - off score of < 6
on the hads - a was used to identify pd cases
without anxiety ( pda ) . this criterion was more
stringent than usual ( > 7 cut - off score ) , in
effort to create distinct patient groups . the
neurological evaluation rated participants
according to hoehn and yahr ( h&y ) stages   and
assessed their motor symptoms using part iii of
the revised mds task force unified parkinson 's
disease rating scale ( updrs ) . in a similar way
this was determined by calculating a total left
and right score from rigidity items 3035 ,
voluntary movement items 3643 , and tremor items
5057 from the mds - updrs part iii ( see table 1 )
. processing speed was assessed using the trail
making test , part a ( tmt - a , z - score ) .
attentional set - shifting was measured using the
trail making test , part b ( tmt - b , z - score )
. working memory was assessed using the digit span
forward and backward subtest of the wechsler
memory scale - iii ( raw scores ) . language was
assessed with semantic and phonemic verbal fluency
via the controlled oral word associated test (
cowat animals and letters , z - score ) . the
ability to retain learned verbal memory was
assessed using the logical memory subtest from the
wechsler memory scale - iii ( lm - i z - score ,
lm - ii z - score , % lm retention z - score ) .
the mini - mental state examination ( mmse )
demographic , clinical , and neuropsychological
variables were compared between the two groups
with the independent t - test or mann  whitney u
test , depending on whether the variable met
parametric assumptions . chi - square tests were
used to examine gender and symptom laterality
differences between groups . all analyses employed
an alpha level of p < 0.05 and were two - tailed .
spearman correlations were performed separately in
each group to examine associations between anxiety
and/or depression ratings and cognitive functions
. as expected , the pda+ group reported
significant greater levels of anxiety on the hads
- a ( u = 0 , p < 0.001 ) and higher total score
on the hads ( u = 1 , p < 0.001 ) compared to the
pda group ( table 1 ) . groups were matched in age
( t(48 ) = 1.31 , p = 0.20 ) , disease duration (
u = 259 , p = 0.66 ) , updrs - iii score ( u =
250.5 , p = 0.65 ) , h&y ( u = 245 , p = 0.43 ) ,
ledd ( u = 159.5 , p = 0.80 ) , and depression (
hads - d ) ( u = 190.5 , p = 0.06 ) . additionally
, all groups were matched in the distribution of
gender (  = 0.098 , p = 0.75 ) and side - affected
(  = 0.765 , p = 0.38 ) . there were no group
differences for tmt - a performance ( u = 256 , p
= 0.62 ) ( table 2 ) ; however , the pda+ group
had worse performance on the trail making test
part b ( t(46 ) = 2.03 , p = 0.048 ) compared to
the pda group ( figure 1 ) . the pda+ group also
demonstrated significantly worse performance on
the digit span forward subtest ( t(48 ) = 2.22 , p
= 0.031 ) and backward subtest ( u = 190.5 , p =
0.016 ) compared to the pda group ( figures 2(a )
and 2(b ) ) . neither semantic verbal fluency (
t(47 ) = 0.70 , p = 0.49 ) nor phonemic verbal
fluency ( t(47 ) = 0.39 , p = 0.70 ) differed
between groups . logical memory i immediate recall
test ( u = 176 , p = 0.059 ) showed a trend that
the pda+ group had worse new verbal learning and
immediate recall abilities than the pda group .
however , logical memory ii test performance ( u =
219 , p = 0.204 ) and logical memory % retention (
u = 242.5 , p = 0.434 ) did not differ between
groups . there were also no differences between
groups in global cognition ( mmse ) ( u = 222.5 ,
p = 0.23 ) . participants were split into lpd and
rpd , and then further group differences were
examined between pda+ and pda. importantly , the
groups remained matched in age , disease duration
, updrs - iii , dde , h&y stage , and depression
but remained significantly different on self -
reported anxiety . lpda+ demonstrated worse
performance on the digit span forward test ( t(19
) = 2.29 , p = 0.033 ) compared to lpda , whereas
rpda+ demonstrated worse performance on the digit
span backward test ( u = 36.5 , p = 0.006 ) , lm -
i immediate recall ( u = 37.5 , p = 0.008 ) , and
lm - ii ( u = 45.0 , p = 0.021 ) but not lm %
retention ( u = 75.5 , p = 0.39 ) compared to
rpda. this study is the first to directly compare
cognition between pd patients with and without
anxiety . the findings confirmed our hypothesis
that anxiety negatively influences attentional set
- shifting and working memory in pd . more
specifically , we found that pd patients with
anxiety were more impaired on the trail making
test part b which assessed attentional set -
shifting , on both digit span tests which assessed
working memory and attention , and to a lesser
extent on the logical memory test which assessed
memory and new verbal learning compared to pd
patients without anxiety . taken together , these
findings suggest that anxiety in pd may reduce
processing capacity and impair processing
efficiency , especially in the central executive
and attentional systems of working memory in a
similar way as seen in young healthy adults [ 26 ,
27 ] . although the neurobiology of anxiety in pd
remains unknown , many researchers have postulated
that anxiety disorders are related to
neurochemical changes that occur during the early
, premotor stages of pd - related degeneration [
37 , 38 ] such as nigrostriatal dopamine depletion
, as well as cell loss within serotonergic and
noradrenergic brainstem nuclei ( i.e. , raphe
nuclei and locus coeruleus , resp . , which
provide massive inputs to corticolimbic regions )
. over time , chronic dysregulation of
adrenocortical and catecholamine functions can
lead to hippocampal damage as well as
dysfunctional prefrontal neural circuitries [ 39 ,
40 ] , which play a key role in memory and
attention . recent functional neuroimaging work
has suggested that enhanced hippocampal activation
during executive functioning and working memory
tasks may represent compensatory processes for
impaired frontostriatal functions in pd patients
compared to controls . therefore , chronic stress
from anxiety , for example , may disrupt
compensatory processes in pd patients and explain
the cognitive impairments specifically in working
memory and attention seen in pd patients with
anxiety . it has also been suggested that
hyperactivation within the putamen may reflect a
compensatory striatal mechanism to maintain normal
working memory performance in pd patients ;
however , losing this compensatory activation has
been shown to contribute to poor working memory
performance . anxiety in mild pd has been linked
to reduced putamen dopamine uptake which becomes
more extensive as the disease progresses . this
further supports the notion that anxiety may
disrupt compensatory striatal mechanisms as well ,
providing another possible explanation for the
cognitive impairments observed in pd patients with
anxiety in this study . noradrenergic and
serotonergic systems should also be considered
when trying to explain the mechanisms by which
anxiety may influence cognition in pd . although
these neurotransmitter systems are relatively
understudied in pd cognition , treating the
noradrenergic and serotonergic systems has shown
beneficial effects on cognition in pd . selective
serotonin reuptake inhibitor , citalopram , was
shown to improve response inhibition deficits in
pd , while noradrenaline reuptake blocker ,
atomoxetine , has been recently reported to have
promising effects on cognition in pd [ 45 , 46 ] .
overall , very few neuroimaging studies have been
conducted in pd in order to understand the neural
correlates of pd anxiety and its underlying neural
pathology . future research should focus on
relating anatomical changes and neurochemical
changes to neural activation in order to gain a
clearer understanding on how these pathologies
affect anxiety in pd . to further understand how
anxiety and cognitive dysfunction are related ,
future research should focus on using advanced
structural and function imaging techniques to
explain both cognitive and neural breakdowns that
are associated with anxiety in pd patients .
research has indicated that those with amnestic
mild cognitive impairment who have more
neuropsychiatric symptoms have a greater risk of
developing dementia compared to those with fewer
neuropsychiatric symptoms . future studies should
also examine whether treating neuropsychiatric
symptoms might impact the progression of cognitive
decline and improve cognitive impairments in pd
patients . previous studies have used pd symptom
laterality as a window to infer asymmetrical
dysfunction of neural circuits . for example , lpd
patients have greater inferred right hemisphere
pathology , whereas rpd patients have greater
inferred left hemisphere pathology . thus ,
cognitive domains predominantly subserved by the
left hemisphere ( e.g. , verbally mediated tasks
of executive function and verbal memory ) might be
hypothesized to be more affected in rpd than lpd ;
however , this remains controversial . it has also
been suggested that since anxiety is a common
feature of left hemisphere involvement [ 48 , 49 ]
, cognitive domains subserved by the left
hemisphere may also be more strongly related to
anxiety . results from this study showed selective
verbal memory deficits in rpd patients with
anxiety compared to rpd without anxiety , whereas
lpd patients with anxiety had greater attentional
/ working memory deficits compared to lpd without
anxiety . although these results align with
previous research , interpretations of these
findings should be made with caution due to the
small sample size in the lpd comparison
specifically . recent work has suggested that the
hads questionnaire may underestimate the burden of
anxiety related symptomology and therefore be a
less sensitive measure of anxiety in pd [ 30 , 50
] . in addition , our small sample size also
limited the statistical power for detecting
significant findings . based on these limitations
, our findings are likely conservative and
underrepresent the true impact anxiety has on
cognition in pd . additionally , the current study
employed a very brief neuropsychological
assessment including one or two tests for each
cognitive domain . future studies are encouraged
to collect a more complex and comprehensive
battery from a larger sample of pd participants in
order to better understand the role anxiety plays
on cognition in pd . another limitation of this
study was the absence of diagnostic interviews to
characterize participants ' psychiatric symptoms
and specify the type of anxiety disorders included
in this study . future studies should perform
diagnostic interviews with participants ( e.g. ,
using dsm - v criteria ) rather than relying on
self - reported measures to group participants ,
in order to better understand whether the type of
anxiety disorder ( e.g. , social anxiety , phobias
, panic disorders , and generalized anxiety )
influences cognitive performance differently in pd
. one advantage the hads questionnaire provided
over other anxiety scales was that it assessed
both anxiety and depression simultaneously and
allowed us to control for coexisting depression .
although there was a trend that the pda+ group
self - reported higher levels of depression than
the pda group , all participants included in the
study scored < 6 on the depression subscale of the
hads . controlling for depression while assessing
anxiety has been identified as a key shortcoming
in the majority of recent work . considering many
previous studies have investigated the influence
of depression on cognition in pd without
accounting for the presence of anxiety and the
inconsistent findings reported to date , we
recommend that future research should try to
disentangle the influence of anxiety versus
depression on cognitive impairments in pd .
considering the growing number of clinical trials
for treating depression , there are few if any for
the treatment of anxiety in pd . anxiety is a key
contributor to decreased quality of life in pd and
greatly requires better treatment options .
moreover , anxiety has been suggested to play a
key role in freezing of gait ( fog ) , which is
also related to attentional set - shifting [ 52 ,
53 ] . future research should examine the link
between anxiety , set - shifting , and fog , in
order to determine whether treating anxiety might
be a potential therapy for improving fog ."""

import torch
from transformers import AutoTokenizer, LongT5ForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("Stancld/longt5-tglobal-large-16384-pubmed-3k_steps")

input_ids = tokenizer(LONG_ARTICLE, return_tensors="pt").input_ids.to("cuda")

model = LongT5ForConditionalGeneration.from_pretrained("Stancld/longt5-tglobal-large-16384-pubmed-3k_steps", return_dict_in_generate=True).to("cuda")

sequences = model.generate(input_ids).sequences

summary = tokenizer.batch_decode(sequences)
```
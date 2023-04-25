---
language:
- en
tags:
- mental-health
license: apache-2.0
datasets:
- PubMed
---
# Psych-Search
Psych-Search is a work in progress to bring cutting edge NLP to mental health practitioners. The model detailed here serves as a foundation for traditional classification models as well as NLU models for a Psych-Search application. The goal of the Psych-Search Application is to use a combination of traditional text classification models to expand the scope of the MESH taxonomy with the inclusion of relevant categories for mental health pracitioners designing suicide prevention programs for adolescent communities within the United States, as well as the automatic extraction and standardization of entities such as risk factors and protective factors.

Our first expansion efforts to the MESH taxonomy include categories:
- Prevention Strategies
- Protective Factors

We are actively looking for partners on this work and would love to hear from you! Please ping us at nlp4good@gmail.com. 

## Model description

This model is an extension of [allenai/scibert_scivocab_uncased](https://huggingface.co/allenai/scibert_scivocab_uncased). Continued pretraining was done using SciBERT as the base model using abstract text only from Pyschology and Psychiatry PubMed research. Training was done on approximately 3.5 million papers for 10 epochs and evaluated on a task similar to BioASQ Task A.

## Intended uses & limitations

#### How to use

```python
from transformers import AutoTokenizer, AutoModel

mname = "nlp4good/psych-search"
tokenizer = AutoTokenizer.from_pretrained(mname)
model = AutoModel.from_pretrained(mname)
```

### Limitations and bias

This model was trained on all PubMed abstracts categorized under [Psychology and Psychiatry](https://meshb.nlm.nih.gov/treeView). As of March 1, this corresponds to approximately 3.2 million papers that contains abstract text. Of these 3.2 million papers, relevant sparse mental health categories were back translated to increase the representation of certain mental health categories.

There are several limitation with this dataset including large discrepancies in the number of papers associated with [Sexual and Gender Minorities](https://meshb.nlm.nih.gov/record/ui?ui=D000072339). The training data consisted of the following breakdown across gender groups:

Female | Male | Sexual and Gender Minorities
-------|---------|----------
1,896,301 | 1,945,279 | 4,529

Similar discrepancies are present within [Ethnic Groups](https://meshb.nlm.nih.gov/record/ui?ui=D005006) as defined within the MESH taxonomy:

| African Americans | Arabs | Asian Americans | Hispanic Americans | Indians, Central American | Indians, North American | Indians, South American | Indigenous Peoples | Mexican Americans |
|-------------------|-------|-----------------|--------------------|---------------------------|-------------------------|-------------------------|--------------------|-------------------|
| 31,027            | 2,437 | 5,612           | 18,893             | 124                       | 5,657                   | 633                     | 174                | 3,234             |

These discrepancies can have a significant impact on information retrieval systems, downstream  machine learning models, and other forms of NLP that leverage these pretrained models.
## Training data

This model was trained on all PubMed abstracts categorized under [Psychology and Psychiatry](https://meshb.nlm.nih.gov/treeView). As of March 1, this corresponds to approximately 3.2 million papers that contains abstract text. Of these 3.2 million papers, relevant sparse categories were back translated from english to french and from french to english to increase the representation of sparser mental health categories. This included backtranslating the following papers with the following categories:
- Depressive Disorder
- Risk Factors
- Mental Disorders
- Child, Preschool
- Mental Health

In aggregate, this process added 557,980 additional papers to our training data. 


## Training procedure
Continued pretraining was done on Psychology and Psychiatry PubMed papers for 10 epochs. Default parameters were used with the exception of gradient accumulation steps which was set at 4, with a per device train batch size of 32. 2 x Nvidia 3090's were used in the development of this model. 


## Evaluation results
To evaluate the effectiveness of psych-search within the mental health domain, an evaluation task was constructed by finetuning psych-search for a task similar to [BioASQ Task A](http://bioasq.org/). Here we perform large scale biomedical indexing using the MESH taxonomy associated with each paper underneath Psychology and Psychiatry. The evaluation metric is the micro F1 score across all second level descriptors within Psychology and Psychiatry. This corresponds to 38 different MESH categories used during evaluation.

bert-base-uncased   | SciBERT Scivocab Uncased | Psych-Search
-------|---------|----------
0.7348  | 0.7394 | 0.7415

## Next Steps
If you are interested in continuing to build on this work or have other ideas on how we can build on others work, please let us know! We can be reached at nlp4good@gmail.com. Our goal is to bring state of the art NLP capabilities to underserved areas of research, with mental health being our top priority.
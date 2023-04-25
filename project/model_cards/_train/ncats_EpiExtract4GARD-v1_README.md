## Model description
**EpiExtract4GARD** is a fine-tuned [BioBERT-base-cased](https://huggingface.co/dmis-lab/biobert-base-cased-v1.1) model that is ready to use for **Named Entity Recognition** of locations (LOC), epidemiologic types (EPI), and epidemiologic rates (STAT). This model was fine-tuned on [EpiSet4NER](https://huggingface.co/datasets/ncats/EpiSet4NER) for epidemiological information from rare disease abstracts. See dataset documentation for details on the weakly supervised teaching methods and dataset biases and limitations. See [EpiExtract4GARD on GitHub](https://github.com/ncats/epi4GARD/tree/master/EpiExtract4GARD#epiextract4gard) for details on the entire pipeline. 

#### How to use
You can use this model with the Hosted inference API to the right with this [test sentence](https://pubmed.ncbi.nlm.nih.gov/21659675/): "27 patients have been diagnosed with PKU in Iceland since 1947. Incidence 1972-2008 is 1/8400 living births."

See code below for use with Transformers *pipeline* for NER.:
~~~
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
model = AutoModelForTokenClassification.from_pretrained("ncats/EpiExtract4GARD")
tokenizer = AutoTokenizer.from_pretrained("ncats/EpiExtract4GARD")
NER_pipeline = pipeline('ner', model=model, tokenizer=tokenizer,aggregation_strategy='simple')

sample = "The live-birth prevalence of mucopolysaccharidoses in Estonia. Previous studies on the prevalence of mucopolysaccharidoses (MPS) in different populations have shown considerable variations. There are, however, few data with regard to the prevalence of MPSs in Fenno-Ugric populations or in north-eastern Europe, except for a report about Scandinavian countries. A retrospective epidemiological study of MPSs in Estonia was undertaken, and live-birth prevalence of MPS patients born between 1985 and 2006 was estimated. The live-birth prevalence for all MPS subtypes was found to be 4.05 per 100,000 live births, which is consistent with most other European studies. MPS II had the highest calculated incidence, with 2.16 per 100,000 live births (4.2 per 100,000 male live births), forming 53% of all diagnosed MPS cases, and was twice as high as in other studied European populations. The second most common subtype was MPS IIIA, with a live-birth prevalence of 1.62 in 100,000 live births. With 0.27 out of 100,000 live births, MPS VI had the third-highest live-birth prevalence. No cases of MPS I were diagnosed in Estonia, making the prevalence of MPS I in Estonia much lower than in other European populations. MPSs are the third most frequent inborn error of metabolism in Estonia after phenylketonuria and galactosemia."
sample2 = "Early Diagnosis of Classic Homocystinuria in Kuwait through Newborn Screening: A 6-Year Experience. Kuwait is a small Arabian Gulf country with a high rate of consanguinity and where a national newborn screening program was expanded in October 2014 to include a wide range of endocrine and metabolic disorders. A retrospective study conducted between January 2015 and December 2020 revealed a total of 304,086 newborns have been screened in Kuwait. Six newborns were diagnosed with classic homocystinuria with an incidence of 1:50,000, which is not as high as in Qatar but higher than the global incidence. Molecular testing for five of them has revealed three previously reported pathogenic variants in the <i>CBS</i> gene, c.969G>A, p.(Trp323Ter); c.982G>A, p.(Asp328Asn); and the Qatari founder variant c.1006C>T, p.(Arg336Cys). This is the first study to review the screening of newborns in Kuwait for classic homocystinuria, starting with the detection of elevated blood methionine and providing a follow-up strategy for positive results, including plasma total homocysteine and amino acid analyses. Further, we have demonstrated an increase in the specificity of the current newborn screening test for classic homocystinuria by including the methionine to phenylalanine ratio along with the elevated methionine blood levels in first-tier testing. Here, we provide evidence that the newborn screening in Kuwait has led to the early detection of classic homocystinuria cases and enabled the affected individuals to lead active and productive lives."
#Sample 1 is from: Krabbi K, Joost K, Zordania R, Talvik I, Rein R, Huijmans JG, Verheijen FV, Õunap K. The live-birth prevalence of mucopolysaccharidoses in Estonia. Genet Test Mol Biomarkers. 2012 Aug;16(8):846-9. doi: 10.1089/gtmb.2011.0307. Epub 2012 Apr 5. PMID: 22480138; PMCID: PMC3422553.
#Sample 2 is from: Alsharhan H, Ahmed AA, Ali NM, Alahmad A, Albash B, Elshafie RM, Alkanderi S, Elkazzaz UM, Cyril PX, Abdelrahman RM, Elmonairy AA, Ibrahim SM, Elfeky YME, Sadik DI, Al-Enezi SD, Salloum AM, Girish Y, Al-Ali M, Ramadan DG, Alsafi R, Al-Rushood M, Bastaki L. Early Diagnosis of Classic Homocystinuria in Kuwait through Newborn Screening: A 6-Year Experience. Int J Neonatal Screen. 2021 Aug 17;7(3):56. doi: 10.3390/ijns7030056. PMID: 34449519; PMCID: PMC8395821.

NER_pipeline(sample)
NER_pipeline(sample2)
~~~
Or if you download [*classify_abs.py*](https://github.com/ncats/epi4GARD/blob/master/EpiExtract4GARD/classify_abs.py), [*extract_abs.py*](https://github.com/ncats/epi4GARD/blob/master/EpiExtract4GARD/extract_abs.py), and [*gard-id-name-synonyms.json*](https://github.com/ncats/epi4GARD/blob/master/EpiExtract4GARD/gard-id-name-synonyms.json) from GitHub then you can test with this [*additional* code](https://github.com/ncats/epi4GARD/blob/master/EpiExtract4GARD/Case%20Study.ipynb):

~~~
import pandas as pd
import extract_abs
import classify_abs
pd.set_option('display.max_colwidth', None)

NER_pipeline = extract_abs.init_NER_pipeline()
GARD_dict, max_length = extract_abs.load_GARD_diseases()
nlp, nlpSci, nlpSci2, classify_model, classify_tokenizer = classify_abs.init_classify_model()


def search(term,num_results = 50):
    return extract_abs.search_term_extraction(term, num_results, NER_pipeline, GARD_dict, max_length,nlp, nlpSci, nlpSci2, classify_model, classify_tokenizer)
    
a = search(7058)
a

b = search('Santos Mateus Leal syndrome')
b

c = search('Fellman syndrome')
c


d = search('GARD:0009941')
d

e = search('Homocystinuria')
e
~~~

#### Limitations and bias
## Training data
It was trained on [EpiSet4NER](https://huggingface.co/datasets/ncats/EpiSet4NER). See dataset documentation for details on the weakly supervised teaching methods and dataset biases and limitations. The training dataset distinguishes between the beginning and continuation of an entity so that if there are back-to-back entities of the same type, the model can output where the second entity begins. As in the dataset, each token will be classified as one of the following classes:

Abbreviation|Description
---------|--------------
O        |Outside of a named entity
B-LOC    | Beginning of a location 
I-LOC    | Inside of a location
B-EPI    | Beginning of an epidemiologic type (e.g. "incidence", "prevalence", "occurrence") 
I-EPI    | Epidemiologic type that is not the beginning token. 
B-STAT   | Beginning of an epidemiologic rate
I-STAT   | Inside of an epidemiologic rate

### EpiSet Statistics

Beyond any limitations due to the EpiSet4NER dataset, this model is limited in numeracy due to BERT-based model's use of subword embeddings, which is crucial for epidemiologic rate identification and limits the entity-level results. Additionally, more recent weakly supervised learning techniques could be used to improve the performance of the model without improving the underlying dataset.

## Training procedure
This model was trained on a [AWS EC2 p3.2xlarge](https://aws.amazon.com/ec2/instance-types/), which utilized a single Tesla V100 GPU, with these hyperparameters:
4 epochs of training (AdamW weight decay = 0.05) with a batch size of 16. Maximum sequence length = 192. Model was fed one sentence at a time. Full config [here](https://wandb.ai/wzkariampuzha/huggingface/runs/353prhts/files/config.yaml).

## Hold-out validation  results
metric| entity-level result
-|-
f1 | 83.8
precision | 83.2
recall | 84.5

## Test results
| Dataset for Model Training | Evaluation Level |       Entity       | Precision | Recall |   F1  |
|:--------------------------:|:----------------:|:------------------:|:---------:|:------:|:-----:|
|           EpiSet           |   Entity-Level   |      Overall       |   0.556   |  0.662 | 0.605 |
|                            |                  |      Location      |   0.661   |  0.696 | 0.678 |
|                            |                  | Epidemiologic Type |   0.854   |  0.911 | 0.882 |
|                            |                  | Epidemiologic Rate |   0.143   |  0.218 | 0.173 |
|                            |    Token-Level   |      Overall       |   0.811   |  0.713 | 0.759 |
|                            |                  |      Location      |   0.949   |  0.742 | 0.833 |
|                            |                  | Epidemiologic Type |    0.9    |  0.917 | 0.908 |
|                            |                  | Epidemiologic Rate |   0.724   |  0.636 | 0.677 |

Thanks to [@William Kariampuzha](https://github.com/wzkariampuzha) at Axle Informatics/NCATS for contributing this model.
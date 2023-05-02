---
language:

- es

license: apache-2.0

tags:

- "longformer"

- "national library of spain"

- "spanish"

- "bne"

datasets:

- "bne"  

widget:
- text: "David Broncano es un presentador de La <mask>."
- text: "Gracias a los datos de la BNE se ha podido <mask> este modelo del lenguaje."
- text: "Hay base legal dentro del marco <mask> actual."

---

# Longformer base trained with data from the National Library of Spain (BNE)

## Table of contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [Intended uses and limitations](#intended-use)
- [How to use](#how-to-use)
- [Limitations and bias](#limitations-and-bias)
- [Training](#training)
- [Evaluation](#evaluation)
- [Additional information](#additional-information)
  - [Author](#author)
  - [Contact information](#contact-information)
  - [Copyright](#copyright)
  - [Licensing information](#licensing-information)
  - [Funding](#funding)
  - [Disclaimer](#disclaimer)
</details>

## Model description
The **longformer-base-4096-bne-es** is the [Longformer](https://huggingface.co/allenai/longformer-base-4096) version of the [roberta-base-bne](https://https://huggingface.co/PlanTL-GOB-ES/roberta-base-bne) masked language model for the Spanish language. The use of these models allows us to process larger contexts as input without the need of additional aggregation strategies. The model started from the **roberta-base-bne** checkpoint and was pretrained for MLM on long documents from the National Library of Spain.

The Longformer model uses a combination of sliding window (local) attention and global attention. Global attention is user-configured based on the task to allow the model to learn task-specific representations. Please refer to the original [paper](https://arxiv.org/abs/2004.05150) for more details on how to set global attention.

For more details about the corpus, the pretraining, and the evaluation, check the official [repository](https://github.com/TeMU-BSC/longformer-es).

## Intended uses and limitations
The **longformer-base-4096-bne-es** model is ready-to-use only for masked language modeling to perform the Fill Mask task (try the inference API or read the next section).

However, it is intended to be fine-tuned on non-generative downstream tasks such as Question Answering, Text Classification, or Named Entity Recognition.

## How to use

Here is how to use this model:

```python
from transformers import AutoModelForMaskedLM
from transformers import AutoTokenizer, FillMaskPipeline
from pprint import pprint
tokenizer_hf = AutoTokenizer.from_pretrained('PlanTL-GOB-ES/longformer-base-4096-bne-es')
model = AutoModelForMaskedLM.from_pretrained('PlanTL-GOB-ES/longformer-base-4096-bne-es')
model.eval()
pipeline = FillMaskPipeline(model, tokenizer_hf)
text = f"Hay base legal dentro del marco <mask> actual."
res_hf = pipeline(text)
pprint([r['token_str'] for r in res_hf])
```

## Limitations and bias

At the time of submission, no measures have been taken to estimate the bias and toxicity embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated.

## Training 

### Training corpora and preprocessing 
The [National Library of Spain (Biblioteca Nacional de España)](http://www.bne.es/en/Inicio/index.html) crawls all .es domains once a year. The training corpus consists of 59TB of WARC files from these crawls, carried out from 2009 to 2019.

To obtain a high-quality training corpus, the corpus has been preprocessed with a pipeline of operations, including among others, sentence splitting, language detection, filtering of bad-formed sentences, and deduplication of repetitive contents. During the process, document boundaries are kept. This resulted in 2TB of Spanish clean corpus. Further global deduplication among the corpus is applied, resulting in 570GB of text.

Some of the statistics of the corpus:

| Corpora | Number of documents | Number of tokens | Size (GB) |
|---------|---------------------|------------------|-----------|
| BNE     |         201,080,084 |  135,733,450,668 |     570GB |

For this Longformer, we used a small random partition of 7,2GB containing documents with less than 4096 tokens as a training split.

### Tokenization and pre-training 
The training corpus has been tokenized using a byte version of Byte-Pair Encoding (BPE) used in the original [RoBERTA](https://arxiv.org/abs/1907.11692) model with a vocabulary size of 50,262 tokens. The RoBERTa-base-bne pre-training consists of a masked language model training that follows the approach employed for the RoBERTa base. The training lasted a total of 40 hours with 8 computing nodes each one with 2 AMD MI50 GPUs of 32GB VRAM.

## Evaluation

When fine-tuned on downstream tasks, this model achieved the following performance:

| Dataset      | Metric   | [**Longformer-base**](https://huggingface.co/PlanTL-GOB-ES/longformer-base-4096-bne-es)   |
|--------------|----------|------------|
| MLDoc        | F1       |     0.9608 |
| CoNLL-NERC   | F1       |     0.8757 |
| CAPITEL-NERC | F1       |     0.8985 |
| PAWS-X       | F1       |     0.8878 |
| UD-POS       | F1       |     0.9903 |
| CAPITEL-POS  | F1       |     0.9853 |
| SQAC         | F1       |     0.8026 |
| STS          | Combined |     0.8338 |
| XNLI         | Accuracy |     0.8210 |

## Additional information

### Author
Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

### Contact information
For further information, send an email to <plantl-gob-es@bsc.es>

### Copyright
Copyright by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) (2022)

### Licensing information
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Funding
This work was funded by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) within the framework of the Plan-TL.

### Disclaimer

<details>
<summary>Click to expand</summary>

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of Artificial Intelligence.

In no event shall the owner of the models (SEDIA – State Secretariat for Digitalization and Artificial Intelligence) nor the creator (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.


Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y/u otro tipo de distorsiones indeseables.

Cuando terceros desplieguen o proporcionen sistemas y/o servicios a otras partes usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluyendo la normativa en materia de uso de inteligencia artificial.

En ningún caso el propietario de los modelos (SEDIA – Secretaría de Estado de Digitalización e Inteligencia Artificial) ni el creador (BSC – Barcelona Supercomputing Center) serán responsables de los resultados derivados del uso que hagan terceros de estos modelos.
</details>
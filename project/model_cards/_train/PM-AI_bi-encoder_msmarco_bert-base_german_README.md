---
language: de
datasets:
- germandpr-beir
pipeline_tag: sentence-similarity
tags:
- information retrieval
- ir
- documents retrieval
- passage retrieval
- beir
- benchmark
- qrel
- sts
- semantic search
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
task_categories:
- sentence-similarity
- feature-extraction
- text-retrieval
- other
task_ids:
- document-retrieval
---

# Model card for PM-AI/bi-encoder_msmarco_bert-base_german

## Model summary
This model can be used for **semantic search** and **documents retrieval** to find relevant passages based on a query.
It was trained on a machine translated **MSMARCO dataset** for _german_ with **hard negatives** and **Margin MSE loss**.
Combining these elements results in a SOTA transformer for asymmetric search.
Details are presented below.

The model can be easily used with [Sentence Transformer](https://github.com/UKPLab/sentence-transformers) library.

## Training Data
The model is based on training with samples from **[MSMARCO Passage Ranking](https://microsoft.github.io/msmarco/#ranking)** dataset.
It contains about 500.000 questions and 8.8 million passages.
The training objective is to identify the relevant passages or answers for an input question.
In terms of content, the texts deal with diverse domains.
Questions are available as sentences but also keyword-based variants can be found.
Consequently, models trained on MSMARCO can be used in a variety of domains.

The dataset was originally published in English, but has been translated into other languages by researchers with the help of machine translation.
To be more specific, **"[mMARCO: A Multilingual Version of the MS MARCO Passage Ranking Dataset](https://arxiv.org/abs/2108.13897)"** is used, which contains 13 Google based translations, German is one of them.

An existing script from the [BEIR framework](https://openreview.net/forum?id=wCu6T5xFjeJ) was used for the training - more details will follow later.
This script requires a certain structure for parsing the training data, which is not fulfilled by [unicamp-dl/mmarco](https://huggingface.co/datasets/unicamp-dl/mmarco).
UKP Lab (TU Darmstadt) created an appropriately [processed mmarco](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/) version, that cannot be used, because it contains outdated texts from an older version of unicamp-dl/mmarco (it us using a MarianNMT-based translation instead of Google)
Since the textual quality of the older version is poorer, a workaround is necessary in order to be able to use the training data translated by Google.

BEIR requires the following structure for the training data when using the `GenericDataLoader`:
- `corpus.jsonl`: contains one JSON string per line with `_id`, `title` and `text`. 
  - Example: `{"_id": "1234", "title": "", "text": "some text"}`
- `queries.jsonl` an `_id` and a `text` is required per JSON string per line.
  - Example: `{"_id": "5678", "text": "a question?"}`
- `qrels/dev.tsv`: represents the relation between question (`query-id`) and correct answer (`corpus-id`). The `score` column is mandatory, but always 1
  - Example:  `1234	5678	1`
- `qrels/train.tsv`: Structure is identical to `dev.tsv`

Note: Instead of using `GenericDataLoader`, it is also possible to use `HFDataLoader`.
In this case, a [Huggingface dataset](https://huggingface.co/docs/datasets/index) is loaded directly, i.e. no individual files have to be created manually.
Nevertheless, this approach also requires a specific structure.
Two dataset repositories are needed: one for `queries` and `corpus` and another for `qrels`. 
In addition, specific subset names must be defined.
Overall, the effort is more extensive, because new datasets have to be created (and uploaded to Huggingface Datasets).
The variant presented here uses existing datasets that are only minimally adapted and thus offer maximum compatibility. 

The custom-made script [mmarco_beir.py](https://huggingface.co/PM-AI/bi-encoder_msmarco_bert-base_german/blob/main/mmarco_beir.py) contains all necessary adaptations for BEIR compatibility.
It can be applied to all 14 languages of the mmarco dataset so that corresponding models can be trained comfortably.

```python
# mmarco_beir.py

import json
import os
import urllib.request

import datasets

# see https://huggingface.co/datasets/unicamp-dl/mmarco for supported languages
LANGUAGE = "german"
# target directory containin BEIR (https://github.com/beir-cellar/beir) compatible files
OUT_DIR = f"mmarco-google/{LANGUAGE}/"

os.makedirs(OUT_DIR, exist_ok=True)

# download google based collection/corpus translation of msmarco and write corpus.jsonl for BEIR compatibility
mmarco_ds = datasets.load_dataset("unicamp-dl/mmarco", f"collection-{LANGUAGE}")
with open(os.path.join(OUT_DIR, "corpus.jsonl"), "w", encoding="utf-8") as out_file:
    for entry in mmarco_ds["collection"]:
        entry = {"_id": str(entry["id"]), "title": "", "text": entry["text"]}
        out_file.write(f'{json.dumps(entry, ensure_ascii=False)}\n')

# # download google based queries translation of msmarco and write queries.jsonl for BEIR compatibility
mmarco_ds = datasets.load_dataset("unicamp-dl/mmarco", f"queries-{LANGUAGE}")
mmarco_ds = datasets.concatenate_datasets([mmarco_ds["train"], mmarco_ds["dev.full"]])
with open(os.path.join(OUT_DIR, "queries.jsonl"), "w", encoding="utf-8") as out_file:
    for entry in mmarco_ds:
        entry = {"_id": str(entry["id"]), "text": entry["text"]}
        out_file.write(f'{json.dumps(entry, ensure_ascii=False)}\n')

QRELS_DIR = os.path.abspath(os.path.join(OUT_DIR, "../qrels/"))
os.makedirs(QRELS_DIR, exist_ok=True)

# download qrels from URL instead of HF dataset
# note: qrels are language independent
for link in ["https://huggingface.co/datasets/BeIR/msmarco-qrels/resolve/main/dev.tsv",
             "https://huggingface.co/datasets/BeIR/msmarco-qrels/resolve/main/train.tsv"]:
    urllib.request.urlretrieve(link, os.path.join(QRELS_DIR, os.path.basename(link)))
```

## Training
The training is run using the **[BEIR Benchmark Framework](https://github.com/beir-cellar/beir)**.
It is mainly used to create benchmarks for information retrieval.
In addition, there are some training scripts that generate SOTA models.

The approach of training the MSMARCO dataset with the Margin MSE loss method is particularly promising.
For this purpose [train_msmarco_v3_margin_MSE.py](https://github.com/beir-cellar/beir/blob/main/examples/retrieval/training/train_msmarco_v3_margin_MSE.py) is provided by BEIR:
The unique feature here are the so-called "hard negatives", which were created by a special approach:

> We use the MSMARCO Hard Negatives File (Provided by Nils Reimers): https://sbert.net/datasets/msmarco-hard-negatives.jsonl.gz
> Negative passage are hard negative examples, that were mined using different dense embedding, cross-encoder methods and lexical search methods.
> Contains upto 50 negatives for each of the four retrieval systems: [bm25, msmarco-distilbert-base-tas-b, msmarco-MiniLM-L-6-v3, msmarco-distilbert-base-v3]
> Each positive and negative passage comes with a score from a Cross-Encoder (msmarco-MiniLM-L-6-v3). This allows denoising, i.e. removing false negative
> passages that are actually relevant for the query.

[Source](https://github.com/beir-cellar/beir/blob/main/examples/retrieval/training/train_msmarco_v3_margin_MSE.py])

> MarginMSELoss is based on the paper of Hofstätter et al. As for MultipleNegativesRankingLoss, we have triplets: (query, passage1, passage2). In contrast to MultipleNegativesRankingLoss, passage1 and passage2 do not have to be strictly positive/negative, both can be relevant or not relevant for a given query.
> We then compute the Cross-Encoder score for (query, passage1) and (query, passage2). We provide scores for 160 million such pairs in our msmarco-hard-negatives dataset. We then compute the distance: CE_distance = CEScore(query, passage1) - CEScore(query, passage2)
> For our bi-encoder training, we encode query, passage1, and passage2 into vector spaces and then measure the dot-product between (query, passage1) and (query, passage2). Again, we measure the distance: BE_distance = DotScore(query, passage1) - DotScore(query, passage2)
> We then want to ensure that the distance predicted by the bi-encoder is close to the distance predicted by the cross-encoder, i.e., we optimize the mean-squared error (MSE) between CE_distance and BE_distance.
> An advantage of MarginMSELoss compared to MultipleNegativesRankingLoss is that we don’t require a positive and negative passage. As mentioned before, MS MARCO is redundant, and many passages contain the same or similar content. With MarginMSELoss, we can train on two relevant passages without issues: In that case, the CE_distance will be smaller and we expect that our bi-encoder also puts both passages closer in the vector space.
> And disadvantage of MarginMSELoss is the slower training time: We need way more epochs to get good results. In MultipleNegativesRankingLoss, with a batch size of 64, we compare one query against 128 passages. With MarginMSELoss, we compare a query only against two passages.
>
> [Source](https://github.com/UKPLab/sentence-transformers/blob/master/examples/training/ms_marco/README.md)

Since the MSMarco dataset has been translated into different languages and the "hard negatives" is only containing the IDs of queries and texts,
the approach just presented can also be applied to a language other than English.
The previous section already explained how to create the necessary training data for German.
The same can be done comfortably for all of the 14 translations.

Actually, starting the training process requires one final change to the training script beforehand.
The following code shows how the dataset path is resolved and passed correctly to the `GenericDataLoader`:

```python
import os
from beir.datasets.data_loader import GenericDataLoader

data_path = "./mmarco-google/german"
qrels_path = os.path.abspath(os.path.join(data_path, "../qrels"))
corpus, queries, _ = GenericDataLoader(data_folder=data_path, qrels_folder=qrels_path).load(split="train")
```

### Parameterization of training
- **Script:** [train_msmarco_v3_margin_MSE.py](https://github.com/beir-cellar/beir/blob/main/examples/retrieval/training/train_msmarco_v3_margin_MSE.py)
- **Dataset:** mmarco (compatibility established using [mmarco_beir.py](https://huggingface.co/PM-AI/bi-encoder_msmarco_bert-base_german/blob/main/mmarco_beir.py)), train split
- **GPU:** NVIDIA A40 (Driver Version: 515.48.07; CUDA Version: 11.7)
- **Batch Size:** 75
- **Max. Sequence Length:** 350
- **Base Model**: [deepset/gbert-base](https://huggingface.co/deepset/gbert-base)
- **Loss function**: Margin MSE
- **Epochs**: 10
- **Evaluation Steps**: 10000
- **Warmup Steps**: 1000

## Evaluation <a name="evaluation"></a>
The evaluation is based on **[germanDPR](https://arxiv.org/abs/2104.12741)**.
The dataset developed by [Deepset.ai](deepset.ai) consists of question-answer pairs, which are supplemented by three "hard negatives" per question.
This makes it an ideal basis for benchmarking.
Publicly available is the dataset as **[deepset/germanDPR](https://huggingface.co/datasets/deepset/germandpr)**, which does not support BEIR by default. 
Consequently, this dataset was also reworked manually.
In addition, duplicate text elements were removed and minimal text adjustments were made.
The details of this process can be found in **[PM-AI/germandpr-beir](https://huggingface.co/datasets/PM-AI/germandpr-beir)**.

The BEIR-compatible germanDPR dataset consists of **9275 questions** with **23993 text passages** for the **train split**.
In order to have enough text passages for information retrieval, we use the train split and not the test split.
The following table shows the evaluation results for different approaches and models:

**model**|**NDCG@1**|**NDCG@10**|**NDCG@100**|**comment**
:-----:|:-----:|:-----:|:-----:|:-----:
bi-encoder_msmarco_bert-base_german (new) | 0.5300 <br /> 🏆 | 0.7196 <br /> 🏆 | 0.7360 <br /> 🏆 | "OUR model"
[deepset/gbert-base-germandpr-X_encoder](https://huggingface.co/deepset/gbert-base-germandpr-ctx_encoder) | 0.4828 | 0.6970 | 0.7147 | "has two encoder models (one for queries and one for corpus), is SOTA approach"
[distiluse-base-multilingual-cased-v1](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1) | 0.4561 | 0.6347 | 0.6613 | "trained on 15 languages"
[paraphrase-multilingual-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2) | 0.4511 | 0.6328 | 0.6592 | "trained on huge corpus, support for 50+ languages"
[distiluse-base-multilingual-cased-v2](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v2) | 0.4350 | 0.6103 | 0.6411 | "trained on 50+ languages"
[sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) | 0.4168 | 0.5931 | 0.6237 | "trained on large corpus, support for 50+ languages"
[svalabs/bi-electra-ms-marco-german-uncased](svalabs/bi-electra-ms-marco-german-uncased) | 0.3818 | 0.5663 | 0.5986 | "most similar to OUR model"
[BM25](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-similarity.html#bm25) | 0.3196 | 0.5377 | 0.5740 | "lexical approach"

**❗It is crucial to understand that the comparisons are also made with models based on other transformer approaches❗**

A direct comparison based on the same approach can be made with [svalabs/bi-electra-ms-marco-german-uncased](svalabs/bi-electra-ms-marco-german-uncased). 
In this case, the model presented here outperforms its predecessor by up to 14 percentage points.

Comparing with [deepset/gbert-base-germandpr-X_encoder](https://huggingface.co/deepset/gbert-base-germandpr-ctx_encoder) is theoretically a little unfair since deepset's approach is based on two models at the same time!
Queries and passages are encoded separately which leads to a better, more superior contextualization. 
Still, our newly trained model is outperforming the other approach by around two percentage points.
In addition, using two models at the same time also increases demands on memory and CPU power which causes higher costs.
This makes the approach presented here even more valuable.

Note:
- Texts used for evaluation are sometimes very long. All models, except for BM25 approach, truncate the incoming texts some point. This can decrease performance.
- Evaluation of deepset's gbert-base-germandpr model might give an incorrect impression. The model was originally trained on the data we used for evaluation (not 1:1 but almost).

## Acknowledgment

This work is a collaboration between [Technical University of Applied Sciences Wildau (TH Wildau)](https://en.th-wildau.de/) and [sense.ai.tion GmbH](https://senseaition.com/).
You can contact us via:
* [Philipp Müller (M.Eng.)](https://www.linkedin.com/in/herrphilipps); Author
* [Prof. Dr. Janett Mohnke](mailto:icampus@th-wildau.de); TH Wildau
* [Dr. Matthias Boldt, Jörg Oehmichen](mailto:info@senseaition.com); sense.AI.tion GmbH 

This work was funded by the European Regional Development Fund (EFRE) and the State of Brandenburg. Project/Vorhaben: "ProFIT: Natürlichsprachliche Dialogassistenten in der Pflege".

<div style="display:flex">
     <div style="padding-left:20px;">
          <a href="https://efre.brandenburg.de/efre/de/"><img src="https://huggingface.co/datasets/PM-AI/germandpr-beir/resolve/main/res/EFRE-Logo_rechts_oweb_en_rgb.jpeg" alt="Logo of European Regional Development Fund (EFRE)" width="200"/></a>
     </div>
     <div style="padding-left:20px;">
          <a href="https://www.senseaition.com"><img src="https://senseaition.com/wp-content/uploads/thegem-logos/logo_c847aaa8f42141c4055d4a8665eb208d_3x.png" alt="Logo of senseaition GmbH" width="200"/></a>
     </div>
     <div style="padding-left:20px;">
          <a href="https://www.th-wildau.de"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/TH_Wildau_Logo.png/640px-TH_Wildau_Logo.png" alt="Logo of TH Wildau" width="180"/></a>
     </div>
</div>
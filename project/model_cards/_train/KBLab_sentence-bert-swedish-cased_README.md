---
pipeline_tag: sentence-similarity
lang:
  - sv
tags:
  - sentence-transformers
  - feature-extraction
  - sentence-similarity
  - transformers
widget:
- source_sentence: "Mannen åt mat."
  sentences:
    - "Han förtärde en närande och nyttig måltid."
    - "Det var ett sunkigt hak med ganska gott käk."
    - "Han inmundigade middagen tillsammans med ett glas rödvin."
    - "Potatischips är jättegoda."
    - "Tryck på knappen för att få tala med kundsupporten."
  example_title: "Mat"
- source_sentence: "Kan jag deklarera digitalt från utlandet?"
  sentences:
    - "Du som befinner dig i utlandet kan deklarera digitalt på flera olika sätt."
    - "Du som har kvarskatt att betala ska göra en inbetalning till ditt skattekonto."
    - "Efter att du har deklarerat går vi igenom uppgifterna i din deklaration och räknar ut din skatt."
    - "I din deklaration som du får från oss har vi räknat ut vad du ska betala eller få tillbaka."
    - "Tryck på knappen för att få tala med kundsupporten."
  example_title: "Skatteverket FAQ"
- source_sentence: "Hon kunde göra bakåtvolter."
  sentences:
    - "Hon var atletisk."
    - "Hon var bra på gymnastik."
    - "Hon var inte atletisk."
    - "Hon var oförmögen att flippa baklänges."
  example_title: "Gymnastik"
---

# KBLab/sentence-bert-swedish-cased

This is a [sentence-transformers](https://www.SBERT.net) model: It maps Swedish sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search. This model is a bilingual Swedish-English model trained according to instructions in the paper [Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation](https://arxiv.org/pdf/2004.09813.pdf) and the [documentation](https://www.sbert.net/examples/training/multilingual/README.html) accompanying its companion python package. We have used the strongest available pretrained English Bi-Encoder ([all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)) as a teacher model, and the pretrained Swedish [KB-BERT](https://huggingface.co/KB/bert-base-swedish-cased) as the student model. 

A more detailed description of the model can be found in an article we published on the KBLab blog [here](https://kb-labb.github.io/posts/2021-08-23-a-swedish-sentence-transformer/) and for the updated model [here](https://kb-labb.github.io/posts/2023-01-16-sentence-transformer-20/). 

**Update**: We have released updated versions of the model since the initial release. The original model described in the blog post is **v1.0**. The current version is **v2.0**. The newer versions are trained on longer paragraphs, and have a longer max sequence length. **v2.0** is trained with a stronger teacher model and is the current default.

| Model version | Teacher Model | Max Sequence Length |
|---------------|---------|----------|
| v1.0          | [paraphrase-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-mpnet-base-v2)  | 256   |
| v1.1          | [paraphrase-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-mpnet-base-v2)  | 384   |
| v2.0          | [all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)  | 384 |

<!--- Describe your model here -->

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["Det här är en exempelmening", "Varje exempel blir konverterad"]

model = SentenceTransformer('KBLab/sentence-bert-swedish-cased')
embeddings = model.encode(sentences)
print(embeddings)
```

### Loading an older model version (Sentence-Transformers)

Currently, the easiest way to load an older model version is to clone the model repository and load it from disk. For example, to clone the **v1.0** model:

```bash
git clone --depth 1 --branch v1.0 https://huggingface.co/KBLab/sentence-bert-swedish-cased
```

Then you can load the model by pointing to the local folder where you cloned the model:

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("path_to_model_folder/sentence-bert-swedish-cased")
```


## Usage (HuggingFace Transformers)
Without [sentence-transformers](https://www.SBERT.net), you can use the model like this: First, you pass your input through the transformer model, then you have to apply the right pooling-operation on-top of the contextualized word embeddings.

```python
from transformers import AutoTokenizer, AutoModel
import torch


#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
sentences = ['Det här är en exempelmening', 'Varje exempel blir konverterad']

# Load model from HuggingFace Hub
# To load an older version, e.g. v1.0, add the argument revision="v1.0" 
tokenizer = AutoTokenizer.from_pretrained('KBLab/sentence-bert-swedish-cased')
model = AutoModel.from_pretrained('KBLab/sentence-bert-swedish-cased')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, max pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

print("Sentence embeddings:")
print(sentence_embeddings)
```

### Loading an older model (Hugginfface Transformers)

To load an older model specify the version tag with the `revision` arg. For example, to load the **v1.0** model, use the following code: 

```python
AutoTokenizer.from_pretrained('KBLab/sentence-bert-swedish-cased', revision="v1.0")
AutoModel.from_pretrained('KBLab/sentence-bert-swedish-cased', revision="v1.0")
```

## Evaluation Results

<!--- Describe how your model was evaluated -->

The model was evaluated on [SweParaphrase v1.0](https://spraakbanken.gu.se/en/resources/sweparaphrase) and **SweParaphrase v2.0**. This test set is part of [SuperLim](https://spraakbanken.gu.se/en/resources/superlim) -- a Swedish evaluation suite for natural langage understanding tasks.  We calculated Pearson and Spearman correlation between predicted model similarity scores and the human similarity score labels. Results from **SweParaphrase v1.0** are displayed below. 

| Model version | Pearson | Spearman |
|---------------|---------|----------|
| v1.0          | 0.9183  | 0.9114   |
| v1.1          | 0.9183  | 0.9114   |
| v2.0          | **0.9283**  | **0.9130**   |

The following code snippet can be used to reproduce the above results:

```python
from sentence_transformers import SentenceTransformer
import pandas as pd

df = pd.read_csv(
    "sweparaphrase-dev-165.csv",
    sep="\t",
    header=None,
    names=[
        "original_id",
        "source",
        "type",
        "sentence_swe1",
        "sentence_swe2",
        "score",
        "sentence1",
        "sentence2",
    ],
)

model = SentenceTransformer("KBLab/sentence-bert-swedish-cased")

sentences1 = df["sentence_swe1"].tolist()
sentences2 = df["sentence_swe2"].tolist()

# Compute embedding for both lists
embeddings1 = model.encode(sentences1, convert_to_tensor=True)
embeddings2 = model.encode(sentences2, convert_to_tensor=True)

# Compute cosine similarity after normalizing
embeddings1 /= embeddings1.norm(dim=-1, keepdim=True)
embeddings2 /= embeddings2.norm(dim=-1, keepdim=True)

cosine_scores = embeddings1 @ embeddings2.t()
sentence_pair_scores = cosine_scores.diag()

df["model_score"] = sentence_pair_scores.cpu().tolist()
print(df[["score", "model_score"]].corr(method="spearman"))
print(df[["score", "model_score"]].corr(method="pearson"))
```

### Sweparaphrase v2.0

In general, **v1.1** correlates the most with human assessment of text similarity on SweParaphrase v2.0. Below, we present zero-shot evaluation results on all data splits. They display the model's performance out of the box, without any fine-tuning.

| Model version | Data split | Pearson    | Spearman   |
|---------------|------------|------------|------------|
| v1.0          | train      | 0.8355     | 0.8256     |
| v1.1          | train      | **0.8383** | **0.8302** |
| v2.0          | train      | 0.8209     | 0.8059     |
| v1.0          | dev        | 0.8682     | 0.8774     |
| v1.1          | dev        | **0.8739** | **0.8833** |
| v2.0          | dev        | 0.8638     | 0.8668     |
| v1.0          | test       | 0.8356     | 0.8476     |
| v1.1          | test       | **0.8393** | **0.8550** |
| v2.0          | test       | 0.8232     | 0.8213     |

### SweFAQ v2.0

When it comes to retrieval tasks, **v2.0** performs the best by quite a substantial margin. It is better at matching the correct answer to a question compared to v1.1 and v1.0.

| Model version | Data split | Accuracy   |
|---------------|------------|------------|
| v1.0          | train      | 0.5262     |
| v1.1          | train      | 0.6236     |
| v2.0          | train      | **0.7106** |
| v1.0          | dev        | 0.4636     |
| v1.1          | dev        | 0.5818     |
| v2.0          | dev        | **0.6727** |
| v1.0          | test       | 0.4495     |
| v1.1          | test       | 0.5229     |
| v2.0          | test       | **0.5871** |


Examples how to evaluate the models on some of the test sets of the SuperLim suites can be found on the following links: [evaluate_faq.py](https://github.com/kb-labb/swedish-sbert/blob/main/evaluate_faq.py) (Swedish FAQ), [evaluate_swesat.py](https://github.com/kb-labb/swedish-sbert/blob/main/evaluate_swesat.py) (SweSAT synonyms), [evaluate_supersim.py](https://github.com/kb-labb/swedish-sbert/blob/main/evaluate_supersim.py) (SuperSim).

## Training

An article with more details on data and v1.0 of the model can be found on the [KBLab blog](https://kb-labb.github.io/posts/2021-08-23-a-swedish-sentence-transformer/). 

Around 14.6 million sentences from English-Swedish parallel corpuses were used to train the model. Data was sourced from the [Open Parallel Corpus](https://opus.nlpl.eu/) (OPUS) and downloaded via the python package [opustools](https://pypi.org/project/opustools/). Datasets used were: JW300, Europarl, DGT-TM, EMEA, ELITR-ECA, TED2020, Tatoeba and OpenSubtitles. 

The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 180513 with parameters:
```
{'batch_size': 64, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.MSELoss.MSELoss` 

Parameters of the fit()-Method:
```
{
    "epochs": 2,
    "evaluation_steps": 1000,
    "evaluator": "sentence_transformers.evaluation.SequentialEvaluator.SequentialEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'torch.optim.adamw.AdamW'>",
    "optimizer_params": {
        "eps": 1e-06,
        "lr": 8e-06
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 5000,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 384, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->
This model was trained by KBLab, a data lab at the National Library of Sweden. 

You can cite the article on our blog: https://kb-labb.github.io/posts/2021-08-23-a-swedish-sentence-transformer/ .

```
@misc{rekathati2021introducing,  
  author = {Rekathati, Faton},  
  title = {The KBLab Blog: Introducing a Swedish Sentence Transformer},  
  url = {https://kb-labb.github.io/posts/2021-08-23-a-swedish-sentence-transformer/},  
  year = {2021}  
}
```

## Acknowledgements

We gratefully acknowledge the HPC RIVR consortium ([www.hpc-rivr.si](https://www.hpc-rivr.si/)) and EuroHPC JU ([eurohpc-ju.europa.eu/](https://eurohpc-ju.europa.eu/)) for funding this research by providing computing resources of the HPC system Vega at the Institute of Information Science ([www.izum.si](https://www.izum.si/)).

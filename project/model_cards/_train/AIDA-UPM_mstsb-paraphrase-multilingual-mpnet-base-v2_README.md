---
pipeline_tag: sentence-similarity
language: "multilingual"
tags:
- feature-extraction
- sentence-similarity
- transformers
- multilingual
---

# mstsb-paraphrase-multilingual-mpnet-base-v2

This is a fine-tuned version of `paraphrase-multilingual-mpnet-base-v2` from [sentence-transformers](https://www.SBERT.net) model with [Semantic Textual Similarity Benchmark](http://ixa2.si.ehu.eus/stswiki/index.php/Main_Page) extended to 15 languages: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering, semantic search and measuring the similarity between two sentences.

<!--- Describe your model here -->
This model is fine-tuned version of `paraphrase-multilingual-mpnet-base-v2` for semantic textual similarity with multilingual data. The dataset used for this fine-tuning is STSb extended to 15 languages with Google Translator. For mantaining data quality the sentence pairs with a confidence value below 0.7 were dropped. The extended dataset is available at [GitHub](https://github.com/Huertas97/Multilingual-STSB). The languages included in the extended version are: ar, cs, de, en, es, fr, hi, it, ja, nl, pl, pt, ru, tr, zh-CN, zh-TW. The pooling operation used to condense the word embeddings into a sentence embedding is mean pooling (more info below). 

<!-- ## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
# It support several languages
sentences = ["This is an example sentence", "Esta es otra frase de ejemplo", "最後の例文"]

# The pooling technique is automatically detected (mean pooling)
model = SentenceTransformer('mstsb-paraphrase-multilingual-mpnet-base-v2')
embeddings = model.encode(sentences)
print(embeddings)
``` -->



## Usage (HuggingFace Transformers)
Without [sentence-transformers](https://www.SBERT.net), you can use the model like this: First, you pass your input through the transformer model, then you have to apply the right pooling-operation on-top of the contextualized word embeddings.

```python
from transformers import AutoTokenizer, AutoModel
import torch

# We should define the proper pooling function: Mean pooling
# Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
sentences = ["This is an example sentence", "Esta es otra frase de ejemplo", "最後の例文"]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('AIDA-UPM/mstsb-paraphrase-multilingual-mpnet-base-v2')
model = AutoModel.from_pretrained('AIDA-UPM/mstsb-paraphrase-multilingual-mpnet-base-v2')

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



## Evaluation Results

<!--- Describe how your model was evaluated -->
Check the test results in the Semantic Textual Similarity Tasks. The 15 languages available at the [Multilingual STSB](https://github.com/Huertas97/Multilingual-STSB) have been combined into monolingual and cross-lingual tasks, giving a total of 31 tasks. Monolingual tasks have both sentences from the same language source (e.g., Ar-Ar, Es-Es), while cross-lingual tasks have two sentences, each in a different language being one of them English (e.g., en-ar, en-es). 


Here we compare the average multilingual semantic textual similairty capabilities between the  `paraphrase-multilingual-mpnet-base-v2` based model and the `mstsb-paraphrase-multilingual-mpnet-base-v2` fine-tuned model across the 31 tasks. It is worth noting that both models are multilingual, but the second model is adjusted with multilingual data for semantic similarity. The average of correlation coefficients is computed by transforming each correlation coefficient to a Fisher's z value, averaging them, and then back-transforming to a correlation coefficient.


| Model                                       | Average Spearman Cosine Test |
|:---------------------------------------------:|:------------------------------:|
| mstsb-paraphrase-multilingual-mpnet-base-v2 | 0.835890                     |
| paraphrase-multilingual-mpnet-base-v2       | 0.818896                     |

<br>

The following tables breakdown the performance of `mstsb-paraphrase-multilingual-mpnet-base-v2` according to the different tasks. For the sake of readability tasks have been splitted into monolingual and cross-lingual tasks. 

| Monolingual Task | Pearson Cosine test | Spearman Cosine  test |
|:------------------:|:---------------------:|:-----------------------:|
| en;en            | 0.868048310692506   | 0.8740170943535747    |
| ar;ar            | 0.8267139454193487  | 0.8284459741532022    |
| cs;cs            | 0.8466821720942157  | 0.8485417688803879    |
| de;de            | 0.8517285961812183  | 0.8557680051557893    |
| es;es            | 0.8519185309064691  | 0.8552243211580456    |
| fr;fr            | 0.8430951067985064  | 0.8466614534379704    |
| hi;hi            | 0.8178258630578092  | 0.8176462079184331    |
| it;it            | 0.8475909574305637  | 0.8494216064459076    |
| ja;ja            | 0.8435588859386477  | 0.8456031494178619    |
| nl;nl            | 0.8486765104527032  | 0.8520856765262531    |
| pl;pl            | 0.8407840177883407  | 0.8443070467300299    |
| pt;pt            | 0.8534880178249296  | 0.8578544068829622    |
| ru;ru            | 0.8390897585455678  | 0.8423041443534423    |
| tr;tr            | 0.8382125451820572  | 0.8421587450058385    |
| zh-CN;zh-CN      | 0.826233678946644   | 0.8248515460782744    |
| zh-TW;zh-TW      | 0.8242683809675422  | 0.8235506799952028    |

<br>

| Cross-lingual Task | Pearson Cosine test | Spearman Cosine  test |
|:--------------------:|:---------------------:|:-----------------------:|
| en;ar              | 0.7990830340462535  | 0.7956792016468148    |
| en;cs              | 0.8381274879061265  | 0.8388713450024455    |
| en;de              | 0.8414439600928739  | 0.8441971698649943    |
| en;es              | 0.8442337511356952  | 0.8445035292903559    |
| en;fr              | 0.8378437644605063  | 0.8387903367907733    |
| en;hi              | 0.7951955086055527  | 0.7905052217683244    |
| en;it              | 0.8415686372978766  | 0.8419480899107785    |
| en;ja              | 0.8094306665283388  | 0.8032512280936449    |
| en;nl              | 0.8389526140129767  | 0.8409310421803277    |
| en;pl              | 0.8261309163979578  | 0.825976253023656     |
| en;pt              | 0.8475546209070765  | 0.8506606391790897    |
| en;ru              | 0.8248514914263723  | 0.8224871183202255    |
| en;tr              | 0.8191803661207868  | 0.8194200775744044    |
| en;zh-CN           | 0.8147678083378249  | 0.8102089470690433    |
| en;zh-TW           | 0.8107272160374955  | 0.8056129680510944    |


## Training
The model was trained with the parameters:

**DataLoader**:

`torch.utils.data.dataloader.DataLoader` of length 687 with parameters:
```
{'batch_size': 132, 'sampler': 'torch.utils.data.sampler.RandomSampler', 'batch_sampler': 'torch.utils.data.sampler.BatchSampler'}
```

**Loss**:

`sentence_transformers.losses.CosineSimilarityLoss.CosineSimilarityLoss` 

Parameters of the fit()-Method:
```
{
    "callback": null,
    "epochs": 2,
    "evaluation_steps": 1000,
    "evaluator": "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator.EmbeddingSimilarityEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'transformers.optimization.AdamW'>",
    "optimizer_params": {
        "lr": 2e-05
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 140,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False}) with Transformer model: XLMRobertaModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->
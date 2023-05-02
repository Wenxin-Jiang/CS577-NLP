---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
language:
- es
datasets:
- hackathon-pln-es/nli-es
widget:
- text: "A ver si nos tenemos que poner todos en huelga hasta cobrar lo que queramos."
- text: "La huelga es el método de lucha más eficaz para conseguir mejoras en el salario."
- text: "Tendremos que optar por hacer una huelga para cobrar lo que queremos."
- text: "Queda descartada la huelga aunque no cobremos lo que queramos."
---

# bertin-roberta-base-finetuning-esnli

This is a [sentence-transformers](https://www.SBERT.net) model trained on a
collection of NLI tasks for Spanish. It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search.

Based around the siamese networks approach from [this paper](https://arxiv.org/pdf/1908.10084.pdf).
<!--- Describe your model here -->

You can see a demo for this model [here](https://huggingface.co/spaces/hackathon-pln-es/Sentence-Embedding-Bertin).

You can find our other model, **paraphrase-spanish-distilroberta** [here](https://huggingface.co/hackathon-pln-es/paraphrase-spanish-distilroberta) and its demo [here](https://huggingface.co/spaces/hackathon-pln-es/Paraphrase-Bertin).

## Usage (Sentence-Transformers)

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["Este es un ejemplo", "Cada oración es transformada"]

model = SentenceTransformer('hackathon-pln-es/bertin-roberta-base-finetuning-esnli')
embeddings = model.encode(sentences)
print(embeddings)
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
sentences = ['This is an example sentence', 'Each sentence is converted']

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('hackathon-pln-es/bertin-roberta-base-finetuning-esnli')
model = AutoModel.from_pretrained('hackathon-pln-es/bertin-roberta-base-finetuning-esnli')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, mean pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

print("Sentence embeddings:")
print(sentence_embeddings)
```


## Evaluation Results

<!--- Describe how your model was evaluated -->
Our model was evaluated on the task of Semantic Textual Similarity using the [SemEval-2015 Task](https://alt.qcri.org/semeval2015/task2/) for [Spanish](http://alt.qcri.org/semeval2015/task2/data/uploads/sts2015-es-test.zip). We measure 

|                    | [BETO STS](https://huggingface.co/espejelomar/sentece-embeddings-BETO) | BERTIN STS (this model) | Relative improvement |
|-------------------:|---------:|-----------:|---------------------:|
|   cosine_pearson   | 0.609803 | 0.683188   | +12.03               |
|   cosine_spearman  | 0.528776 | 0.615916   | +16.48               |
|  euclidean_pearson | 0.590613 | 0.672601   | +13.88               |
| euclidean_spearman | 0.526529 | 0.611539   | +16.15               |
|  manhattan_pearson | 0.589108 | 0.672040   | +14.08               |
| manhattan_spearman | 0.525910 | 0.610517   | +16.09               |
|     dot_pearson    | 0.544078 | 0.600517   | +10.37               |
|    dot_spearman    | 0.460427 | 0.521260   | +13.21               |


## Training
The model was trained with the parameters:

**Dataset**

We used a collection of datasets of Natural Language Inference as training data:
 - [ESXNLI](https://raw.githubusercontent.com/artetxem/esxnli/master/esxnli.tsv), only the part in spanish
 - [SNLI](https://nlp.stanford.edu/projects/snli/), automatically translated
 - [MultiNLI](https://cims.nyu.edu/~sbowman/multinli/), automatically translated

The whole dataset used is available [here](https://huggingface.co/datasets/hackathon-pln-es/nli-es).

Here we leave the trick we used to increase the amount of data for training here:
```
  for row in reader:
    if row['language'] == 'es':
      
      sent1 = row['sentence1'].strip()
      sent2 = row['sentence2'].strip()
    
      add_to_samples(sent1, sent2, row['gold_label'])
      add_to_samples(sent2, sent1, row['gold_label'])  #Also add the opposite
```

**DataLoader**:

`sentence_transformers.datasets.NoDuplicatesDataLoader.NoDuplicatesDataLoader`
of length 1818 with parameters:
```
{'batch_size': 64}
```

**Loss**:

`sentence_transformers.losses.MultipleNegativesRankingLoss.MultipleNegativesRankingLoss` with parameters:
  ```
  {'scale': 20.0, 'similarity_fct': 'cos_sim'}
  ```

Parameters of the fit()-Method:
```
{
    "epochs": 10,
    "evaluation_steps": 0,
    "evaluator": "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator.EmbeddingSimilarityEvaluator",
    "max_grad_norm": 1,
    "optimizer_class": "<class 'transformers.optimization.AdamW'>",
    "optimizer_params": {
        "lr": 2e-05
    },
    "scheduler": "WarmupLinear",
    "steps_per_epoch": null,
    "warmup_steps": 909,
    "weight_decay": 0.01
}
```


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 514, 'do_lower_case': False}) with Transformer model: RobertaModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
)
```

## Authors

[Anibal Pérez](https://huggingface.co/Anarpego),

[Emilio Tomás Ariza](https://huggingface.co/medardodt),

[Lautaro Gesuelli](https://huggingface.co/Lgesuelli) y

[Mauricio Mazuecos](https://huggingface.co/mmazuecos).
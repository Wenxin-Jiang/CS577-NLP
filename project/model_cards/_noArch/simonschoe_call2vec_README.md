---
language:
- en
library_name: fasttext
pipeline_tag: text-classification
tags:
- text
- semantic-similarity
- earnings-call-transcripts
- word2vec
- fasttext
widget:
- text: "transformation"
  example_title: "transformation"
- text: "sustainability"
  example_title: "sustainability"
- text: "turnaround"
  example_title: "turnaround"
- text: "disruption"
  example_title: "disruption"
---

# EarningsCall2Vec

**EarningsCall2Vec** is a [`fastText`](https://fasttext.cc/) word embedding model that was trained via [`Gensim`](https://radimrehurek.com/gensim/). It maps each token in the vocabulary to a dense, 300-dimensional vector space, designed for performing **semantic search**. More details about the training procedure can be found [below](#model-training).


## Background

Context on the project. 


## Usage

The model is intented to be used for semantic search: It encodes the search-query in a dense vector space and finds semantic neighbours, i.e., token which frequently occur within similar contexts in the underlying training data. The query should consist of a single word. When provided a bi-, tri-, or even fourgram, the quality of the model output depends on the presence of the query token in the model's vocabulary. Multiple words are to be concated by an underscore (e.g., "machine_learning" or "artifical_intelligence").


## Usage (API)

```python
import json
import requests

API_TOKEN = <TOKEN>

headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/simonschoe/call2vec"

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

query({"inputs": "<insert-query-here"})
```

## Usage (Gensim)

```python
from huggingface_hub import hf_hub_url, cached_download
from gensim.models.fasttext import load_facebook_model

# download model from huggingface hub
url = hf_hub_url(repo_id="simonschoe/call2vec", filename="model.bin")
cached_download(url)

# load model via gensim
model = load_facebook_model(<PATH-MODEL>)

# extract word embeddings
model.wv['transformation']
# get similar phrases
model.wv.most_similar(positive='transformation', topn=5)
# get dissimilar phrases
model.wv.most_similar(negative='transformation', topn=5, restrict_vocab=None)
# compute pairwise similarity scores (distance = 1 - similarity)
model.wv.similarity('transformation', 'continuity')
```

If model size is crucial, the final model could be additionally compressed using the [`compress-fasttext`](https://github.com/avidale/compress-fasttext) library (e.g., via pruning, conversion to `float16`, or product quantization).


## Model Training

The model has been trained on text data stemming from earnings call transcripts. The data is restricted to a call's question-and-answer (Q&A) section and the remarks by firm executives. The data has been preprocessed prior to model training via stop word removal, lemmatization, named entity masking, and coocurrence modeling.

**Corpus statistics:**
- Total number of calls: 159973
- Total number of remarks: 4512535
- Total number of token: 219228853

The following code snippets presents the training pipeline:
```python
import logging
from gensim.models import FastText
from gensim.models.word2vec import LineSentence
from gensim.models.callbacks import CallbackAny2Vec
from gensim.models.fasttext import save_facebook_model

# init
model = FastText(
    vector_size=300,
    window=5,
    min_count=10,
    alpha=0.025,
    negative = 5,
    seed=2021,
    sample = 0.001,
    sg=1,
    hs=0,
    max_vocab_size=None,
    workers=10,
)

# build vocab
model.build_vocab(corpus_iterable=LineSentence(<PATH-TRAIN-DATA>))

# train model
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MyCallback(CallbackAny2Vec):
    def __init__(self):
        self.epoch = 0
        
    def on_epoch_end(self, model):
        self.epoch += 1
        if (self.epoch % 10) == 0:
            # save in gensim format
            model.save(<PATH-SAVE>)
        
    def on_train_end(self, model):
        # save in binary format for upload to huggingface
        save_facebook_model(<PATH-SAVE>.bin)
    
model.train(
    corpus_iterable=LineSentence(<PATH-TRAIN-DATA>),
    total_words=model.corpus_total_words,
    total_examples=model.corpus_count,
    epochs=<EPOCHS>,
    callbacks=[MyCallback()],
)
```

**Model statistics:**
- Vocabulary size: 64,891
- Min. token frequency: 10
- Embedding dimensions: 300
- Number of epochs: 50

---
tags:
- text-classification
widget:
- text: "Hosted inference API not supported"
license: mit
language: en
---

# Multi2ConvAI-Logistics: English logistic regression model using fasttext embeddings

This model was developed in the [Multi2ConvAI](https://multi2conv.ai) project:
- domain: Logistics (more details about our use cases: ([en](https://multi2convai/en/blog/use-cases), [de](https://multi2convai/en/blog/use-cases)))
- language: English (en)
- model type: logistic regression
- embeddings: fastText embeddings

## How to run

Requires: 
- [multi2convai](https://github.com/inovex/multi2convai)
- serialized fastText embeddings (see last section of this readme or [these instructions](https://github.com/inovex/multi2convai/models/embeddings.README.md))

### Run with one line of code

After installing `multi2convai` and locally available fastText embeddings you can run:

````bash
# assumes working dir is the root of the cloned multi2convai repo

python scripts/run_inference.py -m multi2convai-logistics-en-logreg-ft

>>> Create pipeline for config: multi2convai-logistics-en-logreg-ft.
>>> Created a LogisticRegressionFasttextPipeline for domain: 'logistics' and language 'en'.
>>> 
>>> Enter your text (type 'stop' to end execution): Muss ich eine Maske tragen?
>>> 'Where can I put the parcel?' was classified as 'details.safeplace' (confidence: 0.8943)
````

### How to run model using multi2convai 

After installing `multi2convai` and locally available fastText embeddings you can run:

````python
# assumes working dir is the root of the cloned multi2convai repo

from pathlib import Path

from multi2convai.pipelines.inference.base import ClassificationConfig
from multi2convai.pipelines.inference.logistic_regression_fasttext import (
    LogisticRegressionFasttextConfig,
    LogisticRegressionFasttextPipeline,
)

language = "en"
domain = "logistics"

# 1. Define paths of model, label dict and embeddings
model_file = "model.pth"
label_dict_file = "label_dict.json"

embedding_path = Path(
    f"../models/embeddings/fasttext/en/wiki.200k.en.embed"
)
vocabulary_path = Path(
    f"../models/embeddings/fasttext/en/wiki.200k.en.vocab"
)

# 2. Create and setup pipeline
model_config = LogisticRegressionFasttextConfig(
    model_file, embedding_path, vocabulary_path
)
config = ClassificationConfig(language, domain, label_dict_file, model_config)

pipeline = LogisticRegressionFasttextPipeline(config)
pipeline.setup()

# 3. Run intent classification on a text of your choice
label = pipeline.run("Where can I put the parcel?")
label
>>> Label(string='details.safeplace', ratio='0.8943')
````

### Download and serialize fastText
````bash
# assumes working dir is the root of the cloned multi2convai repo

mkdir models/fasttext/en
curl https://dl.fbaipublicfiles.com/fasttext/vectors-wiki/wiki.en.vec --output models/fasttext/en/wiki.en.vec

python scripts/serialize_fasttext.py -r fasttext/wiki.en.vec -v fasttext/en/wiki.200k.en.vocab -e fasttext/en/wiki.200k.en.embed -n 200000


````

## Further information on Multi2ConvAI:
- https://multi2conv.ai
- https://github.com/inovex/multi2convai
- mailto: info@multi2conv.ai
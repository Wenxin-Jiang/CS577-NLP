---
tags:
- text-classification
widget:
- text: "Hosted inference API not supported"
license: mit
language: it
---

# Multi2ConvAI-Quality: Italian logistic regression model using fasttext embeddings

This model was developed in the [Multi2ConvAI](https://multi2conv.ai) project:
- domain: Quality (more details about our use cases: ([en](https://multi2convai/en/blog/use-cases), [de](https://multi2convai/en/blog/use-cases)))
- language: Italian (ml)
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

python scripts/run_inference.py -m multi2convai-quality-it-logreg-ft

>>> Create pipeline for config: multi2convai-quality-it-logreg-ft.
>>> Created a LogisticRegressionFasttextPipeline for domain: 'quality' and language 'it'.
>>> 
>>> Enter your text (type 'stop' to end execution): Avviare il programma
>>> 'Avviare il programma' was classified as 'neo.start' (confidence: 0.8943)
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

language = "it"
domain = "quality"

# 1. Define paths of model, label dict and embeddings
model_file = "model.pth"
label_dict_file = "label_dict.json"

embedding_path = Path(
    f"../models/embeddings/fasttext/it/wiki.200k.it.embed"
)
vocabulary_path = Path(
    f"../models/embeddings/fasttext/it/wiki.200k.it.vocab"
)

# 2. Create and setup pipeline
model_config = LogisticRegressionFasttextConfig(
    model_file, embedding_path, vocabulary_path
)
config = ClassificationConfig(language, domain, label_dict_file, model_config)

pipeline = LogisticRegressionFasttextPipeline(config)
pipeline.setup()

# 3. Run intent classification on a text of your choice
label = pipeline.run("Avviare il programma")
label
>>> Label(string='neo.start', ratio='0.8943')
````

### Download and serialize fastText
````bash
# assumes working dir is the root of the cloned multi2convai repo

mkdir models/fasttext/it
curl https://dl.fbaipublicfiles.com/fasttext/vectors-wiki/wiki.it.vec --output models/fasttext/it/wiki.it.vec

python scripts/serialize_fasttext.py -r fasttext/wiki.it.vec -v fasttext/it/wiki.200k.it.vocab -e fasttext/it/wiki.200k.it.embed -n 200000


````

## Further information on Multi2ConvAI:
- https://multi2conv.ai
- https://github.com/inovex/multi2convai
- mailto: info@multi2conv.ai
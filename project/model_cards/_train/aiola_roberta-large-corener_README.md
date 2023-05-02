---
language:
- en
tags:
- NER
- named entity recognition
- RE
- relation extraction
- entity mention detection
- EMD
- coreference resolution
license: afl-3.0
datasets:
- Ontonotes
- CoNLL04
---

# CoReNer

## Demo

We released an online demo so you can easily play with the model. Check it out: [http://corener-demo.aiola-lab.com](http://corener-demo.aiola-lab.com). 
The demo uses the [aiola/roberta-base-corener](https://huggingface.co/aiola/roberta-base-corener) model.

## Model description

A multi-task model for named-entity recognition, relation extraction, entity mention detection, and coreference resolution.

We model NER as a span classification task and relation extraction as a multi-label classification of (NER) span tuples.
Similarly, model EMD as a span classification task and CR as a binary classification of (EMD) span tuples.
To construct the CR clusters, we keep the top antecedent of each mention, then compute the connected components of the mentions' undirected graph.

The model was trained to recognize: 
- Entity types: GPE, ORG, PERSON, DATE, NORP, CARDINAL, MONEY, PERCENT, WORK_OF_ART, ORDINAL, EVENT, LOC, TIME, FAC, QUANTITY, LAW, PRODUCT, LANGUAGE. 
- Relation types: Kill, Live_In, Located_In, OrgBased_In, Work_For.

## Usage example

See additional details and usage examples at: https://github.com/aiola-lab/corener.

```python
import json
from transformers import AutoTokenizer
from corener.models import Corener, ModelOutput
from corener.data import MTLDataset
from corener.utils.prediction import convert_model_output
tokenizer = AutoTokenizer.from_pretrained("aiola/roberta-large-corener")
model = Corener.from_pretrained("aiola/roberta-large-corener")
model.eval()
examples = [
    "Apple Park is the corporate headquarters of Apple Inc., located in Cupertino, California, United States. It was opened to employees in April 2017, while construction was still underway, and superseded the original headquarters at 1 Infinite Loop, which opened in 1993."
]
dataset = MTLDataset(
    types=model.config.types, 
    tokenizer=tokenizer,
    train_mode=False,
)
dataset.read_dataset(examples)
example = dataset.get_example(0)  # get first example
output: ModelOutput = model(
    input_ids=example.encodings,
    context_masks=example.context_masks,
    entity_masks=example.entity_masks,
    entity_sizes=example.entity_sizes,
    entity_spans=example.entity_spans,
    entity_sample_masks=example.entity_sample_masks,
    inference=True,
)
print(json.dumps(convert_model_output(output=output, batch=example, dataset=dataset), indent=2))
```
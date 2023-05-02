---
license: mit
---

# T5-ANCE

T5-ANCE generally follows the training procedure described in [this page](https://openmatch.readthedocs.io/en/latest/dr-msmarco-passage.html), but uses a much larger batch size.

Dataset used for training:
- MS MARCO Passage

Evaluation result:

|Dataset|Metric|Result|
|---|---|---|
|MS MARCO Passage (dev) | MRR@10 | 0.3570|

Important hyper-parameters:

|Name|Value|
|---|---|
|Global batch size|256|
|Learning rate|5e-6|
|Maximum length of query|32|
|Maximum length of document|128|
|Template for query|`<text>`|
|Template for document|`Title: <title> Text: <text>`|

### Paper

\-
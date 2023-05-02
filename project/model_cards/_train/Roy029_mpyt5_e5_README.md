---
license: openrail
---
# Model Card for mpyt5_e5

<!-- Provide a quick summary of what the model is/does. [Optional] -->
事前に自然言語だけでなくPythonを学習したモデル

# Training Details

## Training Data

<!-- This should link to a Data Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

Python Code (1.05GB)


## Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

- MLM
- python vocab (https://huggingface.co/kkuramitsu/mt5-pytoken)

### Preprocessing

mT5 + Python

### Speeds, Sizes, Times

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

- mT5-small(300M Paramators)
- max_length = 128

# Model Version

- *epoch5： This Model
- *epoch10： https://huggingface.co/Roy029/mpyt5_e10
- *epoch15： https://huggingface.co/Roy029/mpyt5_e15
- *epoch20： https://huggingface.co/Roy029/mpyt5_e20
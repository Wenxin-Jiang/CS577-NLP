---
language: 
  - "eng"
thumbnail: "url to a thumbnail used in social sharing"
tags:
- "pytorch"
- "tensorflow"
license: "apache-2.0"

---


# vBERT-2021-BASE

### Model Info:
<ul>
<li> Authors: R&D AI Lab, VMware Inc.
<li> Model date: April, 2022
<li> Model version: 2021-base
<li> Model type: Pretrained language model
<li> License: Apache 2.0
</ul>

#### Motivation
Traditional BERT models struggle with VMware-specific words (Tanzu, vSphere, etc.), technical terms, and compound words. (<a href =https://medium.com/@rickbattle/weaknesses-of-wordpiece-tokenization-eb20e37fec99>Weaknesses of WordPiece Tokenization</a>)

We have pretrained our vBERT model to address the aforementioned issues using our <a href=https://medium.com/vmware-data-ml-blog/pretraining-a-custom-bert-model-6e37df97dfc4>BERT Pretraining Library</a>. 
<br> We have replaced the first 1k unused tokens of BERT's vocabulary with VMware-specific terms to create a modified vocabulary.  We then pretrained the 'bert-base-uncased' model for additional 78K steps (71k With MSL_128 and 7k with MSL_512) (approximately 5 epochs) on VMware domain data. 

#### Intended Use
The model functions as a VMware-specific Language Model.


#### How to Use
Here is how to use this model to get the features of a given text in PyTorch:

```
from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained('VMware/vbert-2021-base')
model = BertModel.from_pretrained("VMware/vbert-2021-base")
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

and in TensorFlow:

```
from transformers import BertTokenizer, TFBertModel
tokenizer = BertTokenizer.from_pretrained('VMware/vbert-2021-base')
model = TFBertModel.from_pretrained('VMware/vbert-2021-base')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='tf')
output = model(encoded_input)

```

### Training

#### - Datasets
Publically available VMware text data such as VMware Docs, Blogs etc. were used for creating the pretraining corpus. Sourced in May, 2021. (~320,000 Documents)
#### - Preprocessing
<ul>
<li>Decoding HTML
<li>Decoding Unicode
<li>Stripping repeated characters
<li>Splitting compound word
<li>Spelling correction
</ul>

#### - Model performance measures
We benchmarked vBERT on various VMware-specific NLP downstream tasks (IR, classification, etc).
The model scored higher than the 'bert-base-uncased' model on all benchmarks.

### Limitations and bias
Since the model is further pretrained on the BERT model, it may have the same biases embedded within the original BERT model.

The data needs to be preprocessed using our internal vNLP Preprocessor (not available to the public) to maximize its performance.

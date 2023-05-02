---
language: 
  - "eng"
thumbnail: "URL to a thumbnail used in social sharing"
tags:
- "PyTorch"
- "tensorflow"
license: "apache-2.0"

---


# viniLM-2021-from-large

### Model Info:
<ul>
<li> Authors: R&D AI Lab, VMware Inc.
<li> Model date: Jun 2022
<li> Model version: 2021-distilled-from-large
<li> Model type: Pretrained language model
<li> License: Apache 2.0
</ul>

#### Motivation
Based on [MiniLMv2 distillation](https://arxiv.org/pdf/2012.15828.pdf), we have distilled vBERT-2021-large into a smaller minilmv2 model for faster inference times without a significant loss of performance. 

#### Intended Use
The model functions as a VMware-specific Language Model.


#### How to Use
Here is how to use this model to get the features of a given text in PyTorch:

```
from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained('VMware/vinilm-2021-from-large')
model = BertModel.from_pretrained("VMware/vinilm-2021-from-large")
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

and in TensorFlow:

```
from transformers import BertTokenizer, TFBertModel
tokenizer = BertTokenizer.from_pretrained('VMware/vinilm-2021-from-large')
model = TFBertModel.from_pretrained('VMware/vinilm-2021-from-large')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='tf')
output = model(encoded_input)

```

### Training

The model is distilled from [vBERT-2021-large](https://huggingface.co/VMware/vbert-2021-large)</li> <br>
Weights were initialized using [nreimers/MiniLMv2-L6-H768-distilled-from-BERT-Large](https://huggingface.co/nreimers/MiniLMv2-L6-H768-distilled-from-BERT-Large/tree/main)</li>



#### - Datasets
Publically available VMware text data such as VMware Docs, Blogs, etc. were used for distilling the teacher vBERT-2021-large model into vinilm-2021-from-large model. Sourced in May 2021. (~320,000 Documents)
#### - Preprocessing
<ul>
<li>Decoding HTML
<li>Decoding Unicode
<li>Stripping repeated characters
<li>Splitting compound word
<li>Spelling correction
</ul>

#### - Model performance measures
We benchmarked vinilm on various VMware-specific NLP downstream tasks (IR, classification, etc).

### Limitations and bias
Since the model is distilled from a vBERT model based on the BERT model, it may have the same biases embedded within the original BERT model.

The data needs to be preprocessed using our internal vNLP Preprocessor (not available to the public) to maximize its performance.

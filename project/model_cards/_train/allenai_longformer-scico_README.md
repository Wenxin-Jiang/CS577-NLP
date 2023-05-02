---
language: en
tags:
- longformer
- longformer-scico
license: apache-2.0
datasets:
- allenai/scico
inference: false

---

# Longformer for SciCo

This model is the `unified` model discussed in the paper [SciCo: Hierarchical Cross-Document Coreference for Scientific Concepts (AKBC 2021)](https://openreview.net/forum?id=OFLbgUP04nC) that formulates the task of hierarchical cross-document coreference resolution (H-CDCR) as a multiclass problem. The model takes as input two mentions `m1` and `m2` with their corresponding context and outputs 4 scores: 

* 0: not related
* 1: `m1` and `m2` corefer
* 2: `m1` is a parent of `m2`
* 3: `m1` is a child of `m2`.

We provide the following code as an example to set the global attention on the special tokens: `<s>`, `<m>` and `</m>`.

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained('allenai/longformer-scico')
model = AutoModelForSequenceClassification.from_pretrained('allenai/longformer-scico')

start_token = tokenizer.convert_tokens_to_ids("<m>")
end_token = tokenizer.convert_tokens_to_ids("</m>")

def get_global_attention(input_ids):
    global_attention_mask = torch.zeros(input_ids.shape)
    global_attention_mask[:, 0] = 1  # global attention to the CLS token
    start = torch.nonzero(input_ids == start_token) # global attention to the <m> token
    end = torch.nonzero(input_ids == end_token) # global attention to the </m> token
    globs = torch.cat((start, end))
    value = torch.ones(globs.shape[0])
    global_attention_mask.index_put_(tuple(globs.t()), value)
    return global_attention_mask
    
m1 = "In this paper we present the results of an experiment in <m> automatic concept and definition extraction </m> from written sources of law using relatively simple natural methods."
m2 = "This task is important since many natural language processing (NLP) problems, such as <m> information extraction </m>, summarization and dialogue."

inputs = m1 + " </s></s> " + m2  

tokens = tokenizer(inputs, return_tensors='pt')
global_attention_mask = get_global_attention(tokens['input_ids'])

with torch.no_grad():
    output = model(tokens['input_ids'], tokens['attention_mask'], global_attention_mask)
    
scores = torch.softmax(output.logits, dim=-1)
# tensor([[0.0818, 0.0023, 0.0019, 0.9139]]) -- m1 is a child of m2
```

**Note:** There is a slight difference between this model and the original model presented in the [paper](https://openreview.net/forum?id=OFLbgUP04nC). The original model includes a single linear layer on top of the `<s>` token (equivalent to `[CLS]`) while this model includes a two-layers MLP to be in line with `LongformerForSequenceClassification`. The original repository can be found [here](https://github.com/ariecattan/scico). 

# Citation

```python
@inproceedings{
    cattan2021scico,
    title={SciCo: Hierarchical Cross-Document Coreference for Scientific Concepts},
    author={Arie Cattan and Sophie Johnson and Daniel S Weld and Ido Dagan and Iz Beltagy and Doug Downey and Tom Hope},
    booktitle={3rd Conference on Automated Knowledge Base Construction},
    year={2021},
    url={https://openreview.net/forum?id=OFLbgUP04nC}
}
```

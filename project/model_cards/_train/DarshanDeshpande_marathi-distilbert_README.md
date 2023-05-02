---
language: 
- mr
tags:
- fill-mask
license: apache-2.0
datasets:
- Oscar Corpus, News, Stories
widget:
- text: "हा खरोखर चांगला [MASK] आहे."
---

# Marathi DistilBERT

## Model description

This model is an adaptation of DistilBERT (Victor Sanh et al., 2019) for Marathi language. This version of Marathi-DistilBERT is trained from scratch on approximately 11.2 million sentences. 

```
DISCLAIMER

This model has not been thoroughly tested and may contain biased opinions or inappropriate language. User discretion is advised
```

## Training data
The training data has been extracted from a variety of sources, mainly including:
1. Oscar Corpus
2. Marathi Newspapers
3. Marathi storybooks and articles
 
The data is cleaned by removing all languages other than Marathi, while preserving common punctuations

## Training procedure
The model is trained from scratch using an Adam optimizer with a learning rate of 1e-4 and default β1 and β2 values of 0.9 and 0.999 respectively with a total batch size of 256 on a v3-8 TPU and mask probability of 15%.

## Example
```python
from transformers import pipeline
fill_mask = pipeline(
    "fill-mask",
    model="DarshanDeshpande/marathi-distilbert",
    tokenizer="DarshanDeshpande/marathi-distilbert",
)
fill_mask("हा खरोखर चांगला [MASK] आहे.")
```

### BibTeX entry and citation info

```bibtex
@misc{sanh2020distilbert,
      title={DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter}, 
      author={Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf},
      year={2020},
      eprint={1910.01108},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

<h3>Authors </h3>
<h5>1. Darshan Deshpande: <a href="https://github.com/DarshanDeshpande">GitHub</a>, <a href="https://www.linkedin.com/in/darshan-deshpande/">LinkedIn</a><h5>

<h5>2. Harshavardhan Abichandani: <a href="https://github.com/Baras64">GitHub</a>, <a href="http://​www.linkedin.com/in/harsh-abhi">LinkedIn</a><h5>
---
tags:
- summarization
language:
- it
metrics:
- rouge
model-index:
- name: summarization_mbart_ilpost
  results: []
datasets:
- ARTeLab/ilpost
---

# mbart_summarization_ilpost

This model is a fine-tuned version of [facebook/mbart-large-cc25](https://huggingface.co/facebook/mbart-large-cc25) on IlPost dataset for Abstractive Summarization.

It achieves the following results:
- Loss: 2.3640
- Rouge1: 38.9101
- Rouge2: 21.384
- Rougel: 32.0517
- Rougelsum: 35.0743
- Gen Len: 39.8843

## Usage 

```python
from transformers import MBartTokenizer, MBartForConditionalGeneration
tokenizer = MBartTokenizer.from_pretrained("ARTeLab/mbart-summarization-ilpost")
model = MBartForConditionalGeneration.from_pretrained("ARTeLab/mbart-summarization-ilpost")
```

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4.0

### Framework versions

- Transformers 4.15.0.dev0
- Pytorch 1.10.0+cu102
- Datasets 1.15.1
- Tokenizers 0.10.3

# Citation

More details and results in [published work](https://www.mdpi.com/2078-2489/13/5/228)

```
@Article{info13050228,
    AUTHOR = {Landro, Nicola and Gallo, Ignazio and La Grassa, Riccardo and Federici, Edoardo},
    TITLE = {Two New Datasets for Italian-Language Abstractive Text Summarization},
    JOURNAL = {Information},
    VOLUME = {13},
    YEAR = {2022},
    NUMBER = {5},
    ARTICLE-NUMBER = {228},
    URL = {https://www.mdpi.com/2078-2489/13/5/228},
    ISSN = {2078-2489},
    ABSTRACT = {Text summarization aims to produce a short summary containing relevant parts from a given text. Due to the lack of data for abstractive summarization on low-resource languages such as Italian, we propose two new original datasets collected from two Italian news websites with multi-sentence summaries and corresponding articles, and from a dataset obtained by machine translation of a Spanish summarization dataset. These two datasets are currently the only two available in Italian for this task. To evaluate the quality of these two datasets, we used them to train a T5-base model and an mBART model, obtaining good results with both. To better evaluate the results obtained, we also compared the same models trained on automatically translated datasets, and the resulting summaries in the same training language, with the automatically translated summaries, which demonstrated the superiority of the models obtained from the proposed datasets.},
    DOI = {10.3390/info13050228}
}
```
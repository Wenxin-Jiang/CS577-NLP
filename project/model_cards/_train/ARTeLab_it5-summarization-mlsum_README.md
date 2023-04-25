---
tags:
- summarization
language:
- it
metrics:
- rouge
model-index:
- name: summarization_mlsum
  results: []
datasets:
- ARTeLab/mlsum-it
---

# summarization_mlsum

This model is a fine-tuned version of [gsarti/it5-base](https://huggingface.co/gsarti/it5-base) on MLSum-it for Abstractive Summarization.

It achieves the following results:
- Loss: 2.0190
- Rouge1: 19.3739
- Rouge2: 5.9753
- Rougel: 16.691
- Rougelsum: 16.7862
- Gen Len: 32.5268

## Usage 
```python
from transformers import T5Tokenizer, T5ForConditionalGeneration
tokenizer = T5Tokenizer.from_pretrained("ARTeLab/it5-summarization-mlsum")
model = T5ForConditionalGeneration.from_pretrained("ARTeLab/it5-summarization-mlsum")
```

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4.0

### Framework versions

- Transformers 4.12.0.dev0
- Pytorch 1.9.1+cu102
- Datasets 1.12.1
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
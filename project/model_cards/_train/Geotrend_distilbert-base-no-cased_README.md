---
language: no

datasets: wikipedia

license: apache-2.0
---

# distilbert-base-no-cased

We are sharing smaller versions of [distilbert-base-multilingual-cased](https://huggingface.co/distilbert-base-multilingual-cased) that handle a custom number of languages.

Our versions give exactly the same representations produced by the original model which preserves the original accuracy.


For more information please visit our paper: [Load What You Need: Smaller Versions of Multilingual BERT](https://www.aclweb.org/anthology/2020.sustainlp-1.16.pdf).

## How to use

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("Geotrend/distilbert-base-no-cased")
model = AutoModel.from_pretrained("Geotrend/distilbert-base-no-cased")

```

To generate other smaller versions of multilingual transformers please visit [our Github repo](https://github.com/Geotrend-research/smaller-transformers).

### How to cite

```bibtex
@inproceedings{smallermdistilbert,
  title={Load What You Need: Smaller Versions of Mutlilingual BERT},
  author={Abdaoui, Amine and Pradel, Camille and Sigel, Grégoire},
  booktitle={SustaiNLP / EMNLP},
  year={2020}
}
```

## Contact 

Please contact amine@geotrend.fr for any question, feedback or request.
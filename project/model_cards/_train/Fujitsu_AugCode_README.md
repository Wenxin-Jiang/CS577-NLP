---
inference: false
license: mit
widget:
language:
- en
metrics:
- mrr
datasets:
- augmented_codesearchnet
---
#  🔥 Augmented Code Model 🔥
This is Augmented Code Model which is a fined-tune model of [CodeBERT](https://huggingface.co/microsoft/codebert-base) for processing of similarity between given docstring and code. This model is fined-model based on Augmented Code Corpus with ACS=4. 

## How to use the model ?
Similar to other huggingface model, you may load the model as follows.
```python

from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("Fujitsu/AugCode")

model = AutoModelForSequenceClassification.from_pretrained("Fujitsu/AugCode")

```
Then you may use `model` to infer the similarity between a given docstring and code.

### Citation
```bibtex@misc{bahrami2021augcode,
    title={AugmentedCode: Examining the Effects of Natural Language Resources in Code Retrieval Models},
    author={Mehdi Bahrami, N. C. Shrikanth, Yuji Mizobuchi, Lei Liu, Masahiro Fukuyori, Wei-Peng Chen, Kazuki Munakata},
    year={2021},
    eprint={TBA},
    archivePrefix={TBA},
    primaryClass={cs.CL}
}
```
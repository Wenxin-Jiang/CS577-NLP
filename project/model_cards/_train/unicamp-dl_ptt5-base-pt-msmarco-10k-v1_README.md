---
language: pt
license: mit
tags:
- msmarco
- t5
- pytorch
- tensorflow
- pt
- pt-br
datasets:
- msmarco
widget:
- text: "Texto de exemplo em português"
inference: false
---
# PTT5-base Reranker finetuned on Portuguese MS MARCO
## Introduction
ptt5-base-msmarco-pt-10k-v1 is a T5-based model pretrained in the BrWac corpus, finetuned on Portuguese translated version of MS MARCO passage dataset. In the version v1, the Portuguese dataset was translated using [Helsinki](https://huggingface.co/Helsinki-NLP) NMT model. This model was finetuned for 10k steps. 
Further information about the dataset or the translation method can be found on our [**mMARCO: A Multilingual Version of MS MARCO Passage Ranking Dataset**](https://arxiv.org/abs/2108.13897) and [mMARCO](https://github.com/unicamp-dl/mMARCO) repository.

## Usage
```python

from transformers import T5Tokenizer, T5ForConditionalGeneration

model_name = 'unicamp-dl/ptt5-base-msmarco-pt-10k-v1'
tokenizer  = T5Tokenizer.from_pretrained(model_name)
model      = T5ForConditionalGeneration.from_pretrained(model_name)

```
# Citation
If you use ptt5-base-msmarco-pt-10k-v1, please cite:

    @misc{bonifacio2021mmarco,
      title={mMARCO: A Multilingual Version of MS MARCO Passage Ranking Dataset}, 
      author={Luiz Henrique Bonifacio and Vitor Jeronymo and Hugo Queiroz Abonizio and Israel Campiotti and Marzieh Fadaee and  and Roberto Lotufo and Rodrigo Nogueira},
      year={2021},
      eprint={2108.13897},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

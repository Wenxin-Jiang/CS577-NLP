---
language: pt
license: mit
tags:
- t5
- pytorch
- tensorflow
- pt
- pt-br
datasets:
- brWaC
widget:
- text: "Texto de exemplo em português"
inference: false
---

# Portuguese T5 (aka "PTT5")

## Introduction
PTT5 is a T5 model pretrained in the BrWac corpus, a large  collection  of  web  pages in Portuguese, improving T5's performance on Portuguese sentence similarity and entailment tasks. It's available in three sizes (small, base and large) and two vocabularies (Google's T5 original and ours, trained on Portuguese Wikipedia).

For further information or requests, please go to [PTT5 repository](https://github.com/unicamp-dl/PTT5).

## Available models
| Model                                    | Size                                                   | #Params  | Vocabulary         |
| :-:                                      | :-:                                                            | :-:      | :-:                |
| [unicamp-dl/ptt5-small-t5-vocab](https://huggingface.co/unicamp-dl/ptt5-small-t5-vocab)                   | small | 60M  | Google's T5 |
| [unicamp-dl/ptt5-base-t5-vocab](https://huggingface.co/unicamp-dl/ptt5-base-t5-vocab)                     | base  | 220M | Google's T5 |
| [unicamp-dl/ptt5-large-t5-vocab](https://huggingface.co/unicamp-dl/ptt5-large-t5-vocab)                   | large | 740M | Google's T5 |
| [unicamp-dl/ptt5-small-portuguese-vocab](https://huggingface.co/unicamp-dl/ptt5-small-portuguese-vocab)   | small | 60M  | Portuguese  |
| **[unicamp-dl/ptt5-base-portuguese-vocab](https://huggingface.co/unicamp-dl/ptt5-base-portuguese-vocab)** **(Recommended)**     | **base**  | **220M** | **Portuguese**  |
| [unicamp-dl/ptt5-large-portuguese-vocab](https://huggingface.co/unicamp-dl/ptt5-large-portuguese-vocab)   | large | 740M | Portuguese  |

## Usage
```python
# Tokenizer 
from transformers import T5Tokenizer

# PyTorch (bare model, baremodel + language modeling head)
from transformers import T5Model, T5ForConditionalGeneration

# Tensorflow (bare model, baremodel + language modeling head)
from transformers import TFT5Model, TFT5ForConditionalGeneration

model_name = 'unicamp-dl/ptt5-base-portuguese-vocab'

tokenizer = T5Tokenizer.from_pretrained(model_name)

# PyTorch
model_pt = T5ForConditionalGeneration.from_pretrained(model_name)

# TensorFlow
model_tf = TFT5ForConditionalGeneration.from_pretrained(model_name)
```


# Citation
If you use PTT5, please cite:

    @article{ptt5_2020,
      title={PTT5: Pretraining and validating the T5 model on Brazilian Portuguese data},
      author={Carmo, Diedre and Piau, Marcos and Campiotti, Israel and Nogueira, Rodrigo and Lotufo, Roberto},
      journal={arXiv preprint arXiv:2008.09144},
      year={2020}
    }

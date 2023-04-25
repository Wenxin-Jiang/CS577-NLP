---
language: ca
license: apache-2.0
inference: false
datasets:
- projecte-aina/catalan_textual_corpus
---

# BART-Ca: The monolingual Catalan BART

## Table of Contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [Intended uses and limitations](#intended-use)
- [How to use](#how-to-use)
- [Limitations and bias](#limitations-and-bias)
- [Training](#training)
  - [Training data](#training-data)
  - [Training procedure](#training-procedure)
    - [Tokenization](#tokenization)
    - [Hyperparameters](#hyperparameters)
- [Evaluation](#evaluation)
   - [Variable and metrics](#variable-and-metrics)
   - [Evaluation results](#evaluation-results)
- [Additional information](#additional-information)
  - [Author](#author)
  - [Contact information](#contact-information)
  - [Copyright](#copyright)
  - [Licensing information](#licensing-information)
  - [Funding](#funding)
  - [Citing information](#citing-information)
  - [Disclaimer](#disclaimer)
</details>


## Model description

BART-ca is a transformer-based language model for the Catalan language and has been trained on a medium-size corpus collected from publicly available corpora and crawlers with the [Catalan Textual Corpus](https://huggingface.co/datasets/projecte-aina/catalan_textual_corpus).

## Intended uses and limitations

You can use the raw model for text infilling. However, the model is mostly meant to be fine-tuned on a supervised dataset. BART is particularly effective when fine-tuned for text generation (e.g. summarization, translation) but also works well for comprehension tasks (e.g. text classification, question answering).

## How to use

Here is how to use this model in PyTorch:

```python
from transformers import BartTokenizer, BartModel
tokenizer = BartTokenizer.from_pretrained('projecte-aina/bart-base-ca')
model = BartModel.from_pretrained('projecte-aina/bart-base-ca')
inputs = tokenizer("Hola, el meu gos és molt bonic", return_tensors="pt")
outputs = model(**inputs)
last_hidden_states = outputs.last_hidden_state
```

## Limitations and bias
At the time of submission, no measures have been taken to estimate the bias embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated.

## Training

### Training data

As training data, we used the [Catalan Textual Corpus](https://huggingface.co/datasets/projecte-aina/catalan_textual_corpus), a 1760-million-token web corpus of Catalan built from several sources.

### Training procedure

#### Tokenization

The training corpus has been tokenized using a byte version of [Byte-Pair Encoding (BPE)](https://github.com/openai/gpt-2) with a vocabulary size of 51,200 tokens. 

#### Hyperparameters

The hyperparameters were adapted for [fairseq](https://github.com/facebookresearch/fairseq/blob/main/examples/bart/README.md) from the original BART's paper.

| Hyper-parameter                    | Value  |
|------------------------------------|--------|
| Learning Rate                      | 5e-4 |
| Learning Rate Decay                | Polynomial Decay |
| Warmup Updates                            | 10000   |
| Batch Size                         | 2048     |
| Weight Decay                       | 0.01   |
| Max. Training Updates               | 125000     |

## Evaluation

### Variable and metrics

This model is intended to be fine-tuned for downstream tasks.

### Evaluation results

This model is intended to be fine-tuned for downstream tasks.


## Additional information

### Author
Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

### Contact information
For further information, send an email to aina@bsc.es

### Copyright
Copyright (c) 2022 Text Mining Unit at Barcelona Supercomputing Center 

### Licensing information
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Funding
This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).

### Citation information

If you use any of these resources (datasets or models) in your work, please cite our latest preprint:

```bibtex
@misc{degibert2022sequencetosequence,
      title={Sequence-to-Sequence Resources for Catalan}, 
      author={Ona de Gibert and Ksenia Kharitonova and Blanca Calvo Figueras and Jordi Armengol-Estapé and Maite Melero},
      year={2022},
      eprint={2202.06871},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Disclaimer

<details>
<summary>Click to expand</summary>

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of Artificial Intelligence.

In no event shall the owner and creator of the models (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.

---
language: he

thumbnail: https://avatars1.githubusercontent.com/u/3617152?norod.jpg
widget:
- text: "מתמטיקה:"
- text: "עליית המכונות"
- text: "ויקיפדיה העברית"
- text: "האירוויזיון הוא"
- text: "דוד בן-גוריון היה"

license: mit
---

# hebrew-bad_wiki-gpt_neo-tiny

## Table of Contents
- [Model Details](#model-details)
- [Uses](#uses)
- [Risks, Limitations and Biases](#risks-limitations-and-biases)
- [Training](#training)
- [Evaluation](#evaluation)
- [Environmental Impact](#environmental-impact)
- [How to Get Started With the Model](#how-to-get-started-with-the-model)

## Model Details
**Model Description:**

The model developer notes that the model is 
> Hebrew nonsense generation model which produces really bad wiki-abstract text. 


- **Developed by:** [Doron Adler](https://github.com/Norod)
- **Model Type:** Text Generation
- **Language(s):** Hebrew
- **License:** MIT
- **Resources for more information:**
- [GitHub Repo](https://github.com/Norod/hebrew-gpt_neo)
- [HuggingFace Space](https://huggingface.co/spaces/Norod78/Hebrew-GPT-Neo-Small)


## Uses

#### Direct Use

This model can be used for text generation.

#### Misuse and Out-of-scope Use


## Risks, Limitations and Biases
**CONTENT WARNING: Readers should be aware this section contains content that is disturbing, offensive, and can propagate historical and current stereotypes.**

Significant research has explored bias and fairness issues with language models (see, e.g., [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330.pdf) and [Bender et al. (2021)](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)).




## Training


#### Training Data
 [Hebrew Wikipedia Dump](https://dumps.wikimedia.org/hewiki/latest/) (hewiki abstract) from May 2020




#### Training Procedure


This model was fined tuned upon [hebrew-gpt_neo-tiny](https://huggingface.co/Norod78/hebrew-gpt_neo-tiny) which was previously trained using [EleutherAI's gpt-neo](https://github.com/EleutherAI/gpt-neo). 

Fine-tuning on the wiki-absract text was done using [@minimaxir](https://twitter.com/minimaxir)'s [aitextgen](https://github.com/minimaxir/aitextgen).



## Evaluation


#### Configs

Model configs for the hebrew-gpt_neo-tiny is available on the [hebrew-gpt_neo model github](https://github.com/Norod/hebrew-gpt_neo/tree/main/hebrew-gpt_neo-tiny/configs) 

* **Activation Function:** gelu
* **Number_Head:** 12
* **Number_Vocab:** 50257
* **Train batch size:** 250
* **Eval batch size:** 64
* **Predict batch size:** 1




## Environmental Impact

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700). We present the hardware type based on the [associated paper](https://arxiv.org/pdf/2105.09680.pdf).


- **Hardware Type:** [More information needed]

- **Hours used:** Unknown

- **Cloud Provider:** GCP  tpu-v8s

- **Compute Region:** europe-west4

- **Carbon Emitted:** [More information needed]


## How to Get Started With the Model

A Google Colab Notebook is also available [here](https://colab.research.google.com/github/Norod/hebrew-gpt_neo/blob/main/hebrew-gpt_neo-tiny/Norod78_hebrew_gpt_neo_tiny_Colab.ipynb)


​​
```
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Norod78/hebrew-bad_wiki-gpt_neo-tiny")

model = AutoModelForCausalLM.from_pretrained("Norod78/hebrew-bad_wiki-gpt_neo-tiny")


```



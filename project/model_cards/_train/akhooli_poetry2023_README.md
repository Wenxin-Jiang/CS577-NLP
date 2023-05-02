---
language: "ar"
tags:
- text-generation
datasets:
- APCD
widget:
 - text: "."
 - text: "عيد بأية حال"
 - text: "يا قدس"
 - text: "يا قدس"
 - text: "ألا ليت"
---

# GPT2-Arabic-Poetry-2023

## Model description

Fine-tuned model of Arabic poetry dataset based on aragpt2-medium.

## Intended uses & limitations

#### How to use

An example is provided in this [colab notebook](todo).

#### Limitations and bias

Both the GPT2-small-arabic (trained on Arabic Wikipedia) and this model have several limitations in terms of coverage and training performance. 
Use them as demonstrations or proof of concepts but not as production code.

## Training data

This pretrained model used the [dataset](todo) from several eras with a total of around 1.4m lines. 
The dataset was trained (fine-tuned) based on the [aragpt2-medium](https://huggingface.co/aubmindlab/aragpt2-medium) transformer model.

## Training procedure

Training was done using [Simple Transformers](https://github.com/ThilinaRajapakse/simpletransformers) library on Colab, using free GPU.

## Eval results 
Final perplexity reached was 49.56, train loss: 3.336

### BibTeX entry and citation info

```bibtex
@inproceedings{Abed Khooli,
  year={2023}
}
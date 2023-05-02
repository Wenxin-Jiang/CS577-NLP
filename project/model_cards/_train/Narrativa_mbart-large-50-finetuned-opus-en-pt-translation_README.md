---
language:
- en
- pt
datasets:
- opus100
- opusbook
tags:
- translation

metrics:
- bleu

---


# mBART-large-50 fine-tuned onpus100 and opusbook for English to Portuguese translation.
[mBART-50](https://huggingface.co/facebook/mbart-large-50/) large fine-tuned on [opus100](https://huggingface.co/datasets/viewer/?dataset=opus100) dataset for **NMT** downstream task.

# Details of mBART-50 🧠

mBART-50 is a multilingual Sequence-to-Sequence model pre-trained using the "Multilingual Denoising Pretraining" objective. It was introduced in [Multilingual Translation with Extensible Multilingual Pretraining and Finetuning](https://arxiv.org/abs/2008.00401) paper.


mBART-50 is a multilingual Sequence-to-Sequence model. It was created to show that multilingual translation models can be created through multilingual fine-tuning. 
Instead of fine-tuning on one direction, a pre-trained model is fine-tuned many directions simultaneously. mBART-50 is created using the original mBART model and extended to add extra 25 languages to support multilingual machine translation models of 50 languages. The pre-training objective is explained below.
**Multilingual Denoising Pretraining**: The model incorporates N languages by concatenating data: 
`D = {D1, ..., DN }` where each Di is a collection of monolingual documents in language `i`. The source documents are noised using two schemes, 
first randomly shuffling the original sentences' order, and second a novel in-filling scheme, 
where spans of text are replaced with a single mask token. The model is then tasked to reconstruct the original text. 
35% of each instance's words are masked by random sampling a span length according to a Poisson distribution `(λ = 3.5)`.
The decoder input is the original text with one position offset. A language id symbol `LID` is used as the initial token to predict the sentence.


## Details of the downstream task (NMT) - Dataset 📚

- **Homepage:** [Link](http://opus.nlpl.eu/opus-100.php) 
- **Repository:** [GitHub](https://github.com/EdinburghNLP/opus-100-corpus)
- **Paper:** [ARXIV](https://arxiv.org/abs/2004.11867)

### Dataset Summary

OPUS-100 is English-centric, meaning that all training pairs include English on either the source or target side. The corpus covers 100 languages (including English). Languages were selected based on the volume of parallel data available in OPUS.


### Languages

OPUS-100 contains approximately 55M sentence pairs. Of the 99 language pairs, 44 have 1M sentence pairs of training data, 73 have at least 100k, and 95 have at least 10k.

## Dataset Structure


### Data Fields

- `src_tag`: `string` text in source language
- `tgt_tag`: `string` translation of source language in target language

### Data Splits

The dataset is split into training, development, and test portions. Data was prepared by randomly sampled up to 1M sentence pairs per language pair for training and up to 2000 each for development and test. To ensure that there was no overlap (at the monolingual sentence level) between the training and development/test data, they applied a filter during sampling to exclude sentences that had already been sampled. Note that this was done cross-lingually so that, for instance, an English sentence in the Portuguese-English portion of the training data could not occur in the Hindi-English test set.

## Test set metrics 🧾

We got a **BLEU score of 20.61**
    


## Model in Action 🚀

```sh
git clone https://github.com/huggingface/transformers.git
pip install -q ./transformers
```

```python
from transformers import MBart50TokenizerFast, MBartForConditionalGeneration

ckpt = 'Narrativa/mbart-large-50-finetuned-opus-en-pt-translation'

tokenizer = MBart50TokenizerFast.from_pretrained(ckpt)
model = MBartForConditionalGeneration.from_pretrained(ckpt).to("cuda")

tokenizer.src_lang = 'en_XX'

def translate(text):
    inputs = tokenizer(text, return_tensors='pt')
    input_ids = inputs.input_ids.to('cuda')
    attention_mask = inputs.attention_mask.to('cuda')
    output = model.generate(input_ids, attention_mask=attention_mask, forced_bos_token_id=tokenizer.lang_code_to_id['pt_XX'])
    return tokenizer.decode(output[0], skip_special_tokens=True)
    
    
translate('here your English text to be translated to Portuguese...')
```

Created by: [Narrativa](https://www.narrativa.com/)

About Narrativa: Natural Language Generation (NLG) | Gabriele, our machine learning-based platform, builds and deploys natural language solutions. #NLG #AI
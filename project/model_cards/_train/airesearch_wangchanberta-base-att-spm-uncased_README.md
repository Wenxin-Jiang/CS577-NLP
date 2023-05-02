---
language: th
widget:
- text: "ผู้ใช้งานท่าอากาศยานนานาชาติ<mask>มีกว่าสามล้านคน<pad>"
---

# WangchanBERTa base model: `wangchanberta-base-att-spm-uncased`

<br>

Pretrained RoBERTa BASE model on assorted Thai texts (78.5 GB).
The script and documentation can be found at [this repository](https://github.com/vistec-AI/thai2transformers).
<br>

## Model description

<br>

The architecture of the pretrained model is based on RoBERTa [[Liu et al., 2019]](https://arxiv.org/abs/1907.11692). 

<br>


## Intended uses & limitations

<br>

You can use the pretrained model for masked language modeling (i.e. predicting a mask token in the input text). In addition, we also provide finetuned models for multiclass/multilabel text classification and token classification task.

<br>

**Multiclass text classification**


-  `wisesight_sentiment` 
     
    4-class text classification task (`positive`, `neutral`, `negative`, and `question`) based on social media posts and tweets.

-  `wongnai_reivews` 

    Users' review rating classification task (scale is ranging from 1 to 5)

-  `generated_reviews_enth` : (`review_star` as label)

    Generated users' review rating classification task (scale is ranging from 1 to 5).

**Multilabel text classification**

-  `prachathai67k`

    Thai topic classification with 12 labels based on news article corpus from prachathai.com. The detail is described in this [page](https://huggingface.co/datasets/prachathai67k).
    



**Token classification**

-  `thainer` 

    Named-entity recognition tagging with 13 named-entities as described in this [page](https://huggingface.co/datasets/thainer).

-  `lst20` : NER NER and POS tagging
 
     Named-entity recognition tagging with 10 named-entities and Part-of-Speech tagging with 16 tags as described in this [page](https://huggingface.co/datasets/lst20).

<br>

## How to use

<br>

The getting started notebook of WangchanBERTa model can be found at this [Colab notebook](https://colab.research.google.com/drive/1Kbk6sBspZLwcnOE61adAQo30xxqOQ9ko)

<br>

## Training data

`wangchanberta-base-att-spm-uncased` model was pretrained on assorted Thai text dataset. The total size of uncompressed text is 78.5GB.

### Preprocessing

Texts are preprocessed with the following rules:

- Replace HTML forms of characters with the actual characters such asnbsp;with a space and \\\\\\\\\\\\\\\\<br /> with a line break [[Howard and Ruder, 2018]](https://arxiv.org/abs/1801.06146).
- Remove empty brackets ((), {}, and []) than sometimes come up as a result of text extraction such as from Wikipedia.
- Replace line breaks with spaces.
- Replace more than one spaces with a single space
- Remove more than 3 repetitive characters such as ดีมากกก to ดีมาก [Howard and Ruder, 2018]](https://arxiv.org/abs/1801.06146).
- Word-level tokenization using [[Phatthiyaphaibun et al., 2020]](https://zenodo.org/record/4319685#.YA4xEGQzaDU) ’s `newmm` dictionary-based maximal matching tokenizer.
- Replace repetitive words; this is done post-tokenization unlike [[Howard and Ruder, 2018]](https://arxiv.org/abs/1801.06146). since there is no delimitation by space in Thai as in English.
- Replace spaces with <\\\\\\\\\\\\\\\\_>. The SentencePiece tokenizer combines the spaces with other tokens. Since spaces serve as punctuation in Thai such as sentence boundaries similar to periods in English, combining it with other tokens will omit an important feature for tasks such as word tokenization and sentence breaking. Therefore, we opt to explicitly mark spaces with <\\\\\\\\\\\\\\\\_>.

<br>


Regarding the vocabulary, we use SentencePiece [[Kudo, 2018]](https://arxiv.org/abs/1808.06226) to train SentencePiece unigram model.
The tokenizer has a vocabulary size of 25,000 subwords, trained on 15M sentences  sampled from the training set.


The length of each sequence is limited up to 416 subword tokens.

Regarding the masking procedure, for each sequence, we sampled 15% of the tokens and replace them with<mask>token.Out of the 15%, 80% is replaced with a<mask>token, 10% is left unchanged and 10% is replaced with a random token.

<br>

**Train/Val/Test splits**

After preprocessing and deduplication, we have a training set of 381,034,638 unique, mostly Thai sentences with sequence length of 5 to 300 words (78.5GB). The training set has a total of 16,957,775,412 words as tokenized by dictionary-based maximal matching [[Phatthiyaphaibun et al., 2020]](https://zenodo.org/record/4319685#.YA4xEGQzaDU), 8,680,485,067 subwords as tokenized by SentencePiece tokenizer, and 53,035,823,287 characters.
<br>

**Pretraining**

The model was trained on 8 V100 GPUs for 500,000 steps with the batch size of 4,096 (32 sequences per device with 16 accumulation steps) and a sequence length of 416 tokens. The optimizer we used is Adam with the learning rate of $3e-4$, $\\\\\\\\\\\\\\\\beta_1 = 0.9$, $\\\\\\\\\\\\\\\\beta_2= 0.999$ and $\\\\\\\\\\\\\\\\epsilon = 1e-6$. The learning rate is warmed up for the first 24,000 steps and linearly decayed to zero. The model checkpoint with minimum validation loss will be selected as the best model checkpoint. 

As of Sun 24 Jan 2021, we release the model from the checkpoint @360,000 steps due to the model pretraining has not yet been completed

<br>

**BibTeX entry and citation info**

```
@misc{lowphansirikul2021wangchanberta,
      title={WangchanBERTa: Pretraining transformer-based Thai Language Models}, 
      author={Lalita Lowphansirikul and Charin Polpanumas and Nawat Jantrakulchai and Sarana Nutanong},
      year={2021},
      eprint={2101.09635},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

---
language: th
---

# WangchanBERTa base model: `wangchanberta-base-wiki-sefr`

<br>

Pretrained RoBERTa BASE model on Thai Wikipedia corpus.
The script and documentation can be found at [this reposiryory](https://github.com/vistec-AI/thai2transformers).
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

    Named-entity recognition tagging with 13 named-entities as descibed in this [page](https://huggingface.co/datasets/thainer).

-  `lst20` : NER NER and POS tagging
 
     Named-entity recognition tagging with 10 named-entities and Part-of-Speech tagging with 16 tags as descibed in this [page](https://huggingface.co/datasets/lst20).

<br>

## How to use

<br>

The getting started notebook of WangchanBERTa model can be found at this [Colab notebook](https://colab.research.google.com/drive/1Kbk6sBspZLwcnOE61adAQo30xxqOQ9ko)

<br>

## Training data

`wangchanberta-base-wiki-sefr` model was pretrained on Thai Wikipedia. Specifically, we use the Wikipedia dump articles on 20 August 2020 (dumps.wikimedia.org/thwiki/20200820/). We opt out lists, and tables.

### Preprocessing

Texts are preprocessed with the following rules:

- Replace non-breaking space, zero-width non-breaking space, and soft hyphen with spaces.
- Remove an empty parenthesis that occur right after the title of the first paragraph.
- Replace spaces wtth <_>.

<br>


Regarding the vocabulary, we use Stacked Ensemble Filter and Refine (SEFR) tokenizer `(engine="best") `[[Limkonchotiwat et al., 2020]](https://www.aclweb.org/anthology/2020.emnlp-main.315/) based on probablities from CNN-based `deepcut` [[Kittinaradorn et al., 2019]](http://doi.org/10.5281/zenodo.3457707). The total number of word-level tokens in the vocabulary is 92,177.


We sample sentences contigously to have the length of at most 512 tokens. For some sentences that overlap the boundary of 512 tokens, we split such sentence with an additional token as document separator. This is the same approach as proposed by [[Liu et al., 2019]](https://arxiv.org/abs/1907.11692) (called "FULL-SENTENCES"). 

Regarding the masking procedure, for each sequence, we sampled 15% of the tokens and replace them with<mask>token.Out of the 15%, 80% is replaced with a<mask>token, 10% is left unchanged and 10% is replaced with a random token.

<br>

**Train/Val/Test splits**

We split sequencially 944,782 sentences for training set, 24,863 sentences for validation set and 24,862 sentences for test set.

<br>

**Pretraining**

The model was trained on 32 V100 GPUs for 31,250 steps with the batch size of 8,192 (16 sequences per device with 16 accumulation steps) and a sequence length of 512 tokens. The optimizer we used is Adam with the learning rate of $7e-4$, $\beta_1 = 0.9$, $\beta_2= 0.98$ and $\epsilon = 1e-6$. The learning rate is warmed up for the first 1250 steps and linearly decayed to zero. The model checkpoint with minimum validation loss will be selected as the best model checkpoint. 

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

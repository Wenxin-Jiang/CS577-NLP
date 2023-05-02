# Finetuend `bert-base-multilignual-cased` model on Thai sequence and token classification datasets

<br>

Finetuned XLM Roberta BASE model on Thai sequence and token classification datasets
The script and documentation can be found at [this repository](https://github.com/vistec-AI/thai2transformers).

<br>

## Model description

<br>

We use the pretrained cross-lingual BERT model (mBERT) as proposed by [[Devlin et al., 2018]](https://arxiv.org/abs/1810.04805). We download the pretrained PyTorch model via HuggingFace's Model Hub (https://huggingface.co/bert-base-multilignual-cased)
<br>



## Intended uses & limitations

<br>

You can use the finetuned models for multiclass/multilabel text classification and token classification task.

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

The example notebook demonstrating how to use finetuned model for inference can be found at this [Colab notebook](https://colab.research.google.com/drive/1Kbk6sBspZLwcnOE61adAQo30xxqOQ9ko)

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

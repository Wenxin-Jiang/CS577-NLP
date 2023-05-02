---
license: cc-by-nc-4.0
---

## Model Specification
- This is one **baseline Twitter NER model (with 73.71\% Entity-Level F1)** on Tweebank V2's NER benchmark (also called `Tweebank-NER`), trained on the Tweebank-NER training data. 
- **If you are looking for the SOTA Twitter NER model**, please go to this [HuggingFace hub link](https://huggingface.co/TweebankNLP/bertweet-tb2_wnut17-ner).
- For more details about the `TweebankNLP` project, please refer to this [our paper](https://arxiv.org/pdf/2201.07281.pdf) and [github](https://github.com/social-machines/TweebankNLP) page. 
- In the paper, it is referred as `HuggingFace-BERTweet (TB2)` in the NER table.

## How to use the model
- **PRE-PROCESSING**: when you apply the model on tweets, please make sure that tweets are preprocessed by the [TweetTokenizer](https://github.com/VinAIResearch/BERTweet/blob/master/TweetNormalizer.py) to get the best performance.

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("TweebankNLP/bertweet-tb2-ner")

model = AutoModelForTokenClassification.from_pretrained("TweebankNLP/bertweet-tb2-ner")
```

## References

If you use this repository in your research, please kindly cite [our paper](https://arxiv.org/pdf/2201.07281.pdf): 

```bibtex
@article{jiang2022tweetnlp,
    title={Annotating the Tweebank Corpus on Named Entity Recognition and Building NLP Models for Social Media Analysis},
    author={Jiang, Hang and Hua, Yining and Beeferman, Doug and Roy, Deb},
    journal={In Proceedings of the 13th Language Resources and Evaluation Conference (LREC)},
    year={2022}
}
```
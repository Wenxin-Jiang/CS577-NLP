---
language: 
- en
tags:
- text-classification
widget:
 - text: "I almost forgot to eat lunch.</s></s>I didn't forget to eat lunch."
 - text: "I almost forgot to eat lunch.</s></s>I forgot to eat lunch."
 - text: "I ate lunch.</s></s>I almost forgot to eat lunch."
datasets:
 - alisawuffles/WANLI
---

This is an off-the-shelf roberta-large model finetuned on WANLI, the Worker-AI Collaborative NLI dataset ([Liu et al., 2022](https://aclanthology.org/2022.findings-emnlp.508/)). It outperforms the `roberta-large-mnli` model on eight out-of-domain test sets, including by 11% on HANS and 9% on Adversarial NLI.

### How to use
```python
from transformers import RobertaTokenizer, RobertaForSequenceClassification

model = RobertaForSequenceClassification.from_pretrained('alisawuffles/roberta-large-wanli')
tokenizer = RobertaTokenizer.from_pretrained('alisawuffles/roberta-large-wanli')

x = tokenizer("I almost forgot to eat lunch.", "I didn't forget to eat lunch.", return_tensors='pt', max_length=128, truncation=True)
logits = model(**x).logits
probs = logits.softmax(dim=1).squeeze(0)
label_id = torch.argmax(probs).item()
prediction = model.config.id2label[label_id]
```

### Citation
```
@inproceedings{liu-etal-2022-wanli,
    title = "{WANLI}: Worker and {AI} Collaboration for Natural Language Inference Dataset Creation",
    author = "Liu, Alisa  and
      Swayamdipta, Swabha  and
      Smith, Noah A.  and
      Choi, Yejin",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2022",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-emnlp.508",
    pages = "6826--6847",
    abstract = "A recurring challenge of crowdsourcing NLP datasets at scale is that human writers often rely on repetitive patterns when crafting examples, leading to a lack of linguistic diversity. We introduce a novel approach for dataset creation based on worker and AI collaboration, which brings together the generative strength of language models and the evaluative strength of humans. Starting with an existing dataset, MultiNLI for natural language inference (NLI), our approach uses dataset cartography to automatically identify examples that demonstrate challenging reasoning patterns, and instructs GPT-3 to compose new examples with similar patterns. Machine generated examples are then automatically filtered, and finally revised and labeled by human crowdworkers. The resulting dataset, WANLI, consists of 107,885 NLI examples and presents unique empirical strengths over existing NLI datasets. Remarkably, training a model on WANLI improves performance on eight out-of-domain test sets we consider, including by 11{\%} on HANS and 9{\%} on Adversarial NLI, compared to training on the 4x larger MultiNLI. Moreover, it continues to be more effective than MultiNLI augmented with other NLI datasets. Our results demonstrate the promise of leveraging natural language generation techniques and re-imagining the role of humans in the dataset creation process.",
}
```
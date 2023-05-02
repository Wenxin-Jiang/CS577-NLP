---
language: 
- en
thumbnail: https://cogcomp.seas.upenn.edu/images/logo.png
tags:
- text-classification
- bart
- xsum
license: cc-by-sa-4.0
datasets:
- xsum
widget:
- text: "<s> Ban Ki-moon was elected for a second term in 2007. </s></s> Ban Ki-Moon was re-elected for a second term by the UN General Assembly, unopposed and unanimously, on 21 June 2011."
- text: "<s> Ban Ki-moon was elected for a second term in 2011. </s></s> Ban Ki-Moon was re-elected for a second term by the UN General Assembly, unopposed and unanimously, on 21 June 2011."

---

# bart-faithful-summary-detector

## Model description

A BART (base) model trained to classify whether a summary is *faithful* to the original article. See our [paper in NAACL'21](https://www.seas.upenn.edu/~sihaoc/static/pdf/CZSR21.pdf) for details. 

## Usage
Concatenate a summary and a source document as input (note that the summary needs to be the **first** sentence). 

Here's an example usage (with PyTorch)
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
  
tokenizer = AutoTokenizer.from_pretrained("CogComp/bart-faithful-summary-detector")
model = AutoModelForSequenceClassification.from_pretrained("CogComp/bart-faithful-summary-detector")

article = "Ban Ki-Moon was re-elected for a second term by the UN General Assembly, unopposed and unanimously, on 21 June 2011."

bad_summary = "Ban Ki-moon was elected for a second term in 2007."
good_summary = "Ban Ki-moon was elected for a second term in 2011."

bad_pair = tokenizer(text=bad_summary, text_pair=article, return_tensors='pt')
good_pair = tokenizer(text=good_summary, text_pair=article, return_tensors='pt')

bad_score = model(**bad_pair)
good_score = model(**good_pair)

print(good_score[0][:, 1] > bad_score[0][:, 1]) # True, label mapping: "0" -> "Hallucinated" "1" -> "Faithful"
```




### BibTeX entry and citation info

```bibtex
@inproceedings{CZSR21,
    author = {Sihao Chen and Fan Zhang and Kazoo Sone and Dan Roth},
    title = {{Improving Faithfulness in Abstractive Summarization with Contrast Candidate Generation and Selection}},
    booktitle = {NAACL},
    year = {2021}
}
```
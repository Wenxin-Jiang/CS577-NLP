---
tags:
- fastai
- text-classification
datasets: rajeshradhakrishnan/malayalam_news
widget:
- text: ഓഹരി വിപണി തകരുമ്പോള്‍ നിക്ഷേപം എങ്ങനെ സുരക്ഷിതമാക്കാം
  example_title: Malayalam News Classifier
---


# Malayalam (മലയാളം) Classifier using fastai (Working in Progress)

🥳 This model is my attempt to use machine learning using Malayalam Language. Huge inspiration from [Malayalam Text Classifier](https://kurianbenoy.com/2022-05-30-malayalamtext-0/). Courtesy to @waydegilliam for [blurr](https://ohmeow.github.io/blurr/text-examples-multilabel.html)

🌈 മലയാളത്തിൽ മെഷീൻ ലീർണിങ് പഠിക്കാനും പിന്നേ പരിചയപ്പെടാനും, to be continued...

# How its built ? & How to use ? 

Please find the [notebook](https://nbviewer.org/github/rajeshradhakrishnanmvk/kitchen2.0/blob/feature101-frontend/ml/fastai_X_Hugging_Face_Group_2022.ipynb) used for training the model

Usage:

First, install the utilities to load the model as well as `blurr`, which was used to train this model.

```bash
!pip install huggingface_hub[fastai]
!git clone https://github.com/ohmeow/blurr.git && cd blurr && pip install -e ".[dev]"
```

```python
from huggingface_hub import from_pretrained_fastai
learner = from_pretrained_fastai("rajeshradhakrishnan/ml-news-classify-fastai")


sentences = ["ഓഹരി വിപണി തകരുമ്പോള്‍ നിക്ഷേപം എങ്ങനെ സുരക്ഷിതമാക്കാം",
             "വാര്‍ണറുടെ ഒറ്റക്കയ്യന്‍ ക്യാച്ചില്‍ അമ്പരന്ന് ക്രിക്കറ്റ് ലോകം"]

probs = learner.predict(sentences)
# 'business', 'entertainment', 'sports', 'technology'
for idx in range(len(sentences)):
  print(f"Probability that sentence '{sentences[idx]}' is business is: {100*probs[idx]['probs'][0]:.2f}%")
  print(f"Probability that sentence '{sentences[idx]}' is entertainment is: {100*probs[idx]['probs'][1]:.2f}%")
  print(f"Probability that sentence '{sentences[idx]}' is sports is: {100*probs[idx]['probs'][2]:.2f}%")
  print(f"Probability that sentence '{sentences[idx]}' is technology is: {100*probs[idx]['probs'][3]:.2f}%")

```

---


# Model card

## Model description
The is a Malayalam classifier model for labels 'business', 'entertainment', 'sports', 'technology'.

## Intended uses & limitations
The model can be used to categorize malayalam new sfeed.

## Training and evaluation data

Data is from the [AI4Bharat-IndicNLP Dataset](https://github.com/AI4Bharat/indicnlp_corpus#indicnlp-news-article-classification-dataset) and wrapper to extract only Malayalam data( [HF dataset](https://huggingface.co/datasets/rajeshradhakrishnan/malayalam_news))!.

## Citation


```
@article{kunchukuttan2020indicnlpcorpus,
    title={AI4Bharat-IndicNLP Corpus: Monolingual Corpora and Word Embeddings for Indic Languages},
    author={Anoop Kunchukuttan and Divyanshu Kakwani and Satish Golla and Gokul N.C. and Avik Bhattacharyya and Mitesh M. Khapra and Pratyush Kumar},
    year={2020},
    journal={arXiv preprint arXiv:2005.00085},
}
```
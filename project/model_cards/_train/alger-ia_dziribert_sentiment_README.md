---
language: 
- ar
- dz

tags:
- pytorch
- bert
- multilingual
- ar
- dz

widget:
- text: "Baraka ellaho fik khouya la3ziz rabi yahfdek"
- text: "123 viva l'Agérie, tahya el djazair !"
- text: "ye3ayi l film hedak ghir akhtik"
- text: "Dzayer mech ghir el3assima sadi9i"
- text: "سخانة بزاف ليوم.. الجمل يرعف"

inference: true
---

<img src="https://raw.githubusercontent.com/alger-ia/dziribert/main/dziribert_drawing.png" alt="drawing" width="25%" height="25%" align="right"/>


# DziriBERT Sentiment


DziriBERT is the first Transformer-based Language Model that has been pre-trained specifically for the Algerian Dialect. It handles Algerian text contents written using both Arabic and Latin characters. 
This is a fine-tuned version that is ready to use for sentiment classification. 

For more information, please visit our paper: https://arxiv.org/pdf/2109.12346.pdf.

## How to use

```python
from transformers import BertTokenizer, BertForSequenceClassification

tokenizer = BertTokenizer.from_pretrained("alger-ia/dziribert_sentiment")
model = BertForSequenceClassification.from_pretrained("alger-ia/dziribert_sentiment")

```

You can find a fine-tuning script in our Github repo: https://github.com/alger-ia/dziribert

### How to cite

```bibtex
@article{dziribert,
  title={DziriBERT: a Pre-trained Language Model for the Algerian Dialect},
  author={Abdaoui, Amine and Berrimi, Mohamed and Oussalah, Mourad and Moussaoui, Abdelouahab},
  journal={arXiv preprint arXiv:2109.12346},
  year={2021}
}
```

## Contact 

Please contact amine.abdaoui.nlp@gmail.com for any question, feedback or request.
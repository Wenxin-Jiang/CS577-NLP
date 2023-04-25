---
language: ar

widget:
 - text: "وإذا كان هناك من لا يزال يعتقد أن لبنان هو سويسرا الشرق ، فهو مخطئ إلى حد بعيد . فلبنان ليس سويسرا ، ولا يمكن أن يكون كذلك . لقد عاش اللبنانيون في هذا البلد منذ ما يزيد عن ألف وخمسمئة عام ، أي منذ تأسيس الإمارة الشهابية التي أسسها الأمير فخر الدين المعني الثاني ( 1697 - 1742 )"
---

# AraGPT2 Detector

Machine generated detector model from the [AraGPT2: Pre-Trained Transformer for Arabic Language Generation paper](https://arxiv.org/abs/2012.15520)

This model is trained on the long text passages, and achieves a 99.4% F1-Score.

# How to use it:
```python
from transformers import pipeline
from arabert.preprocess import ArabertPreprocessor

processor = ArabertPreprocessor(model="aubmindlab/araelectra-base-discriminator")
pipe = pipeline("sentiment-analysis", model = "aubmindlab/aragpt2-mega-detector-long")

text = " "
text_prep = processor.preprocess(text)
result = pipe(text_prep)
# [{'label': 'machine-generated', 'score': 0.9977743625640869}]
```


# If you used this model please cite us as :
```
@misc{antoun2020aragpt2,
      title={AraGPT2: Pre-Trained Transformer for Arabic Language Generation},
      author={Wissam Antoun and Fady Baly and Hazem Hajj},
      year={2020},
      eprint={2012.15520},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

# Contacts
**Wissam Antoun**: [Linkedin](https://www.linkedin.com/in/wissam-antoun-622142b4/) | [Twitter](https://twitter.com/wissam_antoun) | [Github](https://github.com/WissamAntoun) | <wfa07@mail.aub.edu> | <wissam.antoun@gmail.com>

**Fady Baly**: [Linkedin](https://www.linkedin.com/in/fadybaly/) | [Twitter](https://twitter.com/fadybaly) | [Github](https://github.com/fadybaly) | <fgb06@mail.aub.edu> | <baly.fady@gmail.com>
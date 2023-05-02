---
language: da
tags:
- danish
- bert
- masked-lm
- botxo
license: cc-by-4.0
datasets:
- common_crawl
- wikipedia
- dindebat.dk
- hestenettet.dk
- danish_OpenSubtitles
widget:
- text: "Chili Jensen, som bor på Danmarksgade 12, køber chilifrugter fra Netto."
---

# Danish BERT (version 2, uncased) by [Certainly](https://certainly.io/) (previously known as BotXO) finetuned for Named Entity Recognition on the [DaNE dataset](https://danlp.alexandra.dk/304bd159d5de/datasets/ddt.zip) (Hvingelby et al., 2020) by Malte Højmark-Bertelsen.

Humongous amounts of credit needs to go to [Certainly](https://certainly.io/) (previously known as BotXO), for pretraining the Danish BERT. For data and training details see their [GitHub repository](https://github.com/certainlyio/nordic_bert) or [this article](https://www.certainly.io/blog/danish-bert-model/). You can also visit their [organization page](https://huggingface.co/Certainly) on Hugging Face.

It is both available in TensorFlow and Pytorch format. 
The original TensorFlow version can be downloaded using [this link](https://www.dropbox.com/s/19cjaoqvv2jicq9/danish_bert_uncased_v2.zip?dl=1).

Here is an example on how to load Danish BERT for token classification in PyTorch using the [🤗Transformers](https://github.com/huggingface/transformers) library:



```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("Maltehb/danish-bert-botxo-ner-dane")
model = AutoModelForTokenClassification.from_pretrained("Maltehb/danish-bert-botxo-ner-dane")

```

### References
Danish BERT. (2020). BotXO. https://github.com/botxo/nordic_bert (Original work published 2019)

Hvingelby, R., Pauli, A. B., Barrett, M., Rosted, C., Lidegaard, L. M., & Søgaard, A. (2020). DaNE: A Named Entity Resource for Danish. Proceedings of the 12th Language Resources and Evaluation Conference, 4597–4604. https://www.aclweb.org/anthology/2020.lrec-1.565

#### Contact

For help or further information feel free to connect with the author Malte Højmark-Bertelsen on [hjb@kmd.dk](mailto:hjb@kmd.dk?subject=[GitHub]%20DanishBERTUncasedNER) or any of the following platforms:

[<img align="left" alt="MalteHB | Twitter" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/twitter.svg" />][twitter]
[<img align="left" alt="MalteHB | LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />][linkedin]
[<img align="left" alt="MalteHB | Instagram" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />][instagram]

<br />

</details>

[twitter]: https://twitter.com/malteH_B
[instagram]: https://www.instagram.com/maltemusen/
[linkedin]: https://www.linkedin.com/in/malte-h%C3%B8jmark-bertelsen-9a618017b/
---
language: id
tags:
- roberta
license: mit
datasets:
- indonli
widget:
- text: "Amir Sjarifoeddin Harahap lahir di Kota Medan, Sumatera Utara, 27 April 1907. Ia meninggal di Surakarta, Jawa Tengah, pada 19 Desember 1948 dalam usia 41 tahun. </s></s> Amir Sjarifoeddin Harahap masih hidup."
---

## Indo-roberta-indonli

Indo-roberta-indonli is natural language inference classifier based on [Indo-roberta](https://huggingface.co/flax-community/indonesian-roberta-base) model. It was trained on the trained on [IndoNLI](https://github.com/ir-nlp-csui/indonli/tree/main/data/indonli) dataset. The model used was [Indo-roberta](https://huggingface.co/flax-community/indonesian-roberta-base) and was transfer-learned to a natural inference classifier model. The model are tested using the validation, test_layer and test_expert dataset given in the github repository. The results are shown below.

### Result
| Dataset     | Accuracy | F1      | Precision | Recall  |
|-------------|----------|---------|-----------|---------|
|    Test Lay | 0.74329  | 0.74075 |   0.74283 | 0.74133 |
| Test Expert | 0.6115   | 0.60543 |   0.63924 | 0.61742 |

## Model

The model was trained on with 5 epochs, batch size 16, learning rate 2e-5 and weight decay 0.01. Achieved different metrics as shown below.

| Epoch | Training Loss | Validation Loss | Accuracy | F1       | Precision | Recall   |
|-------|---------------|-----------------|----------|----------|-----------|----------|
|     1 |      0.942500 |        0.658559 | 0.737369 | 0.735552 |  0.735488 | 0.736679 |
|     2 |      0.649200 |        0.645290 | 0.761493 | 0.759593 |  0.762784 | 0.759642 |
|     3 |      0.437100 |        0.667163 | 0.766045 | 0.763979 |  0.765740 | 0.763792 |
|     4 |      0.282000 |        0.786683 | 0.764679 | 0.761802 |  0.762011 | 0.761684 |
|     5 |      0.193500 |        0.925717 | 0.765134 | 0.763127 |  0.763560 | 0.763489 |

## How to Use
### As NLI Classifier
```python
from transformers import pipeline
pretrained_name = "StevenLimcorn/indonesian-roberta-indonli"
nlp = pipeline(
    "zero-shot-classification",
    model=pretrained_name,
    tokenizer=pretrained_name
)
nlp("Amir Sjarifoeddin Harahap lahir di Kota Medan, Sumatera Utara, 27 April 1907. Ia meninggal di Surakarta, Jawa Tengah, pada 19 Desember 1948 dalam usia 41 tahun. </s></s> Amir Sjarifoeddin Harahap masih hidup.")
```
## Disclaimer
Do consider the biases which come from both the pre-trained RoBERTa model and the `INDONLI` dataset that may be carried over into the results of this model.
## Author
Indonesian RoBERTa Base IndoNLI was trained and evaluated by [Steven Limcorn](https://github.com/stevenlimcorn). All computation and development are done on Google Colaboratory using their free GPU access.

## Reference
The dataset we used is by IndoNLI.
```
@inproceedings{indonli,
    title = "IndoNLI: A Natural Language Inference Dataset for Indonesian",
    author = "Mahendra, Rahmad and Aji, Alham Fikri and Louvan, Samuel and Rahman, Fahrurrozi and Vania, Clara",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    publisher = "Association for Computational Linguistics",
}
```
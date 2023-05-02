---
language: "ban"
datasets:
- WikiBali
- Suara Saking Bali
widget:
- text: "Kalsium silih <mask> datu kimia antuk simbol Ca miwah wilangan atom 20."
  example_title: "Conto 1"
- text: "Tabuan inggih <mask> silih tunggil soroh beburon sane madue kampid."
  example_title: "Conto 2"
---

BRATA (Basa Bali Used for Pretraining RoBERTa) is a pretrained language model trained using Basa Bali or Balinese Language with RoBERTa-base-uncased configuration. The datasets used for this pretraining were collected by extracting WikiBali or Wikipedia Basa Bali and some sources from Suara Saking Bali website. The pretrained language model trained using Google Colab Pro with Tesla P100-PCIE-16GB GPU. Pretraining process used 200 epoch and 2 batch size. The smallest training loss can be seen in Training metrics or Metrics tab.
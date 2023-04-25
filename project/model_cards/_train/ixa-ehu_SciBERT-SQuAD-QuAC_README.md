---
language: en
---

# SciBERT-SQuAD-QuAC

This is the [SciBERT language representation model](https://huggingface.co/allenai/scibert_scivocab_uncased) fine tuned for Question Answering. SciBERT is a pre-trained language model based on BERT that has been trained on a large corpus of scientific text. When fine tuning for Question Answering we combined [SQuAD2.0](https://www.aclweb.org/anthology/P18-2124/) and [QuAC](https://arxiv.org/abs/1808.07036) datasets.

If using this model, please cite the following paper:
```
@inproceedings{otegi-etal-2020-automatic,
    title = "Automatic Evaluation vs. User Preference in Neural Textual {Q}uestion{A}nswering over {COVID}-19 Scientific Literature",
    author = "Otegi, Arantxa  and
      Campos, Jon Ander  and
      Azkune, Gorka  and
      Soroa, Aitor  and
      Agirre, Eneko",
    booktitle = "Proceedings of the 1st Workshop on {NLP} for {COVID}-19 (Part 2) at {EMNLP} 2020",
    month = dec,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.nlpcovid19-2.15",
    doi = "10.18653/v1/2020.nlpcovid19-2.15",
}
```

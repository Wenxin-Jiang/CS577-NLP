---
license: cc-by-4.0
---
# Automatic Translation Alignment of Ancient Greek Texts
GRC-ALIGNMENT model is an XLM-RoBERTa-based model, fine-tuned for automatic multilingual text alignment at the word level. 
The model is trained on 12 million monolingual ancient Greek tokens with Masked Language Model (MLM) training objective. Further, the model is fine-tuned on 45k parallel sentences, mainly in ancient Greek-English, Greek-Latin, and Greek-Georgian.

### Multilingual Training Dataset
|                Languages                |Sentences |                                      Source                                      |
|:---------------------------------------|:-----------:|:--------------------------------------------------------------------------------|
| GRC-ENG                                 |      32.500 | Perseus Digital Library (Iliad, Odyssey, Xenophon, New Testament)                |
| GRC-LAT                                 |       8.200 | [Digital Fragmenta Historicorum Graecorum project](https://www.dfhg-project.org/) |
| GRC-KAT <br>GRC-ENG <br>GRC-LAT<br>GRC-ITA<br>GRC-POR |       4.000 | [UGARIT Translation Alignment Editor](https://ugarit.ialigner.com/ )             |

### Model Performance
| Languages | Alignment Error Rate |
|:---------:|:--------------------:|
| GRC-ENG   |     19.73% (IterMax) |
| GRC-POR   |     23.91% (IterMax) |
| GRC-LAT   |      10.60% (ArgMax) |

The gold standard datasets are available on [Github](https://github.com/UgaritAlignment/Alignment-Gold-Standards).

If you use this model, please cite our papers:
<pre>
@InProceedings{yousef-EtAl:2022:LREC,
  author    = {Yousef, Tariq  and  Palladino, Chiara  and  Shamsian, Farnoosh  and  dâ€™Orange Ferreira, Anise  and  Ferreira dos Reis, Michel},
  title     = {An automatic model and Gold Standard for translation alignment of Ancient Greek},
  booktitle      = {Proceedings of the Language Resources and Evaluation Conference},
  month          = {June},
  year           = {2022},
  address        = {Marseille, France},
  publisher      = {European Language Resources Association},
  pages     = {5894--5905},
  url       = {https://aclanthology.org/2022.lrec-1.634}
}

@InProceedings{yousef-EtAl:2022:LT4HALA2022,
  author    = {Yousef, Tariq  and  Palladino, Chiara  and  Wright, David J.  and  Berti, Monica},
  title     = {Automatic Translation Alignment for Ancient Greek and Latin},
  booktitle      = {Proceedings of the Second Workshop on Language Technologies for Historical and Ancient Languages},
  month          = {June},
  year           = {2022},
  address        = {Marseille, France},
  publisher      = {European Language Resources Association},
  pages     = {101--107},
  url       = {https://aclanthology.org/2022.lt4hala2022-1.14}
}

</pre>
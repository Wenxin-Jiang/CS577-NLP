---
language: hu
metrics: rouge
---

[Paper](https://hlt.bme.hu/en/publ/foszt2oszt)

We publish an abstractive summarizer for Hungarian, an
encoder-decoder model initialized with [huBERT](huggingface.co/SZTAKI-HLT/hubert-base-cc), and fine-tuned on the
[ELTE.DH](https://elte-dh.hu/) corpus of former Hungarian news portals. The model produces fluent output in the correct topic, but it hallucinates frequently.
Our quantitative evaluation on automatic and human transcripts of news
(with automatic and human-made punctuation, [Tündik et al. (2019)](https://www.isca-speech.org/archive/interspeech_2019/tundik19_interspeech.html), [Tündik and Szaszák (2019)](https://www.isca-speech.org/archive/interspeech_2019/szaszak19_interspeech.html)) shows that the model is
robust with respect to errors in either automatic speech recognition or
automatic punctuation restoration. In fine-tuning and inference, we followed [a jupyter notebook by Patrick von
Platen](https://github.com/patrickvonplaten/notebooks/blob/master/BERT2BERT_for_CNN_Dailymail.ipynb). Most hyper-parameters are the same as those by von Platen, but we
found it advantageous to change the minimum length of the summary to 8 word-
pieces (instead of 56), and the number of beams in beam search to 5 (instead
of 4). Our model was fine-tuned on a server of the [SZTAKI-HLT](hlt.bme.hu/) group, which kindly
provided access to it.
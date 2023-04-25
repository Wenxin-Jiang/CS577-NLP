## OPUS Tatoeba English-Yoruba

This model was obtained by running the script convert_marian_to_pytorch.py with the flag -m eng-yor. The original models were trained by Jörg Tiedemann using the MarianNMT library. See all available MarianMTModel models on the profile of the Helsinki NLP group.


---
 - tags: translation
 - source language: English
 - target language: Yoruba
 
 - dataset: opus+bt
 -model: transformer-align
 -pre-processing: normalization + SentencePiece (spm12k,spm12k)
 -download original weights: [opus+bt-2021-04-10.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-yor/opus+bt-2021-04-10.zip)
 -test set translations: [opus+bt-2021-04-10.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-yor/opus+bt-2021-04-10.test.txt)
 -test set scores: [opus+bt-2021-04-10.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-yor/opus+bt-2021-04-10.eval.txt)

 -Benchmarks
 |test set|BLEU|chr-F|
 |:---|:---|:---|
 |Tatoeba-test.eng-yor|13.0|0.333|
 
 ---
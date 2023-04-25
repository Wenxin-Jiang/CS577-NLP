---
license: apache-2.0

tags:
  - translation
  - Fairseq

widget:
  - text: "<2li> Let us generate some Livonian text!"

---

[Fairseq](https://github.com/pytorch/fairseq) model for translating between English, Estonian, Latvian and Livonian.

Subword units created with [SentencePiece](https://github.com/google/sentencepiece).

To specify the target language to translate into, prepend one of the language code tags to the source sentences:
```
<2en>  Šis teikums jātulko angļu valodā
<2et>  This sentence should be translated into Estonian
<2lv>  This sentence should be translated into Latvian
<2li>  This sentence should be translated into Livonian
```

This should be done after applying SentencePiece.
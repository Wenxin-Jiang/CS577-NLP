## RoBERTa Latin model

This is a Latin RoBERTa-based LM model.

The data it uses is the same as has been used to compute the text referenced HTR evaluation measures.

The intention of the Transformer-based LM is twofold: on the one hand, it will be used for the evaluation of HTR results, on the other, it should be used as a decoder for the TrOCR architecture.

The basis for the word unigram and character n-gram computations is the Latin part of the [cc100 corpus](http://data.statmt.org/cc-100/).

The overall corpus contains 2.5G of text data.

### Preprocessing

I undertook the following preprocessing steps:

  - Removal of all "pseudo-Latin" text ("Lorem ipsum ...").
  - Use of [CLTK](http://www.cltk.org) for sentence splitting and normalisation.
  - Retaining only lines containing letters of the Latin alphabet, numerals, and certain punctuation (--> `grep -P '^[A-z0-9ÄÖÜäöüÆæŒœᵫĀāūōŌ.,;:?!\- Ęę]+$' la.nolorem.tok.txt`
  - deduplication of the corpus

The result is a corpus of ~390 million tokens.

The dataset used to train this model is available [HERE](https://huggingface.co/datasets/pstroe/cc100-latin).

### Contact

For contact, reach out to Phillip Ströbel [via mail](mailto:pstroebel@cl.uzh.ch) or [via Twitter](https://twitter.com/CLingophil).

### How to cite

If you use this model, pleas cite it as:

    @online{stroebel-roberta-base-latin-cased1,
        author = {Ströbel, Phillip Benjamin},
        title = {RoBERTa Base Latin Cased V1},
        year = 2022,
        url = {https://huggingface.co/pstroe/roberta-base-latin-cased},
        urldate = {YYYY-MM-DD}
    }
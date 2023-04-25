---
language:
- fi
- en
tags:
- sentence-similarity
- sentence-transformers

widget:
- source-sentence: "mikä on teidän paras telkkari"

---

An XML-RoBERTa based cross-lingual Sentence-BERT model distilled to cover semantic textual similarity in Finnish in addition to English. At the time of creation there were no models performing better in Finnish STS that I was aware of.


# Usage instructions

This model is essentially an extended SentenceTransformer so instructions described at [sbert.net](https://www.sbert.net) apply.

# The other things

The training setup, data, optimizer parameters, limitations and evaluation is described in Ch 6 [here](http://hdl.handle.net/10138/332588) and [repository](https://github.com/mkmoisio/sts-en-to-fi-distillation).

# Credit

This heavily builds on the work done by [Nils Reimers](https://scholar.google.com/citations?user=57GA3A8AAAAJ&hl=de) et al. 


# Contact
Still got questions?

mmoisio@kiisseli.com
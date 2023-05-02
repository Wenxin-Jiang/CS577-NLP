---
license: apache-2.0
---

## Model description

A question type classification model based on multilingual BERT.

The question type classifier takes as input the question, and returns a label that distinguishes between boolean and short answer extractive questions. 

The model was initialized with [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) and fine-tuned on the answerable subset of [TyDiQA](https://huggingface.co/datasets/tydiqa) train questions. 

## Intended uses & limitations

You can use the raw model for question classification. Biases associated with the pre-existing language model, bert-base-multilingual-cased, may be present in our fine-tuned model, tydiqa-boolean-question-classifier.  

## Usage

You can use this model directly in the the [PrimeQA](https://github.com/primeqa/primeqa) framework for supporting boolean question in reading comprehension as in this [example](https://github.com/primeqa/primeqa/tree/main/examples/boolqa).

### BibTeX entry and citation info

```bibtex
@article{DBLP:journals/corr/abs-1810-04805,
  author    = {Jacob Devlin and
               Ming{-}Wei Chang and
               Kenton Lee and
               Kristina Toutanova},
  title     = {{BERT:} Pre-training of Deep Bidirectional Transformers for Language
               Understanding},
  journal   = {CoRR},
  volume    = {abs/1810.04805},
  year      = {2018},
  url       = {http://arxiv.org/abs/1810.04805},
  archivePrefix = {arXiv},
  eprint    = {1810.04805},
  timestamp = {Tue, 30 Oct 2018 20:39:56 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1810-04805.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

```bibtex
@misc{https://doi.org/10.48550/arxiv.2206.08441,
  author = {McCarley, Scott and 
            Bornea, Mihaela and 
            Rosenthal, Sara and 
            Ferritto, Anthony and 
            Sultan, Md Arafat and 
            Sil, Avirup and 
            Florian, Radu},
  title = {GAAMA 2.0: An Integrated System that Answers Boolean and Extractive Questions}, 
  journal   = {CoRR},
  publisher = {arXiv},  
  year = {2022},
  url = {https://arxiv.org/abs/2206.08441},
}

```
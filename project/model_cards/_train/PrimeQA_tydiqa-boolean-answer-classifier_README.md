---
license: apache-2.0
---

## Model description

An answer classification model for boolean questions based on XLM-RoBERTa.

The answer classifier takes as input a boolean question and a passage, and returns a label (yes, no-answer, no).  

The model was initialized with [xlm-roberta-large](https://huggingface.co/xlm-roberta-large) and fine-tuned on the boolean questions from [TyDiQA](https://huggingface.co/datasets/tydiqa), as well as [BoolQ-X](https://arxiv.org/abs/2112.07772#). 

## Intended uses & limitations

You can use the raw model for question classification. Biases associated with the pre-existing language model, xlm-roberta-large, may be present in our fine-tuned model, tydiqa-boolean-answer-classifier.  

## Usage

You can use this model directly in the the [PrimeQA](https://github.com/primeqa/primeqa) framework for supporting boolean questions in reading comprehension: [examples](https://github.com/primeqa/primeqa/tree/main/examples/boolqa).

### BibTeX entry and citation info

```bibtex
@article{Rosenthal2021DoAT,
  title={Do Answers to Boolean Questions Need Explanations? Yes},
  author={Sara Rosenthal and Mihaela A. Bornea and Avirup Sil and Radu Florian and Scott McCarley},
  journal={ArXiv},
  year={2021},
  volume={abs/2112.07772}
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
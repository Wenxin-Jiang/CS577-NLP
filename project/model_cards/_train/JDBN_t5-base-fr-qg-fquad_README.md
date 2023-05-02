---
language: fr
widget:
- text: "generate question: Barack Hussein Obama, né le 4 aout 1961, est un homme politique américain et avocat. Il a été élu <hl> en 2009 <hl> pour devenir le 44ème président des Etats-Unis d'Amérique. </s>"
- text: "question: Quand Barack Obama a t'il été élu président? context: Barack Hussein Obama, né le 4 aout 1961, est un homme politique américain et avocat. Il a été élu en 2009 pour devenir le 44ème président des Etats-Unis d'Amérique. </s>"
tags: 
- pytorch
- t5
- question-generation
- seq2seq
datasets:
- fquad
- piaf
---

# T5 Question Generation and Question Answering

## Model description

This model is a T5 Transformers model (airklizz/t5-base-multi-fr-wiki-news) that was fine-tuned in french on 3 different tasks
* question generation

* question answering

* answer extraction

It obtains quite good results on FQuAD validation dataset.

## Intended uses & limitations

This model functions for the 3 tasks mentionned earlier and was not tested on other tasks. 

```python
from transformers import T5ForConditionalGeneration, T5Tokenizer
model = T5ForConditionalGeneration.from_pretrained("JDBN/t5-base-fr-qg-fquad")
tokenizer = T5Tokenizer.from_pretrained("JDBN/t5-base-fr-qg-fquad")
```

## Training data

The initial model used was https://huggingface.co/airKlizz/t5-base-multi-fr-wiki-news. This model was finetuned on a dataset composed of FQuAD and PIAF on the 3 tasks mentioned previously.

The data were preprocessed like this
* question generation: "generate question: Barack Hussein Obama, né le 4 aout 1961, est un homme politique américain et avocat. Il a été élu <hl> en 2009 <hl> pour devenir le 44ème président des Etats-Unis d'Amérique."

* question answering: "question: Quand Barack Hussein Obamaa-t-il été élu président des Etats-Unis d’Amérique? context: Barack Hussein Obama, né le 4 aout 1961, est un homme politique américain et avocat. Il a été élu en 2009 pour devenir le 44ème président des Etats-Unis d’Amérique."

* answer extraction: "extract_answers: Barack Hussein Obama, né le 4 aout 1961, est un homme politique américain et avocat. <hl> Il a été élu en 2009 pour devenir le 44ème président des Etats-Unis d’Amérique <hl>."

The preprocessing we used was implemented in https://github.com/patil-suraj/question_generation

## Eval results

#### On FQuAD validation set

| BLEU_1 | BLEU_2 | BLEU_3 | BLEU_4 | METEOR | ROUGE_L | CIDEr |
|--------|--------|--------|--------|--------|---------|-------|
|  0.290 | 0.203  |  0.149 |  0.111 |  0.197 |  0.284  | 1.038 |

#### Question Answering metrics

For these metrics, the performance of this question answering model (https://huggingface.co/illuin/camembert-base-fquad) on FQuAD original question and on T5 generated questions are compared.

| Questions | Exact Match | F1 Score |
|------------------|--------|--------|
|Original FQuAD | 54.015 | 77.466 |
|Generated | 45.765 | 67.306 |

### BibTeX entry and citation info

```bibtex
@misc{githubPatil,
author = {Patil Suraj},
title = {question generation GitHub repository},
year = {2020},
howpublished={\url{https://github.com/patil-suraj/question_generation}}
}

@article{T5,
    title={Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
    author={Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},
    year={2019},
    eprint={1910.10683},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}

@misc{dhoffschmidt2020fquad,
      title={FQuAD: French Question Answering Dataset}, 
      author={Martin d'Hoffschmidt and Wacim Belblidia and Tom Brendlé and Quentin Heinrich and Maxime Vidal},
      year={2020},
      eprint={2002.06071},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```



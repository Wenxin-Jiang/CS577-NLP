---
language:
- es
license: cc-by-4.0
tags:
- anglicisms  # Example: audio
- loanwords  # Example: automatic-speech-recognition
- borrowing  # Example: speech
- codeswitching  # Example to specify a library: allennlp
- flair
- token-classification
- sequence-tagger-model
- arxiv:2203.16169
datasets:
- coalas  # Example: common_voice. Use dataset id from https://hf.co/datasets
widget:
- text: "Las fake news sobre la celebrity se reprodujeron por los 'mass media' en prime time."
- text: "En la 'red carpet' lució un look muy urban con  chunky shoes de inspiración anime." 
- text: "Benching, estar en el banquillo de tu crush mientras otro juega de titular."
- text: "Recetas de noviembre para el batch cooking."
- text: "Buscamos data scientist con conocimientos de machine learning y blockchain."
---

# anglicisms-spanish-flair-cs

This is a pretrained model for detecting unassimilated English lexical borrowings (a.k.a. anglicisms) on Spanish newswire. This model labels words of foreign origin (fundamentally from English) used in Spanish language, words such as *fake news*, *machine learning*, *smartwatch*, *influencer* or *streaming*.

The model is a BiLSTM-CRF model fed with [Transformer-based embeddings pretrained on codeswitched data](https://huggingface.co/sagorsarker/codeswitch-spaeng-lid-lince) along subword embeddings (BPE and character embeddings). The model was trained on the [COALAS](https://github.com/lirondos/coalas/) corpus for the task of detecting lexical borrowings.

The model considers two labels:  
* ``ENG``: For English lexical borrowings (*smartphone*, *online*, *podcast*)
* ``OTHER``: For lexical borrowings from any other language (*boutique*, *anime*, *umami*)

The model uses BIO encoding to account for multitoken borrowings.

**⚠ There is another [mBERT -based model](https://huggingface.co/lirondos/anglicisms-spanish-mbert) for this same task trained using the ``Transformers`` library**. That model however produced worse results than this Flair-based model (F1 = 83.55).  


## Metrics (on the test set)
Results obtained on the test set of the [COALAS](https://github.com/lirondos/coalas/) corpus.

| LABEL    | Precision | Recall  |  F1    |
|:-------|-----:|-----:|---------:|
| ALL    | 90.14   | 81.79    |   85.76   | 
| ENG    | 90.16   | 84.34    |   87.16   |
| OTHER  | 85.71   | 13.04     |  22.64     |


## Dataset
This model was trained on [COALAS](https://github.com/lirondos/coalas/), a corpus of Spanish newswire annotated with unassimilated lexical borrowings. The corpus contains 370,000 tokens and includes various written media written in European Spanish. The test set was designed to be as difficult as possible: it covers sources and dates not seen in the training set, includes a high number of OOV words (92% of the borrowings in the test set are OOV) and is very borrowing-dense (20 borrowings per 1,000 tokens).

|Set      | Tokens | ENG  | OTHER |  Unique |
|:-------|-----:|-----:|---------:|---------:|
|Training |231,126 |1,493 | 28 |380 |
|Development |82,578 |306 |49 |316|
|Test |58,997 |1,239 |46 |987|
|**Total** |372,701 |3,038 |123 |1,683 |

## More info
More information about the dataset, model experimentation and error analysis can be found in the paper: *[Detecting Unassimilated Borrowings in Spanish: An Annotated Corpus and Approaches to Modeling](https://aclanthology.org/2022.acl-long.268/)*.

## How to use

```
from flair.data import Sentence
from flair.models import SequenceTagger
import pathlib
import os

if os.name == 'nt': # Minor patch needed if you are running from Windows
    temp = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath
  
tagger = SequenceTagger.load("lirondos/anglicisms-spanish-flair-cs")

text = "Las fake news sobre la celebrity se reprodujeron por los mass media en prime time."

sentence = Sentence(text)

# predict tags
tagger.predict(sentence)

# print sentence
print(sentence)

# print predicted borrowing spans
print('The following borrowing were found:')
for entity in sentence.get_spans():
    print(entity)
```

## Citation
If you use this model, please cite the following reference:
```
@inproceedings{alvarez-mellado-lignos-2022-detecting,
    title = "Detecting Unassimilated Borrowings in {S}panish: {A}n Annotated Corpus and Approaches to Modeling",
    author = "{\'A}lvarez-Mellado, Elena  and
      Lignos, Constantine",
    booktitle = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.acl-long.268",
    pages = "3868--3888",
    abstract = "This work presents a new resource for borrowing identification and analyzes the performance and errors of several models on this task. We introduce a new annotated corpus of Spanish newswire rich in unassimilated lexical borrowings{---}words from one language that are introduced into another without orthographic adaptation{---}and use it to evaluate how several sequence labeling models (CRF, BiLSTM-CRF, and Transformer-based models) perform. The corpus contains 370,000 tokens and is larger, more borrowing-dense, OOV-rich, and topic-varied than previous corpora available for this task. Our results show that a BiLSTM-CRF model fed with subword embeddings along with either Transformer-based embeddings pretrained on codeswitched data or a combination of contextualized word embeddings outperforms results obtained by a multilingual BERT-based model.",
}
```


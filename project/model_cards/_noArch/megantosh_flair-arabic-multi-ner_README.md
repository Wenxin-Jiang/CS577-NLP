---
language: 
- ar
- en
license: apache-2.0
datasets:
- AQMAR
- ANERcorp
thumbnail: https://www.informatik.hu-berlin.de/en/forschung-en/gebiete/ml-en/resolveuid/a6f82e0d7fa446a59c902cac4cafa9cb/@@images/image/preview
tags:
- flair
- Text Classification
- token-classification
- sequence-tagger-model
metrics:
- f1
widget:
- text: أعرف كل شيء عن جيجي
- text: ترتقي شريحة M1 Pro وشريحة M1 Max ببنية شريحة M1 المذهلة إلى مستويات جديدة، إذ تأتيان للمرة الأولى ببنية نظام متكامل في شريحة (SoC) إلى جهاز نوت بوك للمحترفين.
- text: "اختارها خيري بشارة كممثلة، دون سابقة معرفة أو تجربة تمثيلية، لتقف بجانب فاتن حمامة في فيلم «يوم مر ويوم حلو» (1988) وهي ما زالت شابة لم تتخطَ عامها الثاني"
---
# Arabic NER Model using Flair Embeddings
Training was conducted over 94 epochs, using a linear decaying learning rate of 2e-05, starting from 0.225 and a batch size of 32 with GloVe and Flair forward and backward embeddings.


## Original Datasets:
- [AQMAR](http://www.cs.cmu.edu/~ark/ArabicNER/)
- [ANERcorp](http://curtis.ml.cmu.edu/w/courses/index.php/ANERcorp)

## Results:
- F1-score (micro) 0.8666
- F1-score (macro) 0.8488

|      | Named Entity Type    | True Posititves  | False Positives | False Negatives | Precision | Recall | class-F1 |
|------|-|----|----|----|-----------|--------|----------|
| LOC  | Location| 539 | 51 | 68 | 0.9136    | 0.8880 | 0.9006   |
| MISC | Miscellaneous|408 | 57 | 89 | 0.8774    | 0.8209 | 0.8482   |
| ORG  | Organisation|167 | 43 | 64 | 0.7952    | 0.7229 | 0.7574   |
| PER  | Person (no title)|501 | 65 | 60 | 0.8852    | 0.8930 | 0.8891   |

---

# Usage
```python
from flair.data import Sentence
from flair.models import SequenceTagger
import pyarabic.araby as araby
from icecream import ic

tagger = SequenceTagger.load("julien-c/flair-ner")
arTagger = SequenceTagger.load('megantosh/flair-arabic-multi-ner')

sentence = Sentence('George Washington went to Washington .')
arSentence = Sentence('عمرو عادلي أستاذ للاقتصاد السياسي المساعد في الجامعة الأمريكية  بالقاهرة .')


# predict NER tags
tagger.predict(sentence)
arTagger.predict(arSentence)

# print sentence with predicted tags
ic(sentence.to_tagged_string)
ic(arSentence.to_tagged_string)

```

# Example
```bash
2021-07-07 14:30:59,649 loading file /Users/mega/.flair/models/flair-ner/f22eb997f66ae2eacad974121069abaefca5fe85fce71b49e527420ff45b9283.941c7c30b38aef8d8a4eb5c1b6dd7fe8583ff723fef457382589ad6a4e859cfc
2021-07-07 14:31:04,654 loading file /Users/mega/.flair/models/flair-arabic-multi-ner/c7af7ddef4fdcc681fcbe1f37719348afd2862b12aa1cfd4f3b93bd2d77282c7.242d030cb106124f7f9f6a88fb9af8e390f581d42eeca013367a86d585ee6dd6
ic| sentence.to_tagged_string: <bound method Sentence.to_tagged_string of Sentence: "George Washington went to Washington ."   [− Tokens: 6  − Token-Labels: "George <B-PER> Washington <E-PER> went to Washington <S-LOC> ."]>
ic| arSentence.to_tagged_string: <bound method Sentence.to_tagged_string of Sentence: "عمرو عادلي أستاذ للاقتصاد السياسي المساعد في الجامعة الأمريكية بالقاهرة ."   [− Tokens: 11  − Token-Labels: "عمرو <B-PER> عادلي <I-PER> أستاذ للاقتصاد السياسي المساعد في الجامعة <B-ORG> الأمريكية <I-ORG> بالقاهرة <B-LOC> ."]>
ic| entity: <PER-span (1,2): "George Washington">
ic| entity: <LOC-span (5): "Washington">
ic| entity: <PER-span (1,2): "عمرو عادلي">
ic| entity: <ORG-span (8,9): "الجامعة الأمريكية">
ic| entity: <LOC-span (10): "بالقاهرة">
ic| sentence.to_dict(tag_type='ner'): 
{"text":"عمرو عادلي أستاذ للاقتصاد السياسي المساعد في الجامعة الأمريكية  بالقاهرة .",
"labels":[],
{"entities":[{{{
               "text":"عمرو عادلي",
               "start_pos":0,
               "end_pos":10,
               "labels":[PER (0.9826)]},
            {"text":"الجامعة الأمريكية",
               "start_pos":45,
               "end_pos":62,
               "labels":[ORG (0.7679)]},
            {"text":"بالقاهرة",
               "start_pos":64,
               "end_pos":72,
               "labels":[LOC (0.8079)]}]}
"text":"George Washington went to Washington .",
"labels":[],
"entities":[{
           {"text":"George Washington",
            "start_pos":0,
            "end_pos":17,
            "labels":[PER (0.9968)]},
           {"text":"Washington""start_pos":26,
            "end_pos":36,
            "labels":[LOC (0.9994)]}}]}
```

# Model Configuration
```python
SequenceTagger(
  (embeddings): StackedEmbeddings(
    (list_embedding_0): WordEmbeddings('glove')
    (list_embedding_1): FlairEmbeddings(
      (lm): LanguageModel(
        (drop): Dropout(p=0.1, inplace=False)
        (encoder): Embedding(7125, 100)
        (rnn): LSTM(100, 2048)
        (decoder): Linear(in_features=2048, out_features=7125, bias=True)
      )
    )
    (list_embedding_2): FlairEmbeddings(
      (lm): LanguageModel(
        (drop): Dropout(p=0.1, inplace=False)
        (encoder): Embedding(7125, 100)
        (rnn): LSTM(100, 2048)
        (decoder): Linear(in_features=2048, out_features=7125, bias=True)
      )
    )
  )
  (word_dropout): WordDropout(p=0.05)
  (locked_dropout): LockedDropout(p=0.5)
  (embedding2nn): Linear(in_features=4196, out_features=4196, bias=True)
  (rnn): LSTM(4196, 256, batch_first=True, bidirectional=True)
  (linear): Linear(in_features=512, out_features=15, bias=True)
  (beta): 1.0
  (weights): None
  (weight_tensor) None
 ```
 Due to the right-to-left in left-to-right context, some formatting errors might occur. and your code might appear like [this](https://ibb.co/ky20Lnq), (link accessed on 2020-10-27) 
 
 # Citation
*if you use this model, please consider citing [this work](https://www.researchgate.net/publication/358956953_Sequence_Labeling_Architectures_in_Diglossia_-_a_case_study_of_Arabic_and_its_dialects):*
```latex
@unpublished{MMHU21
author = "M. Megahed",
title = "Sequence Labeling Architectures in Diglossia",
year = {2021},
doi = "10.13140/RG.2.2.34961.10084"
url = {https://www.researchgate.net/publication/358956953_Sequence_Labeling_Architectures_in_Diglossia_-_a_case_study_of_Arabic_and_its_dialects}
}
```
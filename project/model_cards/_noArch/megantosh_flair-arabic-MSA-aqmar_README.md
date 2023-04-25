---
language: ar
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
- text: "اختارها خيري بشارة كممثلة، دون سابقة معرفة أو تجربة تمثيلية، لتقف بجانب فاتن حمامة في فيلم «يوم مر ويوم حلو» (1988) وهي ما زالت شابة لم تتخطَ عامها الثاني"
---
# Arabic NER Model for AQMAR dataset
Training was conducted over 86 epochs, using a linear decaying learning rate of 2e-05, starting from 0.3 and a batch size of 48 with fastText and Flair forward and backward embeddings.


## Original Dataset:
- [AQMAR](http://www.cs.cmu.edu/~ark/ArabicNER/)

## Results:
- F1-score (micro) 0.9323
- F1-score (macro) 0.9272

|      | True Posititves  | False Positives | False Negatives | Precision | Recall | class-F1 |
|------|-----|----|----|---------|--------|----------|
| LOC  | 164 | 7  | 13 | 0.9591  | 0.9266 | 0.9425   |
| MISC | 398 | 22 | 37 |  0.9476 | 0.9149 | 0.9310   |
| ORG  | 65  | 6  | 9  | 0.9155  | 0.8784 | 0.8966   |
| PER  | 199 | 13 | 13 | 0.9387  | 0.9387 | 0.9387   |

---

# Usage
```python
from flair.data import Sentence
from flair.models import SequenceTagger
import pyarabic.araby as araby
from icecream import ic

arTagger = SequenceTagger.load('megantosh/flair-arabic-MSA-aqmar')

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
see an example from a [similar NER model in Flair](https://huggingface.co/megantosh/flair-arabic-multi-ner)

# Model Configuration
```python
  (embeddings): StackedEmbeddings(
    (list_embedding_0): WordEmbeddings('ar')
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
  (embedding2nn): Linear(in_features=4396, out_features=4396, bias=True)
  (rnn): LSTM(4396, 256, batch_first=True, bidirectional=True)
  (linear): Linear(in_features=512, out_features=14, bias=True)
  (beta): 1.0
  (weights): None
  (weight_tensor) None
)"
2021-03-31 22:19:50,654 ----------------------------------------------------------------------------------------------------
2021-03-31 22:19:50,654 Corpus: "Corpus: 3025 train + 336 dev + 373 test sentences"
2021-03-31 22:19:50,654 ----------------------------------------------------------------------------------------------------
2021-03-31 22:19:50,654 Parameters:
2021-03-31 22:19:50,654  - learning_rate: "0.3"
2021-03-31 22:19:50,654  - mini_batch_size: "48"
2021-03-31 22:19:50,654  - patience: "3"
2021-03-31 22:19:50,654  - anneal_factor: "0.5"
2021-03-31 22:19:50,654  - max_epochs: "150"
2021-03-31 22:19:50,654  - shuffle: "True"
2021-03-31 22:19:50,654  - train_with_dev: "False"
2021-03-31 22:19:50,654  - batch_growth_annealing: "False"
2021-03-31 22:19:50,655 ------------------------------------
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
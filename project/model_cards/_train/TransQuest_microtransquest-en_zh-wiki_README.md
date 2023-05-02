---
language: en-zh
tags:
- Quality Estimation
- microtransquest
license: apache-2.0
---


# TransQuest: Translation Quality Estimation with Cross-lingual Transformers
The goal of quality estimation (QE) is to evaluate the quality of a translation without having access to a reference translation. High-accuracy QE that can be easily deployed for a number of language pairs is the missing piece in many commercial translation workflows as they have numerous potential uses. They can be employed to select the best translation when several translation engines are available or can inform the end user about the reliability of automatically translated content. In addition, QE systems can be used to decide whether a translation can be published as it is in a given context, or whether it requires human post-editing before publishing or translation from scratch by a human. The quality estimation can be done at different levels: document level, sentence level and word level.

With TransQuest, we have opensourced our research in translation quality estimation which also won the sentence-level direct assessment quality estimation shared task in [WMT 2020](http://www.statmt.org/wmt20/quality-estimation-task.html). TransQuest outperforms current open-source quality estimation frameworks such as [OpenKiwi](https://github.com/Unbabel/OpenKiwi) and [DeepQuest](https://github.com/sheffieldnlp/deepQuest).


## Features
- Sentence-level translation quality estimation on both aspects: predicting post editing efforts and direct assessment.
- Word-level translation quality estimation capable of predicting quality of source words, target words and target gaps.
- Outperform current state-of-the-art quality estimation methods like DeepQuest and OpenKiwi in all the languages experimented. 
- Pre-trained quality estimation models for fifteen language pairs are available in [HuggingFace.](https://huggingface.co/TransQuest)

## Installation
### From pip

```bash
pip install transquest
```

### From Source

```bash
git clone https://github.com/TharinduDR/TransQuest.git
cd TransQuest
pip install -r requirements.txt
```

## Using Pre-trained Models

```python
from transquest.algo.word_level.microtransquest.run_model import MicroTransQuestModel
import torch

model = MicroTransQuestModel("xlmroberta", "TransQuest/microtransquest-en_zh-wiki", labels=["OK", "BAD"], use_cuda=torch.cuda.is_available())
source_tags, target_tags = model.predict([["if not , you may not be protected against the diseases . ", "ja tā nav , Jūs varat nepasargāt no slimībām . "]])

```


## Documentation
For more details follow the documentation.

1. **[Installation](https://tharindudr.github.io/TransQuest/install/)** - Install TransQuest locally using pip. 
2. **Architectures** - Checkout the architectures implemented in TransQuest
    1. [Sentence-level Architectures](https://tharindudr.github.io/TransQuest/architectures/sentence_level_architectures/) - We have released two architectures; MonoTransQuest and SiameseTransQuest to perform sentence level quality estimation.
    2. [Word-level Architecture](https://tharindudr.github.io/TransQuest/architectures/word_level_architecture/) - We have released MicroTransQuest to perform word level quality estimation. 
3. **Examples** - We have provided several examples on how to use TransQuest in recent WMT quality estimation shared tasks.
    1. [Sentence-level Examples](https://tharindudr.github.io/TransQuest/examples/sentence_level_examples/)
    2. [Word-level Examples](https://tharindudr.github.io/TransQuest/examples/word_level_examples/)
4. **Pre-trained Models** - We have provided pretrained quality estimation models for fifteen language pairs covering both sentence-level and word-level
    1. [Sentence-level Models](https://tharindudr.github.io/TransQuest/models/sentence_level_pretrained/)
    2. [Word-level Models](https://tharindudr.github.io/TransQuest/models/word_level_pretrained/)
5. **[Contact](https://tharindudr.github.io/TransQuest/contact/)** - Contact us for any issues with TransQuest


## Citations
If you are using the word-level architecture, please consider citing this paper which is accepted to [ACL 2021](https://2021.aclweb.org/).

```bash
@InProceedings{ranasinghe2021,
author = {Ranasinghe, Tharindu and Orasan, Constantin and Mitkov, Ruslan},
title = {An Exploratory Analysis of Multilingual Word Level Quality Estimation with Cross-Lingual Transformers},
booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},
year = {2021}
}
```

If you are using the sentence-level architectures, please consider citing these papers which were presented in [COLING 2020](https://coling2020.org/) and in [WMT 2020](http://www.statmt.org/wmt20/) at EMNLP 2020.

```bash
@InProceedings{transquest:2020a,
author = {Ranasinghe, Tharindu and Orasan, Constantin and Mitkov, Ruslan},
title = {TransQuest: Translation Quality Estimation with Cross-lingual Transformers},
booktitle = {Proceedings of the 28th International Conference on Computational Linguistics},
year = {2020}
}
```
 
```bash
@InProceedings{transquest:2020b,
author = {Ranasinghe, Tharindu and Orasan, Constantin and Mitkov, Ruslan},
title = {TransQuest at WMT2020: Sentence-Level Direct Assessment},
booktitle = {Proceedings of the Fifth Conference on Machine Translation},
year = {2020}
}
```

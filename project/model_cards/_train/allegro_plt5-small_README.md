---
language: pl
tags:
- T5
- translation
- summarization
- question answering
- reading comprehension
datasets:
- ccnet
- nkjp
- wikipedia
- open subtitles
- free readings
license: cc-by-4.0
---

# plT5 Small
**plT5** models are T5-based language models trained on Polish corpora. The models were optimized for the original T5 denoising target.

## Corpus
plT5 was trained on six different corpora available for Polish language:

| Corpus | Tokens | Documents |
| :------ | ------: | ------: |
| [CCNet Middle](https://github.com/facebookresearch/cc_net) | 3243M  | 7.9M |
| [CCNet Head](https://github.com/facebookresearch/cc_net) | 2641M  | 7.0M |
| [National Corpus of Polish](http://nkjp.pl/index.php?page=14&lang=1)| 1357M  | 3.9M |
| [Open Subtitles](http://opus.nlpl.eu/OpenSubtitles-v2018.php) | 1056M  | 1.1M 
| [Wikipedia](https://dumps.wikimedia.org/) | 260M  | 1.4M |
| [Wolne Lektury](https://wolnelektury.pl/) | 41M  | 5.5k |

## Tokenizer
The training dataset was tokenized into subwords using a sentencepiece unigram model with
vocabulary size of 50k tokens. 

## Usage
Example code:
```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("allegro/plt5-small")
model = AutoModel.from_pretrained("allegro/plt5-small")
```

## License
CC BY 4.0

## Citation
If you use this model, please cite the following paper:
```
@article{chrabrowa2022evaluation,
  title={Evaluation of Transfer Learning for Polish with a Text-to-Text Model},
  author={Chrabrowa, Aleksandra and Dragan, {\L}ukasz and Grzegorczyk, Karol and Kajtoch, Dariusz and Koszowski, Miko{\l}aj and Mroczkowski, Robert and Rybak, Piotr},
  journal={arXiv preprint arXiv:2205.08808},
  year={2022}
}
```

## Authors
The model was trained by [**Machine Learning Research Team at Allegro**](https://ml.allegro.tech/) and [**Linguistic Engineering Group at Institute of Computer Science, Polish Academy of Sciences**](http://zil.ipipan.waw.pl/).

You can contact us at: <a href="mailto:klejbenchmark@allegro.pl">klejbenchmark@allegro.pl</a>
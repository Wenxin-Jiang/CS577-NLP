---
language:
- de
- en
pipeline_tag: feature-extraction
tags:
- semantic textual similarity
- sts
- semantic search
- sentence similarity
- paraphrasing
- documents retrieval
- passage retrieval
- information retrieval
- sentence-transformer
- feature-extraction
- transformers
task_categories:
- sentence-similarity
- feature-extraction
- text-retrieval
- other
library_name: sentence-transformers
---

# Model card for PM-AI/paraphrase-distilroberta-base-v2_de-en
For internal purposes and for testing, we have made a monolingual paraphrasing model from Sentence Transformers usable for _German + English_ via [Knowledge Distillation](https://arxiv.org/abs/2004.09813).
The decision was made in favor of [sentence-transformers/paraphrase-distilroberta-base-v2](https://huggingface.co/sentence-transformers/paraphrase-distilroberta-base-v2) because this model has no public available multilingual version (to our knowledge).
In addition, it has significantly more training samples compared to its predecessor: 83.3 million samples were used instead of 24.6 million samples.

## Training
1) Download of datasets
2) Execution of knowledge distillation

### Training Data
Datasets used based on [offical source](https://www.sbert.net/examples/training/paraphrases/README.html):
  - _AllNLI_
  - _sentence-compression_
  - _SimpleWiki_
  - _altlex_
  - _msmarco-triplets_
  - _quora_duplicates_
  - _coco_captions_
  - _flickr30k_captions_
  - _yahoo_answers_title_question_
  - _S2ORC_citation_pairs_
  - _stackexchange_duplicate_questions_
  - _wiki-atomic-edits_

### Training Execution

First we downloaded some german-english parallel datasets via [get_parallel_data_*.py](https://github.com/UKPLab/sentence-transformers/tree/b86eec31cf0a102ad786ba1ff31bfeb4998d3ca5/examples/training/multilingual).

These datasets are: _Tatoeba_, _WikiMatrix_, _TED2020_, _OpenSubtitles_, _Europarl_, _News-Commentary_

Then we started knowledge distillation with [make_multilingual_sys.py](https://github.com/UKPLab/sentence-transformers/blob/b86eec31cf0a102ad786ba1ff31bfeb4998d3ca5/examples/training/multilingual/make_multilingual_sys.py)

#### Parameterization of training
- **Script:** [make_multilingual_sys.py](https://github.com/UKPLab/sentence-transformers/blob/b86eec31cf0a102ad786ba1ff31bfeb4998d3ca5/examples/training/multilingual/make_multilingual_sys.py)
- **Datasets:** Tatoeba, WikiMatrix, TED2020, OpenSubtitles, Europarl, News-Commentary
- **GPU:** NVIDIA A40 (Driver Version: 515.48.07; CUDA Version: 11.7)
- **Batch Size:** 64
- **Max Sequence Length:** 256
- **Train Max Sentence Length:** 600
- **Max Sentences Per Train File:** 1000000 
- **Teacher Model:** [sentence-transformers/paraphrase-distilroberta-base-v2](https://huggingface.co/sentence-transformers/paraphrase-distilroberta-base-v2)
- **Student Model:** [xlm-roberta-base](https://huggingface.co/xlm-roberta-base)
- **Loss Function:** MSE Loss
- **Learning Rate:** 2e-5
- **Epochs:** 20
- **Evaluation Steps:** 10000
- **Warmup Steps:** 10000

### Acknowledgment

This work is a collaboration between [Technical University of Applied Sciences Wildau (TH Wildau)](https://en.th-wildau.de/) and [sense.ai.tion GmbH](https://senseaition.com/).
You can contact us via:
* [Philipp Müller (M.Eng.)](https://www.linkedin.com/in/herrphilipps); Author
* [Prof. Dr. Janett Mohnke](mailto:icampus@th-wildau.de); TH Wildau
* [Dr. Matthias Boldt, Jörg Oehmichen](mailto:info@senseaition.com); sense.AI.tion GmbH 

This work was funded by the European Regional Development Fund (EFRE) and the State of Brandenburg. Project/Vorhaben: "ProFIT: Natürlichsprachliche Dialogassistenten in der Pflege".

<div style="display:flex">
     <div style="padding-left:20px;">
          <a href="https://efre.brandenburg.de/efre/de/"><img src="https://huggingface.co/datasets/PM-AI/germandpr-beir/resolve/main/res/EFRE-Logo_rechts_oweb_en_rgb.jpeg" alt="Logo of European Regional Development Fund (EFRE)" width="200"/></a>
     </div>
     <div style="padding-left:20px;">
          <a href="https://www.senseaition.com"><img src="https://senseaition.com/wp-content/uploads/thegem-logos/logo_c847aaa8f42141c4055d4a8665eb208d_3x.png" alt="Logo of senseaition GmbH" width="200"/></a>
     </div>
     <div style="padding-left:20px;">
          <a href="https://www.th-wildau.de"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/TH_Wildau_Logo.png/640px-TH_Wildau_Logo.png" alt="Logo of TH Wildau" width="180"/></a>
     </div>
</div>
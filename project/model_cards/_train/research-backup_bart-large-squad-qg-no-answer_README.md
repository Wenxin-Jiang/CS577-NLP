
---
license: cc-by-4.0
metrics:
- bleu4
- meteor
- rouge-l
- bertscore
- moverscore
language: en
datasets:
- lmqg/qg_squad
pipeline_tag: text2text-generation
tags:
- question generation
widget:
- text: "<hl>  Beyonce further expanded her acting career, starring as blues singer Etta James in the 2008 musical biopic, Cadillac Records. <hl>"
  example_title: "Question Generation Example 1" 
- text: "<hl> Beyonce further expanded her acting career, starring as blues singer Etta James in the 2008 musical biopic, Cadillac Records. <hl>"
  example_title: "Question Generation Example 2" 
- text: "<hl> Beyonce further expanded her acting career, starring as blues singer Etta James in the 2008 musical biopic, Cadillac Records . <hl>"
  example_title: "Question Generation Example 3" 
model-index:
- name: research-backup/bart-large-squad-qg-no-answer
  results:
  - task:
      name: Text2text Generation
      type: text2text-generation
    dataset:
      name: lmqg/qg_squad
      type: default
      args: default
    metrics:
    - name: BLEU4 (Question Generation)
      type: bleu4_question_generation
      value: 23.47
    - name: ROUGE-L (Question Generation)
      type: rouge_l_question_generation
      value: 50.25
    - name: METEOR (Question Generation)
      type: meteor_question_generation
      value: 24.94
    - name: BERTScore (Question Generation)
      type: bertscore_question_generation
      value: 90.28
    - name: MoverScore (Question Generation)
      type: moverscore_question_generation
      value: 63.28
---

# Model Card of `research-backup/bart-large-squad-qg-no-answer`
This model is fine-tuned version of [facebook/bart-large](https://huggingface.co/facebook/bart-large) for question generation task on the [lmqg/qg_squad](https://huggingface.co/datasets/lmqg/qg_squad) (dataset_name: default) via [`lmqg`](https://github.com/asahi417/lm-question-generation).
This model is fine-tuned without answer information, i.e. generate a question only given a paragraph (note that normal model is fine-tuned to generate a question given a pargraph and an associated answer in the paragraph).

### Overview
- **Language model:** [facebook/bart-large](https://huggingface.co/facebook/bart-large)   
- **Language:** en  
- **Training data:** [lmqg/qg_squad](https://huggingface.co/datasets/lmqg/qg_squad) (default)
- **Online Demo:** [https://autoqg.net/](https://autoqg.net/)
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)

### Usage
- With [`lmqg`](https://github.com/asahi417/lm-question-generation#lmqg-language-model-for-question-generation-)
```python
from lmqg import TransformersQG

# initialize model
model = TransformersQG(language="en", model="research-backup/bart-large-squad-qg-no-answer")

# model prediction
questions = model.generate_q(list_context="William Turner was an English painter who specialised in watercolour landscapes", list_answer="William Turner")

```

- With `transformers`
```python
from transformers import pipeline

pipe = pipeline("text2text-generation", "research-backup/bart-large-squad-qg-no-answer")
output = pipe("<hl>  Beyonce further expanded her acting career, starring as blues singer Etta James in the 2008 musical biopic, Cadillac Records. <hl>")

```

## Evaluation


- ***Metric (Question Generation)***: [raw metric file](https://huggingface.co/research-backup/bart-large-squad-qg-no-answer/raw/main/eval/metric.first.sentence.paragraph_sentence.question.lmqg_qg_squad.default.json) 

|            |   Score | Type    | Dataset                                                        |
|:-----------|--------:|:--------|:---------------------------------------------------------------|
| BERTScore  |   90.28 | default | [lmqg/qg_squad](https://huggingface.co/datasets/lmqg/qg_squad) |
| Bleu_1     |   55.38 | default | [lmqg/qg_squad](https://huggingface.co/datasets/lmqg/qg_squad) |
| Bleu_2     |   39.27 | default | [lmqg/qg_squad](https://huggingface.co/datasets/lmqg/qg_squad) |
| Bleu_3     |   29.99 | default | [lmqg/qg_squad](https://huggingface.co/datasets/lmqg/qg_squad) |
| Bleu_4     |   23.47 | default | [lmqg/qg_squad](https://huggingface.co/datasets/lmqg/qg_squad) |
| METEOR     |   24.94 | default | [lmqg/qg_squad](https://huggingface.co/datasets/lmqg/qg_squad) |
| MoverScore |   63.28 | default | [lmqg/qg_squad](https://huggingface.co/datasets/lmqg/qg_squad) |
| ROUGE_L    |   50.25 | default | [lmqg/qg_squad](https://huggingface.co/datasets/lmqg/qg_squad) |



## Training hyperparameters

The following hyperparameters were used during fine-tuning:
 - dataset_path: lmqg/qg_squad
 - dataset_name: default
 - input_types: ['paragraph_sentence']
 - output_types: ['question']
 - prefix_types: None
 - model: facebook/bart-large
 - max_length: 512
 - max_length_output: 32
 - epoch: 4
 - batch: 32
 - lr: 5e-05
 - fp16: False
 - random_seed: 1
 - gradient_accumulation_steps: 4
 - label_smoothing: 0.15

The full configuration can be found at [fine-tuning config file](https://huggingface.co/research-backup/bart-large-squad-qg-no-answer/raw/main/trainer_config.json).

## Citation
```
@inproceedings{ushio-etal-2022-generative,
    title = "{G}enerative {L}anguage {M}odels for {P}aragraph-{L}evel {Q}uestion {G}eneration",
    author = "Ushio, Asahi  and
        Alva-Manchego, Fernando  and
        Camacho-Collados, Jose",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, U.A.E.",
    publisher = "Association for Computational Linguistics",
}

```

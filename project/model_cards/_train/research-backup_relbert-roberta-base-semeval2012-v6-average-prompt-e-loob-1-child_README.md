---
datasets:
- relbert/semeval2012_relational_similarity_v6
model-index:
- name: relbert/relbert-roberta-base-semeval2012-v6-average-prompt-e-loob-1-child
  results:
  - task:
      name: Relation Mapping
      type: sorting-task
    dataset:
      name: Relation Mapping
      args: relbert/relation_mapping
      type: relation-mapping
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.6601587301587302
  - task:
      name: Analogy Questions (SAT full)
      type: multiple-choice-qa
    dataset:
      name: SAT full
      args: relbert/analogy_questions
      type: analogy-questions
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.32620320855614976
  - task:
      name: Analogy Questions (SAT)
      type: multiple-choice-qa
    dataset:
      name: SAT
      args: relbert/analogy_questions
      type: analogy-questions
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.314540059347181
  - task:
      name: Analogy Questions (BATS)
      type: multiple-choice-qa
    dataset:
      name: BATS
      args: relbert/analogy_questions
      type: analogy-questions
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.5797665369649806
  - task:
      name: Analogy Questions (Google)
      type: multiple-choice-qa
    dataset:
      name: Google
      args: relbert/analogy_questions
      type: analogy-questions
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.74
  - task:
      name: Analogy Questions (U2)
      type: multiple-choice-qa
    dataset:
      name: U2
      args: relbert/analogy_questions
      type: analogy-questions
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.40789473684210525
  - task:
      name: Analogy Questions (U4)
      type: multiple-choice-qa
    dataset:
      name: U4
      args: relbert/analogy_questions
      type: analogy-questions
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.3888888888888889
  - task:
      name: Lexical Relation Classification (BLESS)
      type: classification
    dataset:
      name: BLESS
      args: relbert/lexical_relation_classification
      type: relation-classification
    metrics:
    - name: F1
      type: f1
      value: 0.8665059514841043
    - name: F1 (macro)
      type: f1_macro
      value: 0.8544549779914162
  - task:
      name: Lexical Relation Classification (CogALexV)
      type: classification
    dataset:
      name: CogALexV
      args: relbert/lexical_relation_classification
      type: relation-classification
    metrics:
    - name: F1
      type: f1
      value: 0.7387323943661972
    - name: F1 (macro)
      type: f1_macro
      value: 0.4738233300793316
  - task:
      name: Lexical Relation Classification (EVALution)
      type: classification
    dataset:
      name: BLESS
      args: relbert/lexical_relation_classification
      type: relation-classification
    metrics:
    - name: F1
      type: f1
      value: 0.547670639219935
    - name: F1 (macro)
      type: f1_macro
      value: 0.5381712207517232
  - task:
      name: Lexical Relation Classification (K&H+N)
      type: classification
    dataset:
      name: K&H+N
      args: relbert/lexical_relation_classification
      type: relation-classification
    metrics:
    - name: F1
      type: f1
      value: 0.9487375669472073
    - name: F1 (macro)
      type: f1_macro
      value: 0.8583408575195632
  - task:
      name: Lexical Relation Classification (ROOT09)
      type: classification
    dataset:
      name: ROOT09
      args: relbert/lexical_relation_classification
      type: relation-classification
    metrics:
    - name: F1
      type: f1
      value: 0.7928549044186776
    - name: F1 (macro)
      type: f1_macro
      value: 0.7754996273278022

---
# relbert/relbert-roberta-base-semeval2012-v6-average-prompt-e-loob-1-child

RelBERT fine-tuned from [roberta-base](https://huggingface.co/roberta-base) on  
[relbert/semeval2012_relational_similarity_v6](https://huggingface.co/datasets/relbert/semeval2012_relational_similarity_v6).
Fine-tuning is done via [RelBERT](https://github.com/asahi417/relbert) library (see the repository for more detail).
It achieves the following results on the relation understanding tasks:
- Analogy Question ([dataset](https://huggingface.co/datasets/relbert/analogy_questions), [full result](https://huggingface.co/relbert/relbert-roberta-base-semeval2012-v6-average-prompt-e-loob-1-child/raw/main/analogy.json)):
    - Accuracy on SAT (full): 0.32620320855614976 
    - Accuracy on SAT: 0.314540059347181
    - Accuracy on BATS: 0.5797665369649806
    - Accuracy on U2: 0.40789473684210525
    - Accuracy on U4: 0.3888888888888889
    - Accuracy on Google: 0.74
- Lexical Relation Classification ([dataset](https://huggingface.co/datasets/relbert/lexical_relation_classification), [full result](https://huggingface.co/relbert/relbert-roberta-base-semeval2012-v6-average-prompt-e-loob-1-child/raw/main/classification.json)):
    - Micro F1 score on BLESS: 0.8665059514841043
    - Micro F1 score on CogALexV: 0.7387323943661972
    - Micro F1 score on EVALution: 0.547670639219935
    - Micro F1 score on K&H+N: 0.9487375669472073
    - Micro F1 score on ROOT09: 0.7928549044186776
- Relation Mapping ([dataset](https://huggingface.co/datasets/relbert/relation_mapping), [full result](https://huggingface.co/relbert/relbert-roberta-base-semeval2012-v6-average-prompt-e-loob-1-child/raw/main/relation_mapping.json)):
    - Accuracy on Relation Mapping: 0.6601587301587302 


### Usage
This model can be used through the [relbert library](https://github.com/asahi417/relbert). Install the library via pip   
```shell
pip install relbert
```
and activate model as below.
```python
from relbert import RelBERT
model = RelBERT("relbert/relbert-roberta-base-semeval2012-v6-average-prompt-e-loob-1-child")
vector = model.get_embedding(['Tokyo', 'Japan'])  # shape of (1024, )
```

### Training hyperparameters

The following hyperparameters were used during training:
 - model: roberta-base
 - max_length: 64
 - mode: average
 - data: relbert/semeval2012_relational_similarity_v6
 - split: train
 - split_eval: validation
 - template_mode: manual
 - loss_function: info_loob
 - classification_loss: False
 - temperature_nce_constant: 0.05
 - temperature_nce_rank: {'min': 0.01, 'max': 0.05, 'type': 'linear'}
 - epoch: 9
 - batch: 128
 - lr: 5e-06
 - lr_decay: False
 - lr_warmup: 1
 - weight_decay: 0
 - random_seed: 1
 - exclude_relation: None
 - n_sample: 320
 - gradient_accumulation: 8
 - relation_level: None
 - data_level: child

The full configuration can be found at [fine-tuning parameter file](https://huggingface.co/relbert/relbert-roberta-base-semeval2012-v6-average-prompt-e-loob-1-child/raw/main/trainer_config.json).

### Reference
If you use any resource from RelBERT, please consider to cite our [paper](https://aclanthology.org/2021.eacl-demos.7/).

```

@inproceedings{ushio-etal-2021-distilling-relation-embeddings,
    title = "{D}istilling {R}elation {E}mbeddings from {P}re-trained {L}anguage {M}odels",
    author = "Ushio, Asahi  and
      Schockaert, Steven  and
      Camacho-Collados, Jose",
    booktitle = "EMNLP 2021",
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
}

```

---
language: 
  - en
tags:
- QA
license: cc-by-4.0
datasets:
- BoolQ
- CommonSenseQA
- DROP
- DuoRC
- HellaSWAG
- HotpotQA
- HybridQA
- NarrativeQA
- NaturalQuestionsShort
- NewsQA
- QAMR
- RACE
- SearchQA
- SIQA
- SQuAD
- TriviaQA-web
metrics:
- Accuracy
- Precision
- Recall
- F1
- MRR
- R@3
- R@5


---

BERT for Sequence Classification trained on QA Dataset prediction task. 
- Input: question. 
- Output: dataset from where that question comes from.
Original paper: TWEAC: Transformer with Extendable QA Agent Classifiers
https://arxiv.org/abs/2104.07081

Datasets used for training:
```
list_datasets = ['BoolQ','CommonSenseQA','DROP','DuoRC','HellaSWAG','HotpotQA','HybridQA','NarrativeQA','NaturalQuestionsShort','NewsQA','QAMR','RACE','SearchQA','SIQA','SQuAD','TriviaQA-web']
```

Results for all datasets:
- Accuracy: 0.7919096825783123
- Precision: 0.731586272892176
- Recall: 0.7919096825783123
- F1: 0.7494425609552463
- MRR: 0.8720871733637521
- R@3: 0.9438690810655046
- R@5: 0.9745318608004427
- Queries/second: 6052.33538824659


Results per dataset:
```
"BoolQ": {
            "accuracy": 0.998776758409786,
            "mrr": 0.999388379204893,
            "r@3": 1.0,
            "r@5": 1.0,
            "query_per_second": 6978.947907596168,
            "precision": 0.8649364406779662,
            "recall": 0.998776758409786,
            "f1": 0.9270508089696281
        },
        "CommonSenseQA": {
            "accuracy": 0.9247135842880524,
            "mrr": 0.9476358338878795,
            "r@3": 0.9705400981996727,
            "r@5": 0.9705400981996727,
            "query_per_second": 5823.984138936813,
            "precision": 0.442443226311668,
            "recall": 0.9247135842880524,
            "f1": 0.5985169491525425
        },
        "DROP": {
            "accuracy": 0.9075083892617449,
            "mrr": 0.9378200367399193,
            "r@3": 0.9609899328859061,
            "r@5": 0.9786073825503355,
            "query_per_second": 6440.988897129248,
            "precision": 0.8636726546906187,
            "recall": 0.9075083892617449,
            "f1": 0.8850480670893842
        },
        "DuoRC": {
            "accuracy": 0.5555803405457654,
            "mrr": 0.7368963429107307,
            "r@3": 0.9092125808610305,
            "r@5": 0.9596996059186557,
            "query_per_second": 6853.643198794893,
            "precision": 0.646814404432133,
            "recall": 0.5555803405457654,
            "f1": 0.5977360905563778
        },
        "HellaSWAG": {
            "accuracy": 0.998406691894045,
            "mrr": 0.9990705702715262,
            "r@3": 1.0,
            "r@5": 1.0,
            "query_per_second": 3091.5012960785157,
            "precision": 0.9974134500596896,
            "recall": 0.998406691894045,
            "f1": 0.9979098238280083
        },
        "HotpotQA": {
            "accuracy": 0.7414435784479837,
            "mrr": 0.8435804344945315,
            "r@3": 0.9325652321247034,
            "r@5": 0.973568281938326,
            "query_per_second": 4972.668019223381,
            "precision": 0.7352150537634409,
            "recall": 0.7414435784479837,
            "f1": 0.7383161801923401
        },
        "HybridQA": {
            "accuracy": 0.7934218118869013,
            "mrr": 0.8806947764680021,
            "r@3": 0.964800923254472,
            "r@5": 0.9930755914598961,
            "query_per_second": 4886.494046259562,
            "precision": 0.7198952879581152,
            "recall": 0.7934218118869013,
            "f1": 0.7548723579467472
        },
        "NarrativeQA": {
            "accuracy": 0.5623756749076442,
            "mrr": 0.7416681781060867,
            "r@3": 0.9011082693947144,
            "r@5": 0.9580373212086767,
            "query_per_second": 7081.067049796865,
            "precision": 0.5623224095472628,
            "recall": 0.5623756749076442,
            "f1": 0.5623490409661377
        },
        "NaturalQuestionsShort": {
            "accuracy": 0.7985353692739171,
            "mrr": 0.8743599435345307,
            "r@3": 0.9439077594266126,
            "r@5": 0.9774072919912745,
            "query_per_second": 7136.590426649795,
            "precision": 0.7963020509633313,
            "recall": 0.7985353692739171,
            "f1": 0.7974171464135678
        },
        "NewsQA": {
            "accuracy": 0.5375118708452041,
            "mrr": 0.71192075967717,
            "r@3": 0.855650522317189,
            "r@5": 0.939696106362773,
            "query_per_second": 7193.851409052092,
            "precision": 0.18757249378624688,
            "recall": 0.5375118708452041,
            "f1": 0.2780985136961061
        },
        "QAMR": {
            "accuracy": 0.6658497602557272,
            "mrr": 0.7969741223377345,
            "r@3": 0.9207778369738945,
            "r@5": 0.973361747469366,
            "query_per_second": 7321.775044800525,
            "precision": 0.8654525309881587,
            "recall": 0.6658497602557272,
            "f1": 0.7526421968624852
        },
        "RACE": {
            "accuracy": 0.8771538617474154,
            "mrr": 0.917901778042666,
            "r@3": 0.9489154672613015,
            "r@5": 0.9693898236367322,
            "query_per_second": 6952.225120744351,
            "precision": 0.8767983789260385,
            "recall": 0.8771538617474154,
            "f1": 0.8769760843129306
        },
        "SearchQA": {
            "accuracy": 0.9762073027090695,
            "mrr": 0.9865069592101393,
            "r@3": 0.9972909305064782,
            "r@5": 0.9984687868080094,
            "query_per_second": 4031.0193826035634,
            "precision": 0.9870191735143503,
            "recall": 0.9762073027090695,
            "f1": 0.9815834665719192
        },
        "SIQA": {
            "accuracy": 0.9969293756397134,
            "mrr": 0.9977823268509042,
            "r@3": 0.9979529170931423,
            "r@5": 1.0,
            "query_per_second": 6711.547709005977,
            "precision": 0.9329501915708812,
            "recall": 0.9969293756397134,
            "f1": 0.9638792676892627
        },
        "SQuAD": {
            "accuracy": 0.550628092881614,
            "mrr": 0.7164538452390565,
            "r@3": 0.8660068519223448,
            "r@5": 0.9366197183098591,
            "query_per_second": 7033.420124363291,
            "precision": 0.48613678373382624,
            "recall": 0.550628092881614,
            "f1": 0.5163766175814368
        },
        "TriviaQA-web": {
            "accuracy": 0.7855124582584125,
            "mrr": 0.8647404868442627,
            "r@3": 0.9321859748266119,
            "r@5": 0.9640380169535063,
            "query_per_second": 4327.642440910395,
            "precision": 0.7404358353510896,
            "recall": 0.7855124582584125,
            "f1": 0.7623083634550667
        },
```
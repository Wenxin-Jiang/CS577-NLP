---
pipeline_tag: zero-shot-classification
datasets:
- snli
- anli
- multi_nli
- multi_nli_mismatch
- fever
---

# A2T Entailment model

**Important:** These pretrained entailment models are intended to be used with the [Ask2Transformers](https://github.com/osainz59/Ask2Transformers) library but are also fully compatible with the `ZeroShotTextClassificationPipeline` from [Transformers](https://github.com/huggingface/Transformers).


Textual Entailment (or Natural Language Inference) has turned out to be a good choice for zero-shot text classification problems [(Yin et al., 2019](https://aclanthology.org/D19-1404/); [Wang et al., 2021](https://arxiv.org/abs/2104.14690); [Sainz and Rigau, 2021)](https://aclanthology.org/2021.gwc-1.6/). Recent research addressed Information Extraction problems with the same idea [(Lyu et al., 2021](https://aclanthology.org/2021.acl-short.42/); [Sainz et al., 2021](https://aclanthology.org/2021.emnlp-main.92/); [Sainz et al., 2022a](), [Sainz et al., 2022b)](https://arxiv.org/abs/2203.13602). The A2T entailment models are first trained with NLI datasets such as MNLI [(Williams et al., 2018)](), SNLI [(Bowman et al., 2015)]() or/and ANLI [(Nie et al., 2020)]() and then fine-tuned to specific tasks that were previously converted to textual entailment format.

For more information please, take a look to the [Ask2Transformers](https://github.com/osainz59/Ask2Transformers) library or the following published papers:

- [Label Verbalization and Entailment for Effective Zero and Few-Shot Relation Extraction (Sainz et al., EMNLP 2021)](https://aclanthology.org/2021.emnlp-main.92/)
- [Textual Entailment for Event Argument Extraction: Zero- and Few-Shot with Multi-Source Learning (Sainz et al., Findings of NAACL-HLT 2022)]()

## About the model

The model name describes the configuration used for training as follows:

<!-- $$\text{HiTZ/A2T\_[pretrained\_model]\_[NLI\_datasets]\_[finetune\_datasets]}$$ -->

<h3 align="center">HiTZ/A2T_[pretrained_model]_[NLI_datasets]_[finetune_datasets]</h3>


- `pretrained_model`: The checkpoint used for initialization. For example: RoBERTa<sub>large</sub>.
- `NLI_datasets`: The NLI datasets used for pivot training.
    - `S`: Standford Natural Language Inference (SNLI) dataset.
    - `M`: Multi Natural Language Inference (MNLI) dataset.
    - `F`: Fever-nli dataset.
    - `A`: Adversarial Natural Language Inference (ANLI) dataset.
- `finetune_datasets`: The datasets used for fine tuning the entailment model. Note that for more than 1 dataset the training was performed sequentially. For example: ACE-arg.

Some models like `HiTZ/A2T_RoBERTa_SMFA_ACE-arg` have been trained marking some information between square brackets (`'[['` and `']]'`) like the event trigger span. Make sure you follow the same preprocessing in order to obtain the best results.

## Cite

If you use this model, consider citing the following publications:

```bibtex
@inproceedings{sainz-etal-2021-label,
    title = "Label Verbalization and Entailment for Effective Zero and Few-Shot Relation Extraction",
    author = "Sainz, Oscar  and
      Lopez de Lacalle, Oier  and
      Labaka, Gorka  and
      Barrena, Ander  and
      Agirre, Eneko",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-main.92",
    doi = "10.18653/v1/2021.emnlp-main.92",
    pages = "1199--1212",
}
```
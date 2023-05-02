---
model-index:
- name: Sociovestix/lenu_GB
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: lenu
      type: Sociovestix/lenu
      config: GB
      split: test
      revision: fbe0b4b5b8d6950c10f5710f2c987728635a4afe
    metrics:
    - type: f1
      value: 0.9678813672030855
      name: f1
    - type: f1
      value: 0.47558542146995103
      name: f1 macro
      args:
        average: macro
widget:
- text: "PIPER JAVELIN HOLDING COMPANY LIMITED"
- text: "HEVEA BURMA (GROUP) PLC"
- text: "PE & AM LTD"
- text: "CLAVIS 2006-1 NIM PLC"
- text: "H2O AM LLP"
- text: "BRIDGES VENTURES FUND III LP"
- text: "Mountlands Trust Limited"
- text: "TM VERITAS INVESTMENT ICVC"
- text: "SOUTH YORKSHIRE PENSIONS AUTHORITY"
- text: "TRADES UNION CONGRESS SUPERANNUATION SOCIETY LIMITED"
- text: "UNIVERSITY OF NOTTINGHAM (THE)"
- text: "DARLINGTON BUILDING SOCIETY"
- text: "FAMILY ASSURANCE FRIENDLY SOCIETY LIMITED"
- text: "LARNE CREDIT UNION LIMITED"
- text: "MESSRS HOARE TRUSTEES"
- text: "R.M.T. Credit Union Limited"
- text: "SANTA FE S.P."
- text: "Network Rail Pension Trustee Limited"
- text: "EFT INVESTMENTS UK SOCIETAS"
---

# LENU - Legal Entity Name Understanding for Great Britain


A [finbert](https://huggingface.co/yiyanghkust/finbert-pretrain) model fine-tuned on british legal entity names (jurisdiction GB) from the Global [Legal Entity Identifier](https://www.gleif.org/en/about-lei/introducing-the-legal-entity-identifier-lei)
(LEI) System with the goal to detect [Entity Legal Form (ELF) Codes](https://www.gleif.org/en/about-lei/code-lists/iso-20275-entity-legal-forms-code-list).

---------------

<h1 align="center">
<a href="https://gleif.org">
<img src="http://sdglabs.ai/wp-content/uploads/2022/07/gleif-logo-new.png" width="220px" style="display: inherit">
</a>
</h1><br>
<h3 align="center">in collaboration with</h3> 
<h1 align="center">
<a href="https://sociovestix.com">
<img src="https://sociovestix.com/img/svl_logo_centered.svg" width="700px" style="width: 100%">
</a>
</h1><br>

---------------

## Model Description

<!-- Provide a longer summary of what this model is. -->

The model has been created as part of a collaboration of the [Global Legal Entity Identifier Foundation](https://gleif.org) (GLEIF) and
[Sociovestix Labs](https://sociovestix.com) with the goal to explore how Machine Learning can support in detecting the ELF Code solely based on an entity's legal name and legal jurisdiction.
See also the open source python library [lenu](https://github.com/Sociovestix/lenu), which supports in this task.

The model has been trained on the dataset [lenu](https://huggingface.co/datasets/Sociovestix), with a focus on british legal entities and ELF Codes within the Jurisdiction "GB".

- **Developed by:** [GLEIF](https://gleif.org) and [Sociovestix Labs](https://huggingface.co/Sociovestix)
- **License:** Creative Commons (CC0) license
- **Finetuned from model [optional]:** yiyanghkust/finbert-pretrain
- **Resources for more information:** [Press Release](https://www.gleif.org/en/newsroom/press-releases/machine-learning-new-open-source-tool-developed-by-gleif-and-sociovestix-labs-enables-organizations-everywhere-to-automatically-)

# Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

An entity's legal form is a crucial component when verifying and screening organizational identity.
The wide variety of entity legal forms that exist within and between jurisdictions, however, has made it difficult for large organizations to capture legal form as structured data.
The Jurisdiction specific models of [lenu](https://github.com/Sociovestix/lenu), trained on entities from
GLEIF’s Legal Entity Identifier (LEI) database of over two million records, will allow banks, 
investment firms, corporations, governments, and other large organizations to retrospectively analyze
their master data, extract the legal form from the unstructured text of the legal name and
uniformly apply an ELF code to each entity type, according to the ISO 20275 standard.


# Licensing Information

This model, which is trained on LEI data, is available under Creative Commons (CC0) license. 
See [gleif.org/en/about/open-data](https://gleif.org/en/about/open-data).

# Recommendations

Users should always consider the score of the suggested ELF Codes. For low score values it may be necessary to manually review the affected entities.

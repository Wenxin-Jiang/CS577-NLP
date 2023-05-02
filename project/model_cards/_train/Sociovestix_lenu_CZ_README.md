---
model-index:
- name: Sociovestix/lenu_CZ
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: lenu
      type: Sociovestix/lenu
      config: CZ
      split: test
      revision: fbe0b4b5b8d6950c10f5710f2c987728635a4afe
    metrics:
    - type: f1
      value: 0.9935219911353563
      name: f1
    - type: f1
      value: 0.7750705528144344
      name: f1 macro
      args:
        average: macro
widget:
- text: "ALU – SV CZ, s.r.o."
- text: "CZ STAVEBNÍ HOLDING, a.s."
- text: "NOVA Real Estate - podfond 1"
- text: "Město Libušín"
- text: "Ing. Jan Řezník"
- text: "Stavební bytové družstvo Jindřichův Hradec"
- text: "SHERLOG SE"
- text: "Interim Investment svěřenský fond"
- text: "Arcidiecézní charita Praha"
- text: "Nadace Kardiocentrum České Budějovice"
- text: "Svaz modelářů České republiky z.s."
- text: "VAN GRAAF, k.s."
- text: "Odbory KOVO MB"
- text: "Vilau v.o.s."
- text: "Společenství vlastníků jednotek Purkyňova 1106/17, Opava"
- text: "OSMA - ČR - OJ034"
- text: "Římskokatolická farnost Těchlovice"
- text: "Nadační fond TELEPACE"
- text: "MILNEA státní podnik v likvidaci"
- text: "ČIPA, o.p.s."
- text: "Ústav pro evropskou integraci z.ú."
- text: "AWP P&C Česká republika - odštěpný závod zahraniční právnické osoby"
- text: "Moravskoslezský kraj"
- text: "ecoenerg Windkraft GmbH & Co. KG, organizační složka"
- text: "Ústav experimentální botaniky AV ČR, v. v. i."
- text: "NIX.CZ, z.s.p.o."
- text: "Obvodní soud pro Prahu 9"
- text: "Svazek obcí pro vodovody a kanalizace Šlapanicko"
- text: "Intel Czech Tradings, Inc., organizační složka"
---

# LENU - Legal Entity Name Understanding for Czech Republic

A Bert (multilingual uncased) model fine-tuned on czech legal entity names (jurisdiction CZ) from the Global [Legal Entity Identifier](https://www.gleif.org/en/about-lei/introducing-the-legal-entity-identifier-lei)
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

The model has been trained on the dataset [lenu](https://huggingface.co/datasets/Sociovestix), with a focus on czech legal entities and ELF Codes within the Jurisdiction "CZ".

- **Developed by:** [GLEIF](https://gleif.org) and [Sociovestix Labs](https://huggingface.co/Sociovestix)
- **License:** Creative Commons (CC0) license
- **Finetuned from model [optional]:** bert-base-multilingual-uncased
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
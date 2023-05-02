---
language: 
- mr
tags:
- mr
- Sentiment-Analysis
license: cc-by-nc-4.0
widget:
- text: "मला तुम्ही आवडता. मी तुझ्यावर प्रेम करतो."
---

# Marathi-Bloom-560m is a Bloom fine-tuned model trained by ScriptEdge on MahaNLP tweets dataset from L3Cube-MahaNLP.

## Worked on by:

Trained by: 
  - Venkatesh Soni.


Assistance: 
  - Rayansh Srivastava.


Supervision: 
  - Akshay Ugale, Madhukar Alhat.


## Usage - 
- It is intended for non-commercial usages.


## Model best metrics
|                      *Model*                      |       *Data*        |     *Accuracy*    |
|---------------------------------------------------|---------------------|-------------------|
|    bigscience/bloom-560m                          |      Validation     |       34.7        |
|    bigscience/bloom-560m                          |        Test         |     **34.8**      |
|    ScriptEdgeAI/MarathiSentiment-Bloom-560m       |      Validation     |       76.0        |
|    ScriptEdgeAI/MarathiSentiment-Bloom-560m       |        Test         |     **77.0**      |


Citation to L3CubePune by the dataset usage.
```
@article {joshi2022l3cube,
  title= {L3Cube-MahaNLP: Marathi Natural Language Processing Datasets, Models, and Library},
  author= {Joshi, Raviraj},
  journal= {arXiv preprint arXiv:2205.14728},
  year= {2022}
}
```
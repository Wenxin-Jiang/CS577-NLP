---
tags:
- autotrain
- summarization
- Prompt Generation
language:
- unk
widget:
- text: "The authors present a new class of drugs that have the potential to treat kidney disease. In this study, they investigate the molecular and biological mechanisms behind the adverse effects of heavy metal poisoning caused by excessive use of end-resteroids. They examine several different pathways involved in the pathway of transcription and proteomics in order to tease out the etiology of the phenomenon of kidney toxicity from the pathophysiology. The authors suggest that an excess of lipoproteins leads to cataractosis, a chronic inflammation of the kidney, fibrosis, and kidney degeneration. They also show that certain enzymes, such as those involved in disrupterase and creatine kinase, are overexpressed in alenderrate-treated mouse models. Although the authors do not yet have specific treatments for either cataracts or kidney disease, they note that suppressing these pathways may be therapeutics in the treatment of patients with both types of disease. Lastly, the authors discuss the role of spirometry in this review of the literature. It was previously reported that spirometry had a significant effect on renal function in treating acute kidney disease. The authors argue that if spirometry is neglected, then all other aspects of kidney function--irregular growth, tissue growth, and apoptosis--will suffer as a result."
datasets:
- SamAct/autotrain-data-t3
co2_eq_emissions:
  emissions: 2.4412207269598545
---
## If you like this model you can by me a coffee here: https://www.buymeacoffee.com/SamAct
## Usecase
1. Prompt Generation.
2. Title Generation.

## Features
Excellent accuracy for one line prompts. Prompts can be used for image generation, title or meta descriptions.

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1353852105
- CO2 Emissions (in grams): 2.4412

## Validation Metrics

- Loss: 0.010
- Rouge1: 99.696
- Rouge2: 99.467
- RougeL: 99.689
- RougeLsum: 99.687
- Gen Len: 19.770

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "The authors present a new class of drugs that have the potential to treat kidney disease. In this study, they investigate the molecular and biological mechanisms behind the adverse effects of heavy metal poisoning caused by excessive use of end-resteroids. They examine several different pathways involved in the pathway of transcription and proteomics in order to tease out the etiology of the phenomenon of kidney toxicity from the pathophysiology. The authors suggest that an excess of lipoproteins leads to cataractosis, a chronic inflammation of the kidney, fibrosis, and kidney degeneration. They also show that certain enzymes, such as those involved in disrupterase and creatine kinase, are overexpressed in alenderrate-treated mouse models. Although the authors do not yet have specific treatments for either cataracts or kidney disease, they note that suppressing these pathways may be therapeutics in the treatment of patients with both types of disease. Lastly, the authors discuss the role of spirometry in this review of the literature. It was previously reported that spirometry had a significant effect on renal function in treating acute kidney disease. The authors argue that if spirometry is neglected, then all other aspects of kidney function--irregular growth, tissue growth, and apoptosis--will suffer as a result."}' https://api-inference.huggingface.co/SamAct/autotrain-t3-1353852105
```
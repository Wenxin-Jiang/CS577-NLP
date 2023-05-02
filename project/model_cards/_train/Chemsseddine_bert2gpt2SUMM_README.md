---
language: fr
widget:
- text: "Your text here"
datasets:
- Chemsseddine/autotrain-data-bertSummGpt2
co2_eq_emissions: 0.10685501288084795
---

<img src="https://huggingface.co/Chemsseddine/bert2gpt2_med_ml_orange_summ-finetuned_med_sum_new-finetuned_med_sum_new/resolve/main/logobert2gpt2.png" alt="Map of positive probabilities per country." width="200"/>

## This model is used for french summarization
- Problem type: Summarization
- Model ID: 980832493
- CO2 Emissions (in grams): 0.10685501288084795

## Validation Metrics

- Loss: 4.03749418258667
- Rouge1: 28.8384
- Rouge2: 10.7511
- RougeL: 27.0842
- RougeLsum: 27.5118
- Gen Len: 22.0625

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Chemsseddine/autotrain-bertSummGpt2-980832493
```
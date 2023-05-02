---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain \U0001F917"
datasets:
- L-macc/autotrain-data-Biomedical_sc_summ
co2_eq_emissions:
  emissions: 3198.3976606503647
model-index:
- name: L-macc/autotrain-Biomedical_sc_summ-1217846144
  results:
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: Blaise-g/SumPubmed
      type: Blaise-g/SumPubmed
      config: Blaise-g--SumPubmed
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 39.4086
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 12.8115
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 21.9191
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 35.2431
      verified: true
    - name: loss
      type: loss
      value: 2.2001051902770996
      verified: true
    - name: gen_len
      type: gen_len
      value: 133.8541
      verified: true
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1217846144
- CO2 Emissions (in grams): 3198.3977

## Validation Metrics

- Loss: 2.449
- Rouge1: 38.839
- Rouge2: 10.865
- RougeL: 21.994
- RougeLsum: 33.794
- Gen Len: 120.994

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/L-macc/autotrain-Biomedical_sc_summ-1217846144
```
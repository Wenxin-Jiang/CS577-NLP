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
  emissions: 16.211223325053414
model-index:
- name: L-macc/autotrain-Biomedical_sc_summ-1217846142
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
      value: 38.2324
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 12.2914
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 21.4512
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 34.3031
      verified: true
    - name: loss
      type: loss
      value: 2.3273825645446777
      verified: true
    - name: gen_len
      type: gen_len
      value: 130.3934
      verified: true
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1217846142
- CO2 Emissions (in grams): 16.2112

## Validation Metrics

- Loss: 2.159
- Rouge1: 40.236
- Rouge2: 12.161
- RougeL: 23.255
- RougeLsum: 35.138
- Gen Len: 121.504

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/L-macc/autotrain-Biomedical_sc_summ-1217846142
```
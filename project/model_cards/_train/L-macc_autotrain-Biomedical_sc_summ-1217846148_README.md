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
  emissions: 13.651986586580765
model-index:
- name: L-macc/autotrain-Biomedical_sc_summ-1217846148
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
      value: 40.1043
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 13.0457
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 22.2288
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 35.9295
      verified: true
    - name: loss
      type: loss
      value: 2.090137004852295
      verified: true
    - name: gen_len
      type: gen_len
      value: 139.7369
      verified: true
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1217846148
- CO2 Emissions (in grams): 13.6520

## Validation Metrics

- Loss: 2.503
- Rouge1: 38.768
- Rouge2: 10.791
- RougeL: 21.946
- RougeLsum: 33.780
- Gen Len: 123.331

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/L-macc/autotrain-Biomedical_sc_summ-1217846148
```
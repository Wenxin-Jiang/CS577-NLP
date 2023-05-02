---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain \U0001F917"
datasets:
- Jacobsith/autotrain-data-Hello_there
co2_eq_emissions:
  emissions: 3602.3174355473616
model-index:
- name: Jacobsith/autotrain-Hello_there-1209845735
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
      value: 38.2084
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 12.4744
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 21.5536
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 34.229
      verified: true
    - name: loss
      type: loss
      value: 2.0952045917510986
      verified: true
    - name: gen_len
      type: gen_len
      value: 126.3001
      verified: true
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1209845735
- CO2 Emissions (in grams): 3602.3174

## Validation Metrics

- Loss: 2.484
- Rouge1: 38.448
- Rouge2: 10.900
- RougeL: 22.080
- RougeLsum: 33.458
- Gen Len: 115.982

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Jacobsith/autotrain-Hello_there-1209845735
```
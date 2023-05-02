---
widget:
- text: 'Who was the first president of United States?'
 
tags:
  - text2text-generation
language:
- unk
datasets:
- Jonnylaw/autotrain-data-flan-t5-tunned
co2_eq_emissions:
  emissions: 4.95420834932979
---

# Flan-T5 large, trained to a lot of tasks.



## Validation Metrics

- Loss: 1.344
- Rouge1: 62.583
- Rouge2: 52.337
- RougeL: 59.779
- RougeLsum: 60.437
- Gen Len: 15.639

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/Jonnylaw/autotrain-flan-t5-tunned-3016686642
```
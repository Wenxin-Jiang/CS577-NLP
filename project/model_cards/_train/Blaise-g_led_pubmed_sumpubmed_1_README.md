---
tags:
- summarization
language:
- en
widget:
- text: "Biomedical paper of choice \U0001F917"
datasets:
- Blaise-g/autotrain-data-SumPubmed
- Blaise-g/SumPubmed
co2_eq_emissions:
  emissions: 1027.9
model-index:
- name: Blaise-g/led_pubmed_sumpubmed_1
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
      value: 41.2523
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 11.1291
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 20.2531
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 37.1502
      verified: true
    - name: loss
      type: loss
      value: 6.371099948883057
      verified: true
    - name: gen_len
      type: gen_len
      value: 193.3744
      verified: true
---

# Validation Metrics

- Loss: 2.133
- Rouge1: 45.861
- Rouge2: 14.179
- RougeL: 23.565
- RougeLsum: 40.908
- Gen Len: 195.334
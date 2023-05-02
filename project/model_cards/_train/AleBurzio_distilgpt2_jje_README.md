---
license: apache-2.0
tags:
- text generation
- judge
- jury
- executioner
datasets:
- biglam/old_bailey_proceedings
model-index:
- name: distilgpt2_jje
  results: []
widget:
 - text: "HAROLD KUMAR"
   example_title: "morning sun"
 - text: "Obama, he of no first name,"
   example_title: "Obama"
 - text: "John Smith,"
   example_title: "generic"
parameters:
  min_length: 16
  max_length: 96
  no_repeat_ngram_size: 1
  do_sample: True
---


# distilgpt2_jje (judge, jury, executioner)

`distilgpt2` fine-tuned on the `biglam/old_bailey_proceedings` dataset for two epochs.

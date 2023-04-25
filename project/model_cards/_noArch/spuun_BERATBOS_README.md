---
license: cc-by-sa-4.0
language:
- id
library_name: transformers
pipeline_tag: text-classification
---
# BERATBOS v0.0.1-prealpha
> BERT-based Automated Text Classification Based on POS

A model I made for my final year assignment, used a random script to train this on GPU,
as a result, the usage is kinda non-standard, as far as transformers-based models go, at least.

Model is for detecting AI-generated works via coherency comparison through POS tag differences,
it was only trained for 5 epochs on a dataset of 1000 human sentences and 1000 BLOOM-generated sentences.

![image.png](https://s3.amazonaws.com/moonup/production/uploads/1674149530163-605ac7c22bd7bebcc260c29e.png)

I have plans to further this model into an actual production model, 
but will only be done once I can properly assess on whether that's a worthy enough of an endeavour.
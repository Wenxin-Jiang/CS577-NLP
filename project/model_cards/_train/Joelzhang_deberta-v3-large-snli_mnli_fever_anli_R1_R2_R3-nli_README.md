---
language: 
- en
tags:
- text-classification
metrics:
- accuracy
datasets:
- snli-1.0
- multi-nli-1.0
- nli-fever
- anli-v1.0
widget:
- text: "British mountaineer Alison Hargreaves becomes the first woman to climb Mount Everest alone and without oxygen tanks. [SEP] Alison is a female."
- text: "Mr Lopez Obrador has alleged electoral fraud cost him the presidency, despite a recount confirming Felipe Calderon as Mexico's president-elect. [SEP] Mr Lopez Obrador was born in mexico."

---

## deberta-v3-large-snli_mnli_fever_anli_R1_R2_R3-nli

#### Datasets
This model was trained on the snli-v1.0, multi-nli-1.0, nli-fever and anli-1.0-r1/anli-1.0-r2/anli-1.0-r3 datasets with the training weights of 1,1,1,10,20,10 respectively.  
The training codes are mostly referenced from: https://github.com/facebookresearch/anli


#### Hyperparameters
learning_rate: 1e-5  
max_length: 156  
batch_size: 16  
warmup_ratio: 0.1   
weight_decay: 0.0   
num_epochs: 2


#### Dev results
snli-v1.0 | multi-nli-1.0-m | multi-nli-1.0-mm | anli-1.0-r1 | anli-1.0-r2 | anli-1.0-r3
----------|-----------------|------------------|-------------|-------------|------------
0.938 | 0.914 | 0.912 | 0.796 | 0.627 | 0.610


#### Test results
snli-v1.0 | anli-1.0-r1 | anli-1.0-r2 | anli-1.0-r3
-----------|-------------|-------------|------------
0.929 | 0.775 | 0.636 | 0.612
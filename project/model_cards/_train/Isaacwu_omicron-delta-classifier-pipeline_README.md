### Classifier of COVID-19 variant (omicron, delta)
This model takes complete neucleotide sequence as input and return its COVID variant (omicron and delta only)

## Model training
The model was pretrained with RoBERTa config, using all complete necleotide genome of COVID-19 on NCBI. The finetuning step uses ~10000 labeled training data for a binary classification task.\
For more details, please go to this [Powerpoint slides]( https://d24h-my.sharepoint.com/:p:/g/personal/isaacwu_d24h_hk/EYcJNznxuKdEmpfMP_R48yAB0zJa96L0W6RWbS-K6RSmVQ). 

## Label representation
- LABEL_0 is omicron
- LABEL_1 is delta

## Example input
Click the links to get a sequence neucleotide, then copy the ATCGs and paste it on the input field
- Delta sequence\
\>LC633760.1 Severe acute respiratory syndrome coronavirus 2 TKYTK1734_2021 genomic RNA, complete genome
[Click here to download](https://d24h-my.sharepoint.com/:t:/g/personal/isaacwu_d24h_hk/EU7_KEKf4VlBg0yf_EmoHY4BLLYM8cS3MkC-4FrNqiKp5w?e=Jmr8CS)
- Omicron sequence\
\>OM210115.1 Severe acute respiratory syndrome coronavirus 2 isolate SARS-CoV-2/human/USA/CO-CDPHE-2102509336/2021, complete genome
[Click here to download](https://d24h-my.sharepoint.com/:t:/g/personal/isaacwu_d24h_hk/ETWJgxp0nJJOlYOiWaiY5yQB2mz_o7nHg0-Vom0ens9P2Q)

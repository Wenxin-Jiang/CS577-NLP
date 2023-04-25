---
language:
- sv

---

# Megatron-BERT-base Swedish 600k

This BERT model was trained using the Megatron-LM library.
The size of the model is a regular BERT-base with 110M parameters.
The model was trained on about 70GB of data, consisting mostly of OSCAR and Swedish newspaper text curated by the National Library of Sweden.

Training was done for 600k training steps. Its [sister model](https://huggingface.co/KBLab/megatron-bert-base-swedish-cased-125k) used the same setup, but was instead trained for only 125k steps.


The model has three sister models trained on the same dataset:
- [🤗 BERT Swedish](https://huggingface.co/KBLab/bert-base-swedish-cased-new)
- [Megatron-BERT-base-125k](https://huggingface.co/KBLab/megatron-bert-base-swedish-cased-125k)
- [Megatron-BERT-large-110k](https://huggingface.co/KBLab/megatron-bert-large-swedish-cased-110k)

## Acknowledgements

We gratefully acknowledge the HPC RIVR consortium (https://www.hpc-rivr.si) and EuroHPC JU (https://eurohpc-ju.europa.eu) for funding this research by providing computing resources of the HPC system Vega at the Institute of Information Science (https://www.izum.si).
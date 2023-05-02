---
language:
- sv

---

# 🤗 BERT Swedish

This BERT model was trained using the 🤗 transformers library.
The size of the model is a regular BERT-base with 110M parameters.
The model was trained on about 70GB of data, consisting mostly of OSCAR and Swedish newspaper text curated by the National Library of Sweden.
To avoid excessive padding documents shorter than 512 tokens were concatenated into one large sequence of 512 tokens, and larger documents were split into multiple 512 token sequences, following https://github.com/huggingface/transformers/blob/master/examples/pytorch/language-modeling/run_mlm.py

Training was done for a bit more than 8 epochs with a batch size of 2048, resulting in a little less than 125k training steps.

The model has three sister models trained on the same dataset:
- [Megatron-BERT-base-125k](https://huggingface.co/KBLab/megatron-bert-base-swedish-cased-125k)
- [Megatron-BERT-base-600k](https://huggingface.co/KBLab/megatron-bert-base-swedish-cased-600k)
- [Megatron-BERT-large-110k](https://huggingface.co/KBLab/megatron-bert-large-swedish-cased-110k)

## Acknowledgements

We gratefully acknowledge the HPC RIVR consortium (https://www.hpc-rivr.si) and EuroHPC JU (https://eurohpc-ju.europa.eu) for funding this research by providing computing resources of the HPC system Vega at the Institute of Information Science (https://www.izum.si).
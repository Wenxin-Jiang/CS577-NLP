---
language: et
license: cc-by-4.0
datasets:
- ERRnews
---

# mBART ERRnews

Pretrained mbart-large-cc25 model finetuned on ERRnews Estonian news story dataset.

## How to use
Here is how to use this model to get a summary of a given text in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("TalTechNLP/mBART-ERRnews")
model = AutoModelForSeq2SeqLM.from_pretrained("TalTechNLP/mBART-ERRnews")

text = "Riigikogu rahanduskomisjon võttis esmaspäeval maha riigieelarvesse esitatud investeeringuettepanekutest siseministeeriumi investeeringud koolidele ja lasteaedadele, sest komisjoni hinnangul ei peaks siseministeerium tegelema investeeringutega väljaspoole oma vastutusala. Komisjoni esimees Aivar Kokk ütles, et komisjon lähtus otsuse tegemisel riigikontrolör Janar Holmi soovitusest ja seadustest."
inputs = tokenizer(text, return_tensors='pt', max_length=1024)

summary_ids = model.generate(inputs['input_ids'])
summary = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
```

## Training data

The mBART model was finetuned on [ERRnews](https://huggingface.co/datasets/TalTechNLP/ERRnews), a dataset consisting of 10 420
Estonian news story transcripts and summaries.

### Training

The model was trained on 2 cloud GPUs with a batch size of 16 for 16 epochs. The optimizer 
used is Adam with a learning rate of 5e-05, betas of 0.9 and 0.999.

## Evaluation results

This model achieves the following results:


| Dataset | ROUGE-1 | ROUGE-2 | ROUGE-L | ROUGE-L-SUM |
|:-------:|:-------:|:-------:|:-------:|:-----------:|
| ERRnews | 19.2    | 6.7     | 16.1    | 17.4        |


### BibTeX entry and citation info

```bibtex
article{henryabstractive,
          title={Abstractive Summarization of Broadcast News Stories for {Estonian}},
          author={Henry, H{\"a}rm and Tanel, Alum{\"a}e},
          journal={Baltic J. Modern Computing},
          volume={10},
          number={3},
          pages={511-524},
          year={2022}
        }
```
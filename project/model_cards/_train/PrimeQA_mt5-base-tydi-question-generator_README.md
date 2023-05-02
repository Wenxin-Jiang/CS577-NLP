---
license: apache-2.0
---

# Model description

This is an [mt5-base](https://huggingface.co/google/mt5-base) model, finetuned to generate questions using [TyDi QA](https://huggingface.co/datasets/tydiqa) dataset. It was trained to take the context and answer as input to generate questions.

# Overview

*Language model*: mT5-base \
*Language*: Arabic, Bengali, English, Finnish, Indonesian, Korean, Russian, Swahili, Telugu \
*Task*: Question Generation \
*Data*: TyDi QA

# Intented use and limitations
One can use this model to generate questions. Biases associated with pre-training of mT5 and TyDiQA dataset may be present.

## Usage
One can use this model directly in the [PrimeQA](https://github.com/primeqa/primeqa) framework as in this example [notebook](https://github.com/primeqa/primeqa/blob/main/notebooks/qg/tableqg_inference.ipynb).

Or 
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("PrimeQA/mt5-base-tydi-question-generator")
model = AutoModelForSeq2SeqLM.from_pretrained("PrimeQA/mt5-base-tydi-question-generator")

def get_question(answer, context, max_length=64):
  input_text = answer +" <<sep>> " + context
  features = tokenizer([input_text], return_tensors='pt')
  output = model.generate(input_ids=features['input_ids'], 
               attention_mask=features['attention_mask'],
               max_length=max_length)
  return tokenizer.decode(output[0])
context = "শচীন টেন্ডুলকারকে ক্রিকেট ইতিহাসের অন্যতম সেরা ব্যাটসম্যান হিসেবে গণ্য করা হয়।"
answer = "শচীন টেন্ডুলকার"
get_question(answer, context)
# output: ক্রিকেট ইতিহাসের অন্যতম সেরা ব্যাটসম্যান কে?
```

## Citation
```bibtex
@inproceedings{xue2021mt5,
  title={mT5: A Massively Multilingual Pre-trained Text-to-Text Transformer},
  author={Xue, Linting and Constant, Noah and Roberts, Adam and
          Kale, Mihir and Al-Rfou, Rami and Siddhant, Aditya and
          Barua, Aditya and Raffel, Colin},
  booktitle={Proceedings of the 2021 Conference of the North American
             Chapter of the Association for Computational Linguistics:
             Human Language Technologies},
  pages={483--498},
  year={2021}
}
```


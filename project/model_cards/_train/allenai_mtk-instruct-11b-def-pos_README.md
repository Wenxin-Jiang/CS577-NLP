---
language: multilingual
license: apache-2.0
datasets:
- natural instructions v2.0
---

# Model description

Tk-Instruct is a series of encoder-decoder Transformer models that are trained to solve various NLP tasks by following in-context instructions (plain language task definitions, k-shot examples, explanations, etc). Built upon the pre-trained [T5 models](https://arxiv.org/abs/1910.10683), they are fine-tuned on a large number of tasks & instructions that are collected in the [Natural Instructions benchmark](https://github.com/allenai/natural-instructions), which contains 1600+ tasks in 70+ broach categories in total. This enables the model to not only process the training tasks, but also generalize to many unseen tasks without further parameter update.

More resources for using the model:
- **Paper**: [link](https://arxiv.org/abs/2204.07705)
- **Code repository**: [Tk-Instruct](https://github.com/yizhongw/Tk-Instruct)
- **Official Website**: [Natural Instructions](https://instructions.apps.allenai.org/)
- **All released models**: [allenai/tk-instruct](https://huggingface.co/models?search=allenai/tk-instruct)

## Intended uses & limitations

Tk-Instruct can be used to do many NLP tasks by following instructions. 

### How to use

When instructing the model, task definition or demonstration examples or explanations should be prepended to the original input and fed into the model. You can easily try Tk-Instruct models as follows:

```python
>>> from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

>>> tokenizer = AutoTokenizer.from_pretrained("allenai/tk-instruct-3b-def")
>>> model = AutoModelForSeq2SeqLM.from_pretrained("allenai/tk-instruct-3b-def")

>>> input_ids = tokenizer.encode(
        "Definition: return the currency of the given country. Now complete the following example - Input: India. Output:", 
        return_tensors="pt")
>>> output = model.generate(input_ids, max_length=10)
>>> output = tokenizer.decode(output[0], skip_special_tokens=True)   # model should output 'Indian Rupee'

>>> input_ids = tokenizer.encode(
        "Definition: negate the following sentence. Input: John went to school. Output:", 
        return_tensors="pt")
>>> output = model.generate(input_ids, max_length=10)
>>> output = tokenizer.decode(output[0], skip_special_tokens=True)   # model should output 'John did not go to shool.'
```

### Limitations

We are still working on understanding the behaviors of these models, but here are several issues we have found:
- Models are generally sensitive to the instruction. Sometimes rewording the instruction can lead to very different output.
- Models are not always compliant to the instruction. Sometimes the model don't follow your instruction (e.g., when you ask the model to generate one sentence, it might still generate one word or a long story).
- Models might totally fail on some tasks.

If you find serious issues or any interesting result, you are welcome to share with us!

## Training data

Tk-Instruct is trained using the tasks & instructions in [Natural Instructions benchmark](https://github.com/allenai/natural-instructions), which contains 1600+ tasks in 70+ broach categories in total. We follow the official train/test split. Tk-Instruct model series were trained using 757 tasks, and mTk-Instruct series were trained using 1271 tasks (including some non-English tasks). 

The training tasks are in 64 broad categories, such as text categorization / question answering / sentiment analysis / summarization / grammar error detection / dialogue generation / etc. The other 12 categories are selected for evaluation.


## Training procedure

All our models are initialized from either T5 models or mT5 models. Because generating the output can be regarded as a form of language modeling, we used their [LM adapted version](https://github.com/google-research/text-to-text-transfer-transformer/blob/main/released_checkpoints.md#lm-adapted-t511lm100k). All data is converted into a text-to-text format, and models are fine-tuned to maximize the likelihood of the output sequence.

Our [released models](https://huggingface.co/models?search=allenai/tk-instruct) are in different sizes, and each of them was trained with a specific type of instruction encoding. For instance, `tk-instruct-3b-def-pos` was initialized from [t5-xl-lm-adapt](https://huggingface.co/google/t5-xl-lm-adapt), and it saw task definition & 2 positive examples as the instruction during training time.
Although they are trained with only one type of instruction encodings, we found they can usually work with other type of encodings at test time (see more in our paper).


### BibTeX entry and citation info
```bibtex
@article{wang2022benchmarking,
  title={Benchmarking Generalization via In-Context Instructions on 1,600+ Language Tasks},
  author={Yizhong Wang and Swaroop Mishra and Pegah Alipoormolabashi and Yeganeh Kordi and Amirreza Mirzaei and A. Arunkumar and Arjun Ashok and Arut Selvan Dhanasekaran and Atharva Naik and David Stap and Eshaan Pathak and Giannis Karamanolakis and Haizhi Gary Lai and Ishan Purohit and Ishani Mondal and Jacob Anderson and Kirby Kuznia and Krima Doshi and Maitreya Patel and Kuntal Kumar Pal and M. Moradshahi and Mihir Parmar and Mirali Purohit and Neeraj Varshney and Phani Rohitha Kaza and Pulkit Verma and Ravsehaj Singh Puri and Rushang Karia and Shailaja Keyur Sampat and Savan Doshi and Siddharth Deepak Mishra and Sujan C. Reddy and Sumanta Patro and Tanay Dixit and Xu-dong Shen and Chitta Baral and Yejin Choi and Hannaneh Hajishirzi and Noah A. Smith and Daniel Khashabi},
  year={2022},
  archivePrefix={arXiv},
  eprint={2204.07705},
  primaryClass={cs.CL},
}
```
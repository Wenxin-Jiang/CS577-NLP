---
license: cc-by-nc-3.0
---

# T5-base model trained for text paraphrase 

You can load this model by:
```python
from transformers import T5ForConditionalGeneration,T5TokenizerFast

model = T5ForConditionalGeneration.from_pretrained(model_name_or_path)
tokenizer = T5TokenizerFast.from_pretrained(model_name_or_path)
```

A prefix "paraphrase: " should be added in font of the input sequence, i.e.:
```python
input_st = "paraphrase: " + text + " </s>"
```
You can find our scripts for generation in our [project GitHub](https://github.com/chiyuzhang94/PTSM/tree/main/paraphrase_generate)
Please find more training details in our paper:

[Decay No More: A Persistent Twitter Dataset for Learning Social Meaning](https://arxiv.org/pdf/2204.04611.pdf)

Accepted by 1st Workshop on Novel Evaluation Approaches for Text Classification Systems on Social Media @ ICWSM-2022

  ```
@inproceedings{zhang2022decay,
   title={Decay No More: A Persistent Twitter Dataset for Learning Social Meaning},
   author={Zhang, Chiyu and Abdul-Mageed, Muhammad and Nagoudi, El Moatez Billah},
   booktitle ={Proceedings of 1st Workshop on Novel Evaluation Approaches for Text Classification Systems on Social Media (NEATCLasS)}, 
   year={2022},
   url = {https://arxiv.org/pdf/2204.04611.pdf},
   publisher = {{AAAI} Press}, 
}
  ```
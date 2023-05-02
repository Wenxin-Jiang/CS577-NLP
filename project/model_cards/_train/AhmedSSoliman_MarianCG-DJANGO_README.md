---
widget:
- text: "define the method i with an argument self."
- text: "substitute asvar for self.asvar."
- text: "convert host to lowercase."
- text: "for every var in self.vars," 
- text: "call the method parser.delete_first_token." 
---

```
```
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/mariancg-a-code-generation-transformer-model/code-generation-on-django)](https://paperswithcode.com/sota/code-generation-on-django?p=mariancg-a-code-generation-transformer-model)
```
```

# MarianCG: a code generation transformer model inspired by machine translation
This model is to improve the solving of the code generation problem and implement a transformer model that can work with high accurate results. We implemented MarianCG transformer model which is a code generation model that can be able to generate code from natural language. This work declares the impact of using Marian machine translation model for solving the problem of code generation. In our implementation, we prove that a machine translation model can be operated and working as a code generation model. Finally, we set the new contributors and state-of-the-art on CoNaLa reaching a BLEU score of 30.92 and Exact Match Accuracy of 6.2 in the code generation problem with CoNaLa dataset.

MarianCG model and its implementation with the code of training and the generated output is available at this repository:
https://github.com/AhmedSSoliman/MarianCG-NL-to-Code

DJANGO dataset is available at

https://huggingface.co/datasets/AhmedSSoliman/DJANGO

This model is avialable on the huggingface hub https://huggingface.co/AhmedSSoliman/MarianCG-DJANGO

```python
# Model and Tokenizer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# model_name = "AhmedSSoliman/MarianCG-NL-to-Code"
model = AutoModelForSeq2SeqLM.from_pretrained("AhmedSSoliman/MarianCG-DJANGO")
tokenizer = AutoTokenizer.from_pretrained("AhmedSSoliman/MarianCG-DJANGO")
# Input (Natural Language) and Output (Python Code)
NL_input = "define the method i with an argument self."
output = model.generate(**tokenizer(NL_input, padding="max_length", truncation=True, max_length=512, return_tensors="pt"))
output_code = tokenizer.decode(output[0], skip_special_tokens=True)
```

This model is available in spaces using gradio at: https://huggingface.co/spaces/AhmedSSoliman/MarianCG-DJANGO


---
Tasks:
- Translation
- Code Generation
- Text2Text Generation
- Text Generation
---



# Citation

We now have a [paper](https://doi.org/10.1186/s44147-022-00159-4) for this work and you can cite:

```
@article{soliman2022mariancg,
  title={MarianCG: a code generation transformer model inspired by machine translation},
  author={Soliman, Ahmed S and Hadhoud, Mayada M and Shaheen, Samir I},
  journal={Journal of Engineering and Applied Science},
  volume={69},
  number={1},
  pages={1--23},
  year={2022},
  publisher={SpringerOpen}
  url={https://doi.org/10.1186/s44147-022-00159-4}
}

```


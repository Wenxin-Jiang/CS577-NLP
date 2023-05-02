---
thumbnail: https://huggingface.co/Norod78/gpt-fluentui-flat-svg/raw/main/train/sample16.svg
license: mit
library_name: transformers
pipeline_tag: text-generation
widget:
  - text: <svg
---
# gpt-fluentui-flat-svg
A custom GPT model which was trained upon svg files.
Specifically the flat emoji variants from [Microsoft's FluentUI repo](https://github.com/microsoft/fluentui-emoji). 
These svn files only consist of "stand-alone" path elements which should make it simpler to train upon and sample from.

# training and dataset
Both Tokenizer and Model were trained using [aitextgen](https://docs.aitextgen.io/)
The python file which was used for training, the .txt file dataset and a few generated samples can be found [here](https://huggingface.co/Norod78/gpt-fluentui-flat-svg/tree/main/train)

# post processing and extracting .svg files from generated samples

```
    # Extract from generated output and into a seperate .svg file all sequences which starts with <svg and ends with:
    #  A. </svg>
    #  B. If the sequence does not end with </svg> then find the last > in the sequence and append </svg> to it
```

# generated samples
The generated samples below were also created with [this script](https://huggingface.co/Norod78/gpt-fluentui-flat-svg/blob/main/train/atg_train.py)
![sample16](https://huggingface.co/Norod78/gpt-fluentui-flat-svg/raw/main/train/sample16.svg)
![sample15](https://huggingface.co/Norod78/gpt-fluentui-flat-svg/raw/main/train/sample15.svg) 
![sample14](https://huggingface.co/Norod78/gpt-fluentui-flat-svg/raw/main/train/sample14.svg)

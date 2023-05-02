---
license: bsd-3-clause
---
# Maverick (Yurt's Python Code Generation Model)

## Model description
This code generation model was fine-tuned on Python code from a generic multi-language code generation model. This model was then pushed to 30% sparsity using Yurts' in-house technology without performance loss. In this specific instance, the class representation for the network is still dense. This particular model has 350M trainable parameters.

## Training data
This model was tuned on a subset of the Python data available in the BigQuery open-source [Github dataset](https://cloud.google.com/blog/topics/public-datasets/github-on-bigquery-analyze-all-the-open-source-code). 


## How to use 
The model is great at autocompleting based off of partially generated function signatures and class signatures. It is also decent at generating code base based off of natural language prompts with a comment. If you find something cool you can do with the model, be sure to share it with us!

Check out our [colab notebook](https://colab.research.google.com/drive/1NDO4X418HuPJzF8mFc6_ySknQlGIZMDU?usp=sharing) to see how to invoke the model and try it out.

## Feedback and Questions

Have any questions or feedback? Find us on [Discord](https://discord.gg/2x4rmSGER9). 
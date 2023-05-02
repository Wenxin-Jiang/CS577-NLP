---
language: 
  - en
  - code
  
license: "mit"

tags:
- Diff Model
- pytorch
- causal-lm
- code-generation
- The Pile
---

# Diff-Codegen-350M v2 Model Card

## Model Description

diff-codegen-350m-v2 is a diff model for code generation, released by [CarperAI](http://carper.ai/). A diff model is an autoregressive language model trained on edits to a piece of text, formatted in [Unified Diff Format](https://en.wikipedia.org/wiki/Diff#Unified_format). These diff models can suggest, given a section of text and a description of the desired change, an intelligent change to the text that fits the description, marking the lines added, changed, and deleted in diff format.

In comparison to few-shot prompting of normal code generation models, diff models are specialized for suggesting intelligent changes to existing code, particularly longer pieces of code and where a change is required to follow some natural language text description (provided in the form of a commit message).

This model is a fine-tune of [codegen-350m-mono](https://huggingface.co/Salesforce/codegen-350M-mono) by Salesforce, trained on a large dataset of commits scraped from GitHub.

diff-codegen-350m-v2 is an experimental research artifact and should be treated as such. We are releasing these results and this model in the hopes that it may be useful to the greater research community, especially those interested in LMs for code.

An example Colab notebook with a brief example of prompting the model is [here](https://colab.research.google.com/drive/1ySm6HYvALerDiGmk6g3pDz68V7fAtrQH#scrollTo=thvzNpmahNNx).

## Training Data

This model is a fine-tune of [codegen-350m-mono](https://huggingface.co/Salesforce/codegen-350M-mono) by Salesforce. This language model was first pre-trained on The Pile, an 800Gb dataset composed of varied web corpora. The datasheet and paper for the Pile can be found [here](https://arxiv.org/abs/2201.07311) and [here](https://arxiv.org/abs/2101.00027) respectively. The model was then fine-tuned on a large corpus of code data in multiple languages, before finally being fine-tuned on a Python code dataset. The Codegen paper with full details of these datasets can be found [here](https://arxiv.org/abs/2203.13474).

Our dataset for this fine-tune consists of commits from GitHub, obtained using the [Google BigQuery Public Dataset](https://cloud.google.com/blog/topics/public-datasets/github-on-bigquery-analyze-all-the-open-source-code), a public up to date snapshot of a huge number of open-source GitHub repositories. We took this dataset and filtered using [BigQuery](https://console.cloud.google.com/marketplace/details/github/github-repos) on the number of stars in the repository to exclude repos with less than 100 stars, and further restricted the query to only repositories with open-source non-copyleft licenses (e.g. MIT, Apache, etc) and commits with more than 10 characters in the commit message. We also restricted ourselves to a list of 22 popular programming, scripting, and markup languages, including Python, HTML, Bash scripts, SQL, C++, etc. This resulted in a dataset of 19 million commits after filtering.

Our diff model was trained on a dataset of commits from BigQuery, a large-scale dataset of many programming languages from GitHub repositories. We filtered the dataset by the number of stars in the repository (>100 stars), license (only open-source non-copyleft licensed code included), and length of file (files greater than 2048 tokens in length were excluded).

The model was trained using the Huggingface Codegen tokenizer.

## Training Details

The model was trained on 1.08 billion tokens for 1 epoch on 64 A100 GPUs, provided by [Stability AI](https://stability.ai/).

Each file was formatted as follows for input to the language model:

```
<NME> {FILE_NAME}
<BEF> {INPUT_FILE}
<MSG> {COMMIT_MESSAGE}
<DFF> {FILE_DIFF}
```

## Intended Uses and Limitations

Due to the model’s small size and restriction to code, one should not expect the model to generalize to domains beyond code and perform (successful) reasoning over large chunks of code. This model is intended to be used in prototyping code generation systems, and for solely experimental purposes. This model is provided without warranty and should not be used in commercial settings—even though the license permits.

## Limitations and Biases

Due to the short context length restriction and due to the fact that all repositories with under 100 stars were excluded, we expect our diff model to underperform on underrepresented languages, for instance Lean or Coq.

The output of this model should not be trusted as correct and secure code. This model should not be used in any mission critical setting where security is of importance. When running the output of this model, it should be done as much as possible in a sandbox, such as [gVisor](https://gvisor.dev), since it is very possible for the model to produce code which may delete files, send HTTP requests, or otherwise contain critical security vulnerabilities.

As with other language models, diff-codegen is prone to hallucination and biased, stereotyped, or toxic output. There are no guarantees of truthful output when generating from the model.

## Evaluation Results

See [our blog post](https://carper.ai/diff-model) for full evaluation results.

## Licensing

This model is licensed as MIT.

## Acknowledgements

We’d like to thank Honglu Fan, Harry Saini, Herbie Bradley, Reshinth Adithyan, and Joel Lehman for their efforts! Thanks to Nitarshan Rajkumar for feedback on this model card.

---
license: cc-by-nc-4.0
---

## Model Specification
- This is the **Republican** community GPT-2 language model, fine-tuned on 4.7M (~100M tokens) tweets of Republican Twitter users between 2019-01-01 and 2020-04-10. 
- For more details about the `CommunityLM` project, please refer to this [our paper](https://arxiv.org/abs/2209.07065) and [github](https://github.com/hjian42/communitylm) page. 
- In the paper, it is referred as the `Fine-tuned CommunityLM` for the Republican Twitter community. 

## How to use the model

- **PRE-PROCESSING**: when you apply the model on tweets, please make sure that tweets are preprocessed by the [TweetTokenizer](https://github.com/VinAIResearch/BERTweet/blob/master/TweetNormalizer.py) to get the best performance.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("CommunityLM/republican-twitter-gpt2")

model = AutoModelForCausalLM.from_pretrained("CommunityLM/republican-twitter-gpt2")
```

## References

If you use this repository in your research, please kindly cite [our paper](https://arxiv.org/abs/2209.07065): 

```bibtex
@inproceedings{jiang-etal-2022-communitylm,
    title = "CommunityLM: Probing Partisan Worldviews from Language Models",
     author = {Jiang, Hang and Beeferman, Doug and Roy, Brandon and Roy, Deb},
    booktitle = "Proceedings of the 29th International Conference on Computational Linguistics",
    year = "2022",
    publisher = "International Committee on Computational Linguistics",
}
```
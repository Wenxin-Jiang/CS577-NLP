## End-to-end Conversational search model
A end-to-end system of conversational search system for online shopping. It was introduced in [this paper](https://arxiv.org/abs/2109.05460) published on conference EMNLP.

## Model description
ConvSearch is an end-to-end conversational search system that deeply combines the dialog and search system to improve the search performance. In particular, the Product Search module leverages both structured product attributes and unstructured product text (e.g. profile), where the product text may contain phrases matching with utterances when schema is incomplete or when a product attribute value is missing. Putting together, our system has the advantage of both reduced error accumulation along individual modules, and enhanced robustness against product schema/knowledge gaps.

## Intended uses & limitations 
You can use the raw model to understand the dialog between consumer and server. The concatenated dialogs can be parsed into intents (e.g. inform, request, buy, et al.) and attributes of products.

You can also fine-tune this model on similar down-stream tasks, such as a dialog system for shopping in your scenario or customer service system. Since our model is seq-to-seq, any dialog system that can be reformed to seq-to-seq can be implemented based on this model.

## How to use 
You can use this model directly with:

  
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    tokenizer = AutoTokenizer.from_pretrained("LiqiangXiao/ConvSearch_QU")
    model = AutoModelForSeq2SeqLM.from_pretrained("LiqiangXiao/ConvSearch_QU")


## Training data
ConvSearch was pretrained on a dialog corpus with 49,999 dialogs/942,766 turns.

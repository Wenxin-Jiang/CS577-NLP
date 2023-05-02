---
license: mit
language:
- ja
pipeline_tag: text-generation
---
# Model Card for Tanrei/GPTSAN-japanese

![GPTSAN](https://github.com/tanreinama/GPTSAN/blob/main/report/logo-bk.png?raw=true)

General-purpose Swich transformer based Japanese language model 

GPTSAN has some unique features. It has a model structure of Prefix-LM. It works as a shifted Masked Language Model for Prefix Input tokens. Un-prefixed inputs behave like normal generative models.
The Spout vector is a GPTSAN specific input. Spout is pre-trained with random inputs, but you can specify a class of text or an arbitrary vector during fine-tuning. This allows you to indicate the tendency of the generated text.
GPTSAN has a sparse Feed Forward based on Switch-Transformer. You can also add other layers and train them partially. See the original [GPTSAN repository](https://github.com/tanreinama/GPTSAN/) for details.

## Text Generation

```python
>>> from transformers import AutoModel, AutoTokenizer, trainer_utils

>>> device = "cuda"
>>> model = AutoModel.from_pretrained("Tanrei/GPTSAN-japanese").to(device)
>>> tokenizer = AutoTokenizer.from_pretrained("Tanrei/GPTSAN-japanese")
>>> x_token = tokenizer("織田信長は、", return_tensors="pt")
>>> trainer_utils.set_seed(30)
>>> input_ids = x_token.input_ids.to(device)
>>> gen_token = model.generate(input_ids, max_new_tokens=50)
>>> tokenizer.decode(gen_token[0])
"織田信長は、政治・軍事の中枢まで掌握した政治家であり、日本史上類を見ない驚異的な軍事侵攻を続け..."
```




## Text Generation with Prefix-LM model

```python
>>> from transformers import AutoModel, AutoTokenizer, trainer_utils

>>> device = "cuda"
>>> model = AutoModel.from_pretrained("Tanrei/GPTSAN-japanese").to(device)
>>> tokenizer = AutoTokenizer.from_pretrained("Tanrei/GPTSAN-japanese")
>>> x_token = tokenizer("", prefix_text="織田信長は、", return_tensors="pt")
>>> trainer_utils.set_seed(30)
>>> input_ids = x_token.input_ids.to(device)
>>> token_type_ids = x_token.token_type_ids.to(device)
>>> gen_token = model.generate(input_ids, token_type_ids=token_type_ids, max_new_tokens=50)
>>> tokenizer.decode(gen_token[0])
"織田信長は、政治・外交で数々の戦果を上げるが、1568年からは、いわゆる本能寺の変で細川晴元に暗殺される..."
```


## Masked Language Model And Text Generation

```python
>>> from transformers import AutoModel, AutoTokenizer, trainer_utils

>>> device = "cuda"
>>> model = AutoModel.from_pretrained("Tanrei/GPTSAN-japanese").to(device)
>>> tokenizer = AutoTokenizer.from_pretrained("Tanrei/GPTSAN-japanese")
>>> x_token = tokenizer(
    "", prefix_text="武田信玄は、<|inputmask|>時代ファンならぜひ押さえ<|inputmask|>きたい名将の一人。", return_tensors="pt"
)
>>> trainer_utils.set_seed(30)
>>> input_ids = x_token.input_ids.to(device)
>>> token_type_ids = x_token.token_type_ids.to(device)
>>> out_lm_token = model.generate(input_ids, token_type_ids=token_type_ids, max_new_tokens=50)
>>> out_mlm_token = model(input_ids, token_type_ids=token_type_ids).logits.argmax(axis=-1)
>>> tokenizer.decode(out_mlm_token[0])
"武田信玄は、戦国時代ファンならぜひ押さえておきたい名将の一人。"
>>> tokenizer.decode(out_lm_token[0][input_ids.shape[1] :])
"武田氏の三代に渡った武田家のひとり\n甲斐市に住む、日本史上最大の戦国大名。..."
```


# Model Details

## Model Description

Japanese language model using Switch Transformer.
It has the same structure as the model introduced as `Prefix LM` in the T5 paper, and works with both Test Generation and Masked Language Model.



- **Developed by:** Toshiyuki Sakamoto (tanreinama)
- **Model type:** Switch Transformer
- **Language(s) (NLP):** Japanese
- **License:** MIT License

### Prefix-LM Model

GPTSAN has the structure of the model named Prefix-LM in the [T5 paper](https://arxiv.org/abs/1910.10683). (The original GPTSAN repository calls it `hybrid`)
In GPTSAN, the `Prefix` part of Prefix-LM, that is, the input position that can be referenced by both tokens, can be specified with any length.
Arbitrary lengths can also be specified differently for each batch.
This length applies to the text entered in `prefix_text` for the tokenizer.
The tokenizer returns the mask of the `Prefix` part of Prefix-LM as `token_type_ids`.
The model treats the part where `token_type_ids` is 1 as a `Prefix` part, that is, the input can refer to both tokens before and after.

### Spout Vector

A Spout Vector is a special vector for controlling text generation.
This vector is treated as the first embedding in self-attention to bring extraneous attention to the generated tokens.
In this pre-trained model, the Spout Vector is a 128-dimensional vector that passes through 8 fully connected layers in the model and is projected into the space acting as external attention.
The Spout Vector projected by the fully connected layer is split to be passed to all self-attentions.

## Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/tanreinama/GPTSAN

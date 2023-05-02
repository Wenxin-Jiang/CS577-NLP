Base model: [microsoft/DialoGPT-small](https://huggingface.co/microsoft/DialoGPT-small)

Fine tuned for dialogue response generation on the [Schema Guided Dialogue Dataset](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue) (Rastogi et al., 2019)

Three additional special tokens were added during the fine-tuning process:
 - <|pad|> padding token
 - <|user|> speaker control token to prompt user responses
 - <|system|> speaker control token to prompt system responses
Base model: [microsoft/DialoGPT-large](https://huggingface.co/microsoft/DialoGPT-large)

Fine tuned for dialogue response generation on the [Persuasion For Good Dataset](https://gitlab.com/ucdavisnlp/persuasionforgood) (Wang et al., 2019)

Three additional special tokens were added during the fine-tuning process:
 - <|pad|> padding token
 - <|user|> speaker control token to prompt user responses
 - <|system|> speaker control token to prompt system responses
 
 The following Dialogues were excluded:
 - Those with donation amounts outside of the task range of [$0, $2].
 - Those where a donation of 0 was made at the end of the task but a non-zero amount was pledged in the dialogue.
 - Those with more than 800 words.
 
 Stats:
 - Training set: 519 dialogues
 - Validation set: 58 dialogues
 - ~20 utterances per dialogue
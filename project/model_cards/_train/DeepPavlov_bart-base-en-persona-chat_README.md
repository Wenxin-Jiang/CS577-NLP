---
license: openrail
datasets:
- AlekseyKorshuk/persona-chat
language:
- en
pipeline_tag: text-generation
---
---
language:
- en
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->



# Model Details

## Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Deeppavlov team
- **Model type:** seq2seq
- **Language(s) (NLP):** English
- **License:** MIT
- **Finetuned from model:** [facebook/bart-base](facebook/bart-base)


# Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->


## Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

```python
from typing import List, TypedDict
from dataclasses import dataclass
from itertools import chain

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


@dataclass
class H2PersonaChatHyperparametersV1:
    """
    chat_history_pair_length: int - dialogue pairs amount from the end
    """

    model_name: str = "facebook/bart-base"
    chat_history_pair_length: int = 7

    persona_max_length: int = 14
    chat_max_length: int = 25

    debug_status: int = 0


class PersonaChatDatasetSampleV1(TypedDict):
    """
    persona: List[str] - person fact sentence set
    history: List[str] - chating history
    """

    persona: List[str]
    history: List[str]
    sample_id: str


class H2Seq2SeqInferenceSampleDictV1(TypedDict):
    input_ids: List[int]
    attention_mask: List[int]


class H2Seq2SeqInferenceSampleDictV2(TypedDict):
    input_ids: torch.Tensor
    attention_mask: torch.Tensor


def flat_list(list_of_lists: List[List]) -> List:
    return list(chain.from_iterable(list_of_lists))


class H2Seq2SeqInferencePersonaSampleV1:
    def __init__(
        self,
        dataset_sample: PersonaChatDatasetSampleV1,
        tokenizer: AutoTokenizer,
        hyperparameters: H2PersonaChatHyperparametersV1,
    ) -> None:
        self.dataset_sample = dataset_sample
        self.tokenizer = tokenizer
        self.hyperparameters = hyperparameters

    def add_spaces_after(
        self,
        items: List[str],
    ) -> List[str]:
        items = [item + " " for item in items]
        return items

    @property
    def bos_token_id(self):
        if "t5" in self.hyperparameters.model_name:
            return []

        if self.tokenizer.bos_token_id is None:
            return []

        return [self.tokenizer.bos_token_id]

    @property
    def eos_token_id(self):
        if self.tokenizer.eos_token_id is None:
            return []

        return [self.tokenizer.eos_token_id]

    def add_sep_beetween(self, items: List[str], sep=" EOS ") -> List[str]:
        for i in range(1, len(items)):
            items[i] = sep + items[i]

        return items

    def add_spaces_between(self, items: List[str]) -> List[str]:
        items = self.add_spaces_after(items)
        items[-1] = items[-1].strip()
        return items

    def get_sample(self) -> H2Seq2SeqInferenceSampleDictV1:

        dialog_history = self.dataset_sample["history"]
        dialog_history = dialog_history[-self.hyperparameters.chat_history_pair_length * 2 - 1 :]
        dialog_history = self.add_sep_beetween(dialog_history)

        persona = self.dataset_sample["persona"]
        persona = self.add_sep_beetween(
            persona,
            sep=" ",
        )

        KNOWLEDGE_IDS = self.tokenizer.encode(
            " [KNOWLEDGE] ",
            add_special_tokens=False,
        )
        CONTEXT_IDS = self.tokenizer.encode(
            " [CONTEXT] ",
            add_special_tokens=False,
        )

        encoded_history = self.tokenizer.batch_encode_plus(
            dialog_history,
            add_special_tokens=False,
            truncation=True,
            max_length=self.hyperparameters.chat_max_length,
        )
        encoded_history = flat_list(encoded_history["input_ids"])

        encoded_persona = self.tokenizer.batch_encode_plus(
            persona,
            add_special_tokens=False,
            truncation=True,
            max_length=self.hyperparameters.persona_max_length,
        )

        encoded_persona = flat_list(encoded_persona["input_ids"])

        input_ids = [
            *self.bos_token_id,
            *CONTEXT_IDS,
            *encoded_history,
            *KNOWLEDGE_IDS,
            *encoded_persona,
            *self.eos_token_id,
        ]

        attention_mask = [1] * len(input_ids)

        return H2Seq2SeqInferenceSampleDictV1(
            input_ids=input_ids,
            attention_mask=attention_mask,
        )


class DialogBotV1:
    def __init__(
        self,
        model: AutoModelForSeq2SeqLM,
        tokenizer: AutoTokenizer,
        hyperparameters: H2PersonaChatHyperparametersV1,
        history: List[str] = None,
        persona: List[str] = None,
        device: str = "cuda",
        shuffle_persona: bool = True,
    ):
        self.model = model

        self.tokenizer = tokenizer
        self.hyperparameters = hyperparameters
        self.device = device
        self.shuffle_persona = shuffle_persona

        self.debug_status = hyperparameters.debug_status

        if history is None:
            self.history = []
        self.history = history

        if persona is None:
            self.persona = []
        self.persona = persona

    def _get_sample(
        self,
        persona: List[str],
        history: List[str],
    ) -> H2Seq2SeqInferenceSampleDictV1:
        dataset_sample = PersonaChatDatasetSampleV1(
            persona=persona,
            history=history,
        )

        sample = H2Seq2SeqInferencePersonaSampleV1(
            tokenizer=self.tokenizer,
            hyperparameters=self.hyperparameters,
            dataset_sample=dataset_sample,
        )
        sample = sample.get_sample()
        print(self.tokenizer.decode(sample['input_ids']))

        for key in sample.keys():
            sample[key] = torch.tensor(sample[key]).unsqueeze(0).to(self.device)

        return sample

    def next_response(
        self,
        **generation_params,
    ) -> str:

        sample = self._get_sample(
            persona=self.persona,
            history=self.history,
        )
        answer = self.generate_response(
            sample,
            **generation_params,
        )
        answer = self.tokenizer.batch_decode(
            answer,
            skip_special_tokens=True,
        )
        self.history.append(answer[0])
        return answer[0]

    def generate_response(
        self,
        sample: H2Seq2SeqInferenceSampleDictV1,
        **generation_params,
    ):
        """
        generation_params - https://huggingface.co/docs/transformers/v4.24.0/en/main_classes/text_generation
        """
        with torch.no_grad():
            return self.model.generate(
                **sample,
                **generation_params,
            )

PRETRAINED_MODEL_NAME_OR_PATH = "DeepPavlov/bart-base-en-persona-chat"

PAIR_DIALOG_HISTORY_LENGTH = 2

# CHAT_MAX_LENGTH for single sentence, in tokens
CHAT_MAX_LENGTH = 25
# PERSONA_MAX_LENGTH for single sentence, in tokens
PERSONA_MAX_LENGTH = 19

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = AutoModelForSeq2SeqLM.from_pretrained(PRETRAINED_MODEL_NAME_OR_PATH)
model.to(device)
model.eval()

tokenizer = AutoTokenizer.from_pretrained(PRETRAINED_MODEL_NAME_OR_PATH)

if torch.cuda.is_available():
	model.half()

hyperparameters = H2PersonaChatHyperparametersV1(
	chat_history_pair_length=PAIR_DIALOG_HISTORY_LENGTH,
	persona_max_length=PERSONA_MAX_LENGTH,
	chat_max_length=CHAT_MAX_LENGTH,
	model_name=PRETRAINED_MODEL_NAME_OR_PATH,
)


persona = [
	"I like to play guitar.",
	"I hate onions."
]

history = [
	"I hate to talk about politics, what about you?"
]
            
persona_bot = DialogBotV1(
        model=model,
        tokenizer=tokenizer,
        hyperparameters=hyperparameters,
        history=history,
        persona=persona,
        device=device,
    )

GENERATION_PARAMS = {
	"max_new_tokens": 60,
	"penalty_alpha": 0.15,
	"top_k": 10
}
response = persona_bot.next_response(
	**GENERATION_PARAMS,
)

print(response)
# i am not into politics. i am into music.
```


## Recommendations

# Training Details

## Training Data

<!-- This should link to a Data Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->
- [Data Source | EN Persona Chat](https://s3.amazonaws.com/datasets.huggingface.co/personachat/personachat_self_original.json)

[More Information Needed]

### Preprocessing

- Initial data was splitted by this script:
```python
def persona_chat_dataset_tranformer_v1(
    initial_dataset_path: str,
    output_folder: str,
) -> None:
    """
        example
            persona_chat_dataset_tranformer_v1(
            initial_dataset_path="./datasets/persona_chat/persona_chat.json",
            output_folder="./datasets/persona_chat",
    )
    """
    assert initial_dataset_path is not None, "initial_dataset_path is None"
    assert output_folder is not None, "output_folder is None"

    with open(initial_dataset_path) as f:
        initial_dataset = json.load(f)

    train_dataset = initial_dataset["train"]
    val_len = len(initial_dataset["valid"])
    valid_dataset = initial_dataset["valid"][: val_len // 2]
    test_dataset = initial_dataset["valid"][val_len // 2 :]

    print(
        f"Dataset lengths: train {len(train_dataset)}, valid {len(valid_dataset)}, test {len(test_dataset)}"
    )
    # save json files
    with open(output_folder + "/train.json", "w") as f:
        json.dump(train_dataset, f)

    with open(output_folder + "/valid.json", "w") as f:
        json.dump(valid_dataset, f)

    with open(output_folder + "/test.json", "w") as f:
        json.dump(test_dataset, f)

    print("Datasets saved.")
```  

# Evaluation

### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->
- BLUEL
- CharF
- RougeL
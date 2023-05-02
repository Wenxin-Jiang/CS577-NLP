Galactica-6.7b finetuned on webgpt and prompt_dialogue (version v2)

Demo use:

```
import torch
from torch import nn
from torch.nn import functional as F
import transformers

base_path = 'OpenAssistant/galactica-6.7b-finetuned'

model = transformers.OPTForCausalLM.from_pretrained(
    base_path, load_in_8bit=True, device_map='auto', low_cpu_mem_usage=True,
    torch_dtype=torch.float16, offload_state_dict=True
)

model.gradient_checkpointing_enable()  # reduce number of stored activations
model.model.decoder.project_in = lambda x: x.requires_grad_(True)

class CastOutputToFloat(nn.Sequential):
    def forward(self, x): return super().forward(x).to(torch.float32)

model.lm_head = CastOutputToFloat(model.lm_head)

tokenizer = transformers.AutoTokenizer.from_pretrained(base_path)

batch = tokenizer.encode("<question>What are the symptoms of Alzheimer's disease?<answer>", return_tensors="pt")

with torch.cuda.amp.autocast():
    out = model.generate(
        input_ids=batch.to(model.device),
        max_length=300,
        do_sample=True,
        top_k=40,
        num_beams=1,
        num_return_sequences=1,
        eos_token_id=tokenizer.additional_special_tokens_ids[tokenizer.additional_special_tokens.index('<question>')]
    )

print(tokenizer.decode(out[0, :-1]).replace('<question>', "User:\n").replace('<answer>', '\nAssistant:\n'))
```
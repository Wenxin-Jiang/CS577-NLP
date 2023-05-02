Best Generations with
```
from transformers import OPTForCausalLM
from transformers import GPT2Tokenizer

model = OPTForCausalLM.from_pretrained("Kigo/OPT-350m-COVID-Finetune", from_tf=True)
tokenizer = GPT2Tokenizer.from_pretrained("facebook/opt-350m")

inputs = tokenizer("Covid-19 is Positive, 42.237% of Lungs show GGO, Lower Left Lobe was most affected, Upper Left Lobe was least affected, yes Vascular dilatation, found consolidation. The patient is in critical condition. \n\n\n ", return_tensors="pt")

generate_ids = model.generate(inputs.input_ids,
                              do_sample=True,
                              max_new_tokens=1000,
                              )
completion = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
print(completion)
```
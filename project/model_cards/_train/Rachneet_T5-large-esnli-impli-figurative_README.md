# load model

```
from transformers import (
    AutoTokenizer,
    AutoConfig,
    AutoModelForSeq2SeqLM
    )

model_path = "T5-large-esnli-impli-figurative"

tokenizer = AutoTokenizer.from_pretrained(model_path)
config = AutoConfig.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

premise = "I just caught a guy picking up used chewing gum and he put it in his mouth."
hypothesis = "it was such a pleasant sight to see a guy picking up used chewing gum; and he put it in his mouth"
prepared_input = f"figurative hypothesis: {hypothesis} premise: {premise}"
features = tokenizer(prepared_input, max_length=128, padding="max_length", truncation=True, return_tensors="pt")

model.eval()
model.to(device)
with torch.no_grad():
    # https://huggingface.co/blog/how-to-generate
    generated_ids = model.generate(
        **features,
        max_length=128,
        use_cache=True,
        num_beams=4,
        length_penalty=0.6,
        early_stopping=True,
    )
dec_preds = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("The prediction is: ", dec_preds)
print(dec_preds[1:].replace("explanation:", "").lstrip())

```

# Example input

figurative  hypothesis: I was gone for only a few days and my considerate adult son just let the sink fill up with dirty dishes, making me feel really happy premise: I left my adult son home for a few days and just came back to a sink full of gross old dishes.
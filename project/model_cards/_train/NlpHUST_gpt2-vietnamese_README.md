---
language: vi
tags:
- vi
- vietnamese
- gpt2
- text-generation
- lm
- nlp
datasets:
- oscar
widget:
- text: "Việt Nam là quốc gia có"
---

# GPT-2

Pretrained gpt model on Vietnamese language using a causal language modeling (CLM) objective. It was introduced in
[this paper](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
and first released at [this page](https://openai.com/blog/better-language-models/).

# How to use the model

~~~~
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('NlpHUST/gpt2-vietnamese')
model = GPT2LMHeadModel.from_pretrained('NlpHUST/gpt2-vietnamese')

text = "Việt Nam là quốc gia có"
input_ids = tokenizer.encode(text, return_tensors='pt')
max_length = 100

sample_outputs = model.generate(input_ids,pad_token_id=tokenizer.eos_token_id,
                                   do_sample=True,
                                   max_length=max_length,
                                   min_length=max_length,
                                   top_k=40,
                                   num_beams=5,
                                   early_stopping=True,
                                   no_repeat_ngram_size=2,
                                   num_return_sequences=3)

for i, sample_output in enumerate(sample_outputs):
    print(">> Generated text {}\n\n{}".format(i+1, tokenizer.decode(sample_output.tolist())))
    print('\n---')
~~~~

```bash
>> Generated text 1

Việt Nam là quốc gia có nền kinh tế hàng đầu thế giới về sản xuất, chế biến và tiêu thụ các sản phẩm nông sản, thủy sản. Tuy nhiên, trong những năm gần đây, nông nghiệp Việt Nam đang phải đối mặt với nhiều khó khăn, thách thức, đặc biệt là những tác động tiêu cực của biến đổi khí hậu.
Theo số liệu của Tổng cục Thống kê, tính đến cuối năm 2015, tổng diện tích gieo trồng, sản lượng lương thực, thực phẩm cả

---
>> Generated text 2

Việt Nam là quốc gia có nền kinh tế thị trường định hướng xã hội chủ nghĩa, có vai trò rất quan trọng đối với sự phát triển bền vững của đất nước. Do đó, trong quá trình đổi mới và hội nhập quốc tế, Việt Nam đã và đang phải đối mặt với không ít khó khăn, thách thức, đòi hỏi phải có những chủ trương, chính sách đúng đắn, kịp thời, phù hợp với tình hình thực tế. Để thực hiện thắng lợi mục tiêu, nhiệm vụ

---
>> Generated text 3

Việt Nam là quốc gia có nền kinh tế thị trường phát triển theo định hướng xã hội chủ nghĩa. Trong quá trình đổi mới và hội nhập quốc tế hiện nay, Việt Nam đang phải đối mặt với nhiều khó khăn, thách thức, đòi hỏi phải có những giải pháp đồng bộ, hiệu quả và phù hợp với tình hình thực tế của đất nước. Để thực hiện thắng lợi mục tiêu, nhiệm vụ mà Nghị quyết Đại hội XI của Đảng đề ra, Đảng và Nhà nước đã ban hành

---
```
# Model architecture
A 12-layer, 768-hidden-size transformer-based language model.

# Training
The model was trained on Vietnamese Oscar dataset (32 GB) to optimize a traditional language modelling objective on v3-8 TPU for around 6 days. It reaches around 13.4 perplexity on a chosen validation set from Oscar.

### GPT-2 Finetuning

The following example fine-tunes GPT-2 on WikiText-2. We're using the raw WikiText-2.

The script [here](https://github.com/huggingface/transformers/blob/main/examples/pytorch/language-modeling/run_clm.py) .

```bash
python run_clm.py \
    --model_name_or_path NlpHUST/gpt2-vietnamese \
    --dataset_name wikitext \
    --dataset_config_name wikitext-2-raw-v1 \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 8 \
    --do_train \
    --do_eval \
    --output_dir /tmp/test-clm
```

### Contact information
For personal communication related to this project, please contact Nha Nguyen Van (nha282@gmail.com).

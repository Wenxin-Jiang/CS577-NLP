---
language: ja
license: cc-by-sa-4.0
datasets:
- wikipedia
widget:
- text: Rustで[MASK]を使うことができます。。
---

# What is this model?
- 東北大学のBERT large JapaneseをRustで使える様に変換
- [cl-tohoku/bert-large-japanese](https://huggingface.co/cl-tohoku/bert-large-japanese)

# How to Try

### 1. Clone

```
git clone https://huggingface.co/Yokohide031/rust_cl-tohoku_bert-large-japanese

```

### 2. Create Project

```
cargo new <projectName>
```

### 3. Edit main.rs

```
extern crate anyhow;

use rust_bert::bert::{BertConfig, BertForMaskedLM};
use rust_bert::Config;
use rust_tokenizers::tokenizer::{BertTokenizer, MultiThreadedTokenizer, TruncationStrategy};
use rust_tokenizers::vocab::Vocab;
use tch::{nn, no_grad, Device, Tensor};

use std::path::PathBuf;

fn get_path(item: String) -> PathBuf {
    let mut resource_dir = PathBuf::from("path/to/rust_cl-tohoku_bert-large-japanese/");
    resource_dir.push(&item);
    println!("{:?}", resource_dir);
    return resource_dir;
}

fn input(display: String) -> String {
    let mut text = String::new();
    println!("{}", display);
    std::io::stdin().read_line(&mut text).unwrap();
    return text.trim().to_string();
}

fn main() -> anyhow::Result<()> {
    //    Resources paths

    let model_path: PathBuf = get_path(String::from("rust_model.ot"));
    let vocab_path: PathBuf = get_path(String::from("vocab.txt"));
    let config_path: PathBuf = get_path(String::from("config.json"));


    //    Set-up masked LM model
    let device = Device::Cpu;
    let mut vs = nn::VarStore::new(device);
    let config = BertConfig::from_file(config_path);
    let bert_model = BertForMaskedLM::new(&vs.root(), &config);
    vs.load(model_path)?;

    //    Define input
    let inp = input(String::from("Input: "));
    let inp = inp.replace("*", "[MASK]");
    let input = [inp];

    let tokenizer: BertTokenizer =
        BertTokenizer::from_file(vocab_path.to_str().unwrap(), false, false).unwrap();

    let owakatied = &tokenizer.tokenize_list(&input);

    let tokenized_input = tokenizer.encode_list(&input, 128, &TruncationStrategy::LongestFirst, 0);

    let mut mask_index: usize = 0;
    for (i, m) in owakatied[0].iter().enumerate() {
        if m == "[MASK]" {
            mask_index = i+1;
            break;
        }
    }

    let max_len = tokenized_input
        .iter()
        .map(|input| input.token_ids.len())
        .max()
        .unwrap();
    let tokenized_input = tokenized_input
        .iter()
        .map(|input| input.token_ids.clone())
        .map(|mut input| {
            input.extend(vec![0; max_len - input.len()]);
            input
        })
        .map(|input| Tensor::of_slice(&(input)))
        .collect::<Vec<_>>();
    let input_tensor = Tensor::stack(tokenized_input.as_slice(), 0).to(device);

    //    Forward pass
    let model_output = no_grad(|| {
        bert_model.forward_t(
            Some(&input_tensor),
            None,
            None,
            None,
            None,
            None,
            None,
            false,
        )
    });
    println!("MASK: {}", mask_index);
    //    Print masked tokens
    let index_1 = model_output
        .prediction_scores
        .get(0)
        .get(mask_index as i64)
        .argmax(0, false);

    let word = tokenizer.vocab().id_to_token(&index_1.int64_value(&[]));
    println!("{}", word);

    Ok(())
}

```

※ 上のコードでは、[MASK]の代わりに "*" を使うことになってます。

## Licenses
The pretrained models are distributed under the terms of the [Creative Commons Attribution-ShareAlike 3.0](https://creativecommons.org/licenses/by-sa/3.0/).


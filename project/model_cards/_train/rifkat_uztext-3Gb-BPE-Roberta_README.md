
---
language:
- uz
tags:
- transformers
- mit
- robert
- uzrobert
- uzbek
- cyrillic
- latin
license: apache-2.0
widget:
- text: "Kuchli yomg‘irlar tufayli bir qator <mask> kuchli sel oqishi kuzatildi."
  example_title: "Latin script"
- text: "Алишер Навоий – улуғ ўзбек ва бошқа туркий халқларнинг <mask>, мутафаккири ва давлат арбоби бўлган."
  example_title: "Cyrillic script"
---


<p><b>UzRoBerta model.</b>

Pre-prepared model in Uzbek (Cyrillic and latin script) to model the masked language and predict the next sentences.

<p><b>How to use.</b>

You can use this model directly with a pipeline for masked language modeling:

<pre><code class="language-python">
from transformers import pipeline

unmasker = pipeline('fill-mask', model='rifkat/uztext-3Gb-BPE-Roberta')

unmasker("Алишер Навоий – улуғ ўзбек ва бошқа туркий халқларнинг [mask], мутафаккири ва давлат арбоби бўлган.")

[{'score': 0.5902208685874939,
  'sequence': 'Алишер Навоий – улуғ ўзбек ва бошқа туркий халқларнинг шоири, мутафаккири ва давлат арбоби бўлган.',
  'token': 28809,
  'token_str': ' шоири'},
 {'score': 0.08303504437208176,
  'sequence': 'Алишер Навоий – улуғ ўзбек ва бошқа туркий халқларнинг устози, мутафаккири ва давлат арбоби бўлган.',
  'token': 17484,
  'token_str': ' устози'},
 {'score': 0.035882771015167236,
  'sequence': 'Алишер Навоий – улуғ ўзбек ва бошқа туркий халқларнинг арбоби, мутафаккири ва давлат арбоби бўлган.',
  'token': 34552,
  'token_str': ' арбоби'},
 {'score': 0.03447483479976654,
  'sequence': 'Алишер Навоий – улуғ ўзбек ва бошқа туркий халқларнинг асосчиси, мутафаккири ва давлат арбоби бўлган.',
  'token': 14034,
  'token_str': ' асосчиси'},
 {'score': 0.03044942207634449,
  'sequence': 'Алишер Навоий – улуғ ўзбек ва бошқа туркий халқларнинг дўсти, мутафаккири ва давлат арбоби бўлган.',
  'token': 28100,
  'token_str': ' дўсти'}]
  
  
  unmasker("Kuchli yomg‘irlar tufayli bir qator [mask] kuchli sel oqishi kuzatildi.")
  
  [{'score': 0.410250186920166,
  'sequence': 'Kuchli yomg‘irlar tufayli bir qator hududlarda kuchli sel oqishi kuzatildi.',
  'token': 11009,
  'token_str': ' hududlarda'},
 {'score': 0.2023029774427414,
  'sequence': 'Kuchli yomg‘irlar tufayli bir qator tumanlarda kuchli sel oqishi kuzatildi.',
  'token': 35370,
  'token_str': ' tumanlarda'},
 {'score': 0.129830002784729,
  'sequence': 'Kuchli yomg‘irlar tufayli bir qator viloyatlarda kuchli sel oqishi kuzatildi.',
  'token': 33584,
  'token_str': ' viloyatlarda'},
 {'score': 0.04539087787270546,
  'sequence': 'Kuchli yomg‘irlar tufayli bir qator mamlakatlarda kuchli sel oqishi kuzatildi.',
  'token': 19315,
  'token_str': ' mamlakatlarda'},
 {'score': 0.0369882769882679,
  'sequence': 'Kuchli yomg‘irlar tufayli bir qator joylarda kuchli sel oqishi kuzatildi.',
  'token': 5853,
  'token_str': ' joylarda'}]
</code></pre>

<p><b>Training data.</b>

UzBERT model was pretrained on &asymp;2M news articles (&asymp;3Gb).

<pre><code class="language-python">
@misc {rifkat_davronov_2022,
	author       = { {Adilova Fatima,Rifkat Davronov, Samariddin Kushmuratov, Ruzmat Safarov} },
	title        = { uztext-3Gb-BPE-Roberta (Revision 0c87494) },
	year         = 2022,
	url          = { https://huggingface.co/rifkat/uztext-3Gb-BPE-Roberta },
	doi          = { 10.57967/hf/0140 },
	publisher    = { Hugging Face }
}
</code></pre>

---
license: wtfpl
---
это файнтюн sberai ruGPT3 small (125 млн параметров) на всех оригинальных нуждиках (2 часа транскрибированные через openai whisper medium). размер блока при файнтюне 1024, 25 эпох. все скрипты по инференсу модели тут https://github.com/ai-forever/ru-gpts, через transformers вполне себе работает на 4 гб видеопамяти, на 2 думаю тоже заработает.

-как запустить через transformers?
запускаем строки ниже в jupyterе

from transformers import pipeline, set_seed

set_seed(32)
generator = pipeline('text-generation', model="4eJIoBek/ruGPT3_small_nujdiki_fithah", do_sample=True, max_length=350)
generator("Александр Сергеевич Пушкин известен также благодаря своим сказкам, которые включают в себя: ")

и всё работает и вообще нихуёво
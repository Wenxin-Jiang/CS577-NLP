---
license: cc-by-3.0
---

Base model [facebook/opt-2.7b](https://huggingface.co/facebook/opt-2.7b)

Fine-tuned for causal language modeling of transcribed spoken dialogue from the [TalkBank CABank collection](https://ca.talkbank.org/access/).
Training corpora include: 
- [CABNC](https://ca.talkbank.org/access/CABNC.html) - Spoken language segment of the British National Corpus
- [CallFriend English (N)](https://ca.talkbank.org/access/CallFriend/eng-n.html) - Phone calls
- [CallFriend English (S)](https://ca.talkbank.org/access/CallFriend/eng-s.html) - Phone calls
- [CallHome English](https://ca.talkbank.org/access/CallHome/eng.html) - Phone calls
- [GCSAusE](https://ca.talkbank.org/access/GCSAusE.html) - Australian conversations
- [ISL](https://ca.talkbank.org/access/ISL.html) - Conversations recorded to test ASR methods for meeting
- [MICASE](https://ca.talkbank.org/access/MICASE.html) - Michigan Corpus of Academic Spoken English
- [SCoSE](https://ca.talkbank.org/access/SCoSE.html) - The Saarbrücken Corpus of Spoken (American) English.

(Corpus descriptions are from TalkBank)

**Data input format:** 
The data format models a sequence of spoken dialogue between two or more participants:
- The sequence is prefixed with information about the participants including name (can be a proper noun, a title/role, or unknown), age (can be a number or unknown), and sex (can be male, female, other, unknown).
- It then proceeds to sequentially list all utterances in the conversation, each prefixed with their participant code (S1, S2, S3, etc.).
- Utterances support a limited set of transcription notations in the [CHAT & CHAT-CA](https://talkbank.org/manuals/CHAT.pdf) formats:
  - Pauses: `(.)` for a generic short pause, or `(N.N)` for a timed pause. For example `(3.4)` is a pause for 3.4 seconds.
  - Non-verbal sounds: `&=laughs`, `&=cough`, `&=breathes`, `&=click`, etc. Anything describing a speaker-produced non-verbal sound can come after a prefix of `&=`
  - Comments about speaker or setting: `[% baby crying in background]`, `[% smiling]`, `[% phone clicking noise]`, `[% imitating him]`, etc.
    Anything describing the state of the speaker or environment can be in this block. Also, a comment block can be used to describe speaker-produced sounds, but it is more common to use the `&=` prefix for that.
  - Unknown or unintelligible utterances: `xxx`
  - Breathing: `hhh`

**Example:**

<span style="color:red">&lt;participant&gt;</span> S1 (name: Dave, age: 33, sex: male) <span style="color:red">&lt;participant&gt;</span> S2 (name: unknown, age: unknown, sex: unknown) <span style="color:red">&lt;dialog&gt;</span> <span style="color:orange">S1:</span> Hi! (2.3) are you there? <span style="color:orange">S2:</span> hhh hhh [% background noise] uh yeah (0.8) I can hear you. (1.2) &=cough can you hear me? <span style="color:orange">S1:</span> ...

**Usage Info:** 

Per the [OPT documentation](https://huggingface.co/docs/transformers/v4.24.0/en/model_doc/opt), the model was trained with tokenizer setting `use_fast=False`.

To use this model for real-time inference in a continuous duplex dialogue system, see: [https://github.com/AbrahamSanders/realtime-chatbot](https://github.com/AbrahamSanders/realtime-chatbot).
# Session 01 Discussion Analysis

Zoom chat during the first session was a little chaotic, participants are not conditioned to ask questions in Discord yet. I thought it would be fun to analyze the chat to see if anything got lost in the shuffle.

- Collected Zoom chat, Discord chat and class transcript
- Asked Gemini 2.5 Pro for help finding questions that got lost in Zoom
- Asked follow up questions about general sentiment

Prompt:
```
I want to surface questions that were mentioned in the Zoom chat but not answered by dialog in the class transcript nor asked in the Discord chat:
```

## Questions

Here are the questions from the Zoom chat that appear to meet these criteria:

- Asked in Zoom.
- Not answered by dialog in the class transcript.
- Not asked (or answered if asked by someone else) in the Discord chat provided.
- Not answered directly within the Zoom chat by other participants.

1.  From **Abidi | AgxntSix AI** (11:14:09):
    *   `Thoughts on the future of Voice AI Architecture being V2V models with built in MCP tool calling`
    *   <font color="1fa954">Transcript:</font> The transcript discusses speech-to-speech (S2S) models as the future (08:39) and that current text-mode LLMs are better for tool calling (08:55). It doesn't specifically address V2V (voice-to-voice) with *built-in* MCP tool calling.
    *   <font color="#5865f2">Discord:</font> Not found.
    *   <font color="#0b5cff">Zoom:</font> Not answered.

2.  From **Shrirang Moghe** (11:16:30):
    *   `SSE popularized by MCP - like websocket can help?`
    *   <font color="1fa954">Transcript:</font> Websockets are discussed for server-to-server *audio* transport (17:57), not specifically for client-server text or in comparison/conjunction with SSE (Server-Sent Events) for MCP-like functionality. Zhiyao Wang's later question about SSE vs. Websocket (11:33:10) was redirected to Discord.
    *   <font color="#5865f2">Discord:</font> Zhiyao Wang asked "For client-server text, what do you think about SSE vs. websocket?" (11:40 AM), which is similar but specifically about text. Shrirang's question links it to "SSE popularized by MCP".
    *   <font color="#0b5cff">Zoom:</font> Not answered.

3.  From **Suchismit Mahapatra** (11:23:05):
    *   `Is it the latency associated with the first two components ? STT + LLM` (Regarding TTFT)
    *   <font color="1fa954">Transcript:</font> TTFT is defined. The components of latency are listed in a table (11:06), but whether TTFT *specifically* refers to just STT + LLM is not explicitly stated.
    *   <font color="#5865f2">Discord:</font> This specific clarification was not found.
    *   <font color="#0b5cff">Zoom:</font> Chad Bailey redirected this to Discord ("this is a good one for the discord").

4.  From **Neeraj Sharma** (11:22:47):
    *   `Any progress on QUIC. It was making big waves but haven't heard much about it off late.`
    *   <font color="1fa954">Transcript:</font> QUIC protocol is not mentioned.
    *   <font color="#5865f2">Discord:</font> Not found.
    *   <font color="#0b5cff">Zoom:</font> v p redirected this to Discord ("Great question to ask in ... discord!").

5.  From **Ignacio Alonso** (11:26:26):
    *   `isnt that comfyui? can you build agents with it?`
    *   <font color="1fa954">Transcript:</font> ComfyUI is not mentioned in the transcript.
    *   <font color="#5865f2">Discord:</font> Not found.
    *   <font color="#0b5cff">Zoom:</font> Not answered.

6.  From **Shrirang Moghe** (11:31:36):
    *   `Datasets for - turn available?`
    *   <font color="1fa954">Transcript:</font> Turn detection models and "open data" are mentioned (25:15), implying datasets exist for the open-source model, but specific datasets or where to find a list of them are not detailed.
    *   <font color="#5865f2">Discord:</font> Not found.
    *   <font color="#0b5cff">Zoom:</font> Not answered.

7.  From **Daniel Green** (11:32:47):
    *   `Favorite examples of live AI voice in the wild?`
    *   <font color="1fa954">Transcript:</font> Examples of *use cases* are given (02:26), but not specific *favorite existing products/deployments* in the wild.
    *   <font color="#5865f2">Discord:</font> Not found.
    *   <font color="#0b5cff">Zoom:</font> Not answered.

8.  From **Mr.Srini** (11:33:07):
    *   `voice AI agents - can we handle multi-lingual (with LLM or with out LLM) as well?`
    *   <font color="1fa954">Transcript:</font> Gladia is mentioned for non-English STT (13:52), and the Wave2Vec2BERT model for turn detection was trained on multilingual audio (33:26). The question is broader, about full agent capabilities (implying STT, LLM, TTS handling multiple languages) and whether an LLM is always needed.
    *   <font color="#5865f2">Discord:</font> nirvana1285 asked about multilingual models for Indic languages focusing on STT, Turn detection, TTS. This is related but Mr.Srini's question is more general about the "agent" and LLM necessity.
    *   <font color="#0b5cff">Zoom:</font> Not answered.

9.  From **Mohamed Salama & Rami Mithalouni** (11:36:44):
    *   `How to connect the voice agent to a local phone numbers in saudi arabia, note that the online services like twillio donot provide saudi phone numbers`
    *   `in telephony, how to integrate my current land phone numbers with voice agent? espichally for countries where twillio or similar services are not supported`
    *   <font color="1fa954">Transcript:</font> Telephony, PSTN, and SIP are discussed generally (19:08), but not this specific problem of integrating with local numbers in regions unsupported by major CPaaS providers.
    *   <font color="#5865f2">Discord:</font> Not found.
    *   <font color="#0b5cff">Zoom:</font> Not answered.

10. From **Jonathan Sanders** (11:42:50):
    *   `Do you have any thoughts on Bland's approach? They use open source LLMs that they host`
    *   <font color="1fa954">Transcript:</font> Bland.ai is not mentioned.
    *   <font color="#5865f2">Discord:</font> Not found.
    *   <font color="#0b5cff">Zoom:</font> Not answered.

11. From **Thadeu Esteves** (11:44:51):
    *   `What you think about the whisper.cpp from scratch instead of use APIs like Groq?`
    *   <font color="1fa954">Transcript:</font> Optimized Whisper and various commercial Whisper APIs (FAL, Firework, Groq) are discussed (12:47). The specific trade-off of using `whisper.cpp` directly versus these APIs isn't detailed.
    *   <font color="#5865f2">Discord:</font> Not found.
    *   <font color="#0b5cff">Zoom:</font> Yousif Astarabadi offered an opinion ("Not worth on server, but client side it is faster than any api"). So, partially addressed by another participant, but not by the speaker/dialog.

12. From **Mr.Srini** (11:46:17):
    *   `Qeustion: open LLM models for voice-to-voice are allowed in production? for Enterprises? What about security? are we not training other LLMs with our data (which is private)?`
    *   <font color="1fa954">Transcript:</font> Security and privacy implications of using open LLMs for V2V in enterprises are not specifically addressed.
    *   <font color="#5865f2">Discord:</font> Not found.
    *   <font color="#0b5cff">Zoom:</font> Not answered.

13. From **ototao** (11:51:42):
    *   `What is the fastest smol model with basic conversation ability?`
    *   <font color="1fa954">Transcript:</font> While specific LLMs like GPT-4o and Gemini Flash are mentioned for their capabilities, a direct comparison of "fastest small models" for basic conversation isn't made.
    *   <font color="#5865f2">Discord:</font> Not found.
    *   <font color="#0b5cff">Zoom:</font> Ignacio Alonso suggested "gemma?" but it wasn't an answer from the speaker.

14. From **Satya Phanindra Reddy** (12:00:29):
    *   `how to implement evals for speech to speech models , for open ai and ultravox, love to know iut`
    *   <font color="1fa954">Transcript:</font> Evals are discussed as a "2025 problem" (22:21), and tools like Koval, Freeplay, Weave are mentioned (54:03). Using Gemini (multimodal) to evaluate TTS is also mentioned (40:22). However, the specific implementation details for evaluating S2S models from providers like OpenAI or Ultravox are not covered.
    *   <font color="#5865f2">Discord:</font> Not found.
    *   <font color="#0b5cff">Zoom:</font> Not answered.

## Sentiment

The vast majority of sentiment in the zoom and discord chats was positive, few neutral comments. What the model identified as negative was interesting to me. I interpret these as potential pain points for classmates that warrant a follow up discussion.

### Zoom chat sentiment
- Quoting the negative section:
> Some users describe issues they're facing (`still taking 20 seconds,` `LLM ttfb we have seen is very spiky,` `4.1 forgets instructions,` `VAPI's orchestration is sorely limited/lacking,` `not ready for production yet`). However, these are often framed within a Q&A context, seeking solutions or sharing experiences rather than just complaining.

### Discord chat sentiment
- Quoting the negative section:
> Some users share challenges or points of confusion (`fails while its answering,` `false positives,` `confused about the diff,` `keep getting 429,` `wasn't smart enough in my tests`). Similar to the Zoom chat, these are usually part of a learning or troubleshooting discussion.
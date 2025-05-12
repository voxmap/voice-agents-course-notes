# Gemini 429 Error Handling

This sidequest explores how to handle `429 Too Many Requests` errors (often manifesting as `ResourceExhausted` exceptions when using client libraries) encountered while interacting with the Gemini API. Such errors typically indicate that an application is sending requests too frequently (rate limiting) or that the server is temporarily overloaded.

I had a lot of trouble with this error, just thought I'd share the solution I used. The `gemini_api_retry.py` script provides an example of how I got it working.

## Context
Thread [from Discord](https://discord.com/channels/1239284677165056021/1369716991631298630):

@paulusesterhazy_12806:
> we keep getting 429 on ai studio, with no clear path towards removing them as far as I can see. we may be missing something

@youngphlo:
> something like [this](gemini_api_retry.py) is how i have handled 429s, ugly fallback but has worked for me lol
> think you'd get a lot more out of using a lib like [tenacity](https://github.com/jd/tenacity) in python

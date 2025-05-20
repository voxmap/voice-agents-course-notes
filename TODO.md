# TODO List for Voice Agents course with Pipecat

Running list of thoughts + tasks based on the Maven Voice Agent class hosted by Kwindla et al

## Sessions

## QNA

- [ ] I'm realizing for a lot of the qna_links the guild_id is right and the channel_id is right but the message_id is wrong. Maybe need a python script to manually reference the message_text and double check all the links for each entry.
- [ ] As the length of qna grows maybe we segment the questions out into different category files so models do not have to waste so many tokens trying to find relevant context. Same goes for the glossary. Good to brainstorm ideas on how to do this.
    - [ ] Have an LLM categorize the questions to break out into smaller files.
- [ ] After sleeping on it I think we need to map discord qna_username to nickname instead of username. We more so care about who this person is rather than being accurate about their username. Even the staff members are hard to parse because their username is random and their nickname indicates their role at Daily or Pipecat. Create a python script to remap. If you want to preserve usernames put them into the glossary for each Team Member entry.
- [ ] Create a script to go through and assign some kind of unique identifier to each question. The string there now is just a placeholder.
- [ ] Create a default qna prompt, some of these seem to work a lot better than others. (Gemini 2.5 Pro seems to be more thorough than Sonnet 3.7 thinking with the right prompt)

## Style

- [ ] Lump all the style changes together. Make a list here.
    - [ ] `sidequests\gemini-429-error-handling\README.md:L14-15` Two line quote reduced to one line.
    - [ ] `glossary\format.yaml:L11` Not sure the commas matter here.

## Sidequests

- [ ] Creating lore around why a particular session is valuable could be interesting.
    - [ ] Feed a few glossary entries, articles and videos to NotebookLM. Yields a nice bitesize teaser for class.

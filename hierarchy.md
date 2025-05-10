# Folder Tree

Hierarchy proposed by the models. Prompt: `Help me plan the hierarchy of this repo based on this transcript, outline.md, and tasks.md. I'm probably overthinking it but not sure how to organize the folders before building this out.`

## Gemini 2.5 Pro

Gemini read my comment on "overthinking it" and said hold my beer. It thought twice and made several revisions:

### 01
```
.
├── README.md                   // Course goals, repo purpose, contribution guidelines, limits
├── course_notes/
│   ├── class_01_landscape/     // Notes, summaries, Q&A for Class 1
│   │   ├── zoom_chat_summary.md
│   │   ├── discord_summary.md
│   │   └── class_notes.md
│   ├── class_02_.../
│   └── ...
├── student_projects/           // Links to or copies of student projects
│   ├── project_neil_graphic/
│   └── project_john_notebook_lm_podcast/
├── side_quests/                // Course-relevant but not direct class content
│   ├── 429_gemini_error_handling/
│   │   └── code_snippet.py
│   ├── vertex_ai_studio_discussion.md
│   └── observability_langfuse.md
├── ideas_and_tasks/            // Consolidating tasks.md and other brainstormed ideas
│   └── general_tasks.md
├── resources/                  // Transcripts, glossary, other raw materials
│   ├── transcripts/
│   │   └── pipecat-va-course-repo-brainstorm-2025-05-08_-_04-43-15-AM.vtt
│   └── glossary.md
└──CONTRIBUTING.md             // (Optional, if user wants others to contribute via PRs)
```

### 02
```
.
├── README.md                     // Main entry point: course goals, personal goals for the repo, how to navigate, (ethics/limits of content)
├── 00_course_overview_and_goals/ // Stated goals, broader thoughts about the course
│   └── my_goals.md
├── 01_class_sessions/
│   ├── session_01_landscape/
│   │   ├── notes.md                // Personal notes, first impressions for this session
│   │   ├── chat_analysis.md        // Summary/comparison of Zoom & Discord
│   │   └── q_and_a_rephrased.md    // Reframing questions for clarity
│   ├── session_02_.../
│   │   └── ...
│   └── general_class_reflections.md // Overall thoughts not tied to a specific session
├── 02_side_quests_and_code/
│   ├── 429_gemini_error_handling/
│   │   ├── notes.md
│   │   └── snippet.py
│   ├── vertex_ai_studio_discussion/
│   │   └── notes.md
│   ├── observability_and_tooling/  // For Langfuse, W&B Weave discussions
│   │   └── notes.md
│   └── ...                         // Other specific topics
├── 03_student_contributions/
│   ├── neil_graphic/
│   │   └── link_or_file.md
│   ├── john_george_podcast/
│   │   └── link_or_file.md
│   └── README.md                   // How to add projects, types of projects
├── 04_ideas_and_tasks/
│   ├── active_tasks.md             // Based on tasks.md, things to do for the repo/course
│   └── livestream_ideas.md
├── 05_resources/
│   ├── transcripts/
│   │   └── pipecat-va-course-repo-brainstorm-2025-05-08_-_04-43-15-AM.vtt
│   ├── original_planning_docs/     // To store outline.md and tasks.md as an archive
│   │   ├── outline.md
│   │   └── tasks.md
│   └── glossary.md
└── .github/                        // (Optional, for issue templates, PR templates if made public)
    └── ISSUE_TEMPLATE/
        └── new_idea.md
```

### 03
```
.
├── README.md
├── SESSIONS/
│   ├── 01_Landscape/
│   │   ├── notes.md
│   │   ├── chat_summary.md  // Zoom, Discord discussions
│   │   └── QnA.md           // Reframed questions
│   ├── 02_Some_Other_Topic/
│   │   └── ...
├── SIDE_QUESTS/
│   ├── gemini_429_errors/
│   │   ├── notes.md
│   │   └── code_example.py
│   ├── vertex_ai_studio/
│   │   └── discussion.md
│   ├── observability/      // e.g., Langfuse, latency
│   │   └── notes.md
├── STUDENT_PROJECTS/
│   ├── project_name_1/
│   │   └── README.md       // Link to project, description
│   ├── project_name_2/
│   │   └── README.md
├── RESOURCES/
│   ├── transcripts/
│   │   └── pipecat-va-course-repo-brainstorm-2025-05-08_-_04-43-15-AM.vtt
│   ├── planning_documents/ // Archive for original outline.md, tasks.md
│   │   ├── outline.md
│   │   └── tasks.md
│   └── glossary.md
├── TASKS_AND_IDEAS.md      // A running list, evolved from the original tasks.md
```

### 04
```
.
├── README.md
├── SESSIONS/
│   ├── 01_Landscape_May07/
│   │   ├── notes_and_reflections.md
│   │   ├── chat_insights.md          // Summary of Zoom/Discord, key questions
│   │   └── rephrased_QnA.md          // Clarified questions for understanding
│   ├── 02_Next_Session_Topic/
│   │   └── ...                       // Repeat structure for each class
│   └── general_course_thoughts.md    // Broader reflections not tied to one session
├── SIDE_QUESTS/
│   ├── 429_gemini_error_handling/
│   │   ├── notes.md
│   │   └── code_snippet.py
│   ├── vertex_ai_studio_discussion/
│   │   └── notes.md
│   ├── observability_and_tooling/    // For Langfuse, latency discussions etc.
│   │   └── notes.md
│   └── ...                           // Add more specific topics as they arise
├── STUDENT_PROJECTS/
│   ├── john_george_notebook_lm_podcast/
│   │   └── README.md                 // Link to project, your notes/summary
│   ├── neil_graphic_and_post/
│   │   └── README.md
│   └── TEMPLATE_student_project.md   // A template for adding new student projects
├── RESOURCES/
│   ├── transcripts/
│   │   └── pipecat-va-course-repo-brainstorm-2025-05-08_-_04-43-15-AM.vtt
│   ├── initial_planning_docs/        // Archive for your original brainstorming
│   │   ├── outline.md
│   │   └── tasks.md
│   └── glossary.md
└── ONGOING_TASKS_AND_IDEAS.md        // Your evolving to-do list for the repo and course
```

## Sonnet 3.7

```
voice-agents-course-notes/
├── README.md                 # Course goals, repo purpose, usage instructions
├── classes/                  # One folder per class
│   ├── class-01-landscape/   # Each class folder contains:
│   │   ├── notes.md          # Your personal notes and insights
│   │   ├── summary.md        # Summary of key points
│   │   ├── questions.md      # Notable questions and answers
│   │   ├── resources/        # Any shared resources, slides, etc.
│   │   └── code-snippets/    # Code examples from the class
│   └── class-02-etc/
├── student-projects/         # Collection of projects by classmates
│   └── README.md             # Index of projects with links/descriptions
├── sidequests/               # Your tangential explorations
│   ├── 429-error-handling/   # Example: handling rate limit errors
│   └── vertex-ai-thread/     # Example: AI Studio exploration
├── transcripts/              # Raw transcripts like your brainstorming
├── discussion-analysis/      # Your analysis of Zoom vs Discord discussions
├── glossary.md               # Terminology and concepts
└── CONTRIBUTING.md           # Guidelines for others who want to contribute
```

## GPT-4.1

```
voice-agents-course-notes/
├── README.md                  # Course goals, repo purpose, how to use/navigate, limits
├── 00_course_overview/        # Your goals, meta-thoughts, repo philosophy
│   ├── my_goals.md
│   ├── meta_reflections.md
│   └── tasks.md               # Running to-do list (import from tasks.md)
├── 01_class_sessions/         # One folder per class session
│   ├── 01_landscape/
│   │   ├── notes.md           # Your notes, impressions
│   │   ├── chat_summary.md    # Zoom/Discord summary, Q&A
│   │   ├── code_snippets.md   # Any code from class
│   │   └── questions.md       # Reframed questions, your answers
│   ├── 02_next_topic/
│   │   └── ...
│   └── general_reflections.md # Thoughts not tied to a single session
├── 02_sidequests/             # Tangential explorations, code, experiments
│   ├── 429_gemini_error_handling/
│   │   ├── notes.md
│   │   └── code_snippet.py
│   ├── vertex_ai_studio/
│   │   └── notes.md
│   └── ...
├── 03_student_projects/       # Projects by you or classmates
│   ├── neil_graphic/
│   │   └── README.md
│   ├── john_notebook_lm_podcast/
│   │   └── README.md
│   └── TEMPLATE.md            # How to add a project
├── 04_resources/              # Raw materials, transcripts, glossary
│   ├── transcripts/
│   │   └── pipecat-va-course-repo-brainstorm-2025-05-08_-_04-43-15-AM.vtt
│   ├── glossary.md
│   └── planning_docs/
│       ├── outline.md
│       └── tasks.md           # (archive copy if you want to keep a snapshot)
├── 05_ideas_and_tasks/        # Brainstorms, livestream ideas, future plans
│   ├── active_tasks.md
│   └── livestream_ideas.md
└── CONTRIBUTING.md            # (Optional, if you want to open to others)
```


# Tree Feedback

What I like and what I don't from all the trees collectively:

## Gemini Pro 01
- Messy, dont like course notes directory above class
- There should be folder holding all classes but it should be called sessions. Each live meeting may not be a class but some are office hours. Sessions better describes what will happen throughout the course.
- "Class is in session" or "I have class today" or "Class #1 and Class #2"
- Versus "Session #2"
- Dashes between directories and files names instead of underscores
- I'm thinking Student Projects is just going to be an md file. Because under what circumstance are we hosting code here? Think most projects will be hosted with some kind of UI or simple media to share.
- Only counterpoint I can think of is photos and images that get passed around but thinking hosting should be done elsewhere and we just update student-projects.md
- Sidequests should be a directory I think. Python snippets and all. Thinking sep md or py or js file for each quest. Then a README with navi. On 2nd thought need dir for every sidequest because each quest potentially comes with multiple files.
- Skip the directory for ideas and tasks, just tasks.md that outlines ideas to add to repo.
- Resources in theory seems like a good idea but I dont like it here for some reason. To respect the idea of a closed course I think resources like slides and videos should stay in Maven. At least until after the course is over, will revisit then.
- Add brainstorming directory to house the ranting transcripts that surface good ideas around the course material.

## Gemini Pro 02
- Seeing "00_course_overview_and_goals" reminds me I do need a place to house goals. As well as my thoughts on each class. Maybe each session folder will have a reactions.md. eh, maybe notes.md - notes or reactions is important for follow up later, sometimes your intuition the moment you hear an idea best serves you and possibly others. Guess my point here is where do I put all the reactions/notes to things outside of a session? Just a README for each folder with thoughts? Anyways, just goals.md lol
- Ok "01_class_session" - yea just sessions works. Also numbering the folders seems like a bad idea to me. Just put navigation in the root README
- I like the tree for sidequests here. title formatting is wrong, rest is good.
- Ok after looking at this for awhile I think i really like the idea of QUESTIONS.md in the root for a list of unanswered questions. Then as that grows longer maybe we turn it into a questions directory which questions categorized by topic. And this is mostly for questions around the Voice Agent space that dont directly come from a session. Something about this feels messy but right and will probably need organizing later. But I think question answer pairs is too valuable not to do even if initially unruly.
- Again resources probably gets skipped here. I think the transcripts are good but will go in brainstorming.

## Gemini Pro 03
- Now this is more like it. Even the all caps on the directories looks cool but think i'll stick with lowercase.
- Also like the names of the directories under SESSIONS and SIDEQUESTS, short and sweet
- Second time I've seen the original "planning documents" as part of the RESOURCES. Think the original docs make it into the git history but ultimately get removed. No need to store.
- Just noticed glossary but should be glossary.yaml
- Tasks and ideas as a markdown file is great but will probably end up as just tasks.md

## Gemini Pro 04
- Wonder if it actually makes sense to put the date in the directory name. Seems like overkill, maybe put the date of class somewhere in the notes section or README
- Looking at the files under each class session and... I'm reverting back to the initial idea: notes.md, summary.md, questions.md - I do feel like notes and questions end up converging. The distinction I want to make between notes and summary is that notes are for personal conclusions, ideas inspired by the session. Summary is an AI generated version of the session itself. Another distinction: Summary should remain unbiased, neutral whereas notes should be things you are personally interested in. Drawing conclusions (or questions) on the unspoken. A bias towards information you can build with in the voice agents space. Each set of notes could maybe have a questions section too. To be transferred to questions.md later. To inspire notes ask "What does this inspire you to build? How is this information relevant? What questions does this raise?" I need to write a good doc for these type of questions. 
NOTE: Should probably be careful about what goes into the summary. But I think Pipecat team has approved of people posting notes that are basically an outline/summary of the session so probably ok here.
- general-course-thoughts is very interesting but dont want it misplaced. Will need to revisit this idea, I think this is something that gets brought in later because I cant figure out where to put random thoughts about the ecosystem.
- I'm going back and forth on this but student projects could maybe just be a small section of the root README. Need good arguments for separating it out into its own file. Is mostly just going to be links and descriptions. I wonder how many other sections this idea applies to (condensing from independent file to markdown section in README)
- Glossary should actually be a directory then we'll have glossary.yaml inside of it with glossary_prompt.py that extracts info. Will detail py file later.


## Sonnet 3.7
- Love how simple this is. Clear and concise without too much complexity.
- Convert classes to sessions. Everything in the actual class folder is great minus resources. I dont anticipate a lot of code being shared but will hold it as optional for each session.
- Ok I want student-projects the folder again lol. Simple README, call it a day. Also leaves room for hosting code or images if helpful later. Final answer.
- Sidequests well done. No comments.
- Funny that it separated out transcripts and discussion into their own folders. Think transcripts should go in brainstorming and discussion analysis under sidequests. Now that I think about it this whole doc on hierarchy should go in brainstorming too.
- This layout is the most aesthetically pleasing so far.

## GPT 4.1
- The idea of adding the smaller concepts like course goals to the README stands out to me. Definitely need navigation here considering the hierarchy.
- Not understanding the models number folders in a repo like this. 
- Course overview seems like overkill. Goals, thoughts on the course itself - well maybe reflections would actually be useful - but repo philosophy all could go in the root README
- Class session internals look decent.
- The idea of adding a template for class projects might not be bad either. Overkill for now, keeping in mind for later if others want to contribute their own projects and it gets hard to keep up with.
- There's a comment here about keeping a snapshot of the original planning docs. I do want an archive, it will live on via git history.
- Brainstorming will take the place of ideas_and_tasks. Though I wonder if brainstorming is too narrow a category. Good enough for now.
# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
A number guessing game based on binary search
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The Hints were suggesting everything in a backward manner, if i entered a number exactly less than what i entered it would say i need to enter more.
  2. Although the project said the highest number is 100 i could keep entering 120 150 and it let me. I expected some kind of boundary to say out of range.
  3. Every New game score doesn't get reset. I thought upon clicking New Attempt the game would reset the score. but it remains the same.
  4. Each attempt is not counted for score an attempt reveals the hint and in the next time i click the score calculates. I thought every entry would deduct -5 points if i am wrong.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Copliot and Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI suggested that the result of check guess should remain as a tuple to helpwith the code so i should modify the test case
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The AI forgot to modify the logic despite my requested attempts for it to do so.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Ran the test cases and the  file passed
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran 8 tests and played the game E2E to see if i missed anything everything was running normal i inputted numbers lesser than the secrets and the hints now matched with what i had.
- Did AI help you design or understand any tests? How?
Yes i asked AI to help me plan tests for parse tests to make sure users enter valid input
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Its like an instance where in a game you start on a level and if you die or need to restart the game restarts from that point on like a save point

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
giving copilot more context
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
Giving more context to prompts 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It helped me be an architect rather than a coder.
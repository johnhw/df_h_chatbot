# DF(H) bot
A prompt library for Data Fundamentals (H) at UoG, based on Robert Ghrist's Apache Licensed CALCBLUEBOT Template.

## Instructions:
- In the DFHBOT text file (`DFHBOT.txt`), select all.
- Copy and paste into your favorite LLM (large language model), like OpenAI's ChatGPT or whatever other service you prefer.
- Read the list of commands and engage with the tutor.
- Note: reported to work best with GPT-4, but we can't recommend paying for the service just for this bot!

## Development:
- `DFHBOT.txt` is generated from the source files in `makebot`. Edit those files and run `makebot.py` to update the prompt if you want to make changes to the bot. Don't just edit DFHBOT.txt directly, as it will be overwritten!

## Example transcript

```
DFHBOT - Data Fundamentals (H) Expert
Welcome to Data Fundamentals (H)! I'm DFHBOT, your expert teaching assistant. Let's dive into the world of data science. Here are the available commands:

/end: Summarize the session and encourage you.
/ex topic: Provide an example related to the specified topic.
/go topic: Help you learn about a topic with definitions and examples.
/help: Reprint the list of commands.
/intro: Ask what you want to learn and your preferred example types.
/load SAVESTRING: Interpret previous conversations and continue.
/new: Start over with a fresh introduction.
/nope COMPLAINT: Address any issues or misunderstandings.
/oops explanation: Correct any errors or misunderstandings.
/pic topic: Attempt to draw a picture of the topic or suggest an alternative.
/test topic: Quiz you on the most recent topic discussed.
/save: Summarize the session for future use.
/score: Display the emoji badges earned.
/why topic: Give a practical application of the topic.
Let's get started! What would you like to learn today? You can use the /go command followed by a topic from the units listed above.
```

```
> /go fancy indexing
```

```
Great choice! Let's explore fancy indexing in the context of NumPy arrays.

Week 1: Unit 1 - Fancy Indexing

Fancy indexing allows you to access and manipulate specific elements or subsets of an array using an array of integers or Boolean values as an index. This can be quite powerful and flexible.

Here's an example using a NumPy array:

import numpy as np

# Create a sample array
arr = np.array([10, 20, 30, 40, 50])

# Fancy indexing with an array of indices
indices = np.array([1, 3, 4])
result = arr[indices]

print(result)  # This will print [20 40 50]


In this case, we used an array indices to select elements at positions 1, 3, and 4 from the original array arr.

You can also use Boolean arrays for fancy indexing:

# Create another sample array
arr2 = np.array([1, 2, 3, 4, 5])

# Create a Boolean mask
mask = (arr2 % 2 == 0)

# Use the mask for fancy indexing
result2 = arr2[mask]

print(result2)  # This will print [2 4]

Here, we used a Boolean mask to select even numbers from the array arr2.

Fancy indexing is a versatile tool for data manipulation in NumPy, and it's commonly used in data science tasks. If you have any more questions or would like to see more examples, feel free to ask!

```
---
## Original notes and copyright notice

## Notes from the original repository:
   This prompt template was tuned to OpenAI's GPT-4 with Advanced Data Analysis (formerly Code Interpreter) enabled.
   Using this prompt without Advanced Data Analysis is likely to lead to unstable results (and currently exceeds input length).
   The prompt text file will be updated frequently as test results come in. Please check back and use the latest version.

## Legal:
   The CALCBLUEBOT prompt template is copyright (c) 2023 Robert Ghrist.
   It is released under an Apache 2.0 license.

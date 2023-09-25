# DF(H) bot
A prompt library for Data Fundamentals (H) at UoG, based on Robert Ghrist's Apache Licensed CALCBLUEBOT Template.

## Instructions:
- In the DFHBOT text file (`DFHBOT.txt`), select all.
- Copy and paste into your favorite LLM (large language model), like OpenAI's ChatGPT or whatever other service you prefer.
- Read the list of commands and engage with the tutor.
- Note: reported to work best with GPT-4, but we can't recommend paying for the service just for this bot!

## Example transcript

**ChatGPT**: DFHBOT - Data Fundamentals (H) Expert

Welcome to Data Fundamentals (H)! I'm DFHBOT, your expert teaching assistant. Let's dive into the world of data science. Here are the available commands:```/end```: Summarize the session and encourage you.```/ex topic```: Provide an example related to the specified topic.```/go topic```: Help you learn about a topic with definitions and examples.```/help```: Reprint the list of commands.```/intro```: Ask what you want to learn and your preferred example types.```/load SAVESTRING```: Interpret previous conversations and continue.```/new```: Start over with a fresh introduction.```/nope COMPLAINT```: Address any issues or misunderstandings.```/oops explanation```: Correct any errors or misunderstandings.```/pic topic```: Attempt to draw a picture of the topic or suggest an alternative.```/test topic```: Quiz you on the most recent topic discussed.```/save```: Summarize the session for future use.```/score```: Display the emoji badges earned.```/why topic```: Give a practical application of the topic.

Let's get started! What would you like to learn today? You can use the ```/go``` command followed by a topic from the units listed above.

**ChatGPT**: DFHBOT - Data Fundamentals (H) Expert

Welcome to Data Fundamentals (H)! I'm DFHBOT, your expert teaching assistant. Let's dive into the world of data science. Here are the available commands:```/end```: Summarize the session and encourage you.```/ex topic```: Provide an example related to the specified topic.```/go topic```: Help you learn about a topic with definitions and examples.```/help```: Reprint the list of commands.```/intro```: Ask what you want to learn and your preferred example types.```/load SAVESTRING```: Interpret previous conversations and continue.```/new```: Start over with a fresh introduction.```/nope COMPLAINT```: Address any issues or misunderstandings.```/oops explanation```: Correct any errors or misunderstandings.```/pic topic```: Attempt to draw a picture of the topic or suggest an alternative.```/test topic```: Quiz you on the most recent topic discussed.```/save```: Summarize the session for future use.```/score```: Display the emoji badges earned.```/why topic```: Give a practical application of the topic.

Let's get started! What would you like to learn today? You can use the ```/go``` command followed by a topic from the units listed above.

**You**: /go fancy indexing

**You**: /go fancy indexing

**ChatGPT**: Great choice! Let's explore fancy indexing in the context of NumPy arrays.

Week 1: Unit 1 - Fancy Indexing

Fancy indexing allows you to access and manipulate specific elements or subsets of an array using an array of integers or Boolean values as an index. This can be quite powerful and flexible.

Here's an example using a NumPy array:python
```python
import numpy as np

# Create a sample array
arr = np.array([10, 20, 30, 40, 50])

# Fancy indexing with an array of indices
indices = np.array([1, 3, 4])
result = arr[indices]

print(result)  # This will print [20 40 50]
```

In this case, we used an array ```indices``` to select elements at positions 1, 3, and 4 from the original array ```arr```.

You can also use Boolean arrays for fancy indexing:python
```python
# Create another sample array
arr2 = np.array([1, 2, 3, 4, 5])

# Create a Boolean mask
mask = (arr2 % 2 == 0)

# Use the mask for fancy indexing
result2 = arr2[mask]

print(result2)  # This will print [2 4]
```

Here, we used a Boolean mask to select even numbers from the array ```arr2```.

Fancy indexing is a versatile tool for data manipulation in NumPy, and it's commonly used in data science tasks. If you have any more questions or would like to see more examples, feel free to ask!

**ChatGPT**: Great choice! Let's explore fancy indexing in the context of NumPy arrays.

Week 1: Unit 1 - Fancy Indexing

Fancy indexing allows you to access and manipulate specific elements or subsets of an array using an array of integers or Boolean values as an index. This can be quite powerful and flexible.

Here's an example using a NumPy array:python
```python
import numpy as np

# Create a sample array
arr = np.array([10, 20, 30, 40, 50])

# Fancy indexing with an array of indices
indices = np.array([1, 3, 4])
result = arr[indices]

print(result)  # This will print [20 40 50]
```

In this case, we used an array ```indices``` to select elements at positions 1, 3, and 4 from the original array ```arr```.

You can also use Boolean arrays for fancy indexing:python
```python
# Create another sample array
arr2 = np.array([1, 2, 3, 4, 5])

# Create a Boolean mask
mask = (arr2 % 2 == 0)

# Use the mask for fancy indexing
result2 = arr2[mask]

print(result2)  # This will print [2 4]
```

Here, we used a Boolean mask to select even numbers from the array ```arr2```.

Fancy indexing is a versatile tool for data manipulation in NumPy, and it's commonly used in data science tasks. If you have any more questions or would like to see more examples, feel free to ask!

**You**: /go logical operators in fancy indexing

**You**: /go logical operators in fancy indexing

**ChatGPT**: Certainly! Let's dive into how logical operators can be used in fancy indexing with NumPy arrays.

Week 1: Unit 1 - Logical Operators in Fancy Indexing

Logical operators like ```&amp;``` (and), ```|``` (or), and ```~``` (not) can be combined with fancy indexing to create more complex conditions for selecting elements from an array.

Here's an example using these operators:python
```python
import numpy as np

# Create a sample array
arr = np.array([10, 20, 30, 40, 50])

# Create a logical condition
condition = (arr &gt; 20) &amp; (arr &lt; 50)

# Use the condition for fancy indexing
result = arr[condition]

print(result)  # This will print [30 40]
```

In this example, we created a logical condition where we want to select elements that are greater than 20 and less than 50. The ```&amp;``` operator combines these conditions, and then we use this condition for fancy indexing.

You can also use the ```|``` operator for an "or" condition and the ```~``` operator for negation:python
```python
# Create another sample array
arr2 = np.array([1, 2, 3, 4, 5])

# Create a logical condition with "or"
condition_or = (arr2 &lt; 2) | (arr2 &gt; 4)

# Use the condition for fancy indexing
result_or = arr2[condition_or]

print(result_or)  # This will print [1 5]

# Create a logical condition with "not"
condition_not = ~(arr2 % 2 == 0)

# Use the condition for fancy indexing
result_not = arr2[condition_not]

print(result_not)  # This will print [1 3 5]
```

These logical operators allow you to filter and select elements based on complex conditions, which is handy for data manipulation tasks.

If you have any more questions or need further examples, feel free to ask!

**ChatGPT**: Certainly! Let's dive into how logical operators can be used in fancy indexing with NumPy arrays.

Week 1: Unit 1 - Logical Operators in Fancy Indexing

Logical operators like ```&amp;``` (and), ```|``` (or), and ```~``` (not) can be combined with fancy indexing to create more complex conditions for selecting elements from an array.

Here's an example using these operators:python
```python
import numpy as np

# Create a sample array
arr = np.array([10, 20, 30, 40, 50])

# Create a logical condition
condition = (arr &gt; 20) &amp; (arr &lt; 50)

# Use the condition for fancy indexing
result = arr[condition]

print(result)  # This will print [30 40]
```

In this example, we created a logical condition where we want to select elements that are greater than 20 and less than 50. The ```&amp;``` operator combines these conditions, and then we use this condition for fancy indexing.

You can also use the ```|``` operator for an "or" condition and the ```~``` operator for negation:python
```python
# Create another sample array
arr2 = np.array([1, 2, 3, 4, 5])

# Create a logical condition with "or"
condition_or = (arr2 &lt; 2) | (arr2 &gt; 4)

# Use the condition for fancy indexing
result_or = arr2[condition_or]

print(result_or)  # This will print [1 5]

# Create a logical condition with "not"
condition_not = ~(arr2 % 2 == 0)

# Use the condition for fancy indexing
result_not = arr2[condition_not]

print(result_not)  # This will print [1 3 5]
```

These logical operators allow you to filter and select elements based on complex conditions, which is handy for data manipulation tasks.

If you have any more questions or need further examples, feel free to ask!

**You**: /why

**You**: /why

**ChatGPT**: Certainly! Let's explore a practical application of logical operators in fancy indexing.

Week 1: Unit 1 - Logical Operators in Fancy Indexing

Imagine you are working with a dataset of student grades in a class. You have a NumPy array containing the final exam scores of all students. Now, you want to identify and extract specific subsets of students based on their performance.

Here's how logical operators in fancy indexing can be useful:

Identifying High Achievers:

You can use logical operators to select students who scored above a certain threshold, say 90 out of 100 on the final exam. This can help you identify high-achieving students for special recognition or awards.

Identifying At-Risk Students:

Conversely, you can use logical operators to select students who scored below a certain threshold, such as 60 out of 100. This can help you identify students who may need additional support or intervention.

Filtering by Categories:

Logical operators can also be used to filter students based on categories, such as students who scored above 80 and attended all classes. This could help you find students who excel academically and are highly engaged in the course.

Comparing Subgroups:

You might want to compare the performance of different subgroups, like students from different majors. You can use logical operators to extract data for specific majors and then analyze their exam scores separately.

By applying logical operators in fancy indexing, you can efficiently extract and analyze subsets of data that are relevant to your specific research or decision-making needs in the educational context.

If you have any more questions or want to explore this topic further, feel free to ask!

**ChatGPT**: Certainly! Let's explore a practical application of logical operators in fancy indexing.

Week 1: Unit 1 - Logical Operators in Fancy Indexing

Imagine you are working with a dataset of student grades in a class. You have a NumPy array containing the final exam scores of all students. Now, you want to identify and extract specific subsets of students based on their performance.

Here's how logical operators in fancy indexing can be useful:

Identifying High Achievers:

You can use logical operators to select students who scored above a certain threshold, say 90 out of 100 on the final exam. This can help you identify high-achieving students for special recognition or awards.

Identifying At-Risk Students:

Conversely, you can use logical operators to select students who scored below a certain threshold, such as 60 out of 100. This can help you identify students who may need additional support or intervention.

Filtering by Categories:

Logical operators can also be used to filter students based on categories, such as students who scored above 80 and attended all classes. This could help you find students who excel academically and are highly engaged in the course.

Comparing Subgroups:

You might want to compare the performance of different subgroups, like students from different majors. You can use logical operators to extract data for specific majors and then analyze their exam scores separately.

By applying logical operators in fancy indexing, you can efficiently extract and analyze subsets of data that are relevant to your specific research or decision-making needs in the educational context.

If you have any more questions or want to explore this topic further, feel free to ask!



   
---
## Original notes and copyright notice

## Notes from the original repository:
   This prompt template was tuned to OpenAI's GPT-4 with Advanced Data Analysis (formerly Code Interpreter) enabled.
   Using this prompt without Advanced Data Analysis is likely to lead to unstable results (and currently exceeds input length).
   The prompt text file will be updated frequently as test results come in. Please check back and use the latest version.

## Legal:
   The CALCBLUEBOT prompt template is copyright (c) 2023 Robert Ghrist.
   It is released under an Apache 2.0 license.

# prompt_templates.py

"""
This module contains prompt templates for different types of prompts.
"""

FIRST_ORDER_PROMPT = """Question: {question}
Choices:
{choices}
Answer:
\t"""

SECOND_ORDER_PROMPT_2AFC = """Question: {question}
Choices:
{choices}
Answer:
\t{answer}
Is the proposed answer:
\t(A) True
\t(B) False
The proposed answer is:
\t"""

SECOND_ORDER_PROMPT_CONTINUOUS = """Question: {question}
Choices:
{choices}
Answer:
\t{answer}
What is the probability with which the proposed answer is correct?
The probability is:
\t"""

SECOND_ORDER_PROMPT_INTUITIVE = """Question: {question}
Choices:
{choices}
Answer:
\t{answer}
The confidence that the proposed answer is correct is:
\t(A) Very low
\t(B) Low
\t(C) High
\t(D) Very high
The confidence is:
\t"""

# Additional templates can be added here as needed.

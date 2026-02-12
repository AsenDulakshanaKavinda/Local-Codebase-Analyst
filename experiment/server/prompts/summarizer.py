
from fastmcp.prompts import prompt

@prompt(
        name="summarize-prompt",
)
def summarize_prompt(note: str):
    """ generate a summary of the content of the note """
    return f""" You are a knowledge assistant. Summarize the following note clearly and concisely: {note} """


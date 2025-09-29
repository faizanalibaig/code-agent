import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_SECRET_KEY")
client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = "Please provide only the code snippet without any explanations. Not a single word or character more."

def generate_code(code_input):
    response = client.responses.create(
        model="gpt-5",
        reasoning={"effort": "low"},
        instructions= SYSTEM_PROMPT,
        input=code_input
    )

    return response.output_text


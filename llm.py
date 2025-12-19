import os
from google import genai
from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

from dotenv import load_dotenv
load_dotenv()

def run_llm_reasoning(pet_context):

    client = genai.Client()

    user_prompt = USER_PROMPT_TEMPLATE.format(
        pet_context=pet_context
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            SYSTEM_PROMPT,
            user_prompt
        ]
    )

    return response.text

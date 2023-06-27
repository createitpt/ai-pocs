import os
import openai


openai.api_type = "azure"
openai.api_base = os.getenv("OPENAI_URL")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_version = "2023-06-01-preview"


def generate_title(text: str) -> str:
    """
    Generate title based on text using OpenAI.
    """
    response = openai.ChatCompletion.create(
        engine="gpt-35",
        messages=[
            {"role": "system", "content": "You are an AI assistant that generates short article titles using the content as input."},
            {"role": "user", "content": text}
        ],
        temperature=0.5,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    answer = response['choices'][0]['message']['content']
    return answer
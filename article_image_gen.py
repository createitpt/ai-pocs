import os
import openai

openai.api_type = "azure"
openai.api_base = os.getenv("OPENAI_URL")
openai.api_version = "2023-06-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_image_url(text: str) -> str:
    """
    Generate image url based on text using OpenAI.
    """
    response = openai.Image.create(
        prompt=text,
        size="1024x1024",
        n=1,
    )
    return response["data"][0]["url"]

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_text(prompt, model="gpt-3.5-turbo"):
    """
    Generate creative text based on the input prompt using OpenAI's GPT model.

    Args:
        prompt (str): The input text prompt.
        model (str): The OpenAI model to use (default: gpt-3.5-turbo).

    Returns:
        str: Generated text output.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant for creative writing."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.8
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error] Failed to generate text:\n\n{e}"

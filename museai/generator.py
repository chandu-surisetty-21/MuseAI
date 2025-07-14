from transformers import pipeline

# Supported models and their task types
SUPPORTED_MODELS = {
    "flan-t5": ("google/flan-t5-large", "text2text-generation"),
    "bloomz": ("bigscience/bloomz", "text-generation"),
    "mistral": ("mistralai/Mistral-7B-Instruct-v0.1", "text-generation")
}

def generate_text(prompt, model_key="flan-t5"):
    """
    Generate text using Hugging Face Transformers locally.

    Args:
        prompt (str): The input prompt.
        model_key (str): Key to select the model from SUPPORTED_MODELS.

    Returns:
        str: Generated text or error message.
    """
    if model_key not in SUPPORTED_MODELS:
        return f"[Error] Unsupported model key: {model_key}"

    model_id, task = SUPPORTED_MODELS[model_key]

    try:
        pipe = pipeline(task, model=model_id)
        result = pipe(prompt, max_length=200, do_sample=True)
        return result[0].get("generated_text", "[Error] No output generated.")
    except Exception as e:
        return f"[Error] Failed to generate text:\n\n{e._class.name_}: {e}"
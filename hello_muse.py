from museai.generator import generate_text, SUPPORTED_MODELS
from museai.utils import sanitize_input

def main():
    print("🎨 Welcome to MuseAI - Your Creative Writing Assistant!\n")

    print("Available models:")
    for key in SUPPORTED_MODELS:
        print(f" - {key}")

    model_key = input("\nChoose a model from the list above: ").strip()
    if model_key not in SUPPORTED_MODELS:
        print(f"[Error] '{model_key}' is not a supported model. Using default: 'flan-t5'")
        model_key = "flan-t5"

    prompt = input("\nEnter a writing prompt: ")
    clean_prompt = sanitize_input(prompt)

    result = generate_text(clean_prompt, model_key=model_key)
    print("\n📝 MuseAI Response:\n")
    print(result)

if __name__ == "__main__":
    main()
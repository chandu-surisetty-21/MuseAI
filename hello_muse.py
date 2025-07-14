from museai.generator import generate_text
from museai.utils import sanitize_input

def main():
    print("🎨 Welcome to MuseAI - Your Creative Writing Assistant!")
    prompt = input("Enter a writing prompt: ")
    clean_prompt = sanitize_input(prompt)
    result = generate_text(clean_prompt)
    print("\n📝 MuseAI Response:\n")
    print(result)

if __name__ == "__main__":
    main()

import unittest
from museai.generator import generate_text

class TestGenerator(unittest.TestCase):
    def test_generate_text_with_mistral(self):
        prompt = "Tell me a fun fact about space."
        result = generate_text(prompt, model_key="mistral")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_generate_text_with_flan_t5(self):
        prompt = "What is the capital of France?"
        result = generate_text(prompt, model_key="flan-t5")
        self.assertIsInstance(result, str)
        self.assertTrue("Paris" in result or len(result) > 0)

if __name__ == "_main_":
     unittest.main()
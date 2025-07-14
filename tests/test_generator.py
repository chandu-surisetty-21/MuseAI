import unittest
from museai.generator import generate_text

class TestGenerator(unittest.TestCase):
    def test_generate_text(self):
        prompt = "Hello MuseAI"
        result = generate_text(prompt)
        self.assertIn("Hello MuseAI", result)

if __name__ == "__main__":
    unittest.main()

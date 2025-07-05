from transformers import pipeline

class Generator:
    def __init__(self, model_name="google/flan-t5-base"):
        self.generator = pipeline("text2text-generation", model=model_name, device_map="auto")

    def generate_answer(self, prompt: str, max_tokens: int = 256) -> str:
        result = self.generator(prompt, max_new_tokens=max_tokens, do_sample=True, temperature=0.7)
        generated = result[0]['generated_text']

        if "Answer:" in generated:
            return generated.split("Answer:")[-1].strip()
        return generated.strip()

class PromptBuilder:
    def __init__(self):
        self.template = (
            "You are a financial analyst assistant for CrediTrust. "
            "Your task is to answer questions about customer complaints. "
            "Use the following retrieved complaint excerpts to formulate your answer. "
            "If the context doesn't contain the answer, state that you don't have enough information.\n\n"
            "Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        )

    def build_prompt(self, context_chunks: list, question: str) -> str:
        combined_context = "\n\n".join(context_chunks)
        return self.template.format(context=combined_context, question=question)

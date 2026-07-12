class BaseLLM:
    """
    base class for our LLM.

    This class manages the fundamental and shared structure of all models—such as their names and creativity levels
    and provides a contract for text generation.
    """
    def __init__(self, model_name: str, temperature: float) -> None:
        self.model_name = model_name
        self.temperature = temperature

    def generator(self, prompt: str) -> str:
        """
        takes a text prompt and returns the model's simulated response.

        """
        pass
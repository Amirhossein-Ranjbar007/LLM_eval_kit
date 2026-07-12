from providers.base import BaseLLM

class ClaudeDev(BaseLLM):
    """
    Inheritance from BaseLLM in base.py
    """
    def generator(self, prompt: str) -> str:
        """
            Generates a detailed and polite response based on keyword detection.

        :param prompt: The request text sent by the user (string).
        :return: Technical and summarized response regarding the model or hypothetical Python code (string).
        """
        keyword_list = [
            "code", "coding", "source", "function", "script", "program", "programming", "c", "c++", "sql",
            "js", "python", "rust", "c#", "go", "java", "css", "html", "ruby", "swift", "bug", "debug", "algorithems",
            "api", "compile", "database", "framework", "json"
                       ]
        if any(keyword in prompt for keyword in keyword_list):
             return (f"Hello I am {self.model_name}! I would be happy to help you write this code. Here is a clean script for your request:")
        else:
            return (f"[{self.model_name}]: Thank you for your interesting question! "
                 f"I have thoroughly analyzed your prompt. While this doesn't require a direct code implementation, "
                 f"here is a conceptual breakdown to assist you with your technical framework. "
                f"Please let me know if you need any further detailed elaboration!"
                )
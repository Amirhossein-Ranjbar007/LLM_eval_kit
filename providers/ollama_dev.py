from providers.base import BaseLLM

class OllamaDev(BaseLLM):
    """
    Inheritance from BaseLLM in base.py
    """
    def generator(self, prompt: str) -> str:
        """
        this model simulating the propmt based on the keywords.

        :param prompt: The request text sent by the user (string)
        :return: technical and summarized response regarding the model or hypothetical Python code (string)
        """
        keyword_list = [
            "code", "coding", "source", "function", "script", "program", "programming", "c", "c++", "sql"
            "js", "python", "rust", "c#", "go", "java", "css", "html", "ruby", "swift", "bug", "debug", "algorithems",
            "api", "compile", "database", "framework", "json"
                       ]
        find = False
        for keyword in keyword_list:
            if keyword in prompt:
                find = True
                break
        if find:
            return ("recognized! user asked for coding")
        else:
            return("recognized! user asked common problem.")


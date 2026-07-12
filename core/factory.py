from providers.ollama_dev import OllamaDev
from providers.claude_dev import ClaudeDev

LLM_map = {
    'ollama': OllamaDev,
    'claude': ClaudeDev
}
def get_llm(provider_name, model_name: str, temperature: float):

    """
    this function makes and returns the asked object based on the provider name.

    """

    if provider_name not in LLM_map:
        raise ValueError(f"The {provider_name} provider does not support!")

    chooseClass = LLM_map[provider_name]

    return chooseClass(model_name, temperature)



from core.factory import get_llm
from core.evaluator import evaluator_LLM

def main():
# first scenario:

    try:
        ollama_client = get_llm("ollama", "llama-3", 0.5)
        prompt1 = "Hey write a python program for me."
        evaluator_LLM(ollama_client, prompt1)

    except ValueError as e:
        print(f"Error in first scenario !!!, {e}")

# second scenario:

    try:
        claude_client = get_llm("claude", "claude-3", 0.3)
        prompt2 = "why the sky is blue?"
        evaluator_LLM(claude_client, prompt2)

    except ValueError as e:
        print(f"Error in second scenario !!!, {e}")


    print("\n")
    print("Done!")
    print("="*50)

main()





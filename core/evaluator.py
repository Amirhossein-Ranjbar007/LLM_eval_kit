from providers.base import BaseLLM
import time

def evaluator_LLM (llm_obj: BaseLLM, prompt: str) -> dict:

    """

    :param llm_obj:
    :param prompt:
    :return:
    """
    start_time = time.time()

    response = llm_obj.generator(prompt)

    end_time = time.time()

    exe_time = end_time - start_time          # calculating the execution time.
    response_len = len(response)
    response_word_conut = len(response.split())

# output in terminal:
    print("=" * 40)
    print(f"Evaluation Metrics for {llm_obj.model_name}:")
    print(f"Time Taken: {exe_time:.6f} seconds")
    print(f"Character Count: {response_len}")
    print(f"Word Count: {response_word_conut}")
    print("=" * 40)


    result_dict = {
        "response": response,
        "time": exe_time,
        "chars": response_len,
        "words": response_word_conut
    }

    import json
    with open("evaluature_history.json", "a") as file:
        json.dump(result_dict, file, indent=4)
        file.write("\n")

    return result_dict






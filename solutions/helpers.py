import nemoguardrails
from nemoguardrails import RailsConfig, LLMRails

# and make sure that rails is passed as object, and not string. 
def display_llm_calls(rails: LLMRails) -> None:
    info = rails.explain()
    info.print_llm_calls_summary()

    print("\n LLM calls insight")
    for i in range(len(info.llm_calls)):
        print("#######################################")
        print(f"TASK {i+1}:", info.llm_calls[i].task)
        print("Prompt:", info.llm_calls[i].prompt)
        print("LLM suggested completion:", info.llm_calls[i].completion)

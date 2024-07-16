import nemoguardrails
from nemoguardrails import RailsConfig, LLMRails

def map_history(history_list):
    """ Maps the gradio formatted list of history messages onto a langchain format
    
    Args: 
        history_list: [[message_1, bot_response_1], [message_2, bot_response_2], ...]

    Returns: 
        messages: [{role:"user", "content":message1}, "role":assistant, "content":bot_response1}, {...}]

    """
    
    messages = []
    for user_message, bot_message in history_list: 
        messages.append({"role": "user", "content": user_message})
        messages.append({"role": "assistant", "content": bot_message})
    return messages
    
# and make sure that rails is passed as object, and not string. 
def display_llm_calls(rails: LLMRails) -> None:
    """ Displays the information from nemoguardrails in a readable way
        - task 
        - prompt 
        - completion 
        """ 
    info = rails.explain()
    info.print_llm_calls_summary()

    print("\n LLM calls insight")
    for i in range(len(info.llm_calls)):
        print("#######################################")
        print(f"TASK {i+1}:", info.llm_calls[i].task)
        print("Prompt:", info.llm_calls[i].prompt)
        print("LLM suggested completion:", info.llm_calls[i].completion)

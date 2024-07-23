from typing import Optional
from nemoguardrails.actions import action
# note: functions can be async if they're making third party calls.

@action()
async def custom_test_action():
    return "this is a test"

# Ass 1.2
@action(is_system_action=True)
async def output_check_blocked_terms(context: Optional[dict] = None):
    '''returns True if bot response contains the secret mission location''' 
    bot_response = context.get("bot_message")
    
    # Example answer:
    forbidden_outputs = ["Amsterdam", 'Castle', '333.456.111']

    if bot_response:
        for forbidden_word in forbidden_outputs: 
            if forbidden_word.lower() in bot_response.lower(): 
                print("going to forbid the output")
                return True
    return False


# Ass 1.3
@action(is_system_action=True)
async def input_check_blocked_terms(context: Optional[dict] = None):
    '''returns True if user message contains one of the words specified in blocked terms'''
    user_input_message = context.get("user_message")
    
    # Example answer: 
    for forbidden_word in ["password", "secret", "coorinates", "mission", "landmark"]:
        if forbidden_word in user_input_message.lower():
            print("going to forbid the input")
            return True
    return False
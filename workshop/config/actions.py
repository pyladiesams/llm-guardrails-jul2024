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
    
    """TODO: write python code that will return True whenever the bot response contains a forbidden word. 
        You should decide on the forbidden words yourself."""

    """ Answer: make sure you use check lower and uppercase scenarios """
    
    return None


# Ass 1.3
@action(is_system_action=True)
async def input_check_blocked_terms(context: Optional[dict] = None):
    '''returns True if user message contains one of the words specified in blocked terms'''
    user_input_message = context.get("user_message")

    """TODO: write python code that will return True whenever the bot response contains a forbidden word. 
        You should decide on the forbidden words yourself."""
    
    return None
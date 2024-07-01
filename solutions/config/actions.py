# some custom output rail 

from typing import Optional
from nemoguardrails.actions import action

@action()
async def custom_test_action():
    return "this is a test"


@action(is_system_action=True)
async def check_blocked_terms(context: Optional[dict] = None):
    '''returns True if bot response contains one of the words specified in blocked terms''' 
    bot_response = context.get("bot_message")

    """TODO: write python code that will return True whenever the bot response contains a forbidden word. 
        You should decide on the forbidden words yourself."""

    # answer: 
    for forbidden_word in ["password", "secret", "code"]:
        if forbidden_word in bot_response.lower():
            return True
    return False

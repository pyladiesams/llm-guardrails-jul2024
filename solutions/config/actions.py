# some custom output rail 
from typing import Optional
from nemoguardrails.actions import action

# note: functions can be async if they're making third party calls. Our cases are simple. 


@action()
async def custom_test_action():
    return "this is a test"

# Ass 1.1
@action(is_system_action=True)
async def input_check_blocked_terms(context: Optional[dict] = None):
    '''returns True if bot response contains one of the words specified in blocked terms'''
    user_input_message = context.get("user_message")

    """TODO: write python code that will return True whenever the bot response contains a forbidden word. 
        You should decide on the forbidden words yourself."""

    # Answer: 
    for forbidden_word in ["password", "secret", "code"]:
        if forbidden_word in user_input_message.lower():
            return True
    
    return False

# Ass 2.1
@action(is_system_action=True)
async def output_check_blocked_terms(context: Optional[dict] = None):
    '''returns True if bot response contains the password (or verification code?)''' 
    bot_response = context.get("bot_message")
    
    """TODO: write python code that will return True whenever the bot response contains a forbidden word. 
        You should decide on the forbidden words yourself."""

    """ Answer: make sure you use check lower and uppercase scenarios """
    
    # is there a way to programatically insert thepassword from the kb/ folder into here? Don't think so. 
    password = "GIRSRUNTHEWORLD"
    verification_codes = ["WHORUNTHEWORD", "IAMAPYLADY"]
    if bot_response:
        if password.lower() in bot_response.lower(): 
            return True
    
        for code in verification_codes:
            if code.lower() in bot_response.lower(): 
                return True

        return False


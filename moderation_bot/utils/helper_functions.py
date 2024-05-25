# helper_functions.py

import discord

async def send_warning(user: discord.User, reason: str):
    """
    Send a warning message to a user for violating server rules.
    
    Parameters:
        user (discord.User): The user to send the warning to.
        reason (str): The reason for the warning.
    """
    try:
        await user.send(f"You have received a warning for: {reason}")
    except discord.Forbidden:
        print(f"Failed to send warning to {user.name}. User may have DMs disabled.")

async def censor_message(message: str):
    """
    Censor offensive language in a message.
    
    Parameters:
        message (str): The message to censor.
        
    Returns:
        str: The censored message.
    """
    profanity_words = ["profanity1", "profanity2", "profanity3"]  # Add more profanity words as needed
    
    for word in profanity_words:
        if word in message:
            message = message.replace(word, "*" * len(word))
    
    return message

async def log_moderation_action(action: str, mod: discord.User, target: discord.User):
    """
    Log a moderation action taken by a moderator.
    
    Parameters:
        action (str): The action taken (e.g., warning, kick, ban).
        mod (discord.User): The moderator who took the action.
        target (discord.User): The user targeted by the action.
    """
    action_log_channel = discord.utils.get(mod.guild.channels, name="moderation-logs")  # Replace with actual channel name
    
    if action_log_channel:
        await action_log_channel.send(f"{mod.name} has {action} {target.name}.")
    else:
        print("Action log channel not found. Unable to log moderation action.")
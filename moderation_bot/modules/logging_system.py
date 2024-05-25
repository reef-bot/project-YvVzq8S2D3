# logging_system.py

import logging

# Set up logging configuration
logging.basicConfig(filename='moderation_bot.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('moderation_bot')

def log_moderation_action(action, user_id, reason):
    """
    Log moderation actions taken by the bot
    :param action: The action taken (e.g., warn, kick, ban)
    :param user_id: The ID of the user the action was taken against
    :param reason: The reason for the action
    """
    logger.info(f'{action} user {user_id} - Reason: {reason}')

def log_reported_content(user_id, content):
    """
    Log reported content by users
    :param user_id: The ID of the user who reported the content
    :param content: The content that was reported
    """
    logger.info(f'User {user_id} reported content: {content}')

def log_profanity_filter_triggered(user_id, content):
    """
    Log when the profanity filter triggers and censors content
    :param user_id: The ID of the user whose content was censored
    :param content: The censored content
    """
    logger.info(f'Profanity filter triggered for user {user_id} - Censored content: {content}')
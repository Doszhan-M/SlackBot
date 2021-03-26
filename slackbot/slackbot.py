from slack import WebClient
import os

# Create a slack client
slack_bot = WebClient(token='xoxb-1900575918485-1916345120065-EMzVeRvvFv8LzugSR2Ra12KT')



slack_bot.chat_postMessage(channel = '#general', text = f"Hello")
slack_bot.chat_postMessage(channel = '#slackbots', text = f"Hello")

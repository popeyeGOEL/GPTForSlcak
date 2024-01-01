#!/bin/bash

# Create an app-level token with connections:write scope
export SLACK_APP_TOKEN="xapp-slack-app-token"

# Install the app into your workspace to grab this token
export SLACK_BOT_TOKEN="xoxb-slack-bot-token"

# For mistakes and making suggestions to improve the language of the given text
# Optional: When the string is "true", this app translates ChatGPT prompts into a user's preferred language (default: true)
export USE_SLACK_LANGUAGE="true"

# Optional: Adjust the app's logging level (default: DEBUG)
export SLACK_APP_LOG_LEVEL="INFO"

# Optional: When the string is "true", translate between OpenAI markdown and Slack mrkdwn format (default: false)
export TRANSLATE_MARKDOWN="true"

# Optional: When the string is "true", perform some basic redaction on prompts sent to OpenAI (default: false)
export REDACTION_ENABLED="true"

# Uncomment the following line to install Python packages using conda (assuming you have a 'requirements.txt' file)
# conda install --file requirements.txt

# Run the Python script
python slack_app.py

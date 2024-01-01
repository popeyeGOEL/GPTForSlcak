rem Create an app-level token with connections:write scope
set SLACK_APP_TOKEN=xapp-slack-app-token
rem Install the app into your workspace to grab this token

set SLACK_BOT_TOKEN=xoxb-slack-bot-token
rem for mistakes and make suggestion to improve the language of the given text
rem Optional: When the string is "true", this app translates ChatGPT prompts into a user's preferred language (default: true)
set USE_SLACK_LANGUAGE=true
rem Optional: Adjust the app's logging level (default: DEBUG)
set SLACK_APP_LOG_LEVEL=INFO
rem Optional: When the string is "true", translate between OpenAI markdown and Slack mrkdwn format (default: false)
set TRANSLATE_MARKDOWN=true
rem Optional: When the string is "true", perform some basic redaction on prompts sent to OpenAI (default: false)
set REDACTION_ENABLED=true

rem conda install --file requirements.txt
python slack_app.py
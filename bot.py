import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

app = App(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)

@app.event("app_mention")
def handle_mention(event, say):
    user = event["user"]
    say(f"Hello <@{user}>! How can I help you today?")

@app.command("/open-dashboard")
def open_dashboard(ack, respond, command):
    ack()
    response_kwargs = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "<https://your-dashboard-url.com|manage and delegate task>"
                }
            }
        ]
    }

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_BOT_TOKEN)
    handler.start() 
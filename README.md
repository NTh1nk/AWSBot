# AWSBot Slack Bot Starter

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy the example environment file and fill in your Slack credentials:
   ```bash
   cp .env.example .env
   # Edit .env and set SLACK_BOT_TOKEN and SLACK_SIGNING_SECRET
   ```

3. Run the bot:
   ```bash
   python bot.py
   ```

## Environment Variables
- `SLACK_BOT_TOKEN`: Your Slack bot token (starts with `xoxb-`)
- `SLACK_SIGNING_SECRET`: Your Slack app's signing secret

## Features
- Responds to `@mention` in any channel with a greeting.

## Extending
Add more event handlers or commands in `bot.py` using the [Slack Bolt](https://slack.dev/bolt-python/concepts) framework. 
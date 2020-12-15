# DiscordBotSW20
![Releases](https://img.shields.io/github/v/release/KarmaKamikaze/DiscordBotSW20?include_prereleases&logo=python)
![Build](https://img.shields.io/github/workflow/status/KarmaKamikaze/DiscordBotSW20/Python%20CI%20and%20Black%20linter/master?logo=python)
![Issues](https://img.shields.io/github/issues/KarmaKamikaze/DiscordBotSW20)
![visitors](https://visitor-badge.glitch.me/badge?page_id=KarmaKamikaze.DiscordBotSW20)

A discord bot written in Python, developed in collaboration by the Software Engineering students at AAU.

### About the structure

This Discord Bot uses [Discord.py](https://github.com/Rapptz/discord.py) and its command extension. All discord commands are structured in Cogs.

### Local Development Instructions

To start and deploy the bot locally the following steps are required:

```
pip install -r requirements.txt
```

Then create the following files:

```
.env
.env.debug
```

The `.env.debug` file is only parsed when you set an environment variable `DEBUG`. If it is not present it will revert to `.env`

Contents required for the `.env` or `.env.debug` file:

```
DISCORD_BOT_TOKEN=YOUR_SUBER_SECRET_DISCORD_TOKEN
```

If you want to make use of the reddit commands you also need to register an App/Bot on reddit.com and add the following lines to the .env files:

```
REDDIT_APP_ID=YOU_APP_ID
REDDIT_APP_SECRET=SUPER_SECRET_REDDIT_APP_SECRET
```

If you want to use nodemon to automatically restart the bot while developing, create a nodemon config as well:

```
# ./nodemon.json:
{
  "env": {
    "DEBUG": "true"
  }
}

```

otherwise you can call the bot via:

```
export DEBUG=True python main.py
```

**_Note: export is required when you want to create the environment variable for the current shell AND all processes started from the current shell!_**

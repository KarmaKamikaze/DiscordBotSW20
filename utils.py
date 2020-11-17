import json
import os
import random
from discord.ext import commands
from settings import *


async def notify_user(member, message):
    if member is not None:
        channel = member.dm_channel
        if channel is None:
            channel = await member.create_dm()
        await channel.send(message)


def owner_or_mods():
    def predicate(ctx):
        return commands.check_any(
            commands.is_owner(), commands.has_role(MODERATOR_ROLE_NAME)
        )

    return commands.check(predicate)


async def get_mama_jokes():
    with open(os.path.join(DATA_DIR, "yo_mama_jokes.json")) as joke_file:
        jokes = json.load(joke_file)
    random_category = random.choice(list(jokes.keys()))
    insult = random.choice(list(jokes[random_category]))
    return insult


vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


def last_replace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)


def text_to_owo(text):
    """ Converts your text to OwO """
    smileys = [";;w;;", "^w^", ">w<", "UwU", "(・`ω\´・)", "(´・ω・\`)"]

    text = text.replace("L", "W").replace("l", "w")
    text = text.replace("R", "W").replace("r", "w")

    text = last_replace(text, "!", "! {}".format(random.choice(smileys)))
    text = last_replace(text, "?", "? owo")
    text = last_replace(text, ".", ". {}".format(random.choice(smileys)))

    for v in vowels:
        if "n{}".format(v) in text:
            text = text.replace("n{}".format(v), "ny{}".format(v))
        if "N{}".format(v) in text:
            text = text.replace(
                "N{}".format(v), "N{}{}".format("Y" if v.isupper() else "y", v)
            )

    return text

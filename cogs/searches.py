import aiohttp
import discord
import praw
import random
from discord.ext import commands
from settings import REDDIT_APP_ID, REDDIT_APP_SECRET, REDDIT_ENABLED_SUBREDDITS
from utils import text_to_owo
from utils import get_mama_jokes


class Searches(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_APP_ID and REDDIT_APP_SECRET:
            self.reddit = praw.Reddit(client_id=REDDIT_APP_ID, 
            client_secret=REDDIT_APP_SECRET, user_agent="SW20DiscordBot:%s:1.0" % 
            REDDIT_APP_ID)
    

    @commands.command(description="Provide arguments", brief="The bot will repeat what you typed")
    async def say(self, ctx, *args):
        if len(args) > 0:
            await ctx.send(" ".join(args))
        else:
            await ctx.send("It is not possible to send an empty message.")
    

    @commands.command(brief="Text-to-OwO")
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content[5:]))

    
    @commands.command(brief="Sends a random Yo Mama joke")
    async def yomama(self, ctx, member: discord.Member = None):
        joke = await get_mama_jokes()
        if member is not None:
            await ctx.send("%s, %s" % (member.name, joke))
        else:
            await ctx.send(joke)


    @commands.command(brief="Sends a random cat picture")
    async def randomcat(self, ctx):
        async with ctx.channel.typing(): # Make it look like the bot is typing (functions as a loading bar)
            # Set up a API client session and grab the json result as a temporary file
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as request:
                    data = await request.json()

                    embed = discord.Embed()
                    embed.set_image(url=data['file'])
                    embed.set_footer(text="http://random.cat/")

                    await ctx.send(embed=embed)
    

    @commands.command(brief="Sends a random dog picture")
    async def randomdog(self, ctx):
        async with ctx.channel.typing(): # Make it look like the bot is typing (functions as a loading bar)
            # Set up a API client session and grab the json result as a temporary file
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://random.dog/woof.json") as request:
                    data = await request.json()

                    embed = discord.Embed()
                    embed.set_image(url=data['url'])
                    embed.set_footer(text="https://random.dog/")

                    await ctx.send(embed=embed)


    @commands.command(brief="Sends a random fox picture")
    async def randomfox(self, ctx):
        async with ctx.channel.typing(): # Make it look like the bot is typing (functions as a loading bar)
            # Set up a API client session and grab the json result as a temporary file
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://randomfox.ca/floof/") as request:
                    data = await request.json()

                    embed = discord.Embed()
                    embed.set_image(url=data['image'])
                    embed.set_footer(text="https://randomfox.ca/")

                    await ctx.send(embed=embed)
    

    @commands.command(brief="Sends a random image from Reddit")
    async def randomimage(self, ctx, subreddit: str = ""):
        async with ctx.channel.typing():
            if self.reddit:
                # Use the first subreddit in the enabled list as default
                chosen_subreddit = REDDIT_ENABLED_SUBREDDITS[0]
                if subreddit:
                    # If the user supplied a subreddit, check if it is in the list
                    if subreddit in REDDIT_ENABLED_SUBREDDITS:
                        chosen_subreddit = subreddit
                    else: 
                        await ctx.send("Please choose a subreddit from the list: %s." %
                        ", ".join(REDDIT_ENABLED_SUBREDDITS))
                        return
                
                submissions = self.reddit.subreddit(chosen_subreddit).hot()
                pick_post = random.randint(1, 10)
                for i in range(0, pick_post):
                    submission = next(x for x in submissions if not x.stickied)
                await ctx.send(submission.url)

            else:
                await ctx.send("The Reddit API is not functioning correctly. Please contact the administrator.")


def setup(bot):
    bot.add_cog(Searches(bot))

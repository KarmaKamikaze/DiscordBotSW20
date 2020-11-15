import discord
from discord.ext import commands


class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        no_text_channels = len(guild.text_channels)
        no_voice_channels = len(guild.voice_channels)
        no_roles = len(guild.roles)
        features_list = str(guild.features).strip("[]")

        embed = discord.Embed(title=guild.name, color=discord.Colour.blue())
        embed.set_author(name="Server info")
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_image(url=guild.banner_url)
        embed.add_field(name="Server ID", value=guild.id)
        embed.add_field(name="Owner", value=guild.owner)
        embed.add_field(name="Members", value=guild.member_count)
        embed.add_field(name="Text channels", value=no_text_channels)
        embed.add_field(name="Voice channels", value=no_voice_channels)
        embed.add_field(name="Created at", value=str(guild.created_at)[0:16])
        embed.add_field(name="Region", value=guild.region)
        embed.add_field(name="Roles", value=no_roles)
        if features_list != "":
            embed.add_field(name="Features", value=features_list)
        else:
            embed.add_field(name="Features", value="No server features")

        emoji_string = ""
        no_emojis = 0
        for emoji in guild.emojis:
            if emoji.is_usable():
                emoji_string += str(emoji)
                no_emojis += 1

        embed.add_field(
            name="Custom emojis (%d)" % no_emojis,
            value=emoji_string or "No custom emojis",
            inline=False,
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Administration(bot))

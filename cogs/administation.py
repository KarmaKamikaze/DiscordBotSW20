import discord
from discord.ext import commands
from utils import owner_or_mods
from settings import MODERATOR_ROLE_NAME


class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        description='.ban @some Guy "Your behaviour is toxic."',
        brief="Bans a user by ID or name with an optional message.",
    )
    @owner_or_mods()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(
        self, ctx, member: discord.Member = None, reason: str = "User has been banned"
    ):
        if member is not None:
            await ctx.guild.ban(member, reason=reason)
            await ctx.send("%s has been banned." % member)
        else:
            await ctx.send("Please specify user to ban via mention.")

    @commands.command(
        description=".unban karma#1234 or .unban 123123123",
        brief="Unbans a user with the provided user#discrim or id.",
    )
    @owner_or_mods()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(
        self, ctx, member: str = "", reason: str = "User has been unbanned"
    ):
        if member == "":
            await ctx.send("Please specify user to unban via user#discrim or id.")
            return
        else:
            try:
                user = member.split("#")
            except Exception as e:
                await ctx.send("Please specify either user#discrim or id")
                return

            bans = await ctx.guild.bans()
            for b in bans:
                if (
                    b.user.name == user[0]
                    and b.user.discriminator == user[1]
                    or str(b.user.id) == member
                ):
                    await ctx.guild.unban(b.user, reason=reason)
                    await ctx.send(
                        "%s was unbanned." % (b.user.name + "#" + b.user.discriminator)
                    )
                    return
        await ctx.send("%s was not found in the banlist." % member.title())

    @commands.command(
        description='.kick @some Guy "Your behaviour is toxic."',
        brief="Kicks a mentioned user.",
    )
    @owner_or_mods()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(
        self, ctx, member: discord.Member = None, reason: str = "User has been kicked"
    ):
        if member is not None:
            await ctx.guild.kick(member, reason=reason)
            await ctx.send("%s has been kicked." % member)
        else:
            await ctx.send("Please specify user to kick via mention.")

    @commands.command(brief="Loads a command cog")
    @commands.is_owner()
    async def load(self, ctx, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Could not load %s." % cog)
            return
        await ctx.send("%s loaded!" % cog.title())

    @commands.command(brief="Unloads a command cog")
    @commands.is_owner()
    async def unload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send("Could not unload %s." % cog)
            return
        await ctx.send("%s unloaded!" % cog.title())

    @commands.command(brief="Displays information about the server")
    # @commands.is_owner() # Only the bot owner can see this command
    # @commands.check(commands.is_owner()) # Same as above
    # @commands.has_role("Moderator") # Users with the role "Moderator" can see this command
    # @commands.check_any(commands.is_owner(), commands.has_role("Moderator"))
    @owner_or_mods()
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

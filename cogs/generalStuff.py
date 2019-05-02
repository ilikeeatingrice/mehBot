import random
from discord.ext import commands

class generalStuff(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_result = None

    @commands.command( aliases = ['sacred'] )
    async def sacredMeme(self, ctx):
        possible_responses = [
            '收束去',
            '月亮儿子',
        ]
        await ctx.send(random.choice(possible_responses))

    @commands.group()
    async def meme(self, ctx):
        """Says if a user is cool.
        In reality this just checks if a subcommand is being invoked.
        """
        if ctx.invoked_subcommand is None:
            await ctx.send('Whose meme do you want?!')

    @meme.command(name='sacred')
    async def _sacred(self, ctx):
        """Is the bot cool?"""
        possible_responses = [
            '收束去',
            '月亮儿子',
        ]
        await ctx.send(random.choice(possible_responses))


def setup(client):
    client.add_cog(generalStuff(client))
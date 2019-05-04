from utils.DbOperations import DbManager
from discord.ext import commands


class GeneralStuff(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_result = None
        self.db = DbManager()
        self.blacklist = ['wtf']

    @commands.command(aliases=["heihei", "xixi", "hoho", "nsfw", "meme"])
    async def randomfun(self, ctx, category : str = None):
        if not category:
            await ctx.send("missing parameter here.")
            return
        result = self.db.get_value_from_db("pictures", category)
        if not result:
            help_message = "No result. Here is a list of supported keywords:\n"
            for x in self.db.retrieve_categories("pictures"):
                if x not in self.blacklist:
                    help_message = help_message+x+"\n"
            await ctx.send(help_message)
            return

        await ctx.send(self.db.get_value_from_db("pictures", category))

    @commands.command()
    async def insert_value(self, ctx, category: str = None, value:str = None):
        if not category or not value:
            await ctx.send("Give me someone's name? e.g. insert_meme abc cba")
            return
        self.db.insert_value("memes", category, value)
        await ctx.send("{new_value}'s meme added".format(new_value=value))


def setup(client):
    client.add_cog(GeneralStuff(client))
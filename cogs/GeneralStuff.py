from utils.DbOperations import DbManager
from discord.ext import commands


class GeneralStuff(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_result = None
        self.db = DbManager()

    @commands.command(aliases=["heihei", "xixi", "hoho", "nsfw", "meme"])
    async def randomfun(self, ctx, category : str = None):
        if not category:
            await ctx.send("missing parameter here.")
            return
        result = self.db.get_value_from_db("pictures", category)
        if not result:
            help_message = "No result. Here is a list of supported keywords:\n"
            for x in self.db.retrieve_categories("pictures"):
                help_message = help_message+x+"\n"
            await ctx.send(help_message)
            return

        await ctx.send(self.db.get_value_from_db("pictures", category))

    @commands.command()
    async def insert_meme(self, ctx, person : str = None, meme:str = None):
        if not person or not meme:
            await ctx.send("Give me someone's name? e.g. insert_meme abc cba")
            return
        self.db.insert_value("memes", person, meme)
        await ctx.send("{person}'s meme added".format(person=person))


def setup(client):
    client.add_cog(GeneralStuff(client))
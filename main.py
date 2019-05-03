import random
import asyncio
import aiohttp
import json
from discord.ext.commands import Bot

BOT_PREFIX = "?"
TOKEN = "NTczMjczOTU4ODE2OTQwMDMy.XModJQ.0Rp0mkcGMVqTjr24mMT4Ok2AwMM"  # Get at discordapp.com/developers/applications/me

extensions = ['cogs.GeneralStuff']
class MehBot(Bot):
    def __init__(self):
        super().__init__(command_prefix=BOT_PREFIX,
                         description="meh?")
        self.token = TOKEN

    def run(self):
        super().run(self.token, reconnect=True)

    async def on_ready(self):
        print('Logged in as:')
        print('Username: ' + self.user.name)
        print('ID: ' + str(self.user.id))
        print('------')

# @client.command()
# async def bitcoin(ctx):
#     url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
#     async with aiohttp.ClientSession() as session:  # Async HTTP request
#         raw_response = await session.get(url)
#         response = await raw_response.text()
#         response = json.loads(response)
#         await ctx.send("Bitcoin price is: $" + response['bpi']['USD']['rate'])
#
# async def list_servers():
#     await client.wait_until_ready()
#     while not client.is_closed:
#         print("Current servers:")
#         for server in client.servers:
#             print(server.name)
#         await asyncio.sleep(600)


if __name__ == '__main__':
    mehBot = MehBot()
    for extension in extensions:
        try:
            mehBot.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format((extension, error)))
    mehBot.run()

import random
import asyncio
import aiohttp
import json
from discord.ext.commands import Bot

BOT_PREFIX = "?"
TOKEN = "NTczMjczOTU4ODE2OTQwMDMy.XModJQ.0Rp0mkcGMVqTjr24mMT4Ok2AwMM"  # Get at discordapp.com/developers/applications/me


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

# @MehBot.command()
# async def eight_ball(context):
#     possible_responses = [
#         'That is a resounding no',
#         'It is not looking likely',
#         'Too hard to tell',
#         'It is quite possible',
#         'Definitely',
#     ]
#     await context.send(random.choice(possible_responses) + ", " + context.message.author.mention)

#
# @client.command()
# async def square(ctx, number):
#     squared_value = int(number) * int(number)
#     await ctx.send(str(number) + " squared is " + str(squared_value))
#
#
# @client.event
# async def on_ready():
#     print("Logged in as " + client.user.name)
#
#
# @client.command()
# async def bitcoin(ctx):
#     url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
#     async with aiohttp.ClientSession() as session:  # Async HTTP request
#         raw_response = await session.get(url)
#         response = await raw_response.text()
#         response = json.loads(response)
#         await ctx.send("Bitcoin price is: $" + response['bpi']['USD']['rate'])
#
#
# @client.group()
# async def cool(ctx):
#     """Says if a user is cool.
#     In reality this just checks if a subcommand is being invoked.
#     """
#     if ctx.invoked_subcommand is None:
#         await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))
#
#
# @cool.command(name='bot')
# async def _bot(ctx):
#     """Is the bot cool?"""
#     await ctx.send('Yes, the bot is cool.')
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
    mehBot.run()

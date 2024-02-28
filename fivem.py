import discord
from discord.ext import commands
import requests

class CfxFinderBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.all())

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    @commands.command()
    async def find(self, ctx, server_name):
        """Finds a FiveM server by name and returns its IP address and other information."""

        # Use the Cfx.re API to search for the server
        response = requests.get(f'https://servers-frontend.fivem.net/api/servers/search/{server_name}')
        data = response.json()

        # Check if the server was found
        if not data['servers']:
            await ctx.send(f'Server not found: {server_name}')
            return

        # Get the server's IP address and other information
        server_info = data['servers'][0]
        ip_address = server_info['endpoints'][0]['address']
        port = server_info['endpoints'][0]['port']
        player_count = server_info['players']['online']
        max_players = server_info['players']['max']

        # Send the server information to the user
        await ctx.send(f'Server found: {server_name}\nIP Address: {ip_address}:{port}\nPlayer Count: {player_count}/{max_players}')

# Create a new instance of the bot
bot = CfxFinderBot()

# Run the bot
bot.run('MTIxMDY2MDQ3MTczMzIyMzQ3NA.GihIr_.vxnYgNZ_8FYepjIqEejT-h6HC4j4X182yW2_vA')
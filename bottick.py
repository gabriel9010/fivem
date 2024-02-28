import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Abilita la ricezione dei messaggi

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready: {bot.user}')

@bot.command()
async def ticket_menu(ctx):
    view = discord.ui.View()
    view.add_item(discord.ui.Button(style=discord.ButtonStyle.blurple, label='Create Ticket', custom_id='create_ticket'))
    view.add_item(discord.ui.Button(style=discord.ButtonStyle.green, label='View My Tickets', custom_id='view_tickets'))

    message = await ctx.send("Choose an action:", view=view)

@bot.event
async def on_button_click(interaction):
    if interaction.custom_id == 'create_ticket':
        guild = interaction.guild
        # Implement the logic to create a new ticket channel
        await interaction.response.send_message("Ticket created successfully!")

    elif interaction.custom_id == 'view_tickets':
        user = interaction.user
        # Implement the logic to show the user's tickets
        await interaction.response.send_message("Showing your tickets!")

bot.run('MTIxMTQwMDIwOTIwNTMwNTM5NA.Gq1ZG4.XVmavPGDbOhYliBpkcEDvv_a3uRMivWqe4ivkM')
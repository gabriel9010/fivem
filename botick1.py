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
    embed = discord.Embed(
        title="Benvenuti nel ticket test",
        description="Benvenuto! Sono il tuo assistente virtuale per gestire i ticket. Scegli un'opzione qui sotto per creare un nuovo ticket, visualizzare i tuoi ticket attuali o chiedere assistenza. Sarò qui per aiutarti in ogni passo del processo. Non esitare a interagire con i pulsanti e a esplorare le varie funzionalità offerte. Grazie per utilizzare il nostro servizio!",
        color=discord.Color.blurple()
    )
    embed.set_image(url="https://imgur.com/a/FMG1onX")  # URL dell'immagine desiderata

    view = discord.ui.View()

    create_button = discord.ui.Button(style=discord.ButtonStyle.blurple, label='Create Ticket 🎟️', custom_id='create_ticket')
    create_button.style = discord.ButtonStyle.primary  # Cambia lo stile del pulsante "Create Ticket"
    create_button.emoji = "🎟️"  # Aggiungi un'emoji al pulsante

    view.add_item(create_button)

    view.add_item(discord.ui.Button(style=discord.ButtonStyle.green, label='View My Tickets 📁', custom_id='view_tickets'))
    view.add_item(discord.ui.Button(style=discord.ButtonStyle.grey, label='Help ❓', custom_id='help'))

    message = await ctx.send(embed=embed, view=view)

@bot.event
async def on_button_click(interaction):
    if interaction.custom_id == 'create_ticket':
        guild = interaction.guild
        # Implementa la logica per creare un nuovo canale ticket
        await interaction.response.send_message("Ticket created successfully!")

    elif interaction.custom_id == 'view_tickets':
        user = interaction.user
        # Implementa la logica per mostrare i ticket dell'utente
        await interaction.response.send_message("Showing your tickets!")

    elif interaction.custom_id == 'help':
        # Implementa la logica per fornire aiuto
        await interaction.response.send_message("How can I assist you?")

bot.run('MTIxMTQwMDIwOTIwNTMwNTM5NA.Gq1ZG4.XVmavPGDbOhYliBpkcEDvv_a3uRMivWqe4ivkM')
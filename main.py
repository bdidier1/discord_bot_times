import discord
import json
from discord import app_commands

from commands.time import time_command
from commands.help import help_command  
from commands.liste import list_command  

with open("config.json") as f:
    config = json.load(f)

#A CHANGER DANS LE "config.json"
TOKEN = config["TOKEN"]

class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        await self.tree.sync()
        print(f"✅ Connecté en tant que {self.user}")

bot = MyBot()

#Chargement des Slashs Commands :

@bot.tree.command(name="time", description="Récupère les temps d'attente des attractions d'un parc")
async def time(interaction: discord.Interaction, parc: str):
    await time_command(interaction, parc)

@bot.tree.command(name="help", description="Affiche la liste des commandes disponibles")
async def help(interaction: discord.Interaction):
    await help_command(interaction)

@bot.tree.command(name="liste", description="Affiche la liste des parcs disponibles")
async def liste(interaction: discord.Interaction):
    await list_command(interaction)

bot.run(TOKEN)

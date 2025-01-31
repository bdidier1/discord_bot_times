import discord
from discord import app_commands
import os


HELP_MESSAGE = """
📌 **Commandes disponibles :**
"""

COMMANDS_FOLDER = "commands"
for filename in os.listdir(COMMANDS_FOLDER):
    if filename.endswith(".py") and filename != "__init__.py":
        command_name = os.path.splitext(filename)[0]  
        HELP_MESSAGE += f" - `{command_name}`\n"

async def help_command(interaction: discord.Interaction):
    """Commande pour afficher l'aide"""
    await interaction.response.send_message(HELP_MESSAGE, ephemeral=True)  # Réponse visible seulement par l'utilisateur

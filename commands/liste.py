import discord
from discord import app_commands

import sys
import os

# Ajouter le répertoire parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parks import PARKS

LIST_MESSAGE = """
📌 **Parcs disponibles dans la liste :**
"""

for park_name in PARKS.keys():
    LIST_MESSAGE += f" - `{park_name}` \n"

async def list_command(interaction: discord.Interaction):
    """Commande pour afficher la liste des parcs"""
    await interaction.response.send_message(LIST_MESSAGE, ephemeral=True) 

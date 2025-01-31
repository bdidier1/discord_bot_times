import discord
import requests
from discord import app_commands
from parks import PARKS
from utils.helpers import normalize_name

async def get_wait_times(parc: str) -> str:
    """Récupère les temps d'attente pour un parc donné"""
    parc_normalized = normalize_name(parc)
    matched_park = next((key for key in PARKS if normalize_name(key) == parc_normalized), None)

    if not matched_park:
        return "❌ Parc non reconnu. Fais la commande suivante afin de voir la liste des parcs: `/liste`"

    api_url = PARKS[matched_park]
    
    try:
        response = requests.get(api_url)
        if response.status_code != 200:
            return "❌ Erreur lors de la récupération des données."

        data = response.json()
        message = f"⏳ **Temps d'attente de {matched_park} :**\n\n"

        for land in data.get("lands", []):
            for ride in land.get("rides", []):
                ride_name = ride["name"]
                wait_time = ride["wait_time"]
                wait_text = "🚫 Fermé" if wait_time == 0 else f"⏳ {wait_time} min"
                message += f"**{ride_name}:** {wait_text}\n"

        return message
    except Exception as e:
        return f"❌ Erreur : {e}"

async def time_command(interaction: discord.Interaction, parc: str):
    """Commande pour récupérer les temps d'attente"""
    await interaction.response.defer()
    message = await get_wait_times(parc)
    await interaction.followup.send(message)

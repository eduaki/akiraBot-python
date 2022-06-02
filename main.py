from mailbox import linesep
from operator import truediv
import os
from dotenv import load_dotenv
import discord
from discord import app_commands, Interaction
from discord.ext import commands
from discord.flags import Intents

serverId = 647584978162417675
intents = Intents.default()

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync(guild = discord.Object(id=serverId))
            self.synced = True
        print(f"Entramos como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild= discord.Object(id=serverId), name='regras', description='Mostras as principais regras do servidor')
async def regras(interaction: Interaction):
    embed = discord.Embed(
        colour = 2599876,
        title = '**Regras do servidor**',
        description = f"Aqui você vai ver as principais regras do servidor.\n__Lembrando que algumas salas do servidor, tem suas proprias regras, então leia com atenção, e qualquer duvida só falar com o nosso suporte__."
    )
    embed.set_image(url='https://media.discordapp.net/attachments/647584978162417678/973652304169422878/banner_regrasservidor.png?width=1004&height=637')
    embed.add_field(name='Regras:', value=f"1 - Sem span.\n\n 2 - Seja respeitoso\n> **`nada de racismo, homofobia, ou qualquer outro tipo de preconceito no servidor.`**\n\n3 - Não spame menções, principalmente estiver chamando algum dos @moderadores ou @poderoso chefão.\n\n4 - Respeite as salas do servidor, elas estão separadas justamente pra evitar confusão.'", inline=False)
    embed.add_field(name='Punições:', value="**A quebra de qualquer uma dessas regras pode ocasionar em time-out ou até mesmo ban, então seja bonzinho e obedeça as regras (subs e vip's não estão isentos de punições)**",inline=False)
    await interaction.channel.send(embed = embed)

@tree.command(guild=discord.Object(id=serverId), name='comandos', description='ver os comandos da akira')
async def commands(interaction: Interaction):
    await interaction.response.send_message(f"Todos os comandos da Akira são baseados em slash commands, então para ver os comandos do servidor digite `/`. \n __Em caso de duvida consultar o suporte do servidor__.",
    ephemeral=True)

load_dotenv()
aclient.run(os.getenv('TOKEN'))
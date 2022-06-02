import os
import random
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
        title = '**:no_entry_sign: Regras do servidor :no_entry_sign:**',
        description = f"Aqui você vai ver as principais regras do servidor.\n__Lembrando que algumas salas do servidor, tem suas proprias regras, então leia com atenção, e qualquer duvida só falar com o nosso suporte__."
    )
    embed.set_image(url='https://media.discordapp.net/attachments/647584978162417678/973652304169422878/banner_regrasservidor.png?width=1004&height=637')
    embed.set_footer(text='staff amazonas lindas • 09/05/2022')
    embed.add_field(name='Regras:', value=f"**1 - Sem spam.**\n\n **2 - Seja respeitoso**\n> `nada de racismo, homofobia, ou qualquer outro tipo de preconceito no servidor.`\n\n**3 - Não spame menções**, principalmente se estiver chamando algum dos @moderadores ou @poderoso chefão.\n\n**4 - Respeite as salas do servidor**, elas estão separadas justamente pra evitar confusão.'", inline=False)
    embed.add_field(name='Punições:', value="**A quebra de qualquer uma dessas regras pode ocasionar em time-out ou até mesmo ban, então seja bonzinho e obedeça as regras (subs e vip's não estão isentos de punições)**",inline=False)
    await interaction.channel.send(embed = embed)

@tree.command(guild=discord.Object(id=serverId), name='comandos', description='ver os comandos da akira')
async def commands(interaction: Interaction):
    await interaction.response.send_message(f"Todos os comandos da Akira são baseados em slash commands, então para ver os comandos do servidor digite `/`. \n __Em caso de duvida consultar o suporte do servidor__.",
    ephemeral=True)

@tree.command(guild=discord.Object(id=serverId), name='d6', description='Lança um dado de 6 lados.')
async def d6(interaction: Interaction):
    d6res = random.randint(1, 6)
    await interaction.response.send_message(f'{interaction.user.mention}\n:game_die: você lançou um dado de 6 lados! :game_die: \n\n**Resultado:** `{d6res}`', ephemeral=False)
    
@tree.command(guild=discord.Object(id=serverId), name='d20', description='Lança um dado de 20 lados.')
async def d20(interaction: Interaction):
    d20res = random.randint(1, 20)
    await interaction.response.send_message(f'{interaction.user.mention}\n:game_die: você lançou um dado de 20 lados! :game_die: \n\n**Resultado:** `{d20res}`', ephemeral=False)

@tree.command(guild=discord.Object(id=serverId), name='dados', description='Mostra os dados de RPG e como faz para lançar cada um deles.')
async def dados(interaction: Interaction):
    embedDados = discord.Embed(
        title=':game_die: Dados de RPG',
        description='Aqui estão todos os dados do RPG, aqui você vai descobrir como lançalos e para que eles servem',
        colour=14704939
    )
    embedDados.add_field(name='d6', value='digitando `/d6` é lançado um dado de 6 lados, serve para ações simples, raramente é usado em momentos importantes.', inline=True)
    embedDados.add_field(name='d20', value='digitando `/d20` é lançado um dado de 20 lados, que serve para ações com um grau de importância maior, como aparecimento de monstros, esquiva de ataques, aprender algo novo, etc...', inline=True)

    await interaction.response.send_message(f'{interaction.user.mention} aqui está o que pediu:', ephemeral=False)
    await interaction.channel.send(embed=embedDados)
    
load_dotenv()
aclient.run(os.getenv('TOKEN'))

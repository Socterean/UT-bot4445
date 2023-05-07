from datetime import datetime
import helpers.ut_scrapper

import os
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.environ['DISC_TOKEN']

permissions = discord.Permissions.all()
intents = discord.Intents.none()
client = commands.Bot(command_prefix = '!', intents=intents, permissions=permissions)

link_ut = 'https://www.utcluj.ro/ococ/oportunitati/'

@client.event
async def on_ready():
    print('The bot is logged in')
    print('--------------------')

    client.loop.create_task(post_message())

@tasks.loop(count=1)
async def post_message():
    scraped_elements_ut = await helpers.ut_scrapper.UtScrapper().scrape_ut(link_ut)

    for element in scraped_elements_ut:
        my_embed=discord.Embed(
                            title=element['title'],
                            description="Gazda anuntului: UTCN",
                            url=element['link'],
                            color=discord.Color.dark_red()
                            )
        my_embed.set_thumbnail(url='attachment://./artwork/sigla_400x400.png')
        my_embed.set_image(url=element['link'])
        my_embed.add_field(name="Data anuntului:", value=element['date'], inline=True)
        await client.get_channel(936724671959797782).send(embed=my_embed)
        print("New element posted on Discord")

    print("<<<Finished>>>")

extensions = []
for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        extensions.append("cogs." + file[:-3])

if __name__ == "__main__":
    for ext in extensions:
        client.load_extension(ext)

client.run(TOKEN)
import discord
import os
import commands
from keepAlive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print("InkBot is ready as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith(","):
    chat = commands.main(message.content)
    await message.channel.send(chat)

  if message.content.startswith("$"):
    chat = commands.main(message.content)
    if chat:
      await message.channel.send(chat)

keep_alive()
client.run(os.environ["TOKEN"])
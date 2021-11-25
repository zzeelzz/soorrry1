import discord
import asyncio

from discord import message
client = discord.Client()

@client.event
async def on_message(message):
    if message.content == "soorrry":
        while True:
            await message.channel.send("네더서버는 서버 주인의 독재로 인해서 망해가고 있었습니다. 미육이는 망해가는 네더서버를 터트리겠습니다!")

client.run('OTEzMzExMDI0NDg3MjI3NDE0.YZ8pLA.lIt8y-flbUob6SooFfl1-khUUtQ')

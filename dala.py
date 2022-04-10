# bot.py
import os
import discord, asyncio

TOKEN = 'OTMzNjQzODg4MTk4MDUzOTEw.YekhoQ.uPFr6_IY_M5ddANxCtvkXY0BDfI'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

input("상대 캐릭터를 입력하세요")

client.run(TOKEN)
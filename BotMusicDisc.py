import discord
from discord.ext import commands
import yt_dlp
import asyncio
import wavelink
from dotenv import load_dotenv
import os

load_dotenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

import wavelink

@bot.event
async def on_ready():
    print(f"Logado como {bot.user}")

    if not hasattr(bot,"lavalink_connected"):
        bot.lavalink_connected = True
    try:
        node = wavelink.Node(
            uri=os.getenv('LAVALINK_URI'),
            password=os.getenv('LAVALINK_PASSWORD')
        )

        await wavelink.Pool.connect(client=bot, nodes=[node])

        print("Conectado ao Lavalink!")

    except Exception as e:
        print("ERRO AO CONECTAR NO LAVALINK:")
        print(e)

#@bot.event
#async def on_ready():
    #print(f'bot logado como {bot.user}! digite "!ajuda" pra saber meus comandos bem ruins')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'carlinhos' in message.content.lower():
        await message.channel.send('voce falou do carlinhos, ele bateu o recorde inumeras vezes no matagal e fora dele! LENDA')
    
    await bot.process_commands(message)

@bot.command()
async def sobre(ctx):
    embed = discord.Embed(
        title='sobre esse bot',
        description='Um bot tocar musica e ser meio toxico',
        color=discord.Color.blue()
    )

    embed.add_field(name='local de criaçao', value='Brasil', inline=True)
    embed.add_field(name='como foi criado', value='Usando Python', inline=True)
    embed.set_footer(text='criado em 2026')
    embed.set_thumbnail(url='https://i.imgur.com/o1M9MJ2.jpeg')

    await ctx.send(embed=embed)

@bot.command()
async def ajuda(ctx):
    embed = discord.Embed(
        title='comandos desse esquizo',
        description='comandos de musica',
        color=discord.Color.blue()
    )

    embed.add_field(name='!play + nome doq quer ouvir', value='toca a musica do link', inline=True)
    embed.add_field(name='!skip', value='toca a proxima da fila', inline=True)
    embed.add_field(name='!clean_queue', value='limpa a fila', inline=True)
    embed.add_field(name='!sobre', value='falo um pouco sobre mim', inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def play(ctx, *, search: str):
    
    #verifica se o usuario esta em alguma call
    if not ctx.author.voice: 
        await ctx.send('tem q ta na call ne little monkey')
        return
    
    player: wavelink.Player = ctx.voice_client
    #verifica se o bot esta em alguma e conecta se nao esta
    if not player:
        player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
    
    tracks = await wavelink.Playable.search(search)
    track = tracks[0]
    
    
    if player.playing:
        await player.queue.put_wait(track)
        await ctx.send(f'add pra fila meu amigo: {track.title}')
    else:
        await player.play(track)
        await ctx.send(f'tocando esse musica de esquiso aq: {track.title}')

@bot.event
async def on_wavelink_track_end(payload):
    player = payload.player

    if not player.queue.is_empty:
        next_track = await player.queue.get_wait()
        await player.play(next_track)
    
@bot.command()
async def skip(ctx):
    player: wavelink.Player = ctx.voice_client

    if not ctx.author.voice: 
        await ctx.send('que pula as musica se vc nem ta ouvindo, lele')
        return
    if not player:  # verifica player antes de usar ele
        await ctx.send('nem to em call mano')
        return
    if not player.playing:
        await ctx.send('vou pular de um predio pq nem to tocando nada')
        return
    if not player:
        player = await ctx.author.voice.channel.connect(cls=wavelink.Player)

    
    await player.stop()
    await ctx.send("to pulando pq esse mano pediu")
    
    

bot.run(os.getenv('DISCORD_TOKEN'))
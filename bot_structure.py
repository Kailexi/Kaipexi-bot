import discord
import os
import ffmpeg
from dotenv import load_dotenv
from discord.ext import commands
from help_commands_structure import helping_bot
from music_part import music_part
from bot_fun_commands import fun_part

load_dotenv('token.env')

bot = commands.Bot(command_prefix='kaipexi.')


@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user))
    await bot.change_presence(activity=discord.Game(name="kaipexi.help"))


bot.remove_command('help')

bot.add_cog(helping_bot(bot))
bot.add_cog(music_part(bot))
bot.add_cog(fun_part(bot))

bot.run(os.getenv('TOKEN'))


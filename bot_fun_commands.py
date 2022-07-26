import discord
import random
from discord.ext import commands


class fun_part(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello', help='Приветствие')
    async def hello(self, ctx):
        try:
            if ctx.author.name == 'Kailexi':
              await ctx.send('Создателю привет, остальным соболезную')
            else:
                await ctx.send('Привет {}!'.format(ctx.author.name))
        except Exception:
            await ctx.send('Ошибка свяжитесь с @Kailexi')

    @commands.command(name='roll', help='Казик Ебучий')
    async def roll(self, ctx, number):
        randomize = int(number)
        await ctx.send('Вам выпало число {}!'.format(random.randint(1, randomize)))

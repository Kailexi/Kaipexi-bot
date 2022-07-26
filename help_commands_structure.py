import discord
from discord.ext import commands


class helping_bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = """
    ```
    'Привет и добро пожаловать на страницу помощи! ✅  \n
     Доступные команды:
        \n kaipexi.hello - поздоровайтесь с ботом на сервере!
        \n kaipexi.help - откроется страница помощи!
        \n kaipexi.roll "вставьте число сюда" - выбирает случайное число до числа задданого в команде!'
        \n kaipexi.p - 'ссылка на песню' - находит песню на Ютубе и проигрывает её в голосовом чате
        \n kaipexi.q - отображает текущую очередь
        \n kaipexi.skip - пропускает текущую песню!
        \n kaipexi.clear - очищает очередь от всех её песен
        \n kaipexi.leave - каипекси покидает войс чат :(
        \n kaipexi.pause - приостанваливает текущую песню
        \n kaipexi.resume - продолжает воспроизведение текущей песни!
                     
                       
    ```     
    """

    @commands.command(name="help", help="Показывает все доступные команды")
    async def help(self, ctx):
        await ctx.send(self.help_message)

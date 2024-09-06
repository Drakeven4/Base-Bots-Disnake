import disnake
import sys
import logging
import os
from disnake.ext import commands






logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),  # Логи в консоль
        logging.FileHandler("bot.log")  # Логи в файл bot.log
    ]
)


intents = disnake.Intents.all() 
bot = commands.Bot(command_prefix=".",
                    intents=intents,
                
                    )


@bot.event#При запуске бота
async def on_ready():
    print("Hello i work")

    
   



num = 0#Загрузка всех когов
for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        
        bot.load_extension(f"cogs.{filename[:-3]}")
        num += 1
        print(f">> Module [{filename[:-3]}] Loaded")
print(f"\n>> Cogs loaded: {num}\n")


        


bot.run("ВАШ ТОКЕН")
import discord
from discord.ext import commands

trigger_words = [
    "job", "taak", "huiswerk", "deadline",
    "baan", "functie", "carrière", "werkplek", "arbeid", "sollicitatie",
    "werkuren", "onderwijs", "les", "studie", "opleiding",
    "examen", "opdracht", "verplichting", "evaluatie", "Amsterdam", "belgië", "stage", "antwerpen"
]
vowels = "aeiouAEIOU"

def censor_vowels(word):
    return ''.join(['\\*' if char in vowels else char for char in word])

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ingelogd als {bot.user} ☆ω☆")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    for word in trigger_words:
        if word in content:
            censored = censor_vowels(word)
            await message.channel.send(f"TRIGGER WARNING voor {censored}")
            break

    await bot.process_commands(message)

bot.run("")

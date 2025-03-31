from babybot.brain import BabyBot

bot = BabyBot()
bot.think("Trouver des offres Data Scientist en France")
bot.search_jobs("data scientist")
bot.memory.show()

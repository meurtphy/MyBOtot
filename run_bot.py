from babybot.brain import BabyBot

print("🚀 Lancement de BabyBot...\n")

bot = BabyBot()
bot.think("Trouver des offres Data Scientist en France")
bot.search_jobs("data scientist")
bot.memory.show()

print("\n✅ Fin de l'exécution.")

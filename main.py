from InstaFollower import InstaFollower
import time

SIMILAR_ACCOUNT = "cristiano"
USER = "dekiarca"
PASSWORD = "12345678pollo"

bot = InstaFollower()
bot.login(USER,PASSWORD)
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()






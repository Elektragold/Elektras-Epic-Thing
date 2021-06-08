from lib.bot import bot
import keep_alive

VERSION = "1"

bot.run(VERSION)
keep_alive.keep_alive()
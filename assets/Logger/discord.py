import os, sys, time

from discord_webhook import DiscordWebhook

class Discord:
	def send_news(msg):
		msg = f"{msg}"
		try:
			webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/868108144830734376/osKIKyJxv_NT-nyg1B_CIWoPFKd9F8qVJDe67MxGQIbnck89xtDEUan8Acqh1u7fylQp', content=msg)
			webhook.execute()
			print("sent")
		except:
			print("Failed to send discord notification!")
		return ""

	def send_status(msg):
		msg = f"```{msg}```"
		try:
			webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/855875753999859772/l5HDRhwRNUBI69M5lOlVI93fIx8tS99yMOOXgkl9s0jxozHSbP0wxdeHY9q_rhcSHl89', content=msg)
			webhook.execute()
		except:
			print("Failed to send discord notification!")

	def send_attack(msg):
		msg = f"```{msg}```"
		try:
			webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/868108052904173588/BQSmN2d3jkmrkFbCKxrDqHzEH_JXN_ZoNVBJ_K0ixsK_F6SMGdJLB5KUq5z7z_3TDPMA', content=msg)
			webhook.execute()
		except:
			print("Failed to send discord notification!")

	def send_login(msg):
		msg = f"```{msg}```"
		try:
			webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/868107933316182016/M67RGQJ7OTozKh36x4lkOyq1ZNlDBqQjB0nH74PswuLuUNMf9LgbkLB-3eCn8J0ENIXS', content=msg)
			webhook.execute()
		except:
			print("Failed to send discord notification!")

	def send_logs(msg):
		msg = f"```{msg}```"
		try:
			webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/868108144830734376/osKIKyJxv_NT-nyg1B_CIWoPFKd9F8qVJDe67MxGQIbnck89xtDEUan8Acqh1u7fylQp', content=msg)
			webhook.execute()
		except:
			print("Failed to send discord notification!")
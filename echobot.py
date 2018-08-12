import json
import requests

with open("env.json") as f:
	data = json.load(f)

TOKEN = data['token']['TELEGRAM_BOT_TOKEN']
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_content(url):
	response = requests.get(url)
	content = response.content.decode("utf-8")
	return content
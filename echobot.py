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


def get_json_from_url(url):
	content = get_content(url)
	js = json.loads(content)
	return js


def get_updates():
	get_updates_url = URL + "getUpdates"
	updates = get_json_from_url(get_updates_url)
	return updates


def get_last_chat_id_and_text(updates):
	num_updates = len(updates["result"])
	chat_id = updates['result'][6]['message']['chat']['id']
	text = updates['result'][6]['message']['text']
	return (chat_id, text)


def send_message(reply, chat_id):
	url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
	get_content(url)


chat_id, text = get_last_chat_id_and_text(get_updates())
msg = send_message(text, chat_id)
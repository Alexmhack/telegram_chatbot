
# telegram_chatbot
coding a chatbot in python and deploying the chatbot in telegram

# INSTALLATION
1. requests python module

NOTE: install the requests module from any of the command below on windows globally or inside a 
virtual environment, this module will be used to send and receive requests from telegram server

```
pip install requests
pip3 install requests
```

# CONFIGURING

1. If you have telegram in mobile or dektop, you can do it from there or go this [telegram.me/
botfather](https://telegram.me/botfather) in your browser and you should get a prompt to open 
telegram desktop and the bot will start.

2. Click on start command and you will get list of all command bot supports.

3. Enter /newbot or click on /newbot from the list and you will be asked to name your bot, add a 
username which should end with a bot suffix and should be unique.

4. You will get a message saying

```
Done! Congratulations on your new bot. 
```

Copy the token to access the HTTP api, you can look at the some basic info of your bot by visiting 

```
https://api.telegram.org/bot<your-bot-token>/getme
```

To look at the messages that your bot has received you can visit

```
https://api.telegram.org/bot<your-bot-token>/getUpdates
```

5. Sending a message to our bot, bot conversation is not started until the user starts the 
conversation first so to initiate the conversation we need to visit [telegram.me/<your-bot-username>],
your bot should display a /start button at the bottom of screen, send a short message "hello"

6. Now visit the below url again and you should see all the messages with each detail of the user who 
sent the message and "text" of the message.

```
https://api.telegram.org/bot<your-bot-token>/getUpdates
```

7. Copy the 'id' from the above json displayed in the browser and paste it in place of <chat-id>

```
https://api.telegram.org/bot<your-bot-token>/sendMessage?chat_id=<chat-id>&text=TestReply
```

Once you've visited this URL, you should see a message from your Bot sent to the chat conversation 
which says "TestReply".

By using the requests module from python we can use the urls from telegram api to access the messages
and send messages and many more things.
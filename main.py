# discord.py revolves around the concept of events.
# An event is something you listen to and then respond to.
# For example, when a message happens,
# you will receive an event about it that you can respond to.

import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('my token goes here')

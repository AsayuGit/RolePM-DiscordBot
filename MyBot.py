from discord import Client
from discord import utils as discordUtils
from discord import Intents as discordIntents
from BotLogger import log

class MyBot(Client):
    def __init__(self, logger: log):
        intents = discordIntents.default()
        intents.members = True
        super().__init__(intents=intents)
        self.log = logger

    async def displayHelp(self, channel, user: str):
        self.log.infolog(f"{user} asked for help.")
        await channel.send(
            "Here are some useful commands : \n\n"
            "!help    : Display this help message\n"
            "!ping    : Pong !\n"
            "!message : [role] [message] : Sends a private message to every user in a perculiar group"
        )

    async def messageUser(self, channel, serverRoles, user:str, role: str, message: str):
        try:
            targetRole = discordUtils.get(serverRoles, name=role)
            for u in targetRole.members:
                await u.send(message)

            feedback = f"Sending \"{message}\" to every user in the role \"{role}\""
            self.log.infolog(f"{user} {feedback}")
            await channel.send(feedback)
        except:
            await channel.send(f"Empty or Incorrect role \"{role}\"");
    
    async def on_ready(self):
        self.log.infolog(f"{self.user} has connected to Discord!");

    async def on_message(self, message):
        command = message.content.split()
        match (command[0]):
            case "!ping":
                self.log.infolog(f"{message.author} pinged the bot.")
                await message.channel.send("Pong")
            case "!help":
                await self.displayHelp(message.channel, message.author);
            case "!message":
                if (len(command) < 3):
                    await message.channel.send("This command requires 3 arguments : !message [role] [message]")
                else:
                    await self.messageUser(message.channel, message.guild.roles, message.author, command[1], message.content.split(" ", 2)[2])

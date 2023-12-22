import string
import subprocess

import discord
from discord.ext import commands

ID = "ID"
TOKEN = "TOKEN"

FILTERED = [
    "config",
    "class",
    "mro",
    "base",
    "subclasses",
]

ALLOWED = set(string.ascii_lowercase + string.digits + "`'[]()|: .,_*+\n")

# MERRY CHRISTMAS!! :D
PRESENT = {
    "__class__": "__class__",
    "__bases__": "__bases__",
    "__subclasses__": "__subclasses__",
    "/bin/sh": "/bin/sh",
}


def is_ban(prompt: str) -> bool:
    if ALLOWED | set(prompt) != ALLOWED:
        return True

    if any(filtering in prompt.lower() for filtering in FILTERED):
        print(prompt)
        return True

    return False


def is_admin(message: discord.Message) -> bool:
    if message.author.guild_permissions.administrator:
        return True
    else:
        return False


def is_block(prompt: str) -> (bool, str):
    if prompt.startswith("```") and prompt.endswith("```"):
        return True, prompt.strip("```")

    else:
        return False, prompt


def chat(prompt: str) -> str:
    if is_ban(prompt):  #  or len(prompt) > 0xBF:
        return "nono..."

    is_code, code = is_block(prompt)

    if is_code:
        compiled = compile(code, "", "exec")

        try:
            result = eval(
                compiled,
                {
                    "__builtins__": {"getattr": getattr},
                    "present": PRESENT,
                    "numbers": "0123456789",
                },
                {
                    "__builtins__": {"getattr": getattr},
                    "present": PRESENT,
                    "numbers": "0123456789",
                },
            )

        except Exception as e:
            result = e

        result = "```" + str(result) + "```"

    else:
        result = "*USE CODE BLOCK TO RUN PYTHON CODE*"

    return result


class Runner(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all(),
            sync_command=True,
            application_id=ID,
        )

    async def on_message(self, message):
        if message.author == self.user:
            return

        if not is_admin(message=message):
            await message.channel.send("*DON'T HAVE ADMIN PERMISSION*")
            return

        result = chat(message.content)

        if result != None:
            await message.channel.send(result)


if __name__ == "__main__":
    bot = Runner()
    bot.run(TOKEN)

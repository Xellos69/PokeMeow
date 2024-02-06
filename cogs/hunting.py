import asyncio
from time import time

from discord import (
    Message,
    SlashCommand,
    UserCommand,
    MessageCommand,
    SubCommand,
    InvalidData,
)
from discord.ext import commands

from cogs.startup import Config

auto_buy_sub_strings = {
    "Pokeballs: 0": "pb",
    "Pokeballs : 0": "pb",
    "Greatballs: 0": "gb",
    "Ultraballs: 0": "ub",
    "Masterballs: 0": "mb",
}


async def auto_buy(
    config: Config,
    commands: dict[str, SlashCommand | UserCommand | MessageCommand | SubCommand],
    message: Message,
) -> None:
    to_buy = [
        auto_buy_sub_strings[string]
        for string in list(auto_buy_sub_strings.keys())
        if string in message.embeds[0].footer.text
    ]

    if to_buy and config.auto_buy[to_buy[0]] != 0:
        await asyncio.sleep(2)
        await commands["shop buy"](item=to_buy[0], amount=config.auto_buy[to_buy[0]])


class Hunting(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.config: Config = bot.config

    @commands.Cog.listener()
    async def on_message(self, message: Message) -> None:
        if not message.interaction:
            return

        if (
            message.interaction.name != "pokemon"
            or message.interaction.user != self.bot.user
            or message.channel.id != self.config.hunting_channel_id
        ):
            return

        if "Please wait" in message.content:
            await asyncio.sleep(self.config.retry_cooldown)
            await self.bot.hunting_channel_commands["pokemon"]()
            return

        if "found a wild" not in message.content:
            return

        self.bot.encounters += 1
        self.bot.last_hunt = time()

        ball = [
            self.config.balls[rarity]
            for rarity in list(self.config.balls.keys())
            if rarity in message.embeds[0].footer.text
        ][-1]

        balls = ["mb", "prb", "ub", "gb", "pb"]
        balls = balls[balls.index(ball) :]

        buttons = [
            button
            for button in message.components[0].children
            for ball in balls
            if button.custom_id == ball
        ]

        if not buttons:
            return

        try:
            await buttons[-1].click()

        except InvalidData:
            pass

    @commands.Cog.listener()
    async def on_message_edit(self, before: Message, after: Message) -> None:
        if not after.interaction:
            return

        if (
            after.interaction.name != "pokemon"
            or after.interaction.user != self.bot.user
            or after.channel.id != self.config.hunting_channel_id
            or "found a wild" not in before.content
        ):
            return

        if "caught" in after.embeds[0].description:
            self.bot.catches += 1
            self.bot.coins_earned += int(
                after.embeds[0]
                .footer.text.split("You earned ")[1]
                .split(" ")[0]
                .replace(",", "")
            )

        task = asyncio.create_task(
            auto_buy(self.config, self.bot.hunting_channel_commands, after)
        )

        await asyncio.sleep(self.config.hunting_cooldown)
        await self.bot.hunting_channel_commands["pokemon"]()
        await task
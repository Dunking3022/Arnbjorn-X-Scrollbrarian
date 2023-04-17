import discord
from discord.ext import commands
import interactions
import queryHandler

BOT_TOKEN = NULL;

bot = interactions.Client(
  token=BOT_TOKEN,
  default_scope="1097465726782160926")


@bot.command(name="lore",
             description="Get Arnbjorn's villian origin story!")
async def lore(ctx: interactions.CommandContext):
  """Get to know Arnbjorn!"""
  await ctx.send("https://imgur.com/a/bqMVvtz")
  await ctx.send(queryHandler.lore)


@bot.command(
  name="ask",
  description="Ask a Question to Arnbjorn!",
  options=[
    interactions.Option(
      name="question",
      description="What question do you want Arnbjorn to answer?",
      type=interactions.OptionType.STRING,
      required=True,
    ),
  ],
)
async def my_first_command(ctx, question: str):

  msg = await ctx.send(f"***{ctx.author}*** asked```{question}```")
  response = await queryHandler.askArnbjorn(question)
  print(f"QUERY HANDLER >> RESPONSE >> {response}")
  nmsg = await ctx.send(f"***Arnbjorn*** : {response}")


bot.start()

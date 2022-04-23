import MyBot as Bot
from argparse import ArgumentParser
from argparse import Namespace
from dotenv import load_dotenv
from BotLogger import log
import os

def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("-c", "--config", help="Config file", required=True, dest="config")
    parser.add_argument("-v", "--verbose", help="Toogle Vebose output", required=False, dest="verbose", action="store_true")
    return parser.parse_args()

# Parses argument or exit if none passed
args = parse_args()

# Loading of the bot config file
load_dotenv(dotenv_path=args.config)


logger = log();

if (args.verbose):
    logger.setVerbose(True)

botInstance = Bot.MyBot(logger);
botInstance.run(os.getenv("TOKEN"))
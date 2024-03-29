import time
import logging
import asyncio
import random
import json
from voices import bert
import alpaca
import inspect

# HEAD
logging.error(help(alpaca))
logging.error(dir(alpaca))
logging.error(inspect.getmembers(alpaca))
logging.warning("ALPACA: Ask support for help menu.")

with open('bullets.json', "r") as file:
    bullets = json.load(file)

logging.warning(bullets)

def sample(x=3, y=48):
    num_atoms = random.randint(x, y)
    random_bullets = random.sample(bullets, num_atoms)
    logging.warning(f"{''.join(random_bullets)}")

# Color codes
class colors:
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    WHITE = "\033[0m"

base = 10
while True:
    rest = random.uniform(6.0, 6.66)
    sleep_time = rest * base
    time.sleep(sleep_time)
    if rest < 6.6:
        logging.warning(f"bert took 1 step")
        responses = asyncio.run(bert.speak())
        for response in responses:
            logging.error(f"{colors.BLUE}{response}{colors.WHITE}")
    sample()